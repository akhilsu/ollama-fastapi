# OLLAMA-FASTAPI
FastAPI Ollama Integration

# Python code to generate a README file

readme_content = """
# FastAPI Ollama Integration

This FastAPI-based application integrates with the Ollama API to provide a variety of natural language processing (NLP) functionalities such as text generation, summarization, classification, translation, and more. The application includes several endpoints that allow users to interact with the model for various tasks.

## Table of Contents
- [Installation](#installation)
- [Run the Application](#run-the-application)
- [API Endpoints](#api-endpoints)
  - [1. Basic Text Generation](#1-basic-text-generation)
  - [2. Text Generation with Custom Parameters](#2-text-generation-with-custom-parameters)
  - [3. Text Summarization](#3-text-summarization)
  - [4. Text Classification (Sentiment Analysis)](#4-text-classification-sentiment-analysis)
  - [5. Question Answering](#5-question-answering)
  - [6. Chatbot with Memory (Persistent Chat)](#6-chatbot-with-memory-persistent-chat)
  - [7. Language Translation](#7-language-translation)
  - [8. Text-to-Speech (Simulated)](#8-text-to-speech-simulated)
  - [9. Model Information](#9-model-information)
  - [10. Token Count](#10-token-count)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/akhilsu/ollama-fastapi.git
```

2. Run the Application

```bash
uvicorn main:app --reload
```
```url
http://127.0.0.1:8000/docs
```

3. API Endpoints
   1. Basic Text Generation
      
      Endpoint: POST /chat/
      
      Request Body Example:
      ```json
      {
        "prompt": "Once upon a time..."
      }
      ```
      Response:
      ```json
      {
        "response": "Generated response text based on the prompt."
      }
      ```

   2. Text Generation with Custom Parameters
      
      Endpoint: POST /generate/
      
      Request Body Example:
      ```json
      {
        "prompt": "Tell me a story.",
        "temperature": 0.8,
        "max_tokens": 200,
        "top_p": 0.9
      }
      ```
      
      Response:
      ```json
      {
        "response": "Generated response text based on the prompt and parameters."
      }
      ```

   3. Text Summarization
         
      Endpoint: POST /summarize/
      
      Request Body Example:
      ```json
      {
        "text": "The quick brown fox jumps over the lazy dog. The dog wakes up and chases the fox."
      }
      ```
      
      Response:
      ```json
      {
        "summary": "Shortened version of the text provided."
      }
      ```
      
   4. Text Classification (Sentiment Analysis)
      
      Endpoint: POST /classify/
      
      Request Body Example:
      ```json
      {
        "text": "I love this place!"
      }
      ```
      
      Response:
      ```json
      {
        "classification": "positive"
      }
      ```
      
   5. Question Answering
      
      Endpoint: POST /qa/
      
      Request Body Example:
      ```json
      {
        "context": "The Eiffel Tower is in Paris.",
        "question": "Where is the Eiffel Tower located?"
      }
      ```
      
      Response:
      ```json
      {
        "answer": "Paris"
      }
      ```
      
   6. Chatbot with Memory (Persistent Chat)
      
      Endpoint: POST /chat_with_memory/
      
      Request Body Example:
      ```json
      {
        "prompt": "Hello, how are you?",
        "conversation_history": [{"user": "Hi!"}]
      }
      ```
      
      Response:
      ```json
      {
        "conversation_history": [
          {"user": "Hi!"},
          {"assistant": "Hello, how are you?"}
        ]
      }
      ```
      
   7. Language Translation
      
      Endpoint: POST /translate/
      
      Request Body Example:
      ```json
      {
        "text": "Hello, how are you?",
        "target_language": "es"
      }
      ```
      
      Response:
      ```json
      {
        "translation": "Hola, ¿cómo estás?"
      }
      ```
      
   8. Text-to-Speech (Simulated)
      
      Endpoint: POST /text_to_speech/
      
      Request Body Example:
      ```json
      {
        "prompt": "Hello, welcome!"
      }
      ```
      
      Response:
      ```json
      {
        "audio_file": "Simulated audio for: Hello, welcome!"
      }
      ```
      
   9. Model Information
      
      Endpoint: GET /model_info/
      
      Response:
      ```json
      {
        "model": "llama3.2:3b-instruct-q4_K_M",
        "version": "v1.0",
        "parameters": {
          "num_layers": 32,
          "hidden_units": 4096
        }
      }
      ```
      
   10. Token Count
      
      Endpoint: POST /token_count/
   
      Request Body Example:
      ```json
      {
        "text": "Hello, world!"
      }
      ```
      
      Response:
      ```json
      {
        "token_count": 3
      }
      ```
      
