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
    
    if eda_option == "Average Prices of Used Cars by Brand":
        custom_title("Average Prices of Used Cars by Brand")
        st.markdown("---")
        custom_title("Graph")
        pl.avg_price_by_brand(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("Ford and BMW cars are on average the most expensive cars compared to others. By nationality, Asian-branded cars to the likes of : Honda, Hyundai, Toyota, Kia, and Nissan is on hsa lower average prices compared to other regions. Tesla has the lowest average resale price, this could be caused by the high depreciation value of electric cars when the cars are being resold on the market.")
    
    elif eda_option == "Car Mileage Effect on Car Prices":
        custom_title("Car Mileage Effect on Car Prices")
        custom_md("Does the Mileage of the car affect it's resale value?")
        st.markdown("---")
        custom_title("Background")
        custom_md("Car Mileage refers to the distance the car can reach using a full tank of gas. This metric is measured by using kmpl (Kilometres per Litre). The mileage of a car is an important factor for customers to decide their choice of car. Cars with shorter mileages are often used for city commutes, while cars with longer mileages are usually used for longer road trips or interstate driving. It is also important factor due to the assurance of safety for the customers, since longer mileages would ensure the customer wouldn't need to worry about constantly refueling their cars or having to stop due to coming short on a gas station. Our local dealership wants to analyze the relationship between prices and the car's mileage. The relationship between the two metrics can help the dealership decide on how to price the cars.")
        st.markdown("---")
        custom_title("Graph")
        pl.mileage_effect_car_prices(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("Based on the graph above, the data doesn't show adequate relationship between the increase in mileage to the price of the car. But added with the correlation test that is done and has resulted in a 0.20 correlation score, we can conclude that the mileage of the car has a weak positive relationship with the price of the car.")