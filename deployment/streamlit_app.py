import streamlit as st
import home, prediction, eda

st.set_page_config(page_title = "Credit Risk Analysis & Modelling",
                   layout = 'centered',
                   initial_sidebar_state = 'expanded')
with st.sidebar:
    st.write('# Navigation Sidebar')
    navigation = st.radio('Page', ['Home', 
                                   'Exploratory Data Analysis (EDA) Section', 
                                   'Credit Risk Analysis Prediction Section'])

if navigation == 'Exploratory Data Analysis (EDA) Section':
    eda.show()

if navigation == 'Credit Risk Analysis Prediction Section':
    prediction.run()

if navigation == 'Home':
    home.run()

else:
    home.run()