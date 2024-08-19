def format_itineraries(itineraries):
    formatted_itineraries = []
    
    # Iterate over the list of tuples with enumeration to keep track of the itinerary number
    for i, (traveler_name, origin, destination) in enumerate(itineraries, 1):
        itinerary_string = f"Itinerary {i}: {traveler_name} - From {origin} to {destination}"
        formatted_itineraries.append(itinerary_string)
    
    # Join all formatted itineraries into a single string separated by newlines
    return "\n".join(formatted_itineraries)

# Example usage
flight_itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco")
]

formatted_itineraries = format_itineraries(flight_itineraries)
print(formatted_itineraries)
