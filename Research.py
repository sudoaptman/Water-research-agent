import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    return DDGS()

def research_water_hardness(postcode):
    """
    Searches for water hardness information and ensures a string is returned.
    """
    ddgs = get_search_agent()
    # Try a focused query
    query = f"UK drinking water hardness report {postcode}"
    
    try:
        results = list(ddgs.text(query, max_results=3))
        if results:
            # Join the snippets of the top 3 results
            return "\n\n".join([r['body'] for r in results])
        else:
            return "No specific data found for this postcode. Try a nearby town."
    except Exception as e:
        return f"Research error: {str(e)}"
