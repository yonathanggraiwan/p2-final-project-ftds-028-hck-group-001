import streamlit as st
import pandas as pd
import pickle
import io
from inference import FeatureEngineer


def run():
    # === Load model ===
    @st.cache_resource
    def load_model():
        with open("model_lgbm.pkl", "rb") as f:
            model = pickle.load(f)
        return model

    model = load_model()

    st.title("Machine Learning Inference from Excel File")

    uploaded_file = st.file_uploader("Upload Excel File (.xlsx)", type=["xlsx"])

    if uploaded_file:
        try:
            # Read Excel file
            raw_df = pd.read_excel(uploaded_file)
            st.subheader("Original Uploaded Data")
            st.dataframe(raw_df)

            # Feature engineering
            fe = FeatureEngineer()
            fe.fit(raw_df)
            processed_df = fe.transform(raw_df)

            # Prediction and probabilities
            prediction = model.predict(processed_df)
            probability = model.predict_proba(processed_df)

            result_labels = ['NPL' if p == 1 else 'Good Credit' for p in prediction]
            result_probs = [round(prob[1], 4) if label == 'NPL' else round(prob[0], 4)
                            for prob, label in zip(probability, result_labels)]

            raw_df['prediction'] = result_labels
            raw_df['probability'] = result_probs

            st.subheader("Data with Prediction Results")
            st.dataframe(raw_df)

            # Split filtered data
            df_good_credit = raw_df[raw_df['prediction'] == 'Good Credit']
            df_npl = raw_df[raw_df['prediction'] == 'NPL']

            # === Filtered View Option ===
            filter_option = st.selectbox(
                "Select which prediction result to view:",
                ['Good Credit', 'NPL']
            )

            if filter_option == 'Good Credit':
                st.subheader("Filtered Data: Good Credit Only")
                st.dataframe(df_good_credit)
            else:
                st.subheader("Filtered Data: NPL Only")
                st.dataframe(df_npl)

            # Save all three tables to one Excel file
            def to_excel_with_sheets(df_all, df_good, df_npl):
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
                    df_all.to_excel(writer, sheet_name="All Predictions", index=False)
                    df_good.to_excel(writer, sheet_name="Good Credit Only", index=False)
                    df_npl.to_excel(writer, sheet_name="NPL Only", index=False)
                return buffer.getvalue()

            st.download_button(
                "Download Predictions",
                data=to_excel_with_sheets(raw_df, df_good_credit, df_npl),
                file_name="predictions_results.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"❌ Error processing file: {e}")

if __name__ == "__main__":
    run()