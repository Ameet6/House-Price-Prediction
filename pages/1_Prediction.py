import streamlit as st
import pandas as pd
import joblib

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# ==========================================
# Load Model
# ==========================================
model = joblib.load("model/house_price_model.pkl")
feature_names = joblib.load("model/feature_names.pkl")

# ==========================================
# Title
# ==========================================
st.title("🤖 House Price Prediction")

st.write(
    """
Enter the property details below and click **Predict House Price**
to estimate the value of the property.
"""
)

st.divider()

# ==========================================
# User Inputs
# ==========================================

col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "Area (Square Feet)",
        min_value=500,
        max_value=20000,
        value=5000,
        step=100
    )

    bedrooms = st.selectbox(
        "Bedrooms",
        [1, 2, 3, 4, 5, 6]
    )

    bathrooms = st.selectbox(
        "Bathrooms",
        [1, 2, 3, 4]
    )

    stories = st.selectbox(
        "Stories",
        [1, 2, 3, 4]
    )

    parking = st.selectbox(
        "Parking Spaces",
        [0, 1, 2, 3]
    )

with col2:

    mainroad = st.selectbox(
        "Main Road",
        ["Yes", "No"]
    )

    guestroom = st.selectbox(
        "Guest Room",
        ["Yes", "No"]
    )

    basement = st.selectbox(
        "Basement",
        ["Yes", "No"]
    )

    hotwaterheating = st.selectbox(
        "Hot Water Heating",
        ["Yes", "No"]
    )

    airconditioning = st.selectbox(
        "Air Conditioning",
        ["Yes", "No"]
    )

    prefarea = st.selectbox(
        "Preferred Area",
        ["Yes", "No"]
    )

    furnishingstatus = st.selectbox(
        "Furnishing Status",
        [
            "furnished",
            "semi-furnished",
            "unfurnished"
        ]
    )

st.divider()

# ==========================================
# Convert Yes/No to 1/0
# ==========================================

mainroad = 1 if mainroad == "Yes" else 0
guestroom = 1 if guestroom == "Yes" else 0
basement = 1 if basement == "Yes" else 0
hotwaterheating = 1 if hotwaterheating == "Yes" else 0
airconditioning = 1 if airconditioning == "Yes" else 0
prefarea = 1 if prefarea == "Yes" else 0

# ==========================================
# One-Hot Encoding
# ==========================================

semi_furnished = 1 if furnishingstatus == "semi-furnished" else 0
unfurnished = 1 if furnishingstatus == "unfurnished" else 0

# ==========================================
# Feature Engineering
# ==========================================

luxury_score = (
    airconditioning +
    guestroom +
    basement +
    hotwaterheating +
    prefarea
)

area_per_bedroom = area / bedrooms

# ==========================================
# Prediction Button
# ==========================================

if st.button("🏠 Predict House Price"):
    # ==========================================
    # Create Input Data
    # ==========================================

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus_semi-furnished": [semi_furnished],
        "furnishingstatus_unfurnished": [unfurnished],
        "luxury_score": [luxury_score],
        "area_per_bedroom": [area_per_bedroom]
    })

    # Arrange columns in the same order used during training
    input_data = input_data[feature_names]

    # ==========================================
    # Predict Price
    # ==========================================

    prediction = model.predict(input_data)[0]

    # ==========================================
    # Additional Calculations
    # ==========================================

    price_million = prediction / 1_000_000
    price_per_sqft = prediction / area

    # ==========================================
    # Property Category
    # ==========================================

    if luxury_score >= 4:
        category = "Luxury"

    elif luxury_score >= 2:
        category = "Medium Luxury"

    else:
        category = "Budget"

    # ==========================================
    # Display Results
    # ==========================================

    st.success("🎉 Prediction Completed Successfully!")

    st.subheader("🏠 Estimated House Price")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💰 Estimated House Price",
            f"{prediction:,.0f}"
        )

        st.metric(
            "📈 Price (Millions)",
            f"{price_million:.2f} M"
        )

    with col2:

        st.metric(
            "📏 Price per Sq.Ft.",
            f"{price_per_sqft:,.0f}"
        )

        st.metric(
            "⭐ Luxury Score",
            f"{luxury_score}/5"
        )

    with col3:

        st.metric(
            "🏷 Property Category",
            category
        )

    st.caption(
        "Note: The dataset does not specify a currency. Therefore, the predicted value is displayed in the dataset's original units."
    )

    st.divider()
    # ==========================================
# AI Property Analysis
# ==========================================

    st.subheader("🤖 AI Property Analysis")

    analysis = []

    if parking >= 2:
        analysis.append("🚗 Good parking capacity")

    if prefarea == 1:
        analysis.append("📍 Located in a preferred area")

    if area >= 5000:
        analysis.append("🏡 Spacious property")

    if airconditioning == 1:
        analysis.append("❄️ Air conditioning available")

    if basement == 1:
        analysis.append("🏠 Includes a basement")

    if guestroom == 1:
        analysis.append("🛏 Includes a guest room")

    if hotwaterheating == 1:
        analysis.append("🔥 Hot water heating available")

    if stories >= 2:
        analysis.append("🏢 Multi-story house")

    if luxury_score >= 4:
        analysis.append(
            "⭐ This property offers several premium features, making it a luxury home."
        )

    elif luxury_score >= 2:
        analysis.append(
            "✨ This property provides a balanced combination of comfort and value."
        )

    else:
        analysis.append(
            "💰 This property is a practical choice for budget-conscious buyers."
        )

    st.info("AI-generated insights based on the selected property features.")

    for item in analysis:
        st.write(item)