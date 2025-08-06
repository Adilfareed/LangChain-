import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Annotated,Literal

load_dotenv()

# Define output schema using Pydantic
class Review(BaseModel):
    summary: Annotated[str,"A brief summary about review"] 
    sentiment:Annotated[Literal["pos","neg"],"provide sentiment "]

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.6)

# Apply structured output
structured_model = llm.with_structured_output(Review)

# Input prompt
result = structured_model.invoke("""
I dont like this product very much, bad quality.
""")

# Print result
print(result)
