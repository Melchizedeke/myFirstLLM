# The required libraries import
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Loading  the API_KEY which is saved as an environment variable in the ".env" file
load_dotenv()
api_key = os.environ['API_KEY']

# Configuring the Gemini Model using just the api_key as this is a very basic model
genai.configure(api_key=api_key)
system_message = """
    You are an AI assistant trained to give answers about Nigeria.
    You are to answer correctly when asked about Nigeria.
    If you asked any question outside of this scope, you are to say you do not know.
    You are humble and respectful.
"""
safety_settings = """
    You are not to use any form of profanity or sexually condescending remarks whilst
    generating contents to the user.
"""
model = genai.GenerativeModel(model_name='gemini-1.5-flash', 
                              system_instruction=system_message)

while True:
    # Setting the user input prompt to be passed into the model
    prompt = input("User Query:")

    # Generating the model's response
    response = model.generate_content(prompt)

    # Printing the output to the console
    print("AI Response: ", response.text)