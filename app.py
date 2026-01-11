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
