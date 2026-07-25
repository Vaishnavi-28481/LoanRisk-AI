import streamlit as st


def show_home():

    st.title("🏦 LoanRisk AI")

    st.caption(
        "End-to-End Loan Default Risk Prediction using Machine Learning"
    )

    st.divider()

    st.subheader("📖 Project Overview")

    st.info("""
This project predicts whether a loan application will be approved or rejected using a Random Forest Machine Learning model.

The application integrates FastAPI, PostgreSQL and Streamlit to provide prediction, storage and analytics in one platform.
""")

    st.divider()

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:

        with st.container(border=True):

            st.subheader("🛠 Tech Stack")

            left, right = st.columns(2)

        with left:
           st.write("• Python")
           st.write("• SQL")
           st.write("• Pandas")
           st.write("• NumPy")
           st.write("• Streamlit")

        with right:
          st.write("• Scikit-learn")
          st.write("• FastAPI")
          st.write("• PostgreSQL")
          st.write("• SQLAlchemy")
          st.write("• Plotly")

    with row1_col2:

        with st.container(border=True):

            st.subheader("⭐ Features")
            left, right = st.columns(2)
        with left:

            st.write("✔ Loan Approval Prediction")
            st.write("✔ REST API")
            st.write("✔ PostgreSQL Storage")
        with right:
            st.write("✔ Analytics Dashboard")
            st.write("✔ Prediction History")
            st.write("✔ CSV Download")

    st.write("")

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:

        with st.container(border=True):

            st.subheader("🤖 Model Information")
            st.write("**Model:** Random Forest")
            st.write("**Accuracy:** 86.18%")
            st.write("**Type:** Binary Classification")
            st.write("**Target:** Loan Status")

            
            

    with row2_col2:

        with st.container(border=True):

            st.subheader("🔄 Project Workflow")
            left, right = st.columns(2)
        with left:

            st.write("1. Data Collection")

            st.write("2. Data Cleaning")

            st.write("3. Feature Engineering")

            st.write("4. Model Training")
        with right:

            st.write("5. FastAPI")

            st.write("6. PostgreSQL")

            st.write("7. Streamlit Dashboard")
    st.divider()

    with st.container(border=True):

        st.subheader("🚀 Get Started")
        left, right = st.columns(2)
        with left:

            st.write("1️⃣ Open the Prediction page.")

            st.write("2️⃣ Enter applicant information.")

            st.write("3️⃣ Click Predict Loan Status.")
        with right:

            st.write("4️⃣ View prediction result.")

            st.write("5️⃣ Open Analytics dashboard.")

        

    st.divider()

    st.success(
        "✅ LoanRisk AI is Ready for Prediction"
    )