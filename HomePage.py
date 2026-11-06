# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Homepage",  # The title that appears in the browser tab
    page_icon="🏠",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Web Development Lab02 📊")
st.write("### Most Streamed Songs 🎵")
# INTRODUCTORY TEXT
st.write("""
This application looks at the top streamed songs from Spotify's database and inputs data into a chart and graph

### How to use this app:
- **Survey Page**: Go here to add more streams into the database.
- **Visuals Page**: Go here to see the data visualized in different graphs (scatter plot and bar chart).

This project is part of CS 1301 Lab 2.

William Grijalva
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
