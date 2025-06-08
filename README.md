# Capstone Project: Predict Home Price Index Based on Major Crime Incident in Toronto
 <b>Author:</b> Allan Salamanca

## Table of Contents

1. [App Demo](#app-demo)
2. [Notebook & Presentation Files](#notebook-&-presentation-files)
3. [Overview](#overview)
4. [Objective](#objective)
5. [Data Sets](#data-sets)
6. [EDA](#eda)
7. [Data Preprocessing](#data-preprocessing)
8. [Baseline Modelling](#baseline-modelling)
9. [Advanced Modelling](#advanced-modeeling)
10. [Future State](#future-state)

## App Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]
([https://capstone-z3gwvoh8gmh4eegnyh23k.streamlit.app](https://capstone-rv5xhecomeolprloxvqvac.streamlit.app/))

## Notebook & Presentation Files
1. [EDA](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_EDA.ipynb)
2. [Preprocessing](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_Preprocessing.ipynb)
3. [Baseline Modelling](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_BaselineModelling.ipynb)
4. [Advanced Modelling](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_AdvanceModelling.ipynb)
5. [Capstone Presentation]

## Overview:

Affordable housing has been a hot debate in Canada in the last 10 years.  Housing prices have increased year over year, and affordability is a challenge country-wide.  Toronto, Ontario, which is Canada’s most populated city, is the second most expensive city to live in Canada.  The Home Price Index for Toronto has increased 8% year over year, with property values ending at $1.6M for detached, $1.2M for semi-detached, $870K for townhouses and $690K for apartments by the end of 2024.  Additionally, with Toronto's rising population, major crime incidents also have increased year over year by 4%.

Purchasing a property is one of the most significant investments a person can make, and these investments are assets dependent upon investments for retirement or generating generational wealth.  Understanding what factors affect housing prices is crucial to maximizing equity and return on investment.  With this tool, we aim to predict the housing price impact by neighbourhood based on the estimated crime rate incidents.

## Objective:
Predict home price index (HPI) by house type (Detached, Semi-Detached, Townhouse, or Apartment) and neighbourhood based on major crime incident occurrences to determine which neighbourhoods have the best return on investment.

### Target (Dependent Variable) = Value

### Features (Indendent Variables) = Attribute, Toronto Municiaplity, Crime Count & Year.

## Data Sets:

### 1) MLS® Home Price Index Archive: https://trreb.ca/market-data/mls-home-price-index/mls-home-price-index-archive/

| Column                          | Description                                      | Data Type     |
|---------------------------------|--------------------------------------------------|--------------|
| Toronto Municipality            | Toronto Real Estate Board Municipality Code     | object       |
| HPI - Single-Family Detached    | Home Price Index for Detached Property          | int64        |
| HPI - Single-Family Attached    | Home Price Index for Semi-Detached Property     | int64        |
| HPI - Townhouse                 | Home Price Index for Townhouse Property         | float64      |
| HPI - Apartment                 | Home Price Index for Apartment Property         | int64        |
| Effective Date                  | Date of the HPI                                 | datetime64[ns] |

### 2) Toronto Police Services Major Crime Indicators Open Data: https://data.torontopolice.on.ca/datasets/TorontoPS::major-crime-indicators-open-data/about

| Column                          | Description                                      | Data Type     |
|---------------------------------|--------------------------------------------------|--------------|
| EVENT_UNIQUE_ID                 | Offence Number                                   | object       |
| OCC_DATE                        | Date Offence Occurred                            | datetime64[ns] |
| DIVISION                        | Police Division where Offence Occurred           | object |
| PREMISES_TYPE                   | Premises Type of where Offence Occured           | object |
| OFFENCE                         | Type of Offence                                  | object |
| MCI_CATEGORY                    | Major Crime Incident Category                    | object  |
| NEIGHBOURHOOD_140               | Neighbourhood Name                               | object  |

### 3) Toronto Neighbourhood Index: https://app.trreb.ca/trrebdata/common/maps/Toronto.pdf

| Column                          | Description                                      | Data Type    |
|---------------------------------|--------------------------------------------------|--------------|
| Toronto Police Neighbourhood Categories              | Neighbourhood Name by Toronto Police Service Data                                  | object       |
| MLS Neighbourhood Categories                   | Neighbourhood Name by MLS Data                    | object       |
| MLS Municipality Code               | Municipality Code by Toronto Real Estate Board                               | object       |

### 4) Final Data Frame - "df_v5.csv"

Merged the three data sets above and created one master data frame for our modelling.

| Column                                 | Description                                         | Data Type   |
|-----------------------------------------|-----------------------------------------------------|-------------|
| Attribute_HPI - Apartment              | Apartment Categorical Flag             | float64     |
| Attribute_HPI - Single-Family Attached | Semi-Detached Property Categorical Flag                     | float64     |
| Attribute_HPI - Single-Family Detached | Detached Property Categorical Flag                             | float64     |
| Attribute_HPI - Townhouse              | Townhouse Property   Categorical Flag                         | float64     |
| Crime Count                            | Number of reported crimes in the area               | float64     |
| Toronto Municipality_Toronto C01       | Dummy variable for Toronto C01                      | float64     |
| Toronto Municipality_Toronto C02       | Dummy variable for Toronto C02                      | float64     |
| ...                                    | ...                                                 | ...         |
| Value                                  | Property Value          | float64     |
| Year                                   | Year of observation                                 | float64     |

## EDA

## Data Preprocessing

## Baseline Modelling

### Standard Scaler & Linear Regression Results
- Train R² :  77.06%
- Test  R² :  77.40%
- Test RMSE: 246,819
- Test  MAE: 166,915

### OLS Results
- R-Squared – 0.771
- No p-value > 0.05


## Advanced Modelling

## Future State


