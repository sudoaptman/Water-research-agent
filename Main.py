import streamlit as st
from Database import fetch_from_db, save_to_db
from Research import research_water_hardness

st.set_page_config(page_title="UK Water Quality Checker")
st.title("💧 UK Water Quality Checker")

postcode = st.text_input("Enter your UK Postcode (e.g., PO1 1AA):", key="pc_input")

# Use a button to prevent auto-triggering
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
                
                if info:
                    st.info("Found data via Research Agent:")
                    st.write(info)
                    # 3. Save to DB
                    save_to_db(postcode, info)
                else:
                    st.error("No specific data found for this postcode. Please check the spelling or try a nearby area.")
