import streamlit as st
from Database import fetch_from_db, save_to_db
from Research import research_water_hardness

st.set_page_config(page_title="UK Water Quality Checker")

st.title("💧 UK Water Quality Checker")
postcode = st.text_input("Enter your UK Postcode (e.g., PO1 1AA):")

def get_water_profile(postcode):
    # 1. Try to get from database first
    db_data = fetch_from_db(postcode)
    if db_data:
        return db_data, "Database"
    
    # 2. If not in DB, research it
    hardness_info = research_water_hardness(postcode)
    
    # 3. Save to DB for next time
    save_to_db(postcode, hardness_info)
    return hardness_info, "Research Agent"

if postcode:
    with st.spinner('Researching your water quality...'):
        profile, source = get_water_profile(postcode)
        st.write(f"**Source:** {source}")
        st.write(profile)
