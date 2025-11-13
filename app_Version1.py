import streamlit as st
import pandas as pd
import random
import os

# 🎯 Page Config
st.set_page_config(page_title="Smart Spending Advisor", page_icon="💳", layout="centered")

# 🧾 Title
st.title("💳 Smart Spending Advisor")
st.write("Analyze customer spending habits and get AI-driven payment recommendations.")

# Allow runtime CSV upload (useful for testing in the browser)
st.sidebar.header("Data options")
uploaded_file = st.sidebar.file_uploader("Upload customers CSV (optional)", type=["csv"])

# Try to load CSV from repo path data/customers.csv if it exists, otherwise use uploaded file, otherwise mock
DATA_PATH = os.path.join("data", "customers.csv")

def load_data():
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("Loaded dataset from upload")
            return df
        except Exception as e:
            st.sidebar.error(f"Failed to read uploaded CSV: {e}")
    if os.path.exists(DATA_PATH):
        try:
            df = pd.read_csv(DATA_PATH)
            st.sidebar.success(f"Loaded dataset from {DATA_PATH}")
            return df
        except Exception as e:
            st.sidebar.error(f"Failed to read {DATA_PATH}: {e}")
    # Fallback mock data
    return pd.DataFrame({
        "Customer ID": ["CUST_0159", "CUST_0245", "CUST_0312"],
        "Category": ["Groceries", "Travel", "Fitness"],
        "Total Spent": [45.5, 280.0, 130.0],
        "Payment Method": ["Debit Card", "Credit Card", "Cash"]
    })

data = load_data()

# 🧍 Input Section
customer_id = st.text_input("Enter Customer ID:")

# 🧠 When the user clicks 'Predict'
if st.button("🔍 Analyze Spending"):
    
    if customer_id in data["Customer ID"].values:
        # Retrieve user data
        user_data = data[data["Customer ID"] == customer_id].iloc[0]
        
        st.subheader(f"Customer Summary: {customer_id}")
        st.write(f"**Category:** {user_data['Category']}")
        st.write(f"**Total Spent:** €{user_data['Total Spent']}")
        st.write(f"**Actual Payment Method:** {user_data['Payment Method']}")
        
        # --- Analytical AI Mock (your ML model output here) ---
        predicted_method = random.choice(["Credit Card", "Debit Card", "Cash"])
        confidence = round(random.uniform(0.7, 0.95), 2)
        
        st.success(f"🧠 Predicted Payment Method: **{predicted_method}** (Confidence: {confidence})")
        
        # --- Generative AI Mock (LLM output here) ---
        if predicted_method == "Debit Card":
            ai_tip = "You often use debit for purchases. Try switching to a credit card with cashback offers to save more."
        elif predicted_method == "Credit Card":
            ai_tip = "Your spending on credit cards is high. Consider paying in full each month to avoid interest."
        else:
            ai_tip = "Cash payments limit your rewards. Using digital wallets can help you track and save better."
        
        st.markdown("### 💬 AI Recommendation")
        st.info(ai_tip)
        
        # Optional visualization
        st.markdown("---")
        st.write("📊 *Coming soon:* Spending trend visualization")
        
    else:
        st.error("Customer ID not found in dataset. Please try another ID.")

# Footer
st.markdown("---")
st.caption("Built by Team Flyntric | M2 AI Project | Grenoble Ecole de Management")