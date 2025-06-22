from fastapi import FastAPI
import ollama

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt }])
    return { "message": response["message"]["content"]}
