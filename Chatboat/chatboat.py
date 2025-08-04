from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
load_dotenv()

model=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

chat_history=[
    SystemMessage("you are a ai assistant")
]

while True:
    user_input=input("you:")
    chat_history.append(HumanMessage(user_input))
    if user_input=="exit":
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("Ai:",result.content)

print(chat_history)