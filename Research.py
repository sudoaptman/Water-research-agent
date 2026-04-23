import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    return DDGS()

def research_water_hardness(postcode):
    ddgs = get_search_agent()
    # Broaden query to town/area to ensure we get results
    query = f"water hardness level in {postcode} UK"
    
    try:
        # Use simple text search
        results = ddgs.text(query, max_results=3)
        if results:
            # Combine snippets into a single readable string
            return "\n\n".join([r['body'] for r in results])
        return "No data found for this location."
    except Exception as e:
        return f"Research error: {e}"
