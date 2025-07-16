from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineer(BaseEstimator, TransformerMixin):
    def __init__(self, median_income=None):
        self.median_income = median_income
        self.edu_order = {
            'Lower secondary': 1,
            'Secondary / secondary special': 2,
            'Incomplete higher': 3,
            'Higher education': 4,
            'Academic degree': 5
        }
        self.house_type_order = {
            'With parents': 0,
            'Municipal apartment': 1,
            'Rented apartment': 2,
            'Office apartment': 3,
            'House / apartment': 4,
            'Co-op apartment': 5
        }

    def fit(self, X, y=None):
        if self.median_income is None:
            self.median_income = X['income'].median()
        return self

    def transform(self, X):
        df = X.copy()

        # Feature 1: Age
        df['age'] = (-df['days_birth'] // 365)

        # Feature 2: Years Employed
        df['years_employed'] = df['days_employed'].apply(lambda x: 0 if x > 0 else int(-x // 365))

        # Feature 3: Education Level + Ratio
        df['education_ordinal'] = df['education'].map(self.edu_order)
        df['education_income_ratio'] = df['education_ordinal'] / df['income']

        # Feature 4: Income per person
        df['income_per_person'] = df['income'] / df['family_size'].replace(0, 1)

        # Feature 5: Low Income
        df['low_income'] = (df['income'] < self.median_income).astype(int)

        # Feature 6: Financial Dependence Ratio
        df['financial_dependence_ratio'] = df['family_size'] / (1 + df['child_number'])

        # Feature 7: House Type + Ratio
        df['house_type_ordinal'] = df['house_type'].map(self.house_type_order)
        df['house_income_ratio'] = df['house_type_ordinal'] / df['income']

        return df[[
            'months_balance',
            'email',
            'car',
            'phone',
            'realty',
            'occupation',
            'gender',
            'work_phone',
            'age',
            'years_employed',
            'education_income_ratio',
            'income_per_person',
            'low_income',
            'financial_dependence_ratio',
            'house_income_ratio'
        ]]