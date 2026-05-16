# Diabetes Analysis Project

This project analyzes the `diabetes.csv` dataset to identify risk factors associated with diabetes outcome and to check for multicollinearity among predictors.

Structure
- `data/` - raw and processed data (project root `diabetes.csv` present)
- `src/` - analysis scripts (`analysis.py`)
- `reports/` - generated results (correlation tables, VIF, figures)
- `notebooks/` - exploratory notebooks (if any)

Quick start
1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\Activate      # Windows PowerShell
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the analysis script from the project root:

```bash
python src/analysis.py
```

What the script produces
- `reports/correlation_matrix.csv` — Spearman correlation matrix for numeric features
- `reports/feature_correlation_significance.csv` — Pearson & Spearman r and p-values vs `Outcome`
- `reports/vif.csv` — Variance Inflation Factors for numeric predictors

Next steps
- Review `reports/feature_correlation_significance.csv` for significant predictors (p < 0.05)
- Review `reports/vif.csv` and consider dropping or regularizing features with `VIF > 5` or `VIF > 10`
- Build a baseline model in `src/` and evaluate performance

If you want, I can help draft a short write-up of the findings to copy into `reports/analysis_summary.md`.
