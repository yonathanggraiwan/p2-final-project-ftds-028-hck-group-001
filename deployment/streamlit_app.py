import streamlit as st
from PIL import Image
import home, prediction, eda, profile_page

st.set_page_config(page_title = "Credit Loan Prediction with Credify",
                   layout = 'centered',
                   initial_sidebar_state = 'expanded')
with st.sidebar:
    
    logo = Image.open("deployment/credify.png")
    st.sidebar.image(logo, width=80)
    st.write('# Navigation Sidebar')
    navigation = st.radio('Page', ['Home', 
                                   'About our Team',
                                   'Exploratory Data Analysis (EDA)', 
                                   'Credit Risk Analysis Prediction'])

if navigation == 'Exploratory Data Analysis (EDA)':
    eda.show()

if navigation == 'Credit Risk Analysis Prediction':
    prediction.run()

if navigation == 'About our Team':
    profile_page.show()

if navigation == 'Home':
    home.run()