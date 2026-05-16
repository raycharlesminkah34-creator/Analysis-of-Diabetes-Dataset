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



# --- Save results and compute full significance + VIF for documentation ---
import os
from scipy.stats import pearsonr
from statsmodels.stats.outliers_influence import variance_inflation_factor

out_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
os.makedirs(out_dir, exist_ok=True)

# Save correlation matrix
correlations.to_csv(os.path.join(out_dir, 'correlation_matrix.csv'))

# Compute significance for all numeric features vs Outcome (Pearson & Spearman)
num = df.select_dtypes(include=[np.number])
features = [c for c in num.columns if c != 'Outcome']
rows = []
for f in features:
    x = num[f].dropna()
    y = num['Outcome'].loc[x.index]
    try:
        p_r, p_p = pearsonr(x, y)
    except Exception:
        p_r, p_p = (np.nan, np.nan)
    try:
        s_r, s_p = spearmanr(x, y)
    except Exception:
        s_r, s_p = (np.nan, np.nan)
    rows.append((f, p_r, p_p, s_r, s_p))

res = pd.DataFrame(rows, columns=['feature','pearson_r','pearson_p','spearman_r','spearman_p'])
res.to_csv(os.path.join(out_dir, 'feature_correlation_significance.csv'), index=False)

# Compute VIF (impute mean for missing)
X = num[features].fillna(num[features].mean())
vif = pd.DataFrame({
    'feature': X.columns,
    'VIF': [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
})
vif.to_csv(os.path.join(out_dir, 'vif.csv'), index=False)

print(f"Saved correlation matrix, significance table, and VIF to {out_dir}")



