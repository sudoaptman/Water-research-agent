import streamlit as st
from Database import fetch_from_db, save_to_db
from Research import research_water_hardness

st.set_page_config(page_title="UK Water Quality Checker")
st.title("💧 UK Water Quality Checker")

postcode = st.text_input("Enter your UK Postcode (e.g., PO1 1AA):", key="pc_input")

if st.button("Check Water Quality"):
    if not postcode:
        st.warning("Please enter a postcode.")
    else:
        with st.spinner('Researching...'):
            # Try Database
            db_data = fetch_from_db(postcode)
            
            if db_data:
                st.write("**Source:** Database")
                st.write(db_data)
            else:
                # Try Research Agent
                info = research_water_hardness(postcode)
                st.write("**Source:** Research Agent")
                st.write(info)
                
                # Only save to DB if it's actual data, not an error message
                if "Research error" not in info and "No data found" not in info:
                    save_to_db(postcode, info)
