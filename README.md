# South Africa Inflation and Interest Rate Analysis (2014–2024)

## Project Overview

This project investigates the relationship between inflation and interest rates in South Africa between 2014 and 2024.

The analysis was conducted using Python and explores whether changes in inflation are associated with changes in the South African Reserve Bank's repo rate.

## Objectives

* Analyse historical inflation and repo rate data.
* Measure the relationship between inflation and interest rates.
* Investigate whether interest rate responses occur with a delay.
* Visualise economic trends using graphs.
* Apply basic statistical and machine learning techniques.

## Tools Used

* Python
* pandas
* matplotlib
* scikit-learn

## Methodology

1. Import and clean the data.
2. Merge inflation and repo rate datasets.
3. Calculate the correlation between inflation and repo rates.
4. Create a one-year lagged inflation variable.
5. Calculate lagged correlation.
6. Fit a linear regression model.
7. Visualise the results using line charts and regression plots.

## Results

### Correlation Analysis

* Raw correlation: 0.50
* Lagged correlation: 0.72

### Regression Analysis

* Regression slope: 0.91
* Regression intercept: 1.49

## Key Findings

The analysis found a moderate positive relationship between inflation and repo rates.

When inflation was lagged by one year, the relationship became substantially stronger. This suggests that monetary policy responses may occur with a delay rather than immediately following changes in inflation.

## Project Structure

```text
Inflation_vs_Interest_Rate.py
inflation.csv
interest_rate.csv
graphs/
```

## Data Sources

* Statistics South Africa (inflation data)
* South African Reserve Bank (repo rate data)
* World Bank (cross-checking and validation)

## Author

Hephzibah

