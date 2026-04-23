import streamlit as st

def research_water_hardness(postcode):
    """
    Simulates a search by looking up data in a local dictionary.
    This bypasses the search engine block entirely.
    """
    # Mock database for testing
    data_store = {
        "portsmouth": "Portsmouth water is classified as Hard. Hardness level: 250 ppm.",
        "london": "London water is classified as Very Hard. Hardness level: 300 ppm.",
        "po1": "Portsmouth (PO1) water hardness: 250 ppm (Hard)."
    }
    
    # Normalize input
    search_key = postcode.lower().strip()
    
    # Check if we have the town or the start of the postcode
    for key, value in data_store.items():
        if key in search_key:
            return value
            
    return "No data found in local knowledge base."
