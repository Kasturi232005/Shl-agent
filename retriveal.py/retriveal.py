import json

with open("catalog.json", "r") as f:
    catalog = json.load(f)

def search(query):

    results = []

    query = query.lower()

    for item in catalog:

        if "java" in query and "java" in item["description"].lower():
            results.append(item)

        elif "personality" in query and item["test_type"] == "P":
            results.append(item)

    return results[:5]