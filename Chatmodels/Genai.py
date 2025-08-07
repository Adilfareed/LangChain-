import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize Google Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Prompt template to generate a detailed report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=["topic"]
)


template2 = PromptTemplate(
    template="Write a 20  line summary of the following text:\n{text}",
    input_variables=["text"]
)

parser=StrOutputParser()
chain=template1|model|parser|template2|model|parser

result=chain.invoke({'topic':'Ai'})

print(result)
