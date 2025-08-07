import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()



llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")  # Pass token explicitly
)





model = ChatHuggingFace(llm=llm)

templete1=PromptTemplate(
    template="write a detail report on {topic} ",
    input_variables=['topic']
)



templete2=PromptTemplate(
    template="write a 5 line summary  on {text} ",
    input_variables=['text']
)

prompt1=templete1.invoke({'topic':"black hole"})

result=model.invoke(prompt1)

prompt2=templete2.invoke({'text':result.content})

result = model.invoke(prompt2)
print(result.content)
