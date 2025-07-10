# 📘 Student Score Predictor

This project predicts students' final exam scores (G3) based on:
- Their scores in the 1st and 2nd periods (`G1`, `G2`)
- Weekly study time
- Number of absences

The model is trained using **Linear Regression** and deployed as an interactive **Streamlit app** for real-time predictions.

---

## 🔍 Dataset

- Source: `student-por.csv`  
- Contains student performance data from a Portuguese school.
- Important features used:
  - `studytime`: Weekly study time (1–4 scale)
  - `absences`: Number of school absences
  - `G1`, `G2`: Previous grades
  - `G3`: Final grade (target)

---

## 🧠 ML Model

- **Algorithm**: Linear Regression (scikit-learn)
- **Evaluation**:
  - Metrics: MAE, MSE, RMSE, R²
  - Feature importance analyzed using model coefficients

---

## 📂 Files

| File Name                  | Description                             |
|---------------------------|-----------------------------------------|
| `Student_Score_Predictor.ipynb` | Notebook for data cleaning, training, evaluation |
| `student-por.csv`         | Raw dataset used for training           |
| `student_score_model.pkl` | Saved trained model                     |
| `app.py`                  | Streamlit app for prediction            |

---

## 🚀 Run the App Locally

### ▶️ 1. Install requirements
```bash
pip install streamlit scikit-learn pandas
```

### ▶️ 2. Run Streamlit app
```bash
streamlit run app.py
```

---

## 📈 Sample Prediction Inputs

| Feature     | Example Input |
|-------------|----------------|
| G1          | 14             |
| G2          | 15             |
| studytime   | 3              |
| absences    | 4              |

---

## 📌 Project Info

- Developed as part of **Celebal Internship - Week 7**
- Author: Satvik Vaishnav
- Date: July 2025

---
