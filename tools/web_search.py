# from tavily import TavilyClient
# import os

# client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# def search_web(query):

#     result = client.search(
#         query=query,
#         max_results=3
#     )

#     return result["results"]
from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query):

    results = client.search(query=query, max_results=3)

    print("\nWeb Search Results:\n")

    for r in results["results"]:
        print(r["title"])
        print(r["url"])

    return str(results["results"])