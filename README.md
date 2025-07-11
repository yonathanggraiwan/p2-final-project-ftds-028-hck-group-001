# Credit Risk Analysis / Modelling

## Repository Outline

1. dataset > Dataset folder
    1. P2_FinPro_Applicant_Record_Raw.csv
    2. P2_FinPro_Credit_Record_Raw.csv
2. models > model pkl folder
    1. 
3. `EDA.ipynb`> Data Analysis
4. `load_data_postgres.ipynb` > ...
5. `README.md` > Context to project.

## Problem Background
When talking about finance, most of the industries working in the field are in the fields of banking, credit, and risk assessment. Every day, a large amount of loans are given out to customers daily. This creates lonng lines and long application periods. Employees and staff are also rushed to evaluate customer’s risk assesment and create misjudgements when evaluating a customer’s risk. When a customer’s risk assesment is done incorrectly, it can lead to healthy / risk free customers to not be given any loans and people that have a history of missing payments, be given loans. This creates a negative profits for the company and creates further issues when giving loans.

Therefore, it is important to have a computer model that can evaluate the customer’s credit risk to streamline the process of giving loans. By using computer models, the process of evaluating loans would be halved and more loans can be given out in a much more shorter time span. The risk of miscalculating the risk of a loan would be further reduced due to further verification using computer models.

## Project Output

1. Models :

    The project would output multiple different models to be evaluated and compared to each other. If the user wishes to use a different model to the ones already selected, the user can find the models in `models` folder.

2. Analysis :

    Analysis of the data is compiled in the `EDA.ipynb` where all the explenations of data and analysis would be inserted and can be viewed. The analysis can also be seen in our deployment in [Streamlit] or [HuggingFace]

## Possible Users : 
- Bankers
- Tellers
- Banks

## Datan

Link to dataset : https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction?select=application_record.csv

1. `P2_FinPro_Applicant_Record_Raw.csv`

    | Column                 | Explanation                   | Remarks                                                                 |
    |------------------------|-------------------------------|-------------------------------------------------------------------------|
    | ID                     | Client number                 |                                                                         |
    | CODE_GENDER            | Gender                        |                                                                         |
    | FLAG_OWN_CAR           | Is there a car                |                                                                         |
    | FLAG_OWN_REALTY        | Is there a property           |                                                                         |
    | CNT_CHILDREN           | Number of children            |                                                                         |
    | AMT_INCOME_TOTAL       | Annual income                 |                                                                         |
    | NAME_INCOME_TYPE       | Income category               |                                                                         |
    | NAME_EDUCATION_TYPE    | Education level               |                                                                         |
    | NAME_FAMILY_STATUS     | Marital status                |                                                                         |
    | NAME_HOUSING_TYPE      | Way of living                 |                                                                         |
    | DAYS_BIRTH             | Birthday                      | Count backwards from current day (0), -1 means yesterday                |
    | DAYS_EMPLOYED          | Start date of employment      | Count backwards from current day (0). If positive, currently unemployed |
    | FLAG_MOBIL             | Is there a mobile phone       |                                                                         |
    | FLAG_WORK_PHONE        | Is there a work phone         |                                                                         |
    | FLAG_PHONE             | Is there a phone              |                                                                         |
    | FLAG_EMAIL             | Is there an email             |                                                                         |
    | OCCUPATION_TYPE        | Occupation                    |                                                                         |
    | CNT_FAM_MEMBERS        | Family size                   |                                                                         |

2. `P2_FinPro_Credit_Record_Raw.csv`

    | Feature Name     | Explanation     | Remarks                                                                                                                                       |
    |------------------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
    | ID               | Client number   |                                                                                                                                               |
    | MONTHS_BALANCE   | Record month    | The month of the extracted data is the starting point, backwards. 0 = current month, -1 = previous month, and so on                          |
    | STATUS           | Status          | 0: 1–29 days past due<br>1: 30–59 days past due<br>2: 60–89 days overdue<br>3: 90–119 days overdue<br>4: 120–149 days overdue<br>5: Overdue or bad debts, write-offs for more than 150 days<br>C: Paid off that month<br>X: No loan for the month |

## Method
1. 

## Stacks
1. 

## Reference
1. 