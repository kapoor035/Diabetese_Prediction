# 🩺 Diabetes Prediction System (ML Lab Project)

## 📌 Overview
This project is a **Machine Learning-based web application** that predicts whether a person is likely to have diabetes or not based on medical input parameters.

It uses a trained **Random Forest Classifier** model and a **Flask web application** to provide predictions in real time.

---

## 🚀 Features
- Predicts **Diabetes Risk (High / Low)**
- Simple and clean UI
- Fast and accurate predictions
- Built using Flask + Machine Learning

---

## 🧠 Machine Learning Details
- Algorithm: **Random Forest Classifier**
- Dataset: `diabetes.csv`
- Model File: `diabetes-prediction-rfc-model.pkl`

### 📥 Input Features:
- Pregnancies  
- Glucose  
- Blood Pressure  
- Skin Thickness  
- Insulin  
- BMI  
- Diabetes Pedigree Function  
- Age  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS  
- **Backend:** Flask (Python)  
- **ML Libraries:** NumPy, Scikit-learn  
- **Model Storage:** Pickle  

---

## 📂 Project Structure

ML Project/
│── app.py
│── train_model.py
│── diabetes.csv
│── diabetes-prediction-rfc-model.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── images & assets

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/kapoor035/Diabetese_Prediction.git
cd Diabetese_Prediction

2️⃣ Install Dependencies

pip install flask numpy scikit-learn

3️⃣ Run the App

python app.py

4️⃣ Open in Browser

http://localhost:5001


⸻

📊 How It Works
	1.	User enters medical data
	2.	Data is sent to Flask backend
	3.	Model predicts using trained ML model
	4.	Result is shown:
	•	High Risk of Diabetes
	•	Low Risk of Diabetes

⸻

⚠️ Note
	•	This project is for educational purposes only
	•	Model can be retrained using train_model.py

⸻

👨‍💻 Author

Gaurav Kapoor
23FE10CSE00230
Section C Manipal University Jaipur

⸻

💡 Future Improvements
	•	Add authentication system
	•	Deploy on cloud (Render / AWS)
	•	Improve UI/UX
	•	Increase model accuracy

⸻

⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
