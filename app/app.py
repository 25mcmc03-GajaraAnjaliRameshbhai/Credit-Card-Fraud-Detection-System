import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline (scaler + SMOTE + model, all in one object)
pipeline = joblib.load("model/fraud_pipeline.joblib")

st.title("Credit Card Fraud Detector")
st.write("Upload a CSV of transactions to check which ones look fraudulent.")

# Let the threshold be adjustable instead of hardcoding 0.5
threshold = st.slider("Fraud probability threshold", 0.0, 1.0, 0.5, 0.01)

uploaded_file = st.file_uploader("Upload transactions CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Drop the label column if it's present (some test files include it)
    features = data.drop(columns=["Class"], errors="ignore")

    # predict_proba returns [P(legit), P(fraud)] per row — we want the second column
    fraud_probs = pipeline.predict_proba(features)[:, 1]

    results = data.copy()
    results["fraud_probability"] = fraud_probs
    results["flagged"] = fraud_probs >= threshold

    st.subheader(f"Results — {results['flagged'].sum()} flagged out of {len(results)}")
    st.dataframe(results.sort_values("fraud_probability", ascending=False))

    # Let them download the scored file
    csv = results.to_csv(index=False).encode("utf-8")
    st.download_button("Download scored CSV", csv, "scored_transactions.csv", "text/csv")
