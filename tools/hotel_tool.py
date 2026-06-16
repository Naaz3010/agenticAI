from langchain.tools import tool
from tools.data_loader import hotels_data

@tool
def hotel_recommendation_tool(city: str, min_stars: int = 3, max_price: int = None):
    """
    Recommend hotels based on city, rating, and price.
    """
    results = [
        h for h in hotels_data
        if h["city"].lower() == city.lower()
        and h["stars"] >= min_stars
    ]

    if max_price:
        results = [h for h in results if h["price_per_night"] <= max_price]

    results.sort(key=lambda x: (-x["stars"], x["price_per_night"]))

    if results:
        return results[:3]

    all_hotels = [
        h for h in hotels_data
        if h["city"].lower() == city.lower()
    ]
    
    all_hotels.sort(key=lambda x: x["price_per_night"])
    
    return {
        "message": "No hotels found within budget",
        "closest_option": all_hotels[0] if all_hotels else None
    }
