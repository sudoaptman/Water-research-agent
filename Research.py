import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    # Many cloud environments require this to be instantiated cleanly
    return DDGS()

def research_water_hardness(postcode):
    try:
        ddgs = get_search_agent()
        # Clean the input
        clean_query = f"water hardness in {postcode.split(' ')[0]} UK"
        
        # Use the context manager method which is more stable
        with DDGS() as ddgs:
            results = list(ddgs.text(clean_query, max_results=3))
            
        if results:
            return "\n\n".join([f"{r.get('title', '')}: {r.get('body', '')}" for r in results])
        else:
            return "Search engine returned zero results. Please try a different area."
            
    except Exception as e:
        # This will return the actual error to your screen so we can see it
        return f"CRITICAL SEARCH ERROR: {str(e)}"
