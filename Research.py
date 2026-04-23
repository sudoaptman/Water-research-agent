import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    return DDGS()

def research_water_hardness(postcode):
    ddgs = get_search_agent()
    
    # Extract the 'outward' code (e.g., 'PO1' from 'PO1 1AA')
    # This is much more likely to return official utility reports
    area = postcode.split(' ')[0]
    query = f"water quality report and hardness levels for {area} area UK site:gov.uk"
    
    try:
        # We increase max_results slightly to ensure we capture a good snippet
        results = list(ddgs.text(query, max_results=5))
        
        if results:
            # Join the content of the top results to provide a better context
            return "\n\n".join([f"{r['title']}: {r['body']}" for r in results])
        
        return None
    except Exception as e:
        return f"Research error: {str(e)}"
