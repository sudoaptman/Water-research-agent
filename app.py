import streamlit as st
from Main import get_water_profile

st.set_page_config(page_title="Water Quality Checker", page_icon="💧")

st.title("💧 UK Water Quality Checker")
st.write("Enter your postcode to see your local water profile and filter recommendations.")

# Input field
postcode = st.text_input("Enter your UK Postcode (e.g., PO1 1AA):", "")

if st.button("Check My Water"):
    if postcode:
        with st.spinner('Analyzing your local water profile...'):
            data = get_water_profile(postcode)
            
            if data and "error" not in data:
                st.success(f"Water Data Found for sector: {postcode[:3].upper()}")
                st.metric("Hardness (PPM)", data['ppm_value'])
                st.write(f"**Classification:** {data['classification']}")
                
                # Logic for product suggestion
                if "Hard" in data['classification']:
                    st.warning("We recommend a **Scale Inhibitor Filter** for your area.")
                else:
                    st.info("A **Standard Carbon Filter** is suitable for your area.")
            else:
                st.error("Data not found for this postcode. Please check the format.")
    else:
        st.warning("Please enter a valid postcode.")
