# 📂 Dataset

This project uses the **Credit Card Fraud Detection** dataset, which contains anonymized credit card transactions made by European cardholders over two consecutive days.

## 📊 Dataset Information

| Property | Value |
|----------|-------|
| Dataset Name | Credit Card Fraud Detection |
| Source | Kaggle |
| Total Transactions | 284,807 |
| Fraudulent Transactions | 492 (0.172%) |
| Features | 30 |
| Target Variable | `Class` |

### Features

- **Time** – Seconds elapsed between transactions
- **V1–V28** – PCA-transformed anonymized features
- **Amount** – Transaction amount
- **Class** – Target variable (`0` = Legitimate, `1` = Fraud)

---

## 📥 Download

The original `creditcard.csv` file (~147 MB) is not included in this repository due to GitHub's recommended file size limits.

You can download the dataset using either of the following options:

- [Google Drive](https://drive.google.com/file/d/1Cgi9JSYWNO0qAEbTgoXG8B-BtNTgoWcN/view?usp=sharing)
- [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

---

## 📄 Citation

Andrea Dal Pozzolo, Olivier Caelen, Reid A. Johnson, and Gianluca Bontempi.

*Calibrating Probability with Undersampling for Unbalanced Classification.*

Proceedings of the IEEE Symposium Series on Computational Intelligence (SSCI), 2015.

---

## ⚠️ Note

The dataset is publicly available for **educational and research purposes**. All features except **Time**, **Amount**, and **Class** have been anonymized using **Principal Component Analysis (PCA)**.
