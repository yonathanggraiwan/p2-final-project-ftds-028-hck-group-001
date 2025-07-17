import streamlit as st
import pandas as pd

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
    Since the invention of currency, loans has always been part of the economy. From lending to corporations, to loaning a singular person. Lending to a single person is called a **personal loan**. A personal loan is a type of installment credit issued to a borrower by a lender, such as a bank, credit union, or online lender. Personal loans allow the client to use the loan funds for practically any purpose, such as home renovations, medical expenses, vacations, and large purchases. They're offered by traditional lenders like banks and credit unions as well as nontraditional sources, such as online lenders (Lake, 2023). To assess how trustworthy the client is, lenders can usually determine if it's safe or not by assessing the client's **credit risks**.

    When assessing credit risks, analysts use the 5 C's of credit : Character, Capacity, Capital, Collateral, and Conditions. **Character** refers to the client's credit history, or how the client have managed debt in the past. **Capacity** refers to the client's ability to repay loans. **Capital** includes the savings, investments, and assets you are willing to put toward a loan. **Collateral** is something the client can provide as security, typically for a secured loan or secured credit card. **Conditions** include other information that helps determine whether the client qualify for credit and the terms your receive (Capital One, 2024).

    Since these 5 C's significantly take time for analysts to analyze, therefore, it is important to have a computer model that can evaluate the customer’s credit risk to streamline the process of giving loans. By using computer models, the process of evaluating loans would be halved and more loans can be given out in a much more shorter time span. The risk of miscalculating the risk of a loan would be further reduced due to further verification using computer models.

    Our research and analysis is further reinforced a research article done by R. Balina & M. Idasz-Balina outlining the [Drivers of Individual Credit Risk of Retail Customers](https://doi.org/10.3390/risks9120219) where the article outlines the factors and example use cases of modelling and the factors that can determine the credit risk of a customer based on other factors other than the 5 C's outlined above (Balina & Idasz-Balina, 2021).

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
    - Click on the options in the **sidebar** to explore EDA and make predictions 
    - Try uploading various data samples to get different results.

    Thank you for visiting this dashboard. See you again next time!
                
    ---
    """)
    
if __name__ == "__main__":
    run()