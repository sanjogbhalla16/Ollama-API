from fastapi import FastAPI
import ollama
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt }])
    return { "message": response["message"]["content"]}
