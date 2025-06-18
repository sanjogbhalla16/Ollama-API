import requests
import json

url = 'http://localhost:11434/api/chat'


payload = {
  "model": "mistral",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}

