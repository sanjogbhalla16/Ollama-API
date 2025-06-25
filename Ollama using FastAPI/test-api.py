# we will run this api with our python code also 
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# this will be a response object which contains all the information about the request and also has methods for we are sending json data to our api so we need to send content type as application/json in headers section of the code above
url = 'http://127.0.0.1:8000/generate?prompt=Tell me about Python'
headers = {
    'x-api-key': os.getenv("API_KEY"),
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers)
print(response.json())
