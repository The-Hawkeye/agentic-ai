# from crewai import Agent


# router_agent = Agent(
#     role="Query Router",
#     goal="Decide whether to use vector search or web search",
#     backstory=(
#         "You are an AI assistant that decides the best source "
#         "to answer a question."
#     ),
#     verbose=True
# )


# def route_query(query):

#     keywords = [
#         "paper",
#         "transformer",
#         "attention",
#         "encoder",
#         "decoder"
#     ]

#     for k in keywords:
#         if k in query.lower():
#             return "vector"

#     return "web"


def route_query(query):

    keywords = [
        "pdf",
        "document",
        "file",
        "section",
        "chapter"
    ]

    query_lower = query.lower()

    for word in keywords:
        if word in query_lower:
            return "vector"

    return "web"