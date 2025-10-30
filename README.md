# 💧 Smart Water Intake Advisor

### 🧠 Overview
**Smart Water Intake Advisor** is a machine learning–based project designed to predict an individual's optimal daily water intake.  
It considers factors such as **ambient temperature, body weight, age, gender, and activity level** to provide a personalized hydration recommendation — especially useful in **hot climate regions like India**.

---

## 🚀 Features
- Predicts **personalized water intake (in liters)**.  
- Uses multiple **regression models** for accurate prediction.  
- Provides **data preprocessing and visualization**.  
- Easy to extend for **real-time or mobile integration**.  

---

## ⚙️ Technologies Used
| Category | Tools / Libraries |
|-----------|-------------------|
| **Language** | Python |
| **Libraries** | pandas, numpy, scikit-learn, matplotlib, seaborn |
| **Environment** | Jupyter Notebook / VS Code |
| **Models Used** | Linear Regression, Random Forest Regression, Support Vector Regression (SVR) |

---

## 🧩 How It Works
1. **Data Collection & Preprocessing**  
   - Dataset includes user and environmental details (age, weight, temperature, etc.).  
   - Missing values handled and categorical variables encoded.  

2. **Model Training**  
   - Trains three regression models: **Linear Regression**, **SVR**, and **Random Forest Regression**.  
   - Each model predicts water intake based on input features.  

3. **Prediction**  
   - User inputs their details → model outputs personalized **daily water requirement (in liters)**.  

---

## 📊 Example Features
| Feature | Description | Example |
|----------|--------------|----------|
| Age | Age of person (years) | 25 |
| Weight | Body weight (kg) | 70 |
| Gender | Male / Female | Male |
| Activity Level | Low / Moderate / High | Moderate |
| Ambient Temperature | Surrounding temperature (°C) | 32 |
| Water Intake (Target) | Predicted daily water intake (L/day) | 3.2 L |

---

## 🛠️ Installation & Usage

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/smart-water-intake-advisor.git
cd smart-water-intake-advisor
## 2️⃣ install dependencies
pip install -r requirements.txt
3️⃣ Run Notebook or Script
jupyter notebook SmartWaterIntakeAdvisor.ipynb
```

##💬 Future Enhancements
Integration with IoT-enabled smart bottles for real-time tracking.

Development of a web or mobile app interface.

Use of live weather APIs for automatic temperature updates.

Health-based recommendations (e.g., for athletes or medical conditions).

##👩‍💻 Authors
Cadence Three
Developed as part of a Semester Case Study Project

##  Conclusion
The Smart Water Intake Advisor helps users maintain proper hydration through intelligent, data-driven insights.
It combines health awareness and technology to promote a smarter, healthier lifestyle.
