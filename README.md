# Capstone Project: Predict Home Price Index Based on Major Crime Incident in Toronto
### Author: Allan Salamanca
### Date: June 09, 2025

## Table of Contents

1. [App Demo](#app-demo)
2. [Notebook and Presentation Files](#notebook-and-presentation-files)
3. [Overview](#overview)
4. [Objective](#objective)
5. [Data Sets](#data-sets)
6. [EDA](#eda)
7. [Data Preprocessing](#data-preprocessing)
8. [Baseline Modelling](#baseline-modelling-linear-regression)
9. [Advanced Modelling](#advanced-modelling)
10. [Future State](#future-state)

## App Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]
([https://capstone-z3gwvoh8gmh4eegnyh23k.streamlit.app](https://capstone-rv5xhecomeolprloxvqvac.streamlit.app/))

## Notebook and Presentation Files
1. [EDA](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_EDA.ipynb)
2. [Preprocessing](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_Preprocessing.ipynb)
3. [Baseline Modelling](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_BaselineModelling.ipynb)
4. [Advanced Modelling](https://github.com/allan-hub-84/Capstone/blob/main/notebooks/AllanSalamanca_Capstone_AdvanceModelling.ipynb)
5. [Capstone Presentation](https://github.com/allan-hub-84/Capstone/blob/main/docs/AllanSalamanca_Capstone.pdf)

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

It is evident that there are varying property value increases by neighbourhood, both in terms of absolute value and percentage.  Certain areas yield a higher return, and we can use this information to check if major crime incidents in specific neighbourhoods can influence property values.

<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/hpiyoy.png?raw=true" alt="Homepage" width="800"/>
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/hpiyoyavgincrease.png?raw=true" alt="Homepage" width="800"/>
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/muniyoyavgincrease.png?raw=true" alt="Homepage" width="800"/>
</p>

According to police data, crime rates have increased annually, but specific neighbourhoods and crime types are more prevalent than others.  We can use this information to analyze whether crimes, categorized by neighbourhood, influence property values within the same neighbourhood.  If there is a significant relationship, this can help predict property values by neighbourhood based on crime incidents.
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/crimeyoy.png?raw=true" alt="Homepage" width="800"/>
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/crimebymuni.png?raw=true" alt="Homepage" width="800"/>
</p>

## Data Preprocessing

To link the two data sets (in our EDA), we need to create a join table that matches the Toronto Municipality column in the MLS data to the NEIGHBOURHOOD_140 column in the Toronto Police data.  After doing online research, I found the neighbourhood maps on the Toronto Real Estate Board website (https://app.trreb.ca/trrebdata/common/maps/Toronto.pdf).

After merging the data, I created dummy variables for categories of property type and neighbourhood.  Additionally, to address the missing values in the data set, I utilized K-nearest neighbours to impute the missing data.  The final version of our data frame is here: https://github.com/allan-hub-84/Capstone/blob/main/data/df_v5.csv

After we merge the data, we can review the correlation matrix.  We can see in the matrix that most values are below 0.5, except for one.  The Toronto Municipality (C01) shows a 0.65 correlation with crime counts; however, the correlation with property values is -0.05.  This makes sense since it's a highly dense area downtown, primarily consisting of apartments.  For now, I am keeping it in my model.  Additionally, I will drop the month column and use the Year, as it has a stronger correlation with property values.
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/correlationmatrix.png?raw=true" alt="Homepage" width="800"/>
</p>

## Baseline Modelling Linear Regression

In general, we have a good R-squared value at 0.77%, which explains most of our variance.  Another thing we notice is that there are no p-values > 0.05.  We can continue working on this model.

### Standard Scaler & Linear Regression Results
- Train R² :  77.06%
- Test  R² :  77.40%
- Test RMSE: $246,819
- Test  MAE: $166,915

### OLS Results
- R-Squared – 0.771
- No p-value > 0.05

We notice that even though the residuals are normally distributed, it is screwed (positive) at the right tail.  We also observe in our Q plot that our model underestimates the value of high-value homes.
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/baselineres.png?raw=true" alt="Homepage" width="800"/>
</p>
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/baselineq.png?raw=true" alt="Homepage" width="800"/>
</p>
Here, we can see that our model exhibits heteroscedasticity, indicating it is not consistent across the dataset.  We see that variances are increasing the value of housing prices increases.  This confirms our residual and Q-plot results.
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/baselinehet.png?raw=true" alt="Homepage" width="800"/>
</p>
Our model from Scikit-learn, even when scaled, yields results that are very similar to those of our initial linear regression model.  It confirms that our model doesn't perform well in predicting high-value properties, and it generally underestimates them.
While our accuracy score is 77%, we notice a significant range in our RMSE and MAE scores.  To make our model more accurate, we need to understand the outliers that impact the RMSE and MAE. 
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/baselineactpre.png?raw=true" alt="Homepage" width="800"/>
</p>


## Advanced Modelling

Our baseline model struggles with high property values.  We notice this in values over $ 2 million.  Since we know that some of our independent variables have a higher influence on our dependent variable (Attribute & Municipality), we need to account for these in our advanced modelling.  Additionally, since property values have a wide range, we can consider scaling the data using a Log, using a percentage change in house price instead.  Logging “shrinks” the extreme values, allowing the model to focus on the majority instead of the outliers.

By simply log-transforming the data, we can already see much smoother linear regression results.
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/logbaselineactpre.png?raw=true" alt="Homepage" width="800"/>
</p>

After log-transforming the data set, we utilized GridSearchCV to determine the best model among Decision Tree Regressor, Random Forest Regressor, and Extreme Gradient Boosting.  After adjusting and testing multiple parameters, the best model recommended is Extreme Gradient Boosting, with the suggested parameters being a 0.2 learning rate, a maximum depth of 8, and 300 n_estimators.

</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/learningrate.png?raw=true" alt="Homepage" width="800"/>
</p>

We can see that the XGBoost Regressor predicts housing prices with very high accuracy. After applying a log transformation and using GridSearch, it achieved an R² of 98.84%, meaning it explains nearly all the variation in prices. Now, the average error went from $167K to $37K, increasing the confidence level in the model. The results demonstrate a strong correlation between predicted and actual prices, enhancing the reliability of the tool.

### Extreme Gradient Boosting Results
- Test  R² :  98.84%
- Test RMSE: $61,482
- Test  MAE: $37,070
</p>
<p align="left">
  <img src="https://github.com/allan-hub-84/Capstone/blob/main/references/advancedactpre.png?raw=true" alt="Homepage" width="800"/>
</p>

## Future State

There are many other data sets we can utilize to enhance this model.  Currently, we are utilizing high-level numbers based on property type, neighbourhood, total crime and year.

The following data sets can be incorporated in the future to enhance the granularity of our analysis and predictions.

- Population Density
- Postal Code
- Crime Type
- Neighbourhood Ratings: School, Hospitals, Community Centers, Police Station, Fire Station, Etc.
- Development
- Number of Open Listings

