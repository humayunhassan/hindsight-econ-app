import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Page Configuration
st.set_page_config(page_title="Hindsight Economics Hub", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select an Episode", ["The Roadmap", "Ep 1: Scarcity & PPC"])

# -----------------------------------------
# PAGE 1: The Roadmap
# -----------------------------------------
if page == "The Roadmap":
    st.title("Hindsight Economics: 10-Episode Roadmap")
    st.markdown("Mapping core Term 1 topics to major economic events from 2016-2024.")
    
    data = {
        "Episode": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Syllabus Topic": [
            "Scarcity & PPC", "Supply, Demand & Eq.", "Price Elasticity", 
            "Negative Externalities", "Gov. Failure", "Monopoly Power", 
            "Labour Markets", "Inflation", "Monetary Policy", "Fiscal Policy"
        ],
        "Historical Case Study": [
            "2020 PPE Shortage", "2021 Suez Canal Blockage", "2020-22 Microchip Shortage", 
            "2018 Sugar Tax", "2022 UK Mini-Budget", "Tech Giant App Stores", 
            "2021 Uber Supreme Court Ruling", "2022-23 Cost of Living Crisis", 
            "2022-24 Global Rate Hikes", "2020-21 Furlough Scheme"
        ]
    }
    df = pd.DataFrame(data)
    st.table(df.set_index("Episode"))

# -----------------------------------------
# PAGE 2: Episode 1 (PPC)
# -----------------------------------------
elif page == "Ep 1: Scarcity & PPC":
    st.title("Episode 1: The 2020 Ventilator Shortage")
    st.markdown("**Topic:** Scarcity, Opportunity Cost, and the Production Possibility Frontier (PPF).")
    
    st.subheader("PPC Simulator: Medical PPE vs. Consumer Goods")
    st.markdown("Adjust the slider to allocate resources. Notice how producing more PPE reduces consumer goods.")
    
    ppe_allocation = st.slider("Resources allocated to Medical PPE (%)", min_value=0, max_value=100, value=50, step=5)
    
    x = np.linspace(0, 100, 100)
    y = np.sqrt(100**2 - x**2) 
    
    current_x = ppe_allocation
    current_y = np.sqrt(100**2 - current_x**2)
    
    fig, ax = plt.subplots()
    ax.plot(x, y, label="PPF Curve", color="blue")
    ax.plot(current_x, current_y, 'ro', markersize=10, label="Current Production")
    
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 110)
    ax.set_xlabel("Medical PPE (Quantity)")
    ax.set_ylabel("Consumer Goods (Quantity)")
    ax.set_title("Production Possibility Curve")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    
    st.pyplot(fig)
    st.info(f"**Opportunity Cost Alert:** By allocating {current_x}% to PPE, you can only produce {current_y:.1f} units of Consumer Goods.")