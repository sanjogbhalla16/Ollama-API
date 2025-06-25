from fastapi import FastAPI,Depends,HTTPException,Header
import ollama
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

API_KEY_CREDITS = {os.getenv("API_KEY"): 100}

print("SERVER API_KEY LOADED:", os.getenv("API_KEY"))
print("API_KEY_CREDITS:", API_KEY_CREDITS)


def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key,0)
    if credits <= 0:
        raise HTTPException(status_code=401,detail="Invalid API key, or no credits")
    
    return x_api_key


@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt }])
    return { "message": response["message"]["content"]}
