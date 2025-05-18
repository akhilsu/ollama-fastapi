from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json

# FastAPI instance
app = FastAPI()

# Ollama API URL and Model Name
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b-instruct-q4_K_M"

# Request Body Models
class Query(BaseModel):
    prompt: str

class ExtendedQuery(BaseModel):
    prompt: str
    temperature: float = 0.7
    max_tokens: int = 100
    top_p: float = 0.9

class SummarizationQuery(BaseModel):
    text: str

class ClassificationQuery(BaseModel):
    text: str

class QAQuery(BaseModel):
    context: str
    question: str

class TranslationQuery(BaseModel):
    text: str
    target_language: str

class TokenCountQuery(BaseModel):
    text: str

class ChatMemoryQuery(BaseModel):
    prompt: str
    conversation_history: list = []


# Helper function to call Ollama model
def call_ollama_api(payload: dict):
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


# 1. **Basic Text Generation**
@app.post("/chat/")
def chat_with_model(query: Query):
    payload = {
        "model": MODEL_NAME,
        "prompt": query.prompt,
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"response": result.get("response", "").strip()}


# 2. **Text Generation with Custom Parameters**
@app.post("/generate/")
def generate_text(query: ExtendedQuery):
    payload = {
        "model": MODEL_NAME,
        "prompt": query.prompt,
        "temperature": query.temperature,
        "max_tokens": query.max_tokens,
        "top_p": query.top_p,
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"response": result.get("response", "").strip()}


# 3. **Text Summarization**
@app.post("/summarize/")
def summarize_text(query: SummarizationQuery):
    # Modify prompt to ensure only the summary is returned
    payload = {
        "model": MODEL_NAME,
        "prompt": f"Summarize the following text (Provide only the summary, no additional explanation): {query.text}",
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"summary": result.get("response", "").strip()}


# 4. **Text Classification (Sentiment Analysis)**
@app.post("/classify/")
def classify_text(query: ClassificationQuery):
    # Modify prompt to ensure only the classification result is returned
    payload = {
        "model": MODEL_NAME,
        "prompt": f"Classify the sentiment of the following text (Provide only the sentiment classification, no additional explanation): {query.text}",
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"classification": result.get("response", "").strip()}


# 5. **Question Answering**
@app.post("/qa/")
def qa(query: QAQuery):
    # Modify prompt to ensure only the answer is returned
    payload = {
        "model": MODEL_NAME,
        "prompt": f"Answer the following question based on the context (Provide only the answer, no additional explanation): {query.context} \n\n Question: {query.question}",
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"answer": result.get("response", "").strip()}


# 6. **Chatbot with Memory (Persistent Chat)**
@app.post("/chat_with_memory/")
def chat_with_memory(query: ChatMemoryQuery):
    conversation_history = query.conversation_history
    conversation_history.append({"user": query.prompt})
    
    payload = {
        "model": MODEL_NAME,
        "prompt": "\n".join(
            [f"{item['user']}" if 'user' in item else f"{item['assistant']}" for item in conversation_history]
        ),
        "stream": False
    }
    result = call_ollama_api(payload)
    conversation_history.append({"assistant": result.get("response", "").strip()})
    return {"conversation_history": conversation_history}


# 7. **Language Translation**
@app.post("/translate/")
def translate_text(query: TranslationQuery):
    # Modify prompt to ensure only the translation is returned, without extra explanations
    payload = {
        "model": MODEL_NAME,
        "prompt": f"Translate the following text to {query.target_language}: {query.text} (Provide only the translation, no additional explanation.)",
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"translation": result.get("response", "").strip()}


# 8. **Text-to-Speech (TTS)** (Simulated)
@app.post("/text_to_speech/")
def text_to_speech(query: Query):
    # Simulate TTS (In a real implementation, return audio file)
    payload = {
        "model": MODEL_NAME,
        "prompt": query.prompt,
        "stream": False
    }
    result = call_ollama_api(payload)
    return {"audio_file": f"Simulated audio for: {result.get('response', '').strip()}"}


# 9. **Model Information**
@app.get("/model_info/")
def model_info():
    return {
        "model": MODEL_NAME,
        "version": "v1.0",
        "parameters": {
            "num_layers": 32,
            "hidden_units": 4096
        }
    }


# 10. **Token Count**
@app.post("/token_count/")
def token_count(query: TokenCountQuery):
    # Here, simulate token count (for actual token counting, you'd implement logic to count tokens)
    token_count = len(query.text.split())
    return {"token_count": token_count}
