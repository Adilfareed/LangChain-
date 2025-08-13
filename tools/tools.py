from langchain_community.tools import DuckDuckGoSearchRun

# Initialize search tool
search_tool = DuckDuckGoSearchRun()

# Perform the search
results = search_tool.invoke("which models of iphone are about to launch")

# Print the results
print(results)
