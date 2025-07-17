import streamlit as st
import pandas as pd
import numpy as np
import plots as pl

data = pd.read_csv("dataset\P2_FinPro_Final_Record.csv") # Input the CSV read file here

def show():
    st.title("Exploratory Data Analysis")
    
    st.markdown("""
    <style>
    .custom-base {
    text-align: center;
    color: white;
    padding: 12px;
    border-radius: 8px;
    width: 100%;
    box-sizing: border-box;
    }
    .custom-markdown {
        background-color: #2c2f33;
            font-size: 16px;
    }
    .custom-title {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)
    
    def custom_md(text):
        st.markdown(f"<div class='custom-base custom-markdown'>{text}</div>", unsafe_allow_html=True)
    def custom_title(text):
        st.markdown(f"<h3 class='custom-base custom-title'>{text}</h3>", unsafe_allow_html=True)
    
    eda_option = st.selectbox("Select EDA Plot :", [
        "Approved vs Declined Credit Applications",
        "Approval by Age",
        "Years Employed vs Credit Approval Status",
        "Car Ownership / House Ownership vs Credit Approval",
        "Occupation vs Credit Acceptance",
        "Which gender dominates the applicant pool and does that affect approval rates?",
        "Do maritial status or family size impact credit approval or target outcomes?",
        "Are customers with children more likely to default or be denied?",
        "What is the average age of applicants? How does age correlate with approval?",
        "Do single vs married applicants show different patterns of repayment?",
        "What house types are most common among applicants, and how do they relate to approval?",
        "Are real estate owners less risky as borrowers?",
        "Are Applicants From Certain Occupations More Likely To Default?",
        "Is There a Relationship Between `years_employed` and `income` or `target`?",
        "How Many Customers Provide a Mobile Phone, Work Phone, or Email?",
        "What is the distribution of months_balance (if it refers to account history)?",
        "Does months_balance provide insight into credit recency or tenure? / Does begin_months have an impact for credit_status",
        "Do longer account histories correlate with approval or reduced risk?",
        "Are there any suspiciously high child_number, income, or family_size values?",
        "Do extreme income values skew the distribution? Should they be capped or log-transformed?",
        "Which variables are most strongly correlated with the target or credit approval?",
        "Is there multicollinearity that could affect model reliability later on?",
    ])
    
    if eda_option == "Approved vs Declined Credit Applications":
        custom_title("Approved vs Declined Credit Applications")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_1_1(data)

    elif eda_option == "Approval by Age":
        custom_title("Approval by Age")
        custom_md("Are certain age groups more likely to be approved for credit?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_1_2(data)

    elif eda_option == "Years Employed vs Credit Approval Status":
        custom_title("Years Employed vs Credit Approval Status")
        custom_md("Does job tenure impact the likelihood of getting approved?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_1_3(data)

    elif eda_option == "Car Ownership / House Ownership vs Credit Approval":
        custom_title("Car Ownership / House Ownership vs Credit Approval")
        custom_md("Does owning a car or house influence credit decisions?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_1_4(data)

    elif eda_option == "Occupation vs Credit Acceptance":
        custom_title("Occupation vs Credit Acceptance")
        custom_md("Are some jobs more likely to be approved than others?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_1_5(data)

    elif eda_option == "Which gender dominates the applicant pool and does that affect approval rates?":
        custom_title("Which gender dominates the applicant pool and does that affect approval rates?")
        custom_md("Analyzing gender distribution and approval rates.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_2_1(data)

    elif eda_option == "Do maritial status or family size impact credit approval or target outcomes?":
        custom_title("Do maritial status or family size impact credit approval or target outcomes?")
        custom_md("Does having a spouse or large family affect approval?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_2_2(data)

    elif eda_option == "Are customers with children more likely to default or be denied?":
        custom_title("Are customers with children more likely to default or be denied?")
        custom_md("Assessing risk and approval by child count.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_2_3(data)

    elif eda_option == "What is the average age of applicants? How does age correlate with approval?":
        custom_title("What is the average age of applicants? How does age correlate with approval?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_2_4(data)

    elif eda_option == "Do single vs married applicants show different patterns of repayment?":
        custom_title("Do single vs married applicants show different patterns of repayment?")
        custom_md("Comparing default rates across marital status.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_2_5(data)

    elif eda_option == "What house types are most common among applicants, and how do they relate to approval?":
        custom_title("What house types are most common among applicants, and how do they relate to approval?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_3_1(data)

    elif eda_option == "Are real estate owners less risky as borrowers?":
        custom_title("Are real estate owners less risky as borrowers?")
        custom_md("Assessing risk or approval status among property owners.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_3_2(data)

    elif eda_option == "Are Applicants From Certain Occupations More Likely To Default?":
        custom_title("Are Applicants From Certain Occupations More Likely To Default?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_4_1(data)

    elif eda_option == "Is There a Relationship Between `years_employed` and `income` or `target`?":
        custom_title("Is There a Relationship Between `years_employed` and `income` or `target`?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_4_2(data)

    elif eda_option == "How Many Customers Provide a Mobile Phone, Work Phone, or Email?":
        custom_title("How Many Customers Provide a Mobile Phone, Work Phone, or Email?")
        custom_md("Examining communication channel availability.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_5_1(data)

    elif eda_option == "What is the distribution of months_balance (if it refers to account history)?":
        custom_title("What is the distribution of months_balance (if it refers to account history)?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_6_1(data)

    elif eda_option == "Does months_balance provide insight into credit recency or tenure? / Does begin_months have an impact for credit_status":
        custom_title("Does months_balance provide insight into credit recency or tenure? / Does begin_months have an impact for credit_status")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_6_2(data)

    elif eda_option == "Do longer account histories correlate with approval or reduced risk?":
        custom_title("Do longer account histories correlate with approval or reduced risk?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_6_3(data)

    elif eda_option == "Are there any suspiciously high child_number, income, or family_size values?":
        custom_title("Are there any suspiciously high child_number, income, or family_size values?")
        custom_md("Outlier detection for key demographic variables.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_7_1(data)

    elif eda_option == "Do extreme income values skew the distribution? Should they be capped or log-transformed?":
        custom_title("Do extreme income values skew the distribution? Should they be capped or log-transformed?")
        custom_md("Exploring transformation strategies for skewed variables.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_7_2(data)

    elif eda_option == "Which variables are most strongly correlated with the target or credit approval?":
        custom_title("Which variables are most strongly correlated with the target or credit approval?")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_8_1(data)

    elif eda_option == "Is there multicollinearity that could affect model reliability later on?":
        custom_title("Is there multicollinearity that could affect model reliability later on?")
        custom_md("Variance Inflation Factor (VIF) analysis.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_8_2(data)

if __name__ == "__main__":
    show()