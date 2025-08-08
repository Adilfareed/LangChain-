from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence


load_dotenv()

prompt=PromptTemplate(

    template="what is the capital of {country}",
    input_variables=['country']
)

llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

result=RunnableSequence(prompt,llm,parser)

print(result.invoke({'country':'pakistan'}))