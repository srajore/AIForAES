from langchain_openai import AzureChatOpenAI

from dotenv import load_dotenv

import os

load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    temperature=0
)

response = llm.invoke("Tell me the key achievements of ROhit Sharma in 3 bullet points ")

print(response.content)