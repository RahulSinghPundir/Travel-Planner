# Chat-Based Travel Planner

A Python-based conversational system designed to interact with users, extract their preferences, and generate personalized travel plans. This project leverages an LLM (Large Language Model) with prompts to manage conversation flow and generate contextual responses.

## Features

- **System Initialization**: Initializes the system with a predefined prompt.
- **Preference Extraction**: Extracts user preferences based on input and chat history.
- **Chat Summarization**: Summarizes the chat history for better context handling.
- **Travel Plan Generation**: Creates a personalized travel itinerary based on extracted preferences.

## Project Structure
  - `extract_user_preference(user_input)`: Processes user input, extracts preferences, and updates the chat history.
  - `summarize_chat(chat_history)`: Summarizes the chat history to provide context for other operations.
  - `generate_travel_plan()`: Generates a travel itinerary using the summarized chat history.

