from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
('system','You are a helpful AI assistant '),
('human','Tell me the {topic} in 3 bullet points.'),
])

llm = ChatOllama(
    model="llama3.2:3b"
)

chain = prompt | llm



while True:
    print('Type  "exit" to quit.')
    username = input('Ask me about anything ')

    if username.lower() == 'exit':
        break

    response = chain.invoke({"topic": username})
    print("\n" ,response.content , "\n")
