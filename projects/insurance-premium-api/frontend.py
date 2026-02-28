import os
import requests
import streamlit as st

DEFAULT_API_BASE = "http://18.117.168.71:8000/predict"


st.set_page_config(page_title="Insurance Premium Predictor", page_icon="💡", layout="centered")
st.title("Insurance Premium Predictor")
st.caption("Enter user details to predict insurance premium category")

with st.sidebar:
    st.subheader("Backend Settings")
    api_base = st.text_input("API Base URL", value=DEFAULT_API_BASE).rstrip("/")
    if api_base.lower().endswith("/predict"):
        api_base = api_base[:-8]
    st.write(f"Predict endpoint: `{api_base}/predict`")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=30, step=1)
        weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0, step=0.1)
        height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
        income_lpa = st.number_input("Annual Income (LPA)", min_value=0.0, value=8.0, step=0.1)

    with col2:
        smoker = st.selectbox("Smoker", options=[False, True], format_func=lambda x: "Yes" if x else "No")
        city = st.text_input("City", value="Mumbai")
        occupation = st.selectbox(
            "Occupation",
            options=[
                "retired",
                "freelancer",
                "student",
                "government_job",
                "business_owner",
                "private_job",
                "unemployed",
            ],
        )

    submit = st.form_submit_button("Predict")

if submit:
    payload = {
        "age": int(age),
        "weight": float(weight),
        "height": float(height),
        "income_lpa": float(income_lpa),
        "smoker": bool(smoker),
        "city": city.strip(),
        "occupation": occupation,
    }

    try:
        response = requests.post(f"{api_base}/predict", json=payload, timeout=20)
        data = response.json()
    except requests.exceptions.RequestException as exc:
        st.error("Could not connect to backend API. Make sure FastAPI is running and URL is correct.")
        st.code(str(exc))
    except ValueError:
        st.error("Backend did not return valid JSON.")
    else:
        if response.status_code != 200:
            st.error(f"API Error ({response.status_code})")
            st.json(data)
        else:
            result = data.get("response", {})
            category = result.get("predicted_category") or result.get("prediction")
            confidence = result.get("confidence")
            probabilities = result.get("class_probabilities") or result.get("probabilities", {})

            if not category:
                st.error("Unexpected API response format.")
                st.json(data)
            else:
                st.success(f"Predicted Premium Category: {category}")
                if confidence is not None:
                    st.write(f"Confidence: **{confidence:.4f}**")
                if probabilities:
                    st.subheader("Class Probabilities")
                    st.json(probabilities)
