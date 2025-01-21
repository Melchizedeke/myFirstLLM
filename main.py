# The required libraries import
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Loading  the API_KEY which is saved as an environment variable in the ".env" file
load_dotenv()
api_key = os.environ['API_KEY']

# Configuring the Gemini Model using just the api_key as this is a very basic model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Setting the user input prompt to be passed into the model
prompt = input("User Query:")

# Generating the model's response
response = model.generate_content(prompt)

# Printing the output to the console
print("AI Response: ", response.text)