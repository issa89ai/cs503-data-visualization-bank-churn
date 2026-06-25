# CS503 – Data Visualization: Bank Customer Churn

## 📘 Course Information

- **Course:** CS503 – Data Visualization  
- **Term:** Winter 2025  
- **Institution:** Bishop's University  
- **Project Type:** Final Project  
- **Topic:** Visual Analysis of Bank Customer Churn  

---

## 📌 Project Description

This project applies data visualization techniques to explore and analyze a **bank customer churn dataset** (10,000 customers, 12 features). The goal is to identify patterns and factors that contribute to customer churn using a variety of visualization methods.

Key questions explored:
- What is the churn rate overall and by country/gender?
- How do credit score, age, and balance differ between churned and retained customers?
- Which features are most correlated with churn?

---

## 📊 Dataset

- **File:** `data/Bank Customer Churn Prediction.csv`
- **Rows:** 10,000 customers
- **Columns:** 12 features

| Feature | Description |
|---|---|
| `customer_id` | Unique customer identifier |
| `credit_score` | Customer credit score |
| `country` | Country of residence (France, Germany, Spain) |
| `gender` | Male / Female |
| `age` | Customer age |
| `tenure` | Years as a bank customer |
| `balance` | Account balance |
| `products_number` | Number of bank products held |
| `credit_card` | Has credit card (1/0) |
| `active_member` | Active member (1/0) |
| `estimated_salary` | Estimated annual salary |
| `churn` | Churned (1) or retained (0) — target variable |

---

## 📈 Visualizations Included

- Churn rate by country and gender (bar charts)
- Age and credit score distributions by churn status (histograms)
- Balance distribution for churned vs retained customers
- Correlation heatmap of all numerical features
- Churn rate by number of products held

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

---

## 📂 Repository Structure

```
cs503-data-visualization-bank-churn/
├── data/
│   └── Bank Customer Churn Prediction.csv
├── visualizations.py          # Main visualization script
├── presentation/
│   ├── Project Data visualization.pptx
│   └── Project_DVis.pdf
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

1. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```

2. Run the visualization script:
   ```bash
   python visualizations.py
   ```

---

## 📝 Notes

This project was developed as part of an academic course.  
The code is intended for educational and research purposes only.

## 👤 Author

**Ahmad Issa**  
Bishop's University  
Department of Computer Science
