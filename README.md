# Analysis of Diabetes Dataset

## Overview
This project explores the Pima Indians Diabetes Dataset to identify which clinical features are most strongly associated with a diabetes diagnosis. The analysis focuses on correlation analysis using Spearman's method and statistical significance testing.

## Dataset
- **Source:** [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Features:** Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age, Pregnancies
- **Target Variable:** Outcome (1 = diabetic, 0 = non-diabetic)

## Tools & Libraries
- Python
- Pandas & NumPy — data loading and manipulation
- Seaborn & Matplotlib — data visualization
- SciPy — statistical testing

## What Was Done

### Correlation Analysis
- Computed a full Spearman correlation matrix across all features
- Extracted correlations with the `Outcome` variable and ranked them by strength
- Visualized the full correlation matrix as a heatmap
- Plotted risk factors as a horizontal bar chart ranked by absolute correlation

### Statistical Significance Testing
- Applied Spearman's correlation test for each feature against `Outcome`
- Reported correlation coefficients and p-values to assess significance

## Key Findings
- **Glucose** showed the strongest correlation with diabetes outcome
- **BMI** and **Age** were also among the top risk factors
- All major risk factors returned p-values of < 0.05, confirming statistically significant relationships

## Repository Structure
```
Analysis-of-Diabetes-Dataset/
│
├── diabetes.csv               # Dataset
├── eda_notebooks.ipynb        # Full analysis notebook
└── README.md                  
```

## Author
Ray-charles | Biomedical Sciences & Data Analysis