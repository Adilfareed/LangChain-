from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda

load_dotenv()


class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Sentiment of the feedback")

parser1=StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


prompt = PromptTemplate(
    template=(
        "Classify the sentiment of the following feedback as either 'positive' or 'negative'.\n"
        "{feedback}\n"
        "Respond ONLY in the following JSON format:\n{format_instructions}"
    ),
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

# Create the chain
classifier_chain = prompt | model | parser2

prompt2=PromptTemplate(
    template='write an appropriate response to this possitive feedback \n {feedback}',
    input_variables=['feedback']

)

prompt3=PromptTemplate(
    template='write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']

)


branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2|model|parser1),
    (lambda x:x.sentiment=='negative',prompt3|model|parser1),
    RunnableLambda(lambda x:"sentiment not found")

)

chain=classifier_chain|branch_chain


result=chain.invoke({'feedback':'this is good product'})

# Print result
print(result)
