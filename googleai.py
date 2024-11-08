import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

ask = input("What would you like? ")

while ask.lower()!="exit":
    aitalk = model.generate_content(ask)
    print(aitalk.text)
    ask = input("What would you like? ")
