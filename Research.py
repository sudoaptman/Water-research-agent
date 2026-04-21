import streamlit as st
from duckduckgo_search import DDGS

@st.cache_resource
def get_search_agent():
    return DDGS()

def research_water_hardness(postcode):
    """
    Refined search query to target UK water quality report formats.
    """
    ddgs = get_search_agent()
    # Adding 'drinking water quality report' significantly improves hit rate
    query = f"UK drinking water quality report hardness {postcode} site:gov.uk OR site:*.co.uk"
    
    try:
        results = list(ddgs.text(query, max_results=3))
        if results:
            # Join top 2 results to give the agent more context
            extracted_info = "\n".join([r['body'] for r in results[:2]])
            return extracted_info
        return None
    except Exception as e:
        return f"Research error: {str(e)}"
