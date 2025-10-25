# -------------------- Page config --------------------
import streamlit as st
import pandas as pd
import cloudpickle  # Safe for scikit-learn pipelines

# Streamlit page settings
st.set_page_config(page_title="Smart Water Intake Advisor", layout="wide")

# Load trained model safely using cloudpickle
with open("model/lr_intake.pkl", "rb") as f:
    model = cloudpickle.load(f)

# Debug: check type and attributes
st.write(type(model))
# st.write("Has predict method:", hasattr(model, "predict"))


# -------------------- Custom Styling --------------------
st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e2f;
        }
        .description-box {
            background-color: #2c3e50;
            padding: 20px;
            border-radius: 10px;
            color: #f5f5f5;
        }
        .input-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            color: #000000;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# -------------------- Layout Columns --------------------
left_col, right_col = st.columns([1, 2])

# -------------------- RIGHT COLUMN: Inputs + Prediction --------------------
with right_col:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    st.header("Personalized Hydration Recommendation")

    # -------------------- Input Fields --------------------
    age = st.number_input("Age", min_value=1, max_value=120, value=20)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=60.0)
    height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=155.0)
    temperature = st.slider("Ambient Temperature (°C)", 10.0, 45.0, 25.0)
    humidity = st.slider("Humidity (%)", 10.0, 100.0, 50.0)
    exercise = st.slider("Exercise Duration (min)", 0, 180, 30)
    gender = st.selectbox("Gender", ["Male", "Female"])
    activity = st.selectbox("Activity Level", ["Sedentary", "Moderate", "Active"])
    health = st.selectbox("Health Condition", ["Healthy", "Chronic Issues"])
    consumed = st.number_input("Water Already Consumed (liters)", min_value=0.0, max_value=10.0, step=0.1, value=1.0)

    prediction_value = None
    hydration_percentage = 0

    # if st.button("Predict Water Intake"):
    #     # -------------------- Data Preparation --------------------
    #     input_data = pd.DataFrame({
    #         'Age': [age],
    #         'Gender': [1 if gender == "Male" else 0],
    #         'Weight_kg': [weight],
    #         'Height_cm': [height],
    #         'Temperature_C': [temperature],
    #         'Humidity': [humidity],
    #         'Activity_Level': [activity],
    #         'Exercise_Duration_min': [exercise],
    #         'Health_Condition': [health]
    #     })

    #     # Make prediction safely

    #     prediction_value = model.predict(input_data)[0]
    #     remaining = max(0, prediction_value - consumed)
    #     hydration_percentage = min(100, (consumed / prediction_value) * 100)

    #     st.success(f"💧 Recommended Daily Water Intake: {prediction_value:.2f} liters")
    #     st.info(f"🚰 Water Left to Drink Today: {remaining:.2f} liters")
    if st.button("Predict Water Intake"):
        # -------------------- Data Preparation --------------------
        input_data = pd.DataFrame([{
            'Age': age,
            'Gender': 1 if gender == "Male" else 0,
            'Weight_kg': weight,
            'Height_cm': height,
            'Temperature_C': temperature,
            'Humidity': humidity,
            'Activity_Level': activity,
            'Exercise_Duration_min': exercise,
            'Health_Condition': health
        }])

        # -------------------- Debug Preview --------------------
        st.write("Input shape:", input_data.shape)
        st.write("Input preview:", input_data)

        # -------------------- Prediction --------------------
        try:
            prediction_value = model.predict(input_data)[0]
            remaining = max(0, prediction_value - consumed)
            hydration_percentage = min(100, (consumed / prediction_value) * 100)

            st.success(f"Predicted daily water intake: {prediction_value:.2f} ml")
            st.info(f"Remaining intake: {remaining:.2f} ml")
            st.progress(hydration_percentage / 100)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- LEFT COLUMN: Description + Hydration Glass --------------------
with left_col:
    st.markdown('<div class="description-box">', unsafe_allow_html=True)
    st.header("💧 Personalised Smart Water Intake Advisor")
    st.write(
        "A Smart Personalized Water Intake Advisor predicts an individual’s daily water requirement "
        "based on age, weight, activity, and lifestyle factors using machine learning. It provides "
        "personalized hydration recommendations and insights to promote better health and well-being."
    )

    st.subheader("🔍 Feature Descriptions")
    st.markdown("""
    - **Age**: Your current age  
    - **Weight & Height**: Used to estimate hydration needs  
    - **Temperature & Humidity**: Environmental factors  
    - **Exercise Duration**: Daily physical activity (in minutes)  
    - **Gender**: Biological sex (0 = Female, 1 = Male)  
    - **Activity Level**: Lifestyle intensity  
    - **Health Condition**: General health status  
    - **Water Already Consumed**: Track your hydration progress  
    """)

    st.markdown("## 🧊 Hydration Glass")
    
    # If prediction not made yet, show default 50%
    display_level = hydration_percentage if prediction_value is not None else 50

    # Water level visualization
    water_html = f"""
    <div style="
        width: 120px;
        height: 220px;
        border: 4px solid #00BFFF;
        border-radius: 15px;
        position: relative;
        background: linear-gradient(to top, #00BFFF {display_level}%, transparent {display_level}%);
        margin: 20px auto;
    ">
        <p style='position: absolute; bottom: 10px; width: 100%; text-align: center; color: white; font-weight: bold;'>
            {display_level:.0f}%
        </p>
    </div>
    """
    st.markdown(water_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
