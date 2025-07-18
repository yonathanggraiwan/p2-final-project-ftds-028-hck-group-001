import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr
from scipy.stats import chi2_contingency
from statsmodels.tools import add_constant
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy.stats import skew

import streamlit as st


def custom_md(text):
    st.markdown(f"<div class='custom-base custom-markdown'>{text}</div>", unsafe_allow_html=True)
def custom_title(text):
    st.markdown(f"<h3 class='custom-base custom-title'>{text}</h3>", unsafe_allow_html=True)

def EDA_1_1 (data):
    plt.figure(figsize = (6,4))
    sns.countplot(x = "credit_status", data = data, palette = "Set2")
    plt.title("Distribution of Credit Approval")
    plt.xlabel("Credit Approval Status")
    plt.ylabel("Number of Applicants")
    plt.tight_layout()
    st.pyplot(plt)

def EDA_1_2 (data):
    data["age"] = (-data["days_birth"]) // 365
    plt.figure(figsize=(6, 4))
    sns.barplot(x='credit_status', y='age', data=data, estimator='mean', ci=None, palette='Set2')
    plt.title('Average Age by Credit Approval')
    plt.xlabel('Credit Approval Status')
    plt.ylabel('Average Age')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_1_3 (data):
    data['years_employed'] = data['days_employed'].apply(lambda x: 0 if x == 365243 else -x // 365)
    plt.figure(figsize=(6, 4))
    sns.barplot(x='credit_status', y='years_employed', data=data, estimator='mean', ci=None, palette='Set2')
    plt.title('Average Years Employed by Credit Approval')
    plt.xlabel('Credit Approval')
    plt.ylabel('Years Employed')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_1_4 (data):
    car_approval = data.groupby('car')['credit_status'].value_counts(normalize=True).unstack()
    realty_approval = data.groupby('realty')['credit_status'].value_counts(normalize=True).unstack()
    
    car_approval["Good Credit"].plot(kind='bar', color='green')
    plt.title('Approval Rate by Car Ownership')
    plt.xlabel('Owns a Car')
    plt.ylabel('Approval Rate')
    plt.xticks(rotation=0)
    plt.ylim(0, 1)
    plt.tight_layout()
    st.pyplot(plt)
    
    realty_approval["Good Credit"].plot(kind='bar', color='blue')
    plt.title('Approval Rate by Realty Ownership')
    plt.xlabel('Owns Real Estate')
    plt.ylabel('Approval Rate')
    plt.xticks(rotation=0)
    plt.ylim(0, 1)
    plt.tight_layout()
    st.pyplot(plt)

def EDA_1_5 (data):
    default_rates = data.groupby('occupation')['target'].mean().sort_values()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=default_rates.values, y=default_rates.index, palette='coolwarm')
    plt.title('Default Risk by Occupation Type')
    plt.xlabel('Average Default Rate (target)')
    plt.ylabel('Occupation')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_2_1 (data):
    # Countplot
    sns.countplot(x='gender', data=data, palette='Set2')
    plt.title('Gender Distribution of Applicants')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.tight_layout()
    st.pyplot(plt)
    
    approval_by_gender = data.groupby('gender')['credit_status'].value_counts(normalize=True).unstack()

    approval_by_gender[["Good Credit", "NPL"]].plot(kind='bar', stacked=True, colormap='Set2')
    plt.title('Credit Approval Rate by Gender')
    plt.ylabel('Proportion')
    plt.xlabel('Gender')
    plt.legend(title='Credit Approval')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_2_2 (data):
    
    # Maritial Status
    
    approval_by_marital = data.groupby('marital_status')['credit_status'].value_counts(normalize=True).unstack()
    default_by_marital = data.groupby('marital_status')['target'].mean().sort_values()
    # Approval Rate
    approval_by_marital['Good Credit'].plot(kind='bar', color='green', title='Approval Rate by Marital Status')
    plt.ylabel('Approval Rate')
    plt.tight_layout()
    st.pyplot(plt)

    # Default Risk
    default_by_marital.plot(kind='bar', color='red', title='Default Rate by Marital Status')
    plt.ylabel('Default Rate')
    plt.tight_layout()
    st.pyplot(plt)
    
    # Family Size
    data['family_size_group'] = pd.cut(data['family_size'], bins=[0,1,2,3,5,10], labels=['1','2','3','4-5','6+'])
    
    # Credit approval rate by family size
    approval_by_family = data.groupby('family_size_group')['credit_status'].value_counts(normalize=True).unstack()
    # Default risk by family size
    default_by_family = data.groupby('family_size_group')['target'].mean()
    
    # Approval rate plot
    approval_by_family['Good Credit'].plot(kind='bar', color='blue', title='Approval Rate by Family Size')
    plt.ylabel('Approval Rate')
    plt.xlabel('Family Size')
    plt.tight_layout()
    st.pyplot(plt)

    # Default rate plot
    default_by_family.plot(kind='bar', color='orange', title='Default Rate by Family Size')
    plt.ylabel('Default Rate')
    plt.xlabel('Family Size')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_2_3 (data):
    data['has_children'] = data['child_number'] > 0
    
    approval_by_children = data.groupby('has_children')['credit_status'].value_counts(normalize=True).unstack()
    approval_by_children['Good Credit'].plot(kind='bar', color='green', title='Approval Rate by Child Status')
    plt.xticks([0, 1], ['No Children', 'Has Children'], rotation=0)
    plt.ylabel('Approval Rate')
    plt.tight_layout()
    st.pyplot(plt)
    
    default_by_children = data.groupby('has_children')['target'].mean()
    
    default_by_children.plot(kind='bar', color='red', title='Default Rate by Child Status')
    plt.xticks([0, 1], ['No Children', 'Has Children'], rotation=0)
    plt.ylabel('Default Rate')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_2_4 (data):
    average_age = data['age'].mean()
    
    data['approval_numeric'] = data['credit_status'].map({'Good Credit': 1, 'NPL': 0})
    correlation = data[['age', 'approval_numeric']].corr().loc['age', 'approval_numeric']
    
    data['age_group'] = pd.cut(data['age'], bins=[20,30,40,50,60,70], labels=['20s','30s','40s','50s','60s'])

    approval_by_age = data.groupby('age_group')['approval_numeric'].mean()

    approval_by_age.plot(kind='bar', color='skyblue', title='Approval Rate by Age Group')
    plt.ylabel('Approval Rate')
    plt.xlabel('Age Group')
    plt.tight_layout()
    st.pyplot(plt)
    
    data.groupby('age_group')['target'].mean().plot(kind='bar', color='salmon', title='Default Rate by Age Group')
    plt.ylabel('Default Rate')
    plt.xlabel('Age Group')
    plt.tight_layout()
    st.pyplot(plt)
    
def EDA_2_5 (data):
    data['marital_status'].value_counts()
    
    data['marital_group'] = data['marital_status'].replace({
        'Single / not married': 'Single',
        'Civil marriage': 'Married',
        'Separated': 'Other',
        'Widow': 'Other',
        'Widowed': 'Other'
    })
    
    default_by_marital = data.groupby('marital_group')['target'].mean().sort_values()
    
    default_by_marital.plot(kind='bar', color='orange')
    plt.title('Default Rate by Marital Status')
    plt.ylabel('Default Rate')
    plt.xlabel('Marital Group')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_3_1 (data):
    house_counts = data['house_type'].value_counts()
    
    sns.countplot(data=data, y='house_type', order=house_counts.index, palette='pastel')
    plt.title('Distribution of House Types Among Applicants')
    plt.xlabel('Number of Applicants')
    plt.ylabel('House Type')
    plt.tight_layout()
    st.pyplot(plt)
    
    approval_by_house = data.groupby('house_type')['credit_status'].value_counts(normalize=True).unstack()
    
    approval_by_house['Good Credit'].sort_values().plot(kind='barh', color='lightgreen')
    plt.title('Approval Rate by House Type')
    plt.xlabel('Approval Rate')
    plt.ylabel('House Type')
    plt.tight_layout()
    st.pyplot(plt)
    
    default_by_house = data.groupby('house_type')['target'].mean().sort_values()
    default_by_house.plot(kind='barh', color='coral')
    plt.title('Default Rate by House Type')
    plt.xlabel('Default Rate')
    plt.ylabel('House Type')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_3_2 (data):
    default_by_realty = data.groupby('realty')['target'].mean()
    
    default_by_realty.plot(kind='bar', color=['green', 'red'], title='Default Rate by Realty Ownership')
    plt.xticks([0, 1], ['Owns Real Estate', 'Does Not Own'], rotation=0)
    plt.ylabel('Default Rate')
    plt.xlabel('Real Estate Ownership')
    plt.tight_layout()
    st.pyplot(plt)
    
def EDA_4_1 (data):
    # Count each combination of occupation and credit_status
    group_counts = data.groupby(['occupation', 'credit_status']).size().unstack(fill_value=0)

    # Define colors: green for higher count, red for lower
    colors = []
    for occ in group_counts.index:
        values = group_counts.loc[occ]
        if values.iloc[0] > values.iloc[1]:
            colors.append(['red', 'green'])

    # Flatten the color list
    flat_colors = [color for pair in colors for color in pair]

    # Create the plot
    plt.figure(figsize=(10, 6))
    ax = sns.countplot(data=data, x='occupation', hue='credit_status', palette=flat_colors)
    plt.title('Credit Approval by Occupation')
    plt.xlabel('Occupation')
    plt.ylabel('Count')
    plt.legend(title='Credit Status')
    plt.tight_layout()

    # Annotate each bar with its count
    for bar in ax.patches:
        height = bar.get_height()
        if height > 0:
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f'{int(height)}',
                ha='center',
                va='bottom',
                fontsize=9,
                color='black'
            )

    st.pyplot(plt)

def EDA_4_2 (data): # Please Revisit
    # Convert days_employed to years as a standalone object

    plt.figure(figsize=(8, 6))
    sns.regplot(
        data=data,
        x=abs(data['days_employed'] / 365),
        y='income',
        fit_reg=False,  # Matikan garis regresi
        scatter_kws={'color': 'green'}  # Ubah warna titik jadi hijau
    )
    plt.title('Income vs Years Employed')
    plt.xlabel('Years Employed')
    plt.ylabel('Income')
    plt.tight_layout()
    st.pyplot(plt)

def EDA_5_1 (data):
    contact_cols = ['email', 'work_phone', 'mobile_phone']
    data[contact_cols] = data[contact_cols].notnull().astype(int)  # assume null = not available
    contact_counts = data[contact_cols].sum()

    # Create full labels with counts
    labels = [f"{idx} - {int(val)} customers" for idx, val in contact_counts.items()]

    # Plot pie chart
    plt.figure(figsize=(6,6))
    plt.pie(contact_counts, labels=labels, autopct='%1.1f%%', colors=['lightgreen', 'lightblue', 'salmon'])
    plt.title('Number of Customers with Available Contact Information')
    st.pyplot(plt)

def EDA_6_1 (data):
    sns.histplot(data=data, x='months_balance', bins=50, color='steelblue')
    plt.title('Distribution of Months Balance')
    plt.xlabel('Months Balance')
    plt.ylabel('Frequency')
    st.pyplot(plt)

def EDA_6_2 (data):
    # Define custom colors for each category in credit_status
    palette_colors = {
        'Good Credit': 'green',
        'NPL': 'red'
    }

    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=data,
        x=-data['months_balance'],  # Negative sign to flip the x-axis if needed
        hue='credit_status',
        bins=20,
        kde=True,
        palette=palette_colors
    )
    plt.title("Tenure (Months) by Credit Status")
    plt.xlabel("Tenure in Months")
    plt.ylabel("Count")
    plt.tight_layout()
    st.pyplot(plt)

def EDA_7_1 (data):
    features = ['child_number', 'income', 'family_size']

    fig, axes = plt.subplots(1, len(features), figsize=(18, 6))

    for i, feature in enumerate(features):
        sns.boxplot(y=data[feature], ax=axes[i], color='green')  # Tambah warna hijau
        axes[i].set_title(f'Boxplot of {feature}')
        axes[i].set_xlabel(feature)
        axes[i].grid(True)

    plt.tight_layout()
    st.pyplot(plt)

def EDA_7_2 (data):
    income_skew = skew(data['income'].dropna())
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.metric(label="Skewness of Income", value=f"{income_skew:.4f}")

def EDA_8_1_1 (data):
    # Step 1: Map target variable
    target = data['credit_status'].map({'Good Credit': 0, 'NPL': 1})

    # Step 2: Select numeric columns and drop metadata-like columns
    excluded_cols = ['mobile_phone', 'work_phone', 'email']
    numeric_cols = data.select_dtypes(include='number').drop(columns=excluded_cols, errors='ignore').columns

    # Step 3: Calculate Spearman correlations
    spearman_results = []

    for col in numeric_cols:
        # Skip target itself
        if col == 'credit_status' or col == 'target':
            continue
        corr, pval = spearmanr(data[col], target, nan_policy='omit')
        spearman_results.append((col, corr, pval))

    # Step 4: Create DataFrame of results and round p-values
    spearman_df = pd.DataFrame(spearman_results, columns=['Feature', 'Spearman Correlation', 'p-value'])
    spearman_df['p-value'] = spearman_df['p-value'].round(3)
    spearman_df = spearman_df.sort_values(by='Spearman Correlation', ascending=False)

    st.subheader("Table")
    st.dataframe(spearman_df)

def EDA_8_1_2 (data):
    # Define Cramér's V calculation function
    def cramers_v(col1, col2):
        contingency = pd.crosstab(col1, col2)
        if contingency.empty or contingency.shape[0] < 2 or contingency.shape[1] < 2:
            return np.nan  # skip if not enough variation
        chi2 = chi2_contingency(contingency)[0]
        n = contingency.to_numpy().sum()
        r, k = contingency.shape
        return np.sqrt(chi2 / (n * (min(r, k) - 1)))

    # Step 1: Select categorical columns (excluding target)
    categorical_cols = data.select_dtypes(include='object').columns
    categorical_cols = categorical_cols.drop('credit_status', errors='ignore')

    # Step 2: Calculate Cramér's V
    cramers_results = []

    for col in categorical_cols:
        score = cramers_v(data[col], data['credit_status'])
        if not np.isnan(score):  # only include valid results
            cramers_results.append((col, round(score, 3)))

    # Step 3: Compile results into a DataFrame
    cramers_df = pd.DataFrame(cramers_results, columns=['Feature', "Cramér's V"])
    cramers_df = cramers_df.sort_values(by="Cramér's V", ascending=False).reset_index(drop=True)

    st.subheader("Table")
    st.dataframe(cramers_df)

def EDA_8_2 (data):
    # Select only numeric features (excluding 'target')
    numerical_features = data.select_dtypes(include=['float64', 'int64']).drop(columns=['target'])

    # Compute VIF for each feature (no intercept added)
    vif_scores = pd.DataFrame()
    vif_scores['Feature'] = numerical_features.columns
    vif_scores['VIF'] = [variance_inflation_factor(numerical_features.values, i) for i in range(numerical_features.shape[1])]
    
    sorted_vif = vif_scores.sort_values(by='VIF', ascending=False)
    
    st.subheader("Table")
    st.dataframe(sorted_vif)

