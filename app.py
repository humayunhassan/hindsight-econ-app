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
    st.markdown("**Topic:** Scarcity, Opportunity Cost, and the Production Possibility Curve (PPC).")
    
    st.subheader("PPC Simulator: Medical PPE vs. Consumer Goods")
    st.markdown("Adjust the slider to allocate resources. Notice how producing more PPE reduces consumer goods.")
    
    ppe_allocation = st.slider("Resources allocated to Medical PPE (%)", min_value=0, max_value=100, value=50, step=5)
    
    x = np.linspace(0, 100, 100)
    y = np.sqrt(100**2 - x**2) 
    
    current_x = ppe_allocation
    current_y = np.sqrt(100**2 - current_x**2)
    
    # Fixed chart size using figsize=(8, 4.5) to prevent overflow
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(x, y, label="PPC", color="blue")
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

    # -----------------------------------------
# PAGE 3: Episode 2 (Supply & Demand)
# -----------------------------------------
elif page == "Ep 2: Supply & Demand":
    st.title("Episode 2: The Suez Canal Blockage")
    st.markdown("**Topic:** Exogenous Supply Shocks and Market Equilibrium.")
    
    st.subheader("Supply Shift Simulator")
    st.markdown("Simulate the Ever Given getting stuck by shifting the supply curve to the left.")
    
    # Slider to simulate shock
    supply_shock = st.slider("Severity of Supply Chain Blockage", min_value=0, max_value=40, value=0, step=10)
    
    # Base Data
    q = np.linspace(0, 100, 100)
    demand = 100 - q
    supply_base = q
    supply_shocked = q + supply_shock # Shifts supply curve up/left
    
    # Find Equilibriums
    eq_q_base = 50
    eq_p_base = 50
    eq_q_shock = (100 - supply_shock) / 2
    eq_p_shock = 100 - eq_q_shock
    
    # Plotting
    fig, ax = plt.subplots()
    ax.plot(q, demand, label="Demand", color="blue")
    ax.plot(q, supply_base, label="Original Supply (S1)", color="green")
    
    if supply_shock > 0:
        ax.plot(q, supply_shocked, label="Shocked Supply (S2)", color="red", linestyle="--")
        ax.plot(eq_q_shock, eq_p_shock, 'ro', markersize=8)
        ax.annotate(f'New Eq: P={eq_p_shock:.0f}, Q={eq_q_shock:.0f}', (eq_q_shock+2, eq_p_shock+2))
    
    ax.plot(eq_q_base, eq_p_base, 'go', markersize=8)
    ax.annotate(f'Original Eq: P={eq_p_base}, Q={eq_q_base}', (eq_q_base+2, eq_p_base+2))
    
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Quantity of Shipping Containers")
    ax.set_ylabel("Price of Shipping")
    ax.set_title("Global Shipping Freight Market")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    
    st.pyplot(fig)
    
    if supply_shock > 0:
        st.warning("Notice how the exogenous shock shifts the supply curve left, increasing the market-clearing price and reducing quantity.")
