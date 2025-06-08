import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from the notebooks directory
with open("notebooks/house_price_model.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Title
st.title("Toronto Housing Price Index Predictor based on Crime Rates")

# Dropdowns
attribute = st.selectbox("Attribute HPI", [
    'Apartment', 'Detached', 'Townhouse', 'Semi-Detached'
])

municipality = st.selectbox("Toronto Municipality", [
    'C01', 'C02', 'C03', 'C04', 'C06', 'C07', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08', 'E09', 'E10', 'E11', 'W01', 'W02', 'W03', 'W04', 'W05', 'W06', 'W07', 'W08', 'W09', 'W10'
])

# Numeric Inputs
year = st.number_input("Year", min_value=2015, max_value=2030, step=1, format="%d")
crime_count = st.number_input("Crime Count", min_value=0, step=1)

# Predict button
if st.button("Predict Price"):
    # Create input data matching the model's expected features
    input_dict = {
        'Year': year,
        'Crime Count': crime_count,
        f'Attribute_{attribute}': 1,
        f'Toronto Municipality_{municipality}': 1
    }

    # Fill the rest of the required features with 0s
    expected_features = loaded_model.feature_names_in_
    input_data = pd.DataFrame([{feat: input_dict.get(feat, 0) for feat in expected_features}])

    # Predict and reverse log-transform
    prediction_log = loaded_model.predict(input_data)[0]
    prediction_dollar = np.exp(prediction_log)

    st.success(f"Predicted Price: ${prediction_dollar:,.0f}")
