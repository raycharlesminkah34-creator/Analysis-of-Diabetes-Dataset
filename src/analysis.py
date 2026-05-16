import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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
