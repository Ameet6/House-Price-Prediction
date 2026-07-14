import streamlit as st

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="AI House Price Estimator",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Sidebar
# ==========================================
with st.sidebar:
    st.title("🏠 AI House Price Estimator")

    st.markdown("---")

    st.markdown("""
### 📌 Navigation

Use the pages below to navigate through the application.

- 🏠 Home
- 🤖 Prediction
- ℹ️ About
""")

    st.markdown("---")

    st.info("Built with Python, Machine Learning & Streamlit")

# ==========================================
# Main Title
# ==========================================
st.title("🏠 AI House Price Estimator")

st.markdown("""
### Welcome!

This application estimates the value of residential properties using a trained **Machine Learning** model.

Simply open the **Prediction** page from the sidebar, enter the house details, and receive an instant estimated house price along with AI-generated property insights.
""")

st.divider()

# ==========================================
# Features & Technology
# ==========================================

col1, col2 = st.columns(2)

with col1:
    st.subheader("✨ Features")

    st.markdown("""
✅ Instant house price estimation

✅ Interactive Streamlit dashboard

✅ Feature-engineered Linear Regression model

✅ Property insights

✅ Luxury score calculation

✅ Price per square foot

✅ Clean and intuitive interface
""")

with col2:
    st.subheader("🛠 Technology Stack")

    st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 🐼 Pandas
- 🔢 NumPy
- 🤖 Scikit-learn
- 💾 Joblib
""")

st.divider()

# ==========================================
# Machine Learning Model
# ==========================================

st.subheader("🧠 Machine Learning Model")

st.info("""
This application uses a trained **Linear Regression** model to estimate house prices.

The model was developed using a complete Machine Learning workflow including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Model Evaluation
- Hyperparameter Tuning
""")

st.divider()

# ==========================================
# Dataset
# ==========================================

st.subheader("📊 Dataset")

st.write("""
The application is based on a publicly available housing dataset from **Kaggle**.

The dataset contains information about residential properties, including:

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

st.warning("""
**Note:** The original dataset does **not specify a currency**. Therefore, the predicted value is displayed in the dataset's original units.
""")

st.divider()

# ==========================================
# Navigation
# ==========================================

st.subheader("📌 How to Use")

st.success("""
1️⃣ Open the **Prediction** page from the sidebar.

2️⃣ Enter the property details.

3️⃣ Click **Predict House Price**.

4️⃣ View the estimated price and AI-generated property insights.
""")

st.divider()

# ==========================================
# Footer
# ==========================================

st.caption(
    "© 2026 | AI House Price Estimator | Machine Learning Portfolio Project"
)