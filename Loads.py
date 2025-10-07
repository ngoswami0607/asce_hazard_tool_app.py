import streamlit as st
import urllib.parse

st.set_page_config(page_title="ASCE Hazard Tool Finder", layout="centered")

st.title("🌪️ ASCE Hazard Tool Data Finder")

st.markdown("""
Use this app to quickly generate a direct ASCE Hazard Tool query  
to get **wind, snow, and ice load data** for your project location.
""")

# User inputs
location = st.text_input("📍 Enter Project Location (Address, City, or Lat,Long):")
asce_version = st.selectbox("📘 ASCE Code Edition:", ["ASCE 7-05", "ASCE 7-10", "ASCE 7-16", "ASCE 7-22"])
risk_category = st.selectbox("🏗️ Risk Category:", ["I", "II", "III", "IV"])
site_class = st.selectbox("🪨 Site Class (Soil Type):", ["A", "B", "C", "D", "E", "F"])

if st.button("🔍 Generate ASCE Hazard Tool Link"):
    if not location:
        st.error("Please enter a location.")
    else:
        encoded_location = urllib.parse.quote(location)
        # Remove spaces from ASCE version for URL
        asce_code = asce_version.replace(" ", "")
        url = f"https://ascehazardtool.org/#/search?address={encoded_location}&edition={asce_code}"

        st.success(f"✅ Click below to view results for **{location}**")
        st.markdown(f"[Open ASCE Hazard Tool →]({url})")

st.markdown("---")
st.caption("⚙️ This app does not scrape or store data — it only generates the official ASCE Hazard Tool link.")
