import streamlit as st

def run():
    # HEADER SECTION
    st.markdown("<h1 style='font-size: 62px;text-align: center;'>Welcome to Credify!</h1>", unsafe_allow_html=True)
    
    # Project logo/image
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("credify.png", width=300) 

    # Introduction paragraph
    paragraph1 = "This interactive dashboard provides an end-to-end view of our credit scoring project, focusing on predicting whether a customer is eligible for a credit card based on key financial and demographic information."
    st.markdown(
        f"""
        <style>
        .paragraph {{
            text-align: justify;
            font-size: 16px;
            line-height: 1.6;
        }}
        </style>
        <p class="paragraph">{paragraph1}</p>
        """,
        unsafe_allow_html=True
    )

    # PROJECT DEFINITION SECTION
    st.header("What is Credify?")
    paragraph2 = "Credify is a credit classification system developed to help financial institutions evaluate the creditworthiness of new applicants. Using historical data and machine learning models, Credify can accurately classify whether an applicant is likely to be a Good Credit holder or fall into Non-Performing Loan (NPL) risk."
    st.markdown(
        f"""
        <style>
        .paragraph {{
            text-align: justify;
            font-size: 16px;
            line-height: 1.6;
        }}
        </style>
        <p class="paragraph">{paragraph2}</p>
        """,
        unsafe_allow_html=True
    )

    # HOW IT WORKS SECTION
    st.write("<h1 style='font-size: 20px;'>How does it work?</h1>", unsafe_allow_html=True)
    st.write("""
    **Credit Risk Prediction**: The system classifies new applicants into either:
    - **Good Credit**: Eligible for credit card approval.
    - **Non-Performing Loan (NPL)**: High risk and ineligible for approval.
    """)

    # TOOLS SECTION
    st.write("<h1 style='font-size: 20px;'>Tools for model development:</h1>", unsafe_allow_html=True)
    st.write("""
    - **Machine Learning Algorithms**: We experimented with K-Nearest Neighbors (KNN), Decision Tree, Random Forest, XGBoost, LightGBM, and HistGradientBoosting.  
      The best performing model was **Light Gradient Boosting (LGBM)** with the highest recall and the smallest model size.
    - **Streamlit**: Used to build and deploy the interactive web application.
    """)

    # FEATURES SECTION
    st.write("<h1 style='font-size: 20px;'>Features:</h1>", unsafe_allow_html=True)
    st.write("""
    - **About Our Team**: Meet the aspiring data team behind this project.        
    - **Exploratory Data Analysis (EDA)**: Dive into data distributions, correlations, and key findings from the dataset.
    - **Prediction**: Upload your own credit application data (.xlsx) to receive an instant credit risk classification.
    """)

    # HOW TO USE SECTION
    st.write("<h1 style='font-size: 20px;'>How to Use This App?</h1>", unsafe_allow_html=True)
    paragraph3 = "Explore the **EDA section** to learn more about the data we used and the patterns we uncovered. Then, try the **Prediction** tab by uploading an Excel file of your own applicants to see how our model evaluates their credit risk."
    st.markdown(paragraph3)


if __name__ == "__main__":
    run()