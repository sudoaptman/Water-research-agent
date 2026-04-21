import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    """
    Initializes the search agent only once and caches it.
    This prevents the agent from re-initializing on every script re-run.
    """
    return DDGS()

def get_water_profile(query):
    """
    Uses the cached search agent to perform a search.
    """
    ddgs = get_search_agent()
    
    # Perform the search
    # We use a context manager safely here
    try:
        results = list(ddgs.text(query, max_results=3))
        # Add your processing logic here
        return results
    except Exception as e:
        return f"Error performing search: {e}"

# Example usage within this file if you were to run it directly:
if __name__ == "__main__":
    profile = get_water_profile("water hardness in Portsmouth")
    print(profile)
