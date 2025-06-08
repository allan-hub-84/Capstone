import streamlit as st
import pandas as pd
import numpy as np
import pickle
from pathlib import Path

# ──────────────────────────────────────────────────────────────
#  Page settings
# ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Toronto HPI Predictor", layout="centered")

# ──────────────────────────────────────────────────────────────
#  Banner image  ❱❱  place the PNG inside /references
# ──────────────────────────────────────────────────────────────
image_path = Path("references/homepage.png")
if image_path.exists():
    st.image(image_path, use_column_width=True)
else:
    # Fallback to raw-GitHub URL if the local file isn't found
    st.image(
        "https://raw.githubusercontent.com/allan-hub-84/Capstone/main/references/homepage.png",
        use_column_width=True,
    )

# ──────────────────────────────────────────────────────────────
#  Centred title
# ──────────────────────────────────────────────────────────────
st.markdown(
    "<h1 style='text-align:center;'>Toronto Housing Price Index Predictor based on Crime Rates</h1>",
    unsafe_allow_html=True
)

# ──────────────────────────────────────────────────────────────
#  Load model
# ──────────────────────────────────────────────────────────────
with open("notebooks/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

feature_names = model.feature_names_in_

# ──────────────────────────────────────────────────────────────
#  Mapping dictionaries
# ──────────────────────────────────────────────────────────────
attr_label_to_col = {
    "Apartment":      "Attribute_HPI - Apartment",
    "Detached":       "Attribute_HPI - Single-Family Detached",
    "Townhouse":      "Attribute_HPI - Townhouse",
    "Semi-Detached":  "Attribute_HPI - Single-Family Attached",
}

muni_codes = [
    'C01','C02','C03','C04','C06','C07','C08','C09','C10','C11','C12',
    'C13','C14','C15','E01','E02','E03','E04','E05','E06','E07','E08',
    'E09','E10','E11','W01','W02','W03','W04','W05','W06','W07','W08',
    'W09','W10'
]
muni_label_to_col = {code: f"Toronto Municipality_Toronto {code}" for code in muni_codes}

# ──────────────────────────────────────────────────────────────
#  UI widgets
# ──────────────────────────────────────────────────────────────
attr_choice = st.selectbox("Attribute HPI", list(attr_label_to_col.keys()))
muni_choice = st.selectbox("Toronto Municipality", muni_codes)

year_str        = st.text_input("Year (e.g. 2020)")
crime_count_str = st.text_input("Crime Count (whole number)")

# simple validator
def _to_int(value: str, field: str) -> int:
    if not value.strip().isdigit():
        st.error(f"❌ Please enter a valid integer for **{field}**")
        st.stop()
    return int(value)

if st.button("Predict Price"):

    year        = _to_int(year_str,        "Year")
    crime_count = _to_int(crime_count_str, "Crime Count")

    X = pd.DataFrame(np.zeros((1, len(feature_names))), columns=feature_names)

    X.loc[0, attr_label_to_col[attr_choice]] = 1
    X.loc[0, muni_label_to_col[muni_choice]] = 1
    X.loc[0, "Year"]        = year
    X.loc[0, "Crime Count"] = crime_count

    log_pred    = model.predict(X)[0]
    dollar_pred = np.exp(log_pred)

    st.success(f"Predicted Price: **${dollar_pred:,.0f}**")