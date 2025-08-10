from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader=PyPDFLoader('Introduction_to_AI.pdf')

docs=loader.load()

spiliter= RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
   
)

result=spiliter.split_documents(docs)
print(result[0].page_content)