import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    return DDGS()

def research_water_hardness(postcode):
    ddgs = get_search_agent()
    # Broaden the search by using just the first part of the postcode
    area = postcode.split(' ')[0]
    query = f"water hardness level in {area} UK"
    
    try:
        results = list(ddgs.text(query, max_results=3))
        if results:
            # Join the snippets of the top 3 results
            return "\n\n".join([r['body'] for r in results])
        else:
            return "No information found for this area. Please try a major town nearby."
    except Exception as e:
        return f"Research error: {str(e)}"
