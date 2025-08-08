# 🍔 Obesity Prediction with FastAPI & Streamlit

This project predicts obesity categories based on a person's lifestyle and health-related data. It covers the full machine learning workflow: from preprocessing and model training to API deployment with FastAPI and a user-friendly interface with Streamlit.

---

## 🎯 Main Objectives
- 📊 Process and prepare obesity-related data
- 🧠 Train and evaluate classification models
- 🌐 Deploy the best-performing model via FastAPI
- 💻 Build a Streamlit frontend for interactive prediction

---

## 🧾 Dataset Description
The dataset contains lifestyle habits, physical condition, and dietary patterns of individuals.

| Feature | Description |
|---------|-------------|
| `Gender` | 👤 Gender (`Male` / `Female`) |
| `Age` | 📅 Age in years |
| `Height` | 📏 Height in meters |
| `Weight` | ⚖️ Weight in kilograms |
| `family_history_with_overweight` | 🧬 Family history of being overweight (`yes` / `no`) |
| `FAVC` | 🍟 Frequent consumption of high-calorie food (`yes` / `no`) |
| `FCVC` | 🥦 Frequency of vegetable consumption (0–3) |
| `NCP` | 🍽 Number of main meals per day |
| `CAEC` | 🍫 Consumption between meals (`Always`, `Frequently`, `Sometimes`, `no`) |
| `SMOKE` | 🚬 Smoking habit (`yes` / `no`) |
| `CH2O` | 💧 Daily water consumption (liters) |
| `SCC` | 🧾 Calorie monitoring (`yes` / `no`) |
| `FAF` | 🏃 Weekly physical activity (hours) |
| `TUE` | 🖥 Daily technology use (hours) |
| `CALC` | 🍺 Alcohol consumption (`Frequently`, `Sometimes`, `no`) |
| `MTRANS` | 🚗 Mode of transportation |
| `NObeyesdad` | 🎯 Target variable: Obesity category |

---

## 🧹 Data Cleaning & Preprocessing
- Split the dataset into **train** and **test** sets  
- Removed duplicates and handled anomalies in the `Age` column (removed the word “years” to keep integer values)  
- Built preprocessing pipelines:  
  - **without_outlier_pipeline**: Mean imputation + StandardScaler  
  - **with_outlier_pipeline**: Median imputation + RobustScaler  
  - **ordinal_pipeline**: Most frequent imputation + Ordinal encoding (with defined category order) + StandardScaler  
  - **onehot_pipeline**: Most frequent imputation + One-hot encoding (`handle_unknown='ignore'`) + StandardScaler (`with_mean=False`)  

---

## 🧠 Model Development
- Tested **Random Forest** and **CatBoost** classifiers  
- Selected **Random Forest** based on better performance  
- Combined preprocessing pipelines with the model and fitted on `X_train`, `y_train`  
- Predicted on `X_test` and evaluated using **classification report**  

---

## ⚙️ Deployment Architecture

### 1️⃣ FastAPI Backend
- Loads the trained Random Forest model  
- Provides `/predict` endpoint for JSON input and returns predicted obesity category  
- File: `2702235891_NatashaKaylaCahyadi_2.py`

### 2️⃣ Streamlit Frontend
- User-friendly form for entering lifestyle & health details  
- Sends input to FastAPI for prediction  
- Displays predicted obesity category  
- File: `2702235891_NatashaKaylaCahyadi_3.py`

---

## ▶️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/NatashaKayla/Obesity-Prediction-with-Streamlit.git
cd Obesity-Prediction-with-Streamlit
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Start FastAPI Server

```bash
uvicorn 2702235891_NatashaKaylaCahyadi_2:app --reload
```

### 4. Start Streamlit App

```bash
streamlit run 2702235891_NatashaKaylaCahyadi_3.py
```

---

## 📌 Conclusion

* ✅ Built an end-to-end obesity prediction system with separate backend and frontend
* 📊 Preprocessing pipelines handled numerical, ordinal, and nominal features efficiently
* 🖥️ The Streamlit app makes predictions accessible to non-technical users
