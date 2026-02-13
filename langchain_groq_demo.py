from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
)

response = llm.invoke("What is Generative AI?")

print(response.content)