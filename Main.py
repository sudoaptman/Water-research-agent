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
        with st.spinner('Researching local data...'):
            # 1. Try DB
            db_data = fetch_from_db(postcode)
            
            if db_data:
                st.success("Data found in database!")
                st.write(db_data)
            else:
                # 2. Try Research
                info = research_water_hardness(postcode)
                
                # Check if info is actually valid text
                if info and "No information found" not in info and "Research error" not in info:
                    st.info("Found data via Research Agent:")
                    st.write(info)
                    save_to_db(postcode, info)
                else:
                    st.error(info) # Display the friendly message returned by Research.py
