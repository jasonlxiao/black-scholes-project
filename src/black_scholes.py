import numpy as np
from scipy.stats import norm

"""
Parameters:
    S    : Underlying asset price
    K    : Strike price
    T    : Time to expiration (years)
    r    : Risk-free interest rate
    sigma: volatility of the underlying asset
"""

def check_inputs(S, K, T, r, sigma):
    if S <= 0:
        raise ValueError("Asset price must be positive.")
    if K <= 0:
        raise ValueError("Strike price must be positive.")
    if T <= 0:
        raise ValueError("Time must be positive.")
    if sigma <= 0:
        raise ValueError("Volatility must be positive")


def d1(S, K, T, r, sigma):
    #edge cases
    if T <= 1e-10:
        if S > K:
            return np.inf
        elif S < K:
            return -np.inf
        else:
            return 0
        
    if abs(sigma * np.sqrt(T)) <= 1e-10:
        if S > K:
            return np.inf
        else:
            return -np.inf

    return (np.log(S/K) + (r + .5 * pow(sigma, 2)) * T) / (sigma * np.sqrt(T))
    

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


def call_price(S, K, T, r, sigma):
    check_inputs(S, K, T, r, sigma)

    if T <= 1e-10:
        return max(0, S - K)
    
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    return S * norm.cdf(d1_val) - K * np.exp(-r * T) * norm.cdf(d2_val)


def put_price(S, K, T, r, sigma):
    check_inputs(S, K, T, r, sigma)

    if T <= 1e-10:
        return max(0, K - S)
    
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    return K * np.exp(-r * T) * norm.cdf(-d2_val) - S * norm.cdf(-d1_val)


#Call Greeks
def call_delta(S, K, T, r, sigma):
    """
    Measures how much the call option's price changes when the underlying asset price moves. Higher deltas indicate a stronger link between the stock price and the call's value. Ranges between 0 and 1.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        if S > K:
            return 1.0
        else:
            return 0.0
    d1_val = d1(S, K, T, r, sigma)
    return norm.cdf(d1_val)


def call_theta(S, K, T, r, sigma):
    """
    Measures how much value the call option loses as time passes. Call theta is usually negative because time decay reduces the option's value.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        return 0.0
    
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    return -(S * norm.pdf(d1_val) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2_val)


def call_rho(S, K, T, r, sigma):
    """
    Measures how sensitive the call price is to changes in interest rates. Call rho is positive because higher rates increase the relative value of owning the underlying asset instead of paying the strike price later.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        return 0.0
    
    d2_val = d2(S, K, T, r, sigma)
    return K * T * np.exp(-r * T) * norm.cdf(d2_val)


#Put Greeks
def put_delta(S, K, T, r, sigma):
    """
    Measures how much the put option's price changes when the underlying asset moves. Put delta is negative because puts gain value when the stock price falls. Ranges between -1 and 0.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        if S < K:
            return -1.0
        else:
            return 0.0
    d1_val = d1(S, K, T, r, sigma)
    return norm.cdf(d1_val) - 1



def put_theta(S, K, T, r, sigma):
    """
    Measures how much value a put option loses as time passes. Put theta is usually negative because options become less valuable the closer they get to expiration.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        return 0.0
    
    d1_val = d1(S, K, T, r, sigma)
    d2_val = d2(S, K, T, r, sigma)
    return -(S * norm.pdf(d1_val) * sigma) / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2_val)



def put_rho(S, K, T, r, sigma):
    """
    Measures how sensitive a put option's price is to changes in interest rates. Put rho is negative because higher rates reduce the value of receiving the strike price in the future.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        return 0.0
    
    d2_val = d2(S, K, T, r, sigma)
    return -K * T * np.exp(-r * T) * norm.cdf(-d2_val)

#Shared Greeks
def gamma(S, K, T, r, sigma):
    """
    Measures how quickly delta changes as the underlying price moves. High gamma means the option's sensitivity to price changes shifts rapidly, especially near the money.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        return 0.0
    
    d1_val = d1(S, K, T, r, sigma)
    return norm.pdf(d1_val) / (S * sigma * np.sqrt(T))


def vega(S, K, T, r, sigma):
    """
    Measures how much the option's price changes when volatility changes. Higher vega means the option is more affected by uncertainty in future price movement.
    """
    check_inputs(S, K, T, r, sigma)
    if T <= 1e-10:
        return 0.0
    
    d1_val = d1(S, K, T, r, sigma)
    return S * norm.pdf(d1_val) * np.sqrt(T)


#Public API
__all__ = ['call_price',
           'put_price',
           'call_delta',
           'call_theta',
           'call_rho',
           'put_delta',
           'put_theta',
           'put_rho',
           'gamma',
           'vega']


if __name__ == "__main__":
    #Example usage
    S = 100      # Asset price
    K = 100      # Strike price
    T = 1.0      # 1 year to expiration
    r = 0.05     # 5% risk-free rate
    sigma = 0.2  # 20% volatility

    print("=" * 50)
    print("Black-Scholes Option Pricing Model Example")
    print("=" * 50)
    print("\nInputs:")
    print(f"  Underlying Asset Price (S): ${S}")
    print(f"  Strike Price (K): ${K}")
    print(f"  Time to Expiration (T): {T} years")
    print(f"  Risk-free Rate (r): {r * 100}%")
    print(f"  Sigma (σ): {sigma * 100}%")

    print("OPTION PRICES".center(50))
    print("-" * 50)
    call = call_price(S, K, T, r, sigma)
    put = put_price(S, K, T, r, sigma)
    print(f"Call Option Price: {call:.4f}")
    print(f"Put Option Price: {put:.4f}")

    print(f"\n{'THE GREEKS - CALL OPTION':^50}")
    print("-" * 50)
    print(f"Delta:   {call_delta(S, K, T, r, sigma):.4f}")
    print(f"Gamma:   {gamma(S, K, T, r, sigma):.4f}")
    print(f"Theta:   {call_theta(S, K, T, r, sigma):.4f}")
    print(f"Vega:    {vega(S, K, T, r, sigma):.4f}")
    print(f"Rho:     {call_rho(S, K, T, r, sigma):.4f}")
    
    print(f"\n{'THE GREEKS - PUT OPTION':^50}")
    print("-" * 50)
    print(f"Delta:   {put_delta(S, K, T, r, sigma):.4f}")
    print(f"Gamma:   {gamma(S, K, T, r, sigma):.4f}")
    print(f"Theta:   {put_theta(S, K, T, r, sigma):.4f}")
    print(f"Vega:    {vega(S, K, T, r, sigma):.4f}")
    print(f"Rho:     {put_rho(S, K, T, r, sigma):.4f}")


