# Credit Risk Analysis / Modelling

## Repository Outline

1. dataset > Dataset folder
    1. `P2_FinPro_Applicant_Record_Raw.csv` > Applicant Record CSV
    2. `P2_FinPro_Credit_Record_Raw.csv` > Credit Record of Applicant CSV
    3. `P2_FinPro_Final_Record.csv` > Final CSV used for EDA and modelling.
2. `EDA.ipynb`> Data Analysis
3. `FE_Local.ipynb` > Feature Engineering using Local CSV files
4. `FE_Postgres.ipynb` > Feature Engineering using Postgres as file storage
5. `inference.ipynb` > Inference file, prooving model
6. `inference.py` > Python file used for inference
7. `model_terbaik.pkl` > model results
8. `README.md` > Context to project.
9. `training.ipynb` > IPYNB used for training
10. `vintage_analysis.ipynb` > ipynb used for vintage analysis

## Problem Background

Since the invention of currency, loans has always been part of the economy. From lending to corporations, to loaning a singular person. Lending to a single person is called a **personal loan**. A personal loan is a type of installment credit issued to a borrower by a lender, such as a bank, credit union, or online lender. Personal loans allow the client to use the loan funds for practically any purpose, such as home renovations, medical expenses, vacations, and large purchases. They're offered by traditional lenders like banks and credit unions as well as nontraditional sources, such as online lenders (Lake, 2023). To assess how trustworthy the client is, lenders can usually determine if it's safe or not by assessing the client's **credit risks**.

When assessing credit risks, analysts use the 5 C's of credit : Character, Capacity, Capital, Collateral, and Conditions. **Character** refers to the client's credit history, or how the client have managed debt in the past. **Capacity** refers to the client's ability to repay loans. **Capital** includes the savings, investments, and assets you are willing to put toward a loan. **Collateral** is something the client can provide as security, typically for a secured loan or secured credit card. **Conditions** include other information that helps determine whether the client qualify for credit and the terms your receive (Capital One, 2024).

Since these 5 C's significantly take time for analysts to analyze, therefore, it is important to have a computer model that can evaluate the customer’s credit risk to streamline the process of giving loans. By using computer models, the process of evaluating loans would be halved and more loans can be given out in a much more shorter time span. The risk of miscalculating the risk of a loan would be further reduced due to further verification using computer models.

Our research and analysis is further reinforced a research article done by R. Balina & M. Idasz-Balina outlining the [Drivers of Individual Credit Risk of Retail Customers](https://doi.org/10.3390/risks9120219) where the article outlines the factors and example use cases of modelling and the factors that can determine the credit risk of a customer based on other factors other than the 5 C's outlined above (Balina & Idasz-Balina, 2021).

## Project Output

1. Models :

    The project would output multiple different models to be evaluated and compared to each other. If the user wishes to use a different model to the ones already selected, the user can find the models in `models` folder.

2. Analysis :

    Analysis of the data is compiled in the `EDA.ipynb` where all the explenations of data and analysis would be inserted and can be viewed. The analysis can also be seen in our deployment in [Streamlit] or [HuggingFace]

## Possible Users :

- Bankers
- Tellers
- Banks

## Data

Link to dataset : https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction?select=application_record.csv

1. `P2_FinPro_Applicant_Record_Raw.csv`

    | Column              | Explanation              | Remarks                                                                 |
    |---------------------|--------------------------|-------------------------------------------------------------------------|
    | ID                  | Client number            |                                                                         |
    | CODE_GENDER         | Gender                   |                                                                         |
    | FLAG_OWN_CAR        | Is there a car           |                                                                         |
    | FLAG_OWN_REALTY     | Is there a property      |                                                                         |
    | CNT_CHILDREN        | Number of children       |                                                                         |
    | AMT_INCOME_TOTAL    | Annual income            |                                                                         |
    | NAME_INCOME_TYPE    | Income category          |                                                                         |
    | NAME_EDUCATION_TYPE | Education level          |                                                                         |
    | NAME_FAMILY_STATUS  | Marital status           |                                                                         |
    | NAME_HOUSING_TYPE   | Way of living            |                                                                         |
    | DAYS_BIRTH          | Birthday                 | Count backwards from current day (0), -1 means yesterday                |
    | DAYS_EMPLOYED       | Start date of employment | Count backwards from current day (0). If positive, currently unemployed |
    | FLAG_MOBIL          | Is there a mobile phone  |                                                                         |
    | FLAG_WORK_PHONE     | Is there a work phone    |                                                                         |
    | FLAG_PHONE          | Is there a phone         |                                                                         |
    | FLAG_EMAIL          | Is there an email        |                                                                         |
    | OCCUPATION_TYPE     | Occupation               |                                                                         |
    | CNT_FAM_MEMBERS     | Family size              |                                                                         |

2. `P2_FinPro_Credit_Record_Raw.csv`

    | Feature Name     | Explanation     | Remarks                                                                             |
    |------------------|-----------------|-------------------------------------------------------------------------------------|
    | ID               | Client number   |                                                                                     |
    | MONTHS_BALANCE   | Record month    | The month of the extracted data is the starting point, backwards. 0 = current month, -1 = previous month, and so on            |
    | STATUS           | Status          | 0: 1–29 days past due<br>1: 30–59 days past due<br>2: 60–89 days overdue<br>3: 90–119 days overdue<br>4: 120–149 days overdue<br>5: Overdue or bad debts, write-offs for more than 150 days<br>C: Paid off that month<br>X: No loan for the month |

## Method

1. [RandomForestClassifier](https://www.geeksforgeeks.org/dsa/random-forest-classifier-using-scikit-learn/)

    Random Forest is a method that combines the predictions of multiple decision trees to produce a more accurate and stable result. It can be used for both classification and regression tasks. In classification tasks, Random Forest Classification predicts categorical outcomes based on the input data. It uses multiple decision trees and outputs the label that has the maximum votes among all the individual tree predictions.

## Stacks

1. 

## Reference

1.  Balina, R., & Idasz-Balina, M. (2021). Drivers of Individual Credit Risk of Retail Customers—A Case Study on the Example of the Polish Cooperative Banking Sector. Risks, 9(12), 219. https://doi.org/10.3390/risks9120219
2.  Capital One. (2024, February 8). What Are the 5 C’s of Credit? Capital One. https://www.capitalone.com/learn-grow/money-management/five-cs-of-credit/
3.  The Investopedia Team. (2024, September 23). Credit Risk: Definition, Role of Ratings, and Examples. Investopedia. https://www.investopedia.com/terms/c/creditrisk.asp
4.  Wells Fargo. (2019). Five Cs of Credit - What Lenders Look For - Wells Fargo. Wellsfargo.com. https://www.wellsfargo.com/financial-education/credit-management/five-c/
5. Lake, R. (2023, December 8). Personal Loan. Investopedia. https://www.investopedia.com/personal-loan-5076027
