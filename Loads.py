import streamlit as st
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import urllib.parse

st.set_page_config(page_title="ASCE Hazard Tool Interface", layout="centered")

st.title("🌪️ ASCE Hazard Tool Data Extractor")

st.markdown("""
This Streamlit app helps you retrieve **wind, snow, and ice load data** from the  
[ASCE Hazard Tool](https://ascehazardtool.org/) for a given location.
""")

# --- Inputs ---
location = st.text_input("📍 Enter Location (Address, City, or Latitude/Longitude):")
asce_version = st.selectbox("📘 ASCE Code Edition:", ["ASCE 7-05", "ASCE 7-10", "ASCE 7-16", "ASCE 7-22"])
risk_category = st.selectbox("🏗️ Risk Category:", ["I", "II", "III", "IV"])
site_class = st.selectbox("🪨 Site Class (Soil Type):", ["A", "B", "C", "D", "E", "F"])

if st.button("Get Hazard Data"):
    if not location:
        st.error("Please enter a location.")
    else:
        # Construct base URL (for user reference)
        encoded_location = urllib.parse.quote(location)
        asce_code = asce_version.replace(" ", "")
        url = f"https://ascehazardtool.org/#/search?address={encoded_location}&edition={asce_code}"

        st.info(f"Querying ASCE Hazard Tool for **{location}** ...")

        # Try to fetch and parse the page
        try:
            response = requests.get(f"https://ascehazardtool.org/#/search?address={encoded_location}")
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # --- Parse Example ---
                # ASCE site uses dynamic JavaScript, so this static scrape might not work directly
                # We’ll display the live URL instead
                st.warning("ASCE Hazard Tool data is dynamically loaded, so scraping is not allowed. You can open the live page below.")
                st.markdown(f"[👉 Open ASCE Hazard Tool for {location}]({url})")
            else:
                st.error("Failed to retrieve data. Please check the location or try again later.")
        except Exception as e:
            st.error(f"Error connecting to ASCE Hazard Tool: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("⚙️ *Developed for educational use. ASCE Hazard data © ASCE.*")
