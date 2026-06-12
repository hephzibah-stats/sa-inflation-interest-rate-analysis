import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the datasets
inflation = pd.read_csv("inflation.csv")
interest = pd.read_csv("interest_rate.csv")

# Merge
merged = pd.merge(inflation, interest, on="Year")

#Correlation
print(merged[['Inflation Rate (%)', 'RepoRate (%)']].corr())

# Lagged Inflation Rate vs Repo Rate
merged["Inflation Rate (%)_lag1"] = merged["Inflation Rate (%)"].shift(1)

print(merged[['Inflation Rate (%)_lag1', 'RepoRate (%)']].corr())

#Regression
df = merged.dropna()

x= df[["Inflation Rate (%)_lag1"]]
y= df["RepoRate (%)"]

model = LinearRegression()
model.fit(x, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

df["Predicted"] = model.predict(x)

# Plotting the Inflation Rate and Repo Rate
plt.figure(figsize=(10, 5))

plt.plot(merged['Year'], merged['Inflation Rate (%)'], marker='o', label='Inflation Rate')
plt.plot(merged['Year'], merged['RepoRate (%)'], marker='o', label='Repo Rate')

plt.xlabel('Year')
plt.ylabel('Rate (%)')
plt.title('South Africa:Inflation Rate vs Repo Rate')
plt.legend()
plt.grid(True)

plt.savefig("graphs/inflation_vs_interest_rate.png", dpi=300)
plt.show()

# Plotting the regression results
plt.figure(figsize=(10, 5))

plt.scatter(df['Inflation Rate (%)_lag1'], df['RepoRate (%)'], label='Actual Data')
plt.plot(df['Inflation Rate (%)_lag1'], df['Predicted'], label='Regression Line', color='red')

plt.xlabel('Inflation Rate (%) (Lagged by 1 Year)')
plt.ylabel('RepoRate (%)')
plt.title('South Africa: Lagged Inflation Rate vs Repo Rate')

plt.legend()
plt.grid(True)
plt.savefig("graphs/regression_plot.png", dpi=300, bbox_inches='tight')
plt.show()

#Insights
raw_corr = merged[['Inflation Rate (%)', 'RepoRate (%)']].corr().iloc[0, 1]
lagged_corr = merged[['Inflation Rate (%)_lag1', 'RepoRate (%)']].corr().iloc[0, 1]
print("\n--- KEY INSIGHTS ---")
print(f"1. Raw correlation: {raw_corr:.2f}")
print(f"2. Lagged correlation: {lagged_corr:.2f}")
print(f"3. Regression slope: {model.coef_[0]:.2f}")
print(f"4. Regression intercept: {model.intercept_:.2f}")

print("\nInterpretation:")
print("Inflation and repo rates show a moderate positive relationship.")
print("The relationship becomes stronger when inflation is lagged by one year.")
print("This suggests monetary policy may respond to inflation with a delay.")