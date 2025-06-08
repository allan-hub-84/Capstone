import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from our pickle file.
with open("notebooks/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

feature_names = model.feature_names_in_

# Map the column labels to our data frame.
attr_label_to_col = {
    "Apartment":        "Attribute_HPI - Apartment",
    "Detached":         "Attribute_HPI - Single-Family Detached",
    "Townhouse":        "Attribute_HPI - Townhouse",
    "Semi-Detached":    "Attribute_HPI - Single-Family Attached",
}
muni_codes = [
    'C01','C02','C03','C04','C06','C07','C08','C09','C10','C11','C12','C13','C14','C15',
    'E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','E11',
    'W01','W02','W03','W04','W05','W06','W07','W08','W09','W10'
]
muni_label_to_col = {code: f"Toronto Municipality_Toronto {code}" for code in muni_codes}

# Set image and title of page.
st.image("references/homepage.png", use_column_width=True)
# --- 3. Streamlit UI ---------------------------------------------------------
st.markdown("<style>h1 {text-align:center;}</style>", unsafe_allow_html=True)
st.title("Toronto Housing Price Index Predictor based on Crime Rates")

# Set drop downs and inputs.
attr_choice = st.selectbox("Property Type", list(attr_label_to_col.keys()))
muni_choice = st.selectbox("Toronto Municipality", muni_codes)
year = st.selectbox(
    "Year",
    options=list(range(2015, 2031)),   # 2031 is non-inclusive, so stops at 2030
    index=5                            # pre-select 2020 (optional)
)
crime_count = st.number_input("Crime Count", min_value=0, step=250)

# Set function for button.
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

import requests

@st.cache_data
def load_csv_from_github(url):
    raw_url = url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return pd.read_csv(raw_url)

# CSV link
github_csv_url = "https://github.com/allan-hub-84/Capstone/blob/main/data/municipality_neighbourhoods.csv"

try:
    df_reference = load_csv_from_github(github_csv_url)

st.markdown("""
    <h3 style='text-align: center;'>Municipality and Neighbourhood Reference Table</h3>
""", unsafe_allow_html=True)
    st.dataframe(df_reference)
except Exception as e:
    st.error("Unable to load the reference table from GitHub.")
    st.error(str(e))