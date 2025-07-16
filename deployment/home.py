import streamlit as st
import pandas as pd

from PIL import Image

def run():
    # Main content
    st.title("Welcome!")
    # img_url = "homepictfinpro.jpg"
    # image = Image.open(img_url)
    # st.image(image)

    # Dashboard Introduction
    st.markdown("""
    ### What is this Dashboard?

    This interactive dashboard explains about predicting the customer application on credit card. This dashboard have 4 sidebar, which is: "Home", "EDA", "Prediction" section.
    

    ---
    ### Background Problem
    The background problem from this project is

    ---
    ### Model
    The model that being used in this project is KNN, Decision Tree, Random Forest, XGBoost, LGBM (Light Gradient Boosting), and Hist Gradient Boosting.
    For the inference and model deployment, the best algorithm is LGBM (Light Gradient Boosting) which has the highest score in recall metrics with the lowest model size.
    
    ---
    """)

    # Dataset
    st.markdown("""
    ### Dataset
    The dataset used is sourced from **Kaggle**, titled **[Credit Card Approval Prediction](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction)**.
    """)

    # How to use Dashboard
    st.markdown("""
    ---
    ### How to use the Dashboard
    - Click on the options in the **sidebar** to explore EDA, make predictions or looking for the SHAP (SHapley Additive exPlanations) section.
    - Try uploading various data samples to get different results.

    Thank you for visiting this dashboard. See you again next time!
                
    ---
    """)
    
if __name__ == "__main__":
    run()