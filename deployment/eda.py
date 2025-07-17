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
        "Is There a Relationship Between `years_employed` and `income`?",
        "How Many Customers Provide a Mobile Phone, Work Phone, or Email?",
        "What is the distribution of months_balance (if it refers to account history)?",
        "Does months_balance have an impact for credit_status",
        "Are there any suspiciously high child_number, income, or family_size values?",
        "Do extreme income values skew the distribution? Should they be capped or log-transformed?",
        "Which variables are most strongly correlated with the credit status? (numeric)",
        "Which variables are most strongly correlated with the credit status? (categorical)",
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
        custom_md("An investigation into whether certain occupations carry higher risk levels.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_4_1(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("Someone who is “working” has the highest number of credit applications, " \
        "totaling 400,000 submissions, followed by “commercial associate,” “pensioner,” “state servant,” " \
        "and “student.” Professional workers make up the largest group both in terms of applications and approvals, " \
        "indicating that being employed significantly boosts creditworthiness. " \
        "Commercial associates and pensioners also show high approval rates, likely due to their stable income and " \
        "consistent financial history. Meanwhile, state servants and students have lower approval rates, which may be " \
        "attributed to limited financial records due to age or stricter evaluation criteria—especially for students who " \
        "often lack a steady income.")
        st.markdown("---")

    elif eda_option == "Is There a Relationship Between `years_employed` and `income`?":
        custom_title("Is There a Relationship Between `years_employed` and `income`?")
        custom_md("An investigation into whether there is a relationship between a person's employment duration and their income level.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_4_2(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("From this scatter plot, we can identify a data outlier—a record showing someone had worked for 1000 years. " \
        "Upon investigation, this was an input error linked to a pensioner, and based on our assessment, the outlier will be " \
        "capped at 0 years of employment. Additionally, the plot shows no clear relationship between the length of employment "
        "and the amount of income earned.")
        st.markdown("---")

    elif eda_option == "How Many Customers Provide a Mobile Phone, Work Phone, or Email?":
        custom_title("How Many Customers Provide a Mobile Phone, Work Phone, or Email?")
        custom_md("Examining communication channel availability.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_5_1(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("Everyone who wants to apply for credit fills out their personal information, " \
        "including email, mobile phone, and work phone.")
        st.markdown("---")

    elif eda_option == "What is the distribution of months_balance (if it refers to account history)?":
        custom_title("What is the distribution of months_balance (if it refers to account history)?")
        custom_md("Analyzing the data distribution based on months_balance.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_6_1(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("The fewest transactions occurred in the earliest period, around five years ago, and have steadily " \
        "increased up to the present month (0).")
        st.markdown("---")

    elif eda_option == "Does months_balance have an impact for credit_status":
        custom_title("Does months_balance have an impact for credit_status")
        custom_md("Analyzing whether the length of months_balance has an impact on credit_status.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_6_2(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("From this, we can observe that the proportion between NPL status and Good Credit tends to be " \
        "more favorable when the credit tenure history is short. As the tenure increases, the proportion of NPL cases " \
        "gradually follows the trend of Good Credit, indicating a potential risk alignment over time.")
        st.markdown("---")

    elif eda_option == "Are there any suspiciously high child_number, income, or family_size values?":
        custom_title("Are there any suspiciously high child_number, income, or family_size values?")
        custom_md("Outlier detection for key demographic variables.")
        st.markdown("---")
        custom_title("Graph")
        pl.EDA_7_1(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("The majority of applicants fall under child number categories of having no children or just one, " \
        "although there are outliers showing as many as 13 or even 18 children. Regarding income, most submissions " \
        "report earnings between €100,000 and €250,000, with outliers reaching up to €1,600,000. As for family size, " \
        "the typical household consists of 2 to 3 members. This column also contains outliers—such as a family size " \
        "of 20—driven by the presence of up to 18 children. Feature engineering was not applied to any of these three columns. " \
        "Income is left as-is since it reflects each individual's earning power, while the outliers in child_number and " \
        "family_size are not capped or removed due to their minimal proportion in the dataset.")
        st.markdown("---")

    elif eda_option == "Do extreme income values skew the distribution? Should they be capped or log-transformed?":
        custom_title("Do extreme income values skew the distribution? Should they be capped or log-transformed?")
        custom_md("Exploring transformation strategies for skewed variables.")
        st.markdown("---")
        custom_title("Statistical Calculation Results")
        pl.EDA_7_2(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("In statistical analysis, a skewness value between -2 and +2 is generally acceptable for distributions " \
        "approaching normality, as suggested by Hair et al. (2010) and George & Mallery (2010). Since the skewness of the " \
        "income column is 2.58, it indicates a strong right skew, likely caused by extreme outlier values significantly " \
        "higher than the mean, however, no capping or outlier handling is applied, as the values in this column directly " \
        "represent an individual's actual income.")
        st.markdown("---")

    elif eda_option == "Which variables are most strongly correlated with the credit status? (numeric)":
        custom_title("Which variables are most strongly correlated with the credit status? (numeric)")
        custom_md("Exploring which numerical column has the strongest correlation with a person’s credit status.")
        st.markdown("---")
        custom_title("Statistical Calculation Results")
        pl.EDA_8_1_1(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("Among the numerical columns, only one—days_employed, which reflects how long someone has been " \
        "employed—shows no correlation with credit_status. All other numerical columns do exhibit some correlation " \
        "with credit_status, although the strength of those correlations remains weak, not even reaching a value of 0.1. " \
        "This is evident from the p-value and Spearman correlation table shown above.")
        st.markdown("---")

    elif eda_option == "Which variables are most strongly correlated with the credit status? (categorical)":
        custom_title("Which variables are most strongly correlated with the credit status? (categorical)")
        custom_md("Exploring which categorical column has the strongest correlation with a person’s credit status.")
        st.markdown("---")
        custom_title("Statistical Calculation Results")
        pl.EDA_8_1_2(data)
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("The categorical column with the strongest correlation to credit_status is the payment status column. " \
        "If an individual’s payments are smooth and on time, they are more likely to have a good credit status, conversely, " \
        "delayed or inconsistent payments tend to align with a poor status or NPL. Aside from this column, all other " \
        "categorical features show weak correlations with credit_status.")
        st.markdown("---")

    elif eda_option == "Is there multicollinearity that could affect model reliability later on?":
        custom_title("Is there multicollinearity that could affect model reliability later on?")
        custom_md("Variance Inflation Factor (VIF) analysis.")
        st.markdown("---")
        custom_title("Statistical Calculation Results")
        pl.EDA_8_2(data) 
        st.markdown("---")
        custom_title("Conclusion")
        custom_md("In regression analysis, VIF values below 5 are generally considered acceptable, as noted by " \
        "James et al. (2013) and Menard (2001), while values above 10 are regarded as signs of serious " \
        "multicollinearity that can hinder model interpretation. From the processed data, the column with " \
        "the highest VIF was mobile_phone, which contained only the value 1 for all records, indicating that " \
        "every applicant listed a mobile phone. Since this column does not contribute meaningful information to " \
        "the model, it was excluded from the prediction process.")
        st.markdown("---")

if __name__ == "__main__":
    show()