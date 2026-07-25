import streamlit as st

from views.home import show_home
from views.prediction import show_prediction
from views.analytics import show_analytics

# ============================================
# Page Configuration
# ============================================

st.set_page_config(
    page_title="LoanRisk AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
.block-container{
    padding-top:1rem;
    padding-bottom:1rem;
}
</style>
""", unsafe_allow_html=True)

# ============================================
# Sidebar
# ============================================

st.sidebar.title("🏦 LoanRisk AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔮 Prediction",
        "📊 Analytics"
    ]
)

st.sidebar.divider()

st.sidebar.markdown("### Project")

st.sidebar.write(
    """
Loan Default Risk Prediction

Built using:

- Python
- Streamlit
- FastAPI
- PostgreSQL
- Random Forest
- Plotly
"""
)

st.sidebar.divider()

st.sidebar.success("MSc Statistics Project")

# ============================================
# Navigation
# ============================================

if page == "🏠 Home":
    show_home()

elif page == "🔮 Prediction":
    show_prediction()

elif page == "📊 Analytics":
    show_analytics()