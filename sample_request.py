import requests
import json

# Set up the base URL for the local Ollama API
url = 'http://localhost:11434/api/chat'

# Define the payload (your input prompt)
payload = {
  "model": "mistral",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}

# Send the HTTP POST request with streaming enabled
response = requests.post(url,json=payload,stream=True)

# Check the response status 
if response.status_code == 200:
    print("Streaming response from Ollama:")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                # Parse each line as a JSON object json.loads(s) parses the string and returns a Python dictionary.
                json_data = json.loads(line)
                # Extract and print the assistant's message content
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()  # Ensure the final output ends with a newline
else:
    print(f"Error: {response.status_code}")
    print(response.text)
                    
     

