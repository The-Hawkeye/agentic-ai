from tavily import TavilyClient
import os

client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


def search_web(query):

    response = client.search(
        query=query,
        max_results=3
    )

    results = ""

    for r in response["results"]:
        results += r["content"] + "\n"

    return results