from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

prompt  = PromptTemplate(
    template="Tell me the key achivements of {name} in 3 bullet points.",
    input_variables=["name"]
)


llm = ChatOllama(
    model="llama3.2:3b"
)

chain= prompt | llm   #LCEL

username = input("Whose achivements you would like to know ? Press Enter to continue...")

response = chain.invoke({"name": username})

#response = llm.invoke(prompt.format(name="Mahatma Gandhi"))


print(response.content)