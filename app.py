import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- 1. Load model -----------------------------------------------------------
with open("notebooks/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

feature_names = model.feature_names_in_

# --- 2. Mapping dictionaries -------------------------------------------------
attr_label_to_col = {
    "Apartment":        "Attribute_HPI - Apartment",
    "Detached":         "Attribute_HPI - Single-Family Detached",
    "Townhouse":        "Attribute_HPI - Townhouse",
    "Semi-Detached":    "Attribute_HPI - Single-Family Attached",
}

# every code just needs "Toronto " in front of it
muni_codes = [
    'C01','C02','C03','C04','C06','C07','C08','C09','C10','C11','C12','C13','C14','C15',
    'E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','E11',
    'W01','W02','W03','W04','W05','W06','W07','W08','W09','W10'
]
muni_label_to_col = {code: f"Toronto Municipality_Toronto {code}" for code in muni_codes}

st.image("references/homepage.png", use_column_width=True)
# --- 3. Streamlit UI ---------------------------------------------------------
st.markdown("<style>h1 {text-align:center;}</style>", unsafe_allow_html=True)
st.title("Toronto Housing Price Index Predictor based on Crime Rates")

attr_choice = st.selectbox("Attribute HPI", list(attr_label_to_col.keys()))
muni_choice = st.selectbox("Toronto Municipality", muni_codes)
year        = st.text_input("Year (e.g. 2020)")
crime_count = st.text_input("Crime Count (whole number)")

if st.button("Predict Price"):

    # start with a single-row DF full of zeros
    X = pd.DataFrame(np.zeros((1, len(feature_names))), columns=feature_names)

    # set the chosen one-hot columns to 1
    X.loc[0, attr_label_to_col[attr_choice]] = 1
    X.loc[0, muni_label_to_col[muni_choice]] = 1

    # set numeric inputs
    X.loc[0, "Year"]         = year
    X.loc[0, "Crime Count"]  = crime_count

    # --- 4. Predict ----------------------------------------------------------
    log_pred = model.predict(X)[0]
    dollar_pred = np.exp(log_pred)

    st.success(f"Predicted Price: ${dollar_pred:,.0f}")