from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5-nano",
    #max_tokens=200,
)

response = llm.invoke("What is Generative AI?")

print(response.content)