# Month 6 + Month 7 — Statistics, ML Foundations & Advanced ML
**Deepanshu Garg | [@deepanshu0110](https://github.com/deepanshu0110)**

> **Month 6 (Days 101–120):** Descriptive statistics, probability, hypothesis testing,
> A/B testing, linear regression, PCA, cross-validation, sklearn pipelines,
> GridSearchCV, ensemble methods, SHAP, imbalanced datasets, full ML capstone.
>
> **Month 7 (Days 121–140):** Advanced ML — XGBoost, LightGBM, CatBoost, SHAP,
> ensemble stacking, Optuna, ARIMA, Prophet, Isolation Forest, capstone.

---

## Summary

| Metric | Month 6 | Month 7 |
|--------|---------|---------|
| Days | 101–120 (20 days) | 121–140 (20 days) |
| Status | **20 / 20 ✅ COMPLETE** | **20 / 20 ✅ PERFECT** |
| Dataset | ShopEase India (seed=42, 300 rows) | RetailPulse India (seed=121, 500 rows) |
| Top Score | 100/100 + 15★ (Day 113) | 80/80 + 10★ (all 20 days) |
| Base Points | **1,659 / 1,660** | **1,440 / 1,440** |
| Bonus Stars | **185★** | **180★** |

---

## Month 6 Scorecard — Stats + ML Foundations (Days 101–120) ✅ COMPLETE

| Day | Topic | Score |
|-----|-------|-------|
| Day 101 | Descriptive Stats + Distributions | 80/80 ✅ |
| Day 102 | T-Tests + Confidence Intervals | 80/80 + 10★ ✅ |
| Day 103 | Chi-Square + ANOVA | 80/80 + 10★ ✅ |
| Day 104 | A/B Testing with scipy | 80/80 + 10★ ✅ |
| Day 105 | Week 1 Mini-Project | 80/80 + 10★ ✅ |
| Day 106 | Hypothesis Testing Deep Dive | 80/80 + 10★ ✅ |
| Day 107 | Effect Size + Statistical Power | 80/80 + 10★ ✅ |
| Day 108 | Week 2 Mini-Project | 80/80 + 10★ ✅ |
| Day 109 | Linear Regression Foundations | 80/80 + 10★ ✅ |
| Day 110 | Train-Test Split + R² + RMSE | 80/80 + 10★ ✅ |
| Day 111 | Feature Selection | 80/80 + 10★ ✅ |
| Day 112 | PCA — Principal Component Analysis | 80/80 + 10★ ✅ |
| Day 113 | Week 3 Mini-Project | **100/100 + 15★** ✅ |
| Day 114 | Cross-Validation (KFold + StratifiedKFold) | 80/80 + 10★ ✅ |
| Day 115 | Scikit-learn Pipeline API | 80/80 + 10★ ✅ |
| Day 116 | GridSearchCV + Hyperparameter Tuning | 80/80 + 10★ ✅ |
| Day 117 | Ensemble Methods — Random Forest + Gradient Boosting | 80/80 + 10★ ✅ |
| Day 118 | SHAP Explainability | 80/80 + 10★ ✅ |
| Day 119 | Imbalanced Datasets (SMOTE + class_weight) | 80/80 + 10★ ✅ |
| Day 120 | **Month 6 Capstone — Full ML Pipeline** | **119/120** ✅ |

**Month 6 final: 1,659 / 1,660 pts + 185★**

---

## Month 7 Scorecard — Advanced ML (Days 121–140) ✅ PERFECT

| Day | Topic | Score |
|-----|-------|-------|
| Day 121 | XGBoost — Gradient Boosting | 80/80 + 10★ ✅ |
| Day 122 | LightGBM — Leaf-wise Boosting | 80/80 + 10★ ✅ |
| Day 123 | CatBoost — Native Categoricals | 80/80 + 10★ ✅ |
| Day 124 | Ensemble Stacking | 80/80 + 10★ ✅ |
| Day 125 | Data Leakage Detection + Prevention | 80/80 + 10★ ✅ |
| Day 126 | SHAP — Advanced Explainability | 80/80 + 10★ ✅ |
| Day 127 | PCA + t-SNE Visualisation | 80/80 + 10★ ✅ |
| Day 128 | K-Means Clustering | 80/80 + 10★ ✅ |
| Day 129 | Hierarchical Clustering + DBSCAN | 80/80 + 10★ ✅ |
| Day 130 | Week 2 Mini-Project | 80/80 + 10★ ✅ |
| Day 131 | Feature Selection (RFE + Permutation) | 80/80 + 10★ ✅ |
| Day 132 | Hyperparameter Tuning with Optuna | 80/80 + 10★ ✅ |
| Day 133 | Time Series — ARIMA + statsmodels | 80/80 + 10★ ✅ |
| Day 134 | Time Series — Prophet + Forecasting | 80/80 + 10★ ✅ |
| Day 135 | Imbalanced Datasets + SMOTE | 80/80 + 10★ ✅ |
| Day 136 | Advanced sklearn Pipelines | 80/80 + 10★ ✅ |
| Day 137 | Cross-Validation Strategies | 80/80 + 10★ ✅ |
| Day 138 | Anomaly Detection — Isolation Forest | 80/80 + 10★ ✅ |
| Day 139 | Month 7 Capstone — Part 1 | 80/80 + 10★ ✅ |
| Day 140 | Month 7 Capstone — Part 2 | 80/80 + 10★ ✅ |

**Month 7 final: 1,440 / 1,440 pts + 180★ — Perfect run.**

---

## Key Lessons

| Day | Lesson |
|-----|--------|
| Day 113 | Verified: NRA insights with exact printed numbers beat generic commentary every time |
| Day 118 | SHAP values need a business sentence — "SHAP = 1.92" means nothing; translate it |
| Day 120 | Recall ≠ Precision — confusion between these two in written NRA costs points on client reports |
| Day 122 | CV ROC-AUC < 0.5 = deployment red flag — never recommend a sub-random model |
| Day 123 | CatBoost's target-encoding advantage doesn't activate on low-cardinality (3–5 value) categoricals |
| Day 125 | Leaving target column in X after `get_dummies()` → AUC = 1.0 (data leakage) |
| Day 134 | Partial months inflate MAPE — always exclude incomplete periods from error metrics |

---

## Tools & Stack

**Month 6:** Python · NumPy · Pandas · scipy.stats · scikit-learn · XGBoost · SHAP · Matplotlib · Seaborn

**Month 7:** scikit-learn · XGBoost · LightGBM · CatBoost · Optuna · SHAP · Prophet ·
statsmodels · imbalanced-learn · Pandas · Matplotlib · Seaborn

---

## Repo Structure

```
Month6-Stats-ML-Portfolio/
├── Day101_Descriptive_Stats.ipynb
├── Day102_T_Tests_CI.ipynb
├── Day103_ChiSquare_ANOVA.ipynb
├── Day104_AB_Testing.ipynb
├── Day105_Week1_MiniProject.ipynb
├── Day106_Hypothesis_Testing.ipynb
├── Day107_Effect_Size_Power.ipynb
├── Day108_Week2_MiniProject.ipynb
├── Day109_Linear_Regression.ipynb
├── Day110_TrainTest_R2_RMSE.ipynb
├── Day111_Feature_Selection.ipynb
├── Day112_PCA.ipynb
├── Day113_Week3_MiniProject.ipynb
├── Day114_CrossValidation.ipynb
├── Day115_PipelineAPI.ipynb
├── Day116_GridSearchCV.ipynb
├── Day117_Ensemble_Methods.ipynb
├── Day118_SHAP.ipynb
├── Day119_Imbalanced_Datasets.ipynb
├── Day120_Month6_Capstone.ipynb
└── auto_sync.py

Month7-AdvancedML-Portfolio/
├── Day121_XGBoost.ipynb
├── Day122_LightGBM.ipynb
├── Day123_CatBoost.ipynb
├── Day124_Ensemble_Stacking.ipynb
├── Day125_Data_Leakage.ipynb
├── Day126_SHAP.ipynb
├── Day127_PCA_tSNE.ipynb
├── Day128_KMeans_Clustering.ipynb
├── Day129_Hierarchical_DBSCAN.ipynb
├── Day130_Week2_MiniProject.ipynb
├── Day131_Feature_Selection.ipynb
├── Day132_Optuna_Tuning.ipynb
├── Day133_ARIMA.ipynb
├── Day134_Prophet.ipynb
├── Day135_SMOTE_Imbalanced.ipynb
├── Day136_Advanced_Pipelines.ipynb
├── Day137_Cross_Validation.ipynb
├── Day138_Isolation_Forest.ipynb
├── capstone/
│   ├── Day139_Month7_Capstone_Part1.ipynb
│   └── Day140_Month7_Capstone_Part2.ipynb
└── auto_sync.py
```

---

## All Months

| Month | Repo | Highlight | Top Score |
|-------|------|-----------|-----------|
| Month 1 — Excel | [excel-data-analytics](https://github.com/deepanshu0110/excel-data-analytics) | 16 workbooks | 88/80 |
| Month 2 — SQL | [Month2-SQL-Portfolio](https://github.com/deepanshu0110/Month2-SQL-Portfolio) | Window functions, CTEs | 119/120 |
| Month 3 — Python/Pandas | [Month3-Python-Portfolio](https://github.com/deepanshu0110/Month3-Python-Portfolio) | EDA + math bridge | 100/100 |
| Month 4 — Power BI + Tableau | [Month4-PowerBI-Tableau-Portfolio](https://github.com/deepanshu0110/Month4-PowerBI-Tableau-Portfolio) | Live Tableau Public dashboard | 110/100 |
| Month 5 — BI + Upwork | [Month5-BI-Upwork-Portfolio](https://github.com/deepanshu0110/Month5-BI-Upwork-Portfolio) | UrbanNest India capstone | **120/120** |
| Month 6 — Stats + ML Foundations | *(this repo)* | ShopEase churn pipeline | **1,659/1,660** |
| Month 7 — Advanced ML | [Month7-AdvancedML-Portfolio](https://github.com/deepanshu0110/Month7-AdvancedML-Portfolio) | RetailPulse India, SHAP, Prophet | **1,440/1,440 🏆** |

---

*Auto-synced via watchdog · Last updated: 29 May 2026*
