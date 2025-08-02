from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001"
)
documents=[
    "hi this issi",
    "what is your name"

]

result = embeddings.embed_documents(documents)

print(result)
