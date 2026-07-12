"""
Serper : Serper (serper.dev) is a fast, low-cost Google Search API designed for developers to integrate real-time
search results, Knowledge Graphs, and image/news data into applications
"""

import requests
from dotenv import load_dotenv
import os

load_dotenv()


url = "https://google.serper.dev/search"

payload = {
  "q": "apple inc"
}

headers = {
  'X-API-KEY':  os.getenv("SERPER_API_KEY") ,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, json=payload)

print(response.text)