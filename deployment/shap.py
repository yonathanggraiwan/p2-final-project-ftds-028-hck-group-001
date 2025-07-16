import streamlit as st
import pandas as pd

from PIL import Image

def run():
    # Main content
    st.title("This is the SHAP section!")
    img_url = "shap.png"
    image = Image.open(img_url)
    st.image(image)

    st.markdown("""
    ### 🧠 SHAP Feature Interpretation (Full Feature Summary)

    | **Feature**                                     | **Interpretation**                                                                                                   |
    |-------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
    | numerical_normal__age                           | Older individuals push model output higher, indicating a positive correlation with predicted risk.                   |
    | numerical_skewed__years_employed                | Shorter employment duration increases risk; possibly reflects job instability.                                       |
    | numerical_skewed__education_income_ratio        | High education-to-income ratio may flag individuals with low earning relative to education, increasing predicted risk.|
    | income_per_person                               | Higher ratio implies better financial capacity per capita, reducing risk and increasing creditworthiness.            |
    | low_income_flag                                 | Value = 1 flags financial vulnerability; strong contributor to increased risk predictions.                           |
    | financial_dependence_ratio                      | More children or dependents elevate this ratio, signaling financial burden and increasing model output.              |
    | house_income_ratio                              | Mismatch between house type and income may reflect affordability concerns, impacting prediction.                     |
    | categorical__occupation_Pensioner               | Being a pensioner increases model prediction; likely linked to income stability or age effects.                      |
    | months_balance                                  | Affects model moderately; variation in account balance history can suggest payment habits.                           |
    | phone                                           | Minimal variance but still influences prediction directionally; may capture technological accessibility indirectly.  |
    | id                                              | Likely serves as a unique identifier; not meaningful for prediction and should be excluded from modeling.            |
    | family_size                                     | Larger families may imply greater financial responsibility, slightly increasing predicted risk.                      |
    | child_number                                    | Closely linked to family size; overlapping signal that can lead to multicollinearity.                                |
    | categorical__gender_M                           | May push predictions up or down depending on dataset context; shows clear directional impact as binary feature.       |
    | categorical__car_Y                               | Car ownership may reflect financial status; model learns potential affordability patterns from this binary signal.   |
    | categorical__realty_Y                            | Owning property might reduce perceived risk depending on context; shows direct impact on prediction.                 |
    | begin_month                                     | Older account start dates may reflect more reliable credit history, slightly reducing risk.                          |

    ---
    """, unsafe_allow_html=True)