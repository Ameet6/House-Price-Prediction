import streamlit as st

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About This Project")

st.markdown("""
## 🏠 AI House Price Estimator

This application predicts the estimated price of a house using a Machine Learning model.

The project demonstrates an end-to-end Machine Learning workflow, from data preprocessing and model training to deployment with Streamlit.
""")

st.divider()

# ==========================================
# Dataset
# ==========================================

st.subheader("📊 Dataset")

st.write("""
The model was trained on a housing dataset containing information about residential properties, including:

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Air Conditioning
- Basement
- Guest Room
- Preferred Area
- Furnishing Status

These features are used to estimate the house price.
""")

st.divider()

# ==========================================
# Machine Learning
# ==========================================

st.subheader("🧠 Machine Learning Workflow")

st.markdown("""
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Hyperparameter Tuning
- Model Deployment
""")

st.info("Final deployed model: Linear Regression")

st.divider()

# ==========================================
# Technology Stack
# ==========================================

st.subheader("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
""")

with col2:
    st.markdown("""
- Streamlit
- Joblib
- Matplotlib
- Seaborn
""")

st.divider()

# ==========================================
# Purpose
# ==========================================

st.subheader("🎯 Purpose")

st.write("""
This project was developed to demonstrate practical Machine Learning skills, including data preprocessing, model development, evaluation, and deployment through an interactive web application.
""")

st.success("Thank you for exploring the AI House Price Estimator!")