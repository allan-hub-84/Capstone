# Capstone Project: Predict Home Price Index Based on Major Crime Incident in Toronto

## Overview:

In Canada, affordable housing has been hot debate in the last 10 years.  Housing prices have increased year over year, and affordability is a challenge country wide.  Toronto, Ontario, which is Canada’s most populated city, is the second most expensive city to live in Canada.  The Home Price Index for Toronto has increased 8% year over year, with property values ending at $1.6M for detached, $1.2M for semi-detached, $870K for townhouses and $690K for apartments by the end of 2024.

Purchasing a property is one of the biggest investments a person can make, and these invests are assets that are dependent upon for investments for retirement or to generate generational wealth.  It’s then crucial to understand what factors can affect housing prices, to maximize equity and return on investment.  With this tool, we aim to predict the housing price impact by neighborhood, based on the estimated crime rate incidents.

## Data:

MLS® Home Price Index Archive: https://trreb.ca/market-data/mls-home-price-index/mls-home-price-index-archive/


Toronto Police Services Major Crime Indicators Open Data: https://data.torontopolice.on.ca/datasets/TorontoPS::major-crime-indicators-open-data/about

Toronto Neighbourhood Index: https://app.trreb.ca/trrebdata/common/maps/Toronto.pdf


## Next Steps:

• Address the null values in the HPI - Townhouse columns, in the MLS data.  Utilize the K Nearest Neighbours approach to get approximate values.
• Address the null values (NSA) in the NEIGHBOURHOOD_140 column, in the Toronto Police data.  Since these areas are unknown, we can omit this from the total data set.
• Create a joined data frame, to link all the data sets together.
• Conduct logistics regression, to determine relationship and statistical significance.
• Feature engineering, to determine which levers we can use for our prediction.
