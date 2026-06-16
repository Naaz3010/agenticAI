
from langchain.tools import tool
from datetime import datetime
from tools.data_loader import flights_data

@tool
def flight_search_tool(source: str, destination: str):
    """
    Find the cheapest and fastest flight between two cities.
    """
    results = [
        f for f in flights_data
        if f["from"].lower() == source.lower()
        and f["to"].lower() == destination.lower()
    ]

    if not results:
        return {"message": "No flights found"}

    for f in results:
        dep = datetime.fromisoformat(f["departure_time"])
        arr = datetime.fromisoformat(f["arrival_time"])
        f["duration_hours"] = round((arr - dep).seconds / 3600, 2)

    cheapest = min(results, key=lambda x: x["price"])
    fastest = min(results, key=lambda x: x["duration_hours"])

    return {
        "cheapest_flight": cheapest,
        "fastest_flight": fastest
    }
