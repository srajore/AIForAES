

import google.generativeai as genai

from dotenv import load_dotenv  

load_dotenv()

# Set API Key
genai.configure()



# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# Generate content
response = model.generate_content("Explain Generative AI in 3 bullet points")

print(response.text)