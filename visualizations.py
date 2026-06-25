"""
CS503 – Data Visualization
Bank Customer Churn Analysis
Bishop's University – Winter 2025
Author: Ahmad Issa
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Load data ────────────────────────────────────────────────────────────────
df = pd.read_csv("data/Bank Customer Churn Prediction.csv")
print(f"Dataset: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Overall churn rate: {df['churn'].mean():.1%}\n")

sns.set_theme(style="whitegrid", palette="Set2")
fig, axes = plt.subplots(3, 2, figsize=(14, 16))
fig.suptitle("Bank Customer Churn – Visual Analysis", fontsize=16, fontweight="bold", y=1.01)

# ── 1. Churn rate by country ──────────────────────────────────────────────────
churn_country = df.groupby("country")["churn"].mean().reset_index()
churn_country.columns = ["country", "churn_rate"]
axes[0, 0].bar(churn_country["country"], churn_country["churn_rate"] * 100,
               color=["#66c2a5", "#fc8d62", "#8da0cb"])
axes[0, 0].set_title("Churn Rate by Country")
axes[0, 0].set_ylabel("Churn Rate (%)")
axes[0, 0].set_xlabel("Country")
for i, v in enumerate(churn_country["churn_rate"]):
    axes[0, 0].text(i, v * 100 + 0.5, f"{v:.1%}", ha="center", fontsize=10)

# ── 2. Churn rate by gender ───────────────────────────────────────────────────
churn_gender = df.groupby("gender")["churn"].mean().reset_index()
axes[0, 1].bar(churn_gender["gender"], churn_gender["churn"] * 100,
               color=["#fc8d62", "#8da0cb"])
axes[0, 1].set_title("Churn Rate by Gender")
axes[0, 1].set_ylabel("Churn Rate (%)")
axes[0, 1].set_xlabel("Gender")
for i, v in enumerate(churn_gender["churn"]):
    axes[0, 1].text(i, v * 100 + 0.5, f"{v:.1%}", ha="center", fontsize=10)

# ── 3. Age distribution by churn status ───────────────────────────────────────
churned = df[df["churn"] == 1]["age"]
retained = df[df["churn"] == 0]["age"]
axes[1, 0].hist(retained, bins=30, alpha=0.6, label="Retained", color="#66c2a5")
axes[1, 0].hist(churned, bins=30, alpha=0.6, label="Churned", color="#fc8d62")
axes[1, 0].set_title("Age Distribution by Churn Status")
axes[1, 0].set_xlabel("Age")
axes[1, 0].set_ylabel("Count")
axes[1, 0].legend()

# ── 4. Credit score distribution by churn status ─────────────────────────────
axes[1, 1].hist(df[df["churn"] == 0]["credit_score"], bins=30,
                alpha=0.6, label="Retained", color="#66c2a5")
axes[1, 1].hist(df[df["churn"] == 1]["credit_score"], bins=30,
                alpha=0.6, label="Churned", color="#fc8d62")
axes[1, 1].set_title("Credit Score Distribution by Churn Status")
axes[1, 1].set_xlabel("Credit Score")
axes[1, 1].set_ylabel("Count")
axes[1, 1].legend()

# ── 5. Churn rate by number of products ───────────────────────────────────────
churn_products = df.groupby("products_number")["churn"].mean().reset_index()
axes[2, 0].bar(churn_products["products_number"].astype(str),
               churn_products["churn"] * 100,
               color=["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3"])
axes[2, 0].set_title("Churn Rate by Number of Products")
axes[2, 0].set_xlabel("Number of Products")
axes[2, 0].set_ylabel("Churn Rate (%)")
for i, v in enumerate(churn_products["churn"]):
    axes[2, 0].text(i, v * 100 + 0.5, f"{v:.1%}", ha="center", fontsize=10)

# ── 6. Correlation heatmap ───────────────────────────────────────────────────
numeric_cols = ["credit_score", "age", "tenure", "balance",
                "products_number", "credit_card", "active_member",
                "estimated_salary", "churn"]
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            ax=axes[2, 1], linewidths=0.5, annot_kws={"size": 8})
axes[2, 1].set_title("Feature Correlation Heatmap")

plt.tight_layout()
plt.savefig("churn_visualizations.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: churn_visualizations.png")
