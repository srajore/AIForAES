from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5-nano",
    
    #max_tokens=200,
)

response = llm.invoke("Tell me the key achievements of ROhit Sharma in 3 bullet points ")

print(response.content)