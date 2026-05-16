import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Run correlation analysis
correlations = df.corr(method='spearman')
outcome_corr = correlations.iloc[:, -1].sort_values(ascending=False)
print("Correlation of features with the outcome variable:")
print(outcome_corr)

# Visualize the correlation matrix
plt.figure(figsize=(10,8))
sns.heatmap(correlations, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix of Diabetes Dataset")
plt.tight_layout()
plt.show()

# Show only risk factors correlated with outcome (excluding outcome itself)
risk_factors = outcome_corr[outcome_corr.index != "Outcome"].abs().sort_values(ascending=False)
print("\nRisk factors sorted by correlation with the outcome variable:")
print(risk_factors)

# Visualize just the outcome correlations
plt.figure(figsize=(6,4))
risk_factors.sort_values(ascending=True).plot(kind='barh')
plt.xlabel("Spearman Correlation with Outcome")
plt.title("Correlation of Risk Factors with Diabetes Outcome")
plt.tight_layout()  
plt.show()

#Dtermining whther the correlation of the highest 3 is statistically significant
for factor in risk_factors.index:
    corr, p_value = spearmanr(df[factor], df["Outcome"])
    print(f"Correlation between {factor} and Outcome: {corr:.2f}, p-value: {p_value:.4f}")  



