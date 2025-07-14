import pandas as pd
import pickle

class CreditApprovalModel:
    def __init__(self, model_path='credit_approval_model.pkl'):
        # Load trained model
        self.model = pickle.load(model_path)

        # Education level mapping
        self.edu_order = {
            'Lower secondary': 1,
            'Secondary / secondary special': 2,
            'Incomplete higher': 3,
            'Higher education': 4,
            'Academic degree': 5
        }

        # Selected features for model input
        self.selected_features = [
            'age',
            'years_employed',
            'education_income_ratio',
            'income_per_person',
            'has_child',
            'low_income',
            'is_single'
        ]

    def preprocess(self, input_data, reference_df):
        """
        - input_data: dict or DataFrame row (1 sample)
        - reference_df: DataFrame used to calculate median_income
        """
        df = pd.DataFrame([input_data])  # single row

        # Map education to ordinal
        df['education_ordinal'] = df['education'].map(self.edu_order)

        # Compute median income from reference_df
        median_income = reference_df['income'].median()

        # Feature creation
        df['age'] = (-df['days_birth'] // 365)
        df['years_employed'] = df['days_employed'].apply(lambda x: 0 if x > 0 else int(-x // 365))
        df['education_income_ratio'] = df['education_ordinal'] / df['income']
        df['income_per_person'] = df['income'] / df['family_size'].replace(0, 1)
        df['has_child'] = (df['child_number'] > 0).astype(int)
        df['low_income'] = (df['income'] < median_income).astype(int)
        df['is_single'] = df['marital_status'].isin(['Single / not married', 'Separated', 'Widow']).astype(int)

        return df[self.selected_features]

    def predict(self, input_data, reference_df):
        # Run full prediction pipeline
        processed = self.preprocess(input_data, reference_df)
        prediction = self.model.predict(processed)
        return "Approved" if prediction[0] == 1 else "Rejected"