import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000/predict"


def show_prediction():

    st.title("🔮 Loan Approval Prediction")
    st.caption("Fill in the applicant details below to predict loan approval.")

    st.divider()

    with st.form("loan_prediction_form"):

        col1, col2 = st.columns(2)

        # ==========================
        # Left Column
        # ==========================

        with col1:

            gender = st.selectbox(
                "Gender",
                ["Male", "Female"]
            )

            married = st.selectbox(
                "Married",
                ["Yes", "No"]
            )

            dependents = st.selectbox(
                "Dependents",
                [0, 1, 2, 3]
            )

            education = st.selectbox(
                "Education",
                ["Graduate", "Not Graduate"]
            )

            self_employed = st.selectbox(
                "Self Employed",
                ["Yes", "No"]
            )

        # ==========================
        # Right Column
        # ==========================

        with col2:

            applicant_income = st.number_input(
                "Applicant Income",
                min_value=0,
                value=5000
            )

            coapplicant_income = st.number_input(
                "Coapplicant Income",
                min_value=0,
                value=0
            )

            loan_amount = st.number_input(
                "Loan Amount",
                min_value=0,
                value=150
            )

            loan_term = st.selectbox(
                "Loan Term (Months)",
                [12, 36, 60, 84, 120, 180, 240, 300, 360, 480]
            )

            credit_history = st.selectbox(
                "Credit History",
                [1, 0]
            )

            property_area = st.selectbox(
                "Property Area",
                [
                    "Urban",
                    "Semiurban",
                    "Rural"
                ]
            )

        submitted = st.form_submit_button(
            "🚀 Predict Loan Status",
            use_container_width=True
        )

    if submitted:

        payload = {

            "Gender": gender,
            "Married": married,
            "Dependents": dependents,
            "Education": education,
            "Self_Employed": self_employed,
            "ApplicantIncome": applicant_income,
            "CoapplicantIncome": coapplicant_income,
            "LoanAmount": loan_amount,
            "Loan_Amount_Term": loan_term,
            "Credit_History": credit_history,

            "Property_Area_Semiurban": 1 if property_area == "Semiurban" else 0,
            "Property_Area_Urban": 1 if property_area == "Urban" else 0

        }

        with st.spinner("Predicting..."):

            try:

                response = requests.post(API_URL, json=payload)
                response.raise_for_status()

                result = response.json()

                prediction = result["Prediction"]
                probability = result["Probability"]
                st.divider()

                st.subheader("📊 Prediction Result")

                metric1, metric2 = st.columns(2)

                with metric1:
                    st.metric(
                        label="Prediction",
                        value=prediction
                    )

                with metric2:
                    st.metric(
                        label="Confidence",
                        value=f"{probability:.2%}"
                    )

                if prediction.lower() == "approved":

                    st.success("✅ Loan is likely to be Approved.")

                    st.progress(min(int(probability * 100), 100))

                else:

                    st.error("❌ Loan is likely to be Rejected.")

                    st.progress(min(int(probability * 100), 100))

                st.divider()

                st.subheader("📋 Applicant Summary")

                summary = pd.DataFrame(
                    {
                        "Feature": [
                            "Gender",
                            "Married",
                            "Dependents",
                            "Education",
                            "Self Employed",
                            "Applicant Income",
                            "Coapplicant Income",
                            "Loan Amount",
                            "Loan Term",
                            "Credit History",
                            "Property Area"
                        ],

                        "Value": [
                            gender,
                            married,
                            dependents,
                            education,
                            self_employed,
                            applicant_income,
                            coapplicant_income,
                            loan_amount,
                            loan_term,
                            credit_history,
                            property_area
                        ]
                    }
                )

                st.dataframe(
                    summary,
                    use_container_width=True,
                    hide_index=True
                )

                with st.expander("Model Output"):

                    st.json(result)

            except requests.exceptions.ConnectionError:

                st.error(
                    "Unable to connect to FastAPI server.\n\n"
                    "Make sure the API is running:\n"
                    "uvicorn api.main:app --reload"
                )

            except requests.exceptions.HTTPError as e:

                st.error(f"HTTP Error : {e}")

            except Exception as e:

                st.error(f"Unexpected Error : {e}")