import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

from src.black_scholes import (
    call_price, put_price,
    call_delta, put_delta,
    call_theta, put_theta,
    call_rho, put_rho,
    gamma, vega
)

#Page Configurations
st.set_page_config(
    page_title="Black-Scholes Option Pricing", 
    layout="wide"
)

st.title("Black-Scholes Option Pricing Dashboard")

#Sidebar Inputs
st.sidebar.header("Input Parameters")

S = st.sidebar.number_input("Underlying Asset Price (S)", value=100.0, min_value=0.01, step=1.0)
K = st.sidebar.number_input("Strike Price (K)", value=100.0, min_value=0.01, step=1.0)
T = st.sidebar.number_input("Time to Expiration (T, years)", value=1.0, min_value=0.01, step=0.1)
r = st.sidebar.number_input("Risk-free Rate (r)", value=0.05, min_value=0.0, step=0.01, format="%.4f")
sigma = st.sidebar.number_input("Volatility (σ)", value=0.20, min_value=0.01, step=0.01, format="%.4f")

#Tabs for Layout
tab_prices, tab_call, tab_put, tab_charts = st.tabs(
    ["💰 Option Prices", "📈 Call Greeks", "📉 Put Greeks", "📊 Charts"]
)

#Error Handling
try:
    #Compute Option Prices
    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)

    #Compute Greeks
    c_delta = call_delta(S, K, T, r, sigma)
    c_theta = call_theta(S, K, T, r, sigma)
    c_rho = call_rho(S, K, T, r, sigma)
    p_delta = put_delta(S, K, T, r, sigma)
    p_theta = put_theta(S, K, T, r, sigma)
    p_rho = put_rho(S, K, T, r, sigma)
    g = gamma(S, K, T, r, sigma)
    v = vega(S, K, T, r, sigma)


    #OPTION PRICES TAB
    with tab_prices:
        st.subheader("Option Prices")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Call Price", f"{call:.4f}")
        with col2:
            st.metric("Put Price", f"{put:.4f}")

    #CALL GREEKS TAB
    with tab_call:
        st.subheader("Call Option Greeks")
        st.write(f"**Delta:** {c_delta:.4f}")
        st.write(f"**Theta:** {c_theta:.4f}")
        st.write(f"**Rho:** {c_rho:.4f}")
        st.write(f"**Gamma:** {g:.4f}")
        st.write(f"**Vega:** {v:.4f}")

    #PUT GREEKS TAB
    with tab_put:
        st.subheader("Put Option Greeks")
        st.write(f"**Delta:** {p_delta:.4f}")
        st.write(f"**Theta:** {p_theta:.4f}")
        st.write(f"**Rho:** {p_rho:.4f}")
        st.write(f"**Gamma:** {g:.4f}")
        st.write(f"**Vega:** {v:.4f}")

    #CHARTS TAB
    with tab_charts:
        st.subheader("Sensitivity: Option Price vs Underlying Price")

        S_range = np.linspace(S * .5, S * 1.5, 50)
        call_vals = []
        put_vals = []
        for s in S_range:
            call_vals.append(call_price(s, K, T, r, sigma))
            put_vals.append(put_price(s, K, T, r, sigma))

        fig, ax = plt.subplots(figsize = (10, 6))
        ax.plot(S_range, call_vals, label="Call Price", color="green")
        ax.plot(S_range, put_vals, label="Put Price", color="blue")
        ax.axvline(S, color='red', linestyle='--', alpha=0.5, label=f"Current S = {S}")
        ax.set_xlabel("Underlying Asset Price (S)")
        ax.set_ylabel("Option Price")
        ax.set_title("Option Prices vs Underlying Asset Price")
        ax.legend()
        ax.grid(True, alpha=0.3)

        st.pyplot(fig)
        
except ValueError as e:
    st.error(f"Error: {str(e)}")
except Exception as e:
    st.error(f"Something went wrong: {str(e)}")
