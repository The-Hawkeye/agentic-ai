# from agents.router_agent import route_query
# from tools.vector_search import search_vector
# from tools.web_search import search_web
# from llm.llm import generate_answer

# query = input("Ask a question: ")

# route = route_query(query)

# if route == "vector":
#     context = search_vector(query)
# else:
#     context = search_web(query)

# answer = generate_answer(context, query)

# print(answer)

from agents.router_agent import route_query
from tools.vector_search import search_vector
from tools.web_search import search_web
from llm.llm import generate_answer

query = input("Ask a question: ")

route = route_query(query)

print("\nRouting Decision:", route)

if route == "vector":
    print("\nUsing VECTOR SEARCH\n")
    context = search_vector(query)

else:
    print("\nUsing WEB SEARCH\n")
    context = search_web(query)

print("\nRetrieved Context:\n")
print(context[:1000])   # print first 1000 chars

answer = generate_answer(context, query)

print("\nFinal Answer:\n")
print(answer)