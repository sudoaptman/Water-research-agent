import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    return DDGS()

def research_water_hardness(postcode):
    """
    Searches for water hardness information.
    """
    ddgs = get_search_agent()
    query = f"water hardness in {postcode} UK ppm"
    
    try:
        # Perform search and get the first result
        results = list(ddgs.text(query, max_results=1))
        if results:
            return results[0]['body']
        return "No specific data found for this area."
    except Exception as e:
        return f"Research error: {str(e)}"
