def route_query(query):

    keywords = ["transformer", "attention", "encoder", "decoder"]

    for k in keywords:
        if k in query.lower():
            return "vector"

    return "web"