import streamlit as st
from PIL import Image

def run():
    st.title("📊 SHAP Feature Impact Dashboard")

    st.markdown("Use this section to understand which features most influence your credit risk predictions. Visual insights are combined with detailed explanations to support decision-making.")

    # Define layout: Image on left, Explanation on right
    col1, col2 = st.columns([1.2, 2])

    # SHAP Beeswarm Plot
    with col1:
        image = Image.open("deployment/shap.png")
        st.image(image, caption="📍 SHAP Beeswarm Plot", use_column_width=True)

    # Feature Explanation Table
    with col2:
        st.markdown("""
        ### 🔍 Feature Interpretations

        <style>
        th, td {
            padding: 6px 10px;
            text-align: left;
        }
        </style>

        <div style="overflow-x:auto">
        <table>
        <thead>
        <tr><th>📌 Feature</th><th>🧠 Interpretation</th></tr>
        </thead>
        <tbody>
        <tr><td><b>numerical_normal__age</b></td><td>Older individuals increase predicted risk, positively influencing output.</td></tr>
        <tr><td><b>numerical_skewed__years_employed</b></td><td>Shorter employment raises risk — signals job instability.</td></tr>
        <tr><td><b>numerical_skewed__education_income_ratio</b></td><td>Higher ratio implies under-earning given education level, increasing risk.</td></tr>
        <tr><td><b>income_per_person</b></td><td>Higher per capita income reduces risk, supporting creditworthiness.</td></tr>
        <tr><td><b>low_income_flag</b></td><td>Value 1 flags financial vulnerability, strongly driving up risk.</td></tr>
        <tr><td><b>financial_dependence_ratio</b></td><td>More dependents increase financial strain and elevate predictions.</td></tr>
        <tr><td><b>house_income_ratio</b></td><td>Mismatched home type vs income signals affordability pressure.</td></tr>
        <tr><td><b>categorical__occupation_Pensioner</b></td><td>Pensioner status increases risk — tied to income or age factors.</td></tr>
        <tr><td><b>months_balance</b></td><td>Account history shows moderate impact; may reflect payment behavior.</td></tr>
        <tr><td><b>phone</b></td><td>Low-variance feature, minor but consistent influence — possibly digital access.</td></tr>
        <tr><td><b>id</b></td><td>Unique identifier — excluded from predictive modeling.</td></tr>
        <tr><td><b>family_size</b></td><td>Larger families imply more financial responsibility, slightly increasing risk.</td></tr>
        <tr><td><b>child_number</b></td><td>Correlates with family size; may introduce redundancy in signals.</td></tr>
        <tr><td><b>categorical__gender_M</b></td><td>Binary gender variable with directional impact based on dataset.</td></tr>
        <tr><td><b>categorical__car_Y</b></td><td>Ownership may reflect financial status; contributes to prediction shift.</td></tr>
        <tr><td><b>categorical__realty_Y</b></td><td>Owning real estate often reduces predicted risk — signals stability.</td></tr>
        <tr><td><b>begin_month</b></td><td>Earlier account start may reflect financial reliability, lowering risk.</td></tr>
        </tbody>
        </table>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()