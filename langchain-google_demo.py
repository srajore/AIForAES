from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    max_tokens=1000,
)

response = llm.invoke("What is Generative AI?")

print(response.content)