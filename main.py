import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)
question = input("ask gemnai:")

name = llm.invoke(question)


print(name.content if hasattr(name, "content") else name)
