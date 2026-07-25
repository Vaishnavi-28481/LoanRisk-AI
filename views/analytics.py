import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ============================================
# PostgreSQL Connection
# ============================================

DATABASE_URL = "postgresql://postgres:root123@localhost:5432/loan_db"

engine = create_engine(DATABASE_URL)


# ============================================
# Load Data
# ============================================


def load_data():

    query = """
    SELECT *
    FROM prediction_history
    ORDER BY "Created_At" DESC
    """

    df = pd.read_sql(query, engine)

    return df


# ============================================
# Analytics Page
# ============================================

def show_analytics():

    st.title("📊 Analytics Dashboard")
    st.caption("Real-time Prediction Analytics")

    try:

        df = load_data()

    except Exception as e:

        st.error(f"Database Error : {e}")
        return

    if df.empty:

        st.warning("No prediction history available.")
        return

    st.divider()

    # ============================================
    # KPI Metrics
    # ============================================

    total_predictions = len(df)

    approved = (df["Prediction"] == "Approved").sum()

    rejected = (df["Prediction"] == "Rejected").sum()

    approval_rate = round(
        approved / total_predictions * 100,
        2
    )

    avg_income = round(
        df["ApplicantIncome"].mean(),
        2
    )

    avg_loan = round(
        df["LoanAmount"].mean(),
        2
    )

    k1, k2, k3, k4, k5 = st.columns(5)

    with k1:
        st.metric(
            "Total Predictions",
            total_predictions
        )

    with k2:
        st.metric(
            "Approved",
            approved
        )

    with k3:
        st.metric(
            "Rejected",
            rejected
        )

    with k4:
        st.metric(
            "Approval Rate",
            f"{approval_rate}%"
        )

    with k5:
        st.metric(
            "Avg Loan",
            f"{avg_loan:.2f}"
        )

    st.divider()

    # ============================================
    # Charts
    # ============================================

    left, right = st.columns(2)
    # ============================================
    # Approval vs Rejection
    # ============================================

    with left:

        approval_df = (
            df["Prediction"]
            .value_counts()
            .reset_index()
        )

        approval_df.columns = [
            "Prediction",
            "Count"
        ]

        fig1 = px.pie(
            approval_df,
            names="Prediction",
            values="Count",
            title="Loan Approval Distribution",
            hole=0.45
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    # ============================================
    # Credit History
    # ============================================

    with right:

        fig2 = px.histogram(
            df,
            x="Credit_History",
            color="Prediction",
            title="Credit History Analysis",
            barmode="group"
        )

        st.plotly_chart(
            fig2,
            width="stretch"
        )

    st.divider()

    # ============================================
    # Income & Loan Amount
    # ============================================

    c1, c2 = st.columns(2)

    with c1:

        fig3 = px.histogram(
            df,
            x="ApplicantIncome",
            nbins=25,
            color="Prediction",
            title="Applicant Income Distribution"
        )

        st.plotly_chart(
            fig3,
            width="stretch"
        )

    with c2:

        fig4 = px.histogram(
            df,
            x="LoanAmount",
            nbins=25,
            color="Prediction",
            title="Loan Amount Distribution"
        )

        st.plotly_chart(
            fig4,
            width="stretch"
        )

    st.divider()

    # ============================================
    # Property Area
    # ============================================

    property_counts = pd.DataFrame({
        "Property Area": [
            "Urban",
            "Semiurban"
        ],
        "Count": [
            df["Property_Area_Urban"].sum(),
            df["Property_Area_Semiurban"].sum()
        ]
    })

    fig5 = px.bar(
        property_counts,
        x="Property Area",
        y="Count",
        title="Property Area Distribution"
    )

    st.plotly_chart(
        fig5,
        width="stretch"
    )

    st.divider()

    # ============================================
    # Prediction History
    # ============================================

    st.subheader("📋 Prediction History")

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )
    # ============================================
    # Download CSV
    # ============================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        width="stretch"
    )

    st.divider()

    # ============================================
    # Quick Insights
    # ============================================

    st.subheader("📌 Business Insights")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.info(f"""
**Total Predictions:** {total_predictions}

**Approved Loans:** {approved}

**Rejected Loans:** {rejected}

**Approval Rate:** {approval_rate}%
""")

    with insight2:

        st.success(f"""
**Average Applicant Income:** {avg_income:.2f}

**Average Loan Amount:** {avg_loan:.2f}
""")

    st.divider()

    st.success("✅ Dashboard updated successfully from PostgreSQL.")