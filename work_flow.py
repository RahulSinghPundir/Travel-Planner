from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


import json

from get_prompts import SYSTEM_PROMPT, ITINERARY_PROMPT, EXTRACT_USER_PREFERENCE_PROMPT,SUMMARIZATION_PROMPT


def save_chat_history(chat_entry, filename='chat_history.json'):
    try:
        # Load existing history
        with open(filename, 'r') as file:
            chat_history = json.load(file)
    except FileNotFoundError:
        chat_history = {"chat_history": []}

    # Append new entry
    chat_history["chat_history"].append(chat_entry)

    # Write back to file
    with open(filename, 'w') as file:
        json.dump(chat_history, file, indent=4)

def load_chat_history(filename='chat_history.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)["chat_history"]
    except FileNotFoundError:
        return []
    
def summarize_chat(chat_summary,chat_history):
    # Summarize chat history
    
    summarize_chain = LLMChain(
        llm=chat_history_llm,
        prompt=PromptTemplate(
            input_variables=["chat_history"],
            template=SUMMARIZATION_PROMPT
        )
    )
    
    chat_history = "\n".join([f"User: {chat['user_input']}, Response: {chat['response']}" for chat in chat_history]) + str(chat_summary)
    summary = summarize_chain.run({"chat_history": chat_history})
    return summary

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyCapW0ltP_b2j9bg7tA4M1KqlnErc0hCs4")
chat_history_llm=llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyCapW0ltP_b2j9bg7tA4M1KqlnErc0hCs4")
chat_summary=""

def extract_user_preference(user_input,chat_summary):
    
            chat_history = load_chat_history()  # Load the complete chat history

            


            # Use the summary and user input in the system prompt
            system_prompt = PromptTemplate(
                input_variables=["user_input", "chat_summary"],
                template=SYSTEM_PROMPT + EXTRACT_USER_PREFERENCE_PROMPT
            )

            # Generate a response using the system chain
            system_chain = LLMChain(llm=llm, prompt=system_prompt)
            bot_response = system_chain.run({"user_input": user_input, "chat_summary": chat_summary})

            # Save the chat entry to history
            chat_entry = {
                "id": len(chat_history) + 1,
                "user_input": user_input,
                "response": bot_response
            }
            save_chat_history(chat_entry)

            # Summarize the chat history for context
            chat_history = load_chat_history()
            summary = summarize_chat(chat_summary,chat_history)

            response={
                "chat_summary": summary,
                "bot_response": bot_response
            }
            return response


def generate_travel_plan(state):
        chat_summary=state['chat_summary']
        answer_prompt = PromptTemplate(input_variables=["chat_summary"], template=ITINERARY_PROMPT)
        chat_chain = LLMChain(llm=llm, prompt=answer_prompt)
        bot_response = chat_chain.run({"chat_summary": chat_summary,})
        return bot_response