# Black-Scholes Option Pricing Calculator

A Python implementation of the Black-Scholes option pricing model with an interactive Streamlit dashboard for calculating option prices and analyzing Greeks in real-time.

## Overview

This project implements the classic Black-Scholes formula for European option pricing with an interactive web interface. Built to explore quantitative finance concepts and option sensitivity analysis.

## Features

### Core Pricing Engine
- European call and put option pricing using Black-Scholes formula
- Comprehensive Greeks calculation (Delta, Gamma, Theta, Vega, Rho)
- Input validation and edge case handling
- Efficient numerical computations with NumPy and SciPy

### Interactive Dashboard
- Real-time option price calculations with parameter sliders
- Tabbed interface for organized data visualization
- Price sensitivity charts showing option behavior across different underlying prices
- Automatic updates as parameters change (no submit button needed)

## The Greeks Explained

- **Delta (Δ)**: Rate of change of option price with respect to underlying price
  - Call: 0 to 1 | Put: -1 to 0
  
- **Gamma (Γ)**: Rate of change of delta with respect to underlying price
  - Same for calls and puts
  - Highest near at-the-money
  
- **Theta (Θ)**: Rate of option value decay over time
  - Usually negative (options lose value as expiration approaches)
  
- **Vega (ν)**: Sensitivity to volatility changes
  - Same for calls and puts
  - Higher for at-the-money options
  
- **Rho (ρ)**: Sensitivity to interest rate changes
  - Call: positive | Put: negative

## Project Structure

```
black-scholes-project/
├── src/
│   ├── __init__.py
│   └── black_scholes.py    # Core Black-Scholes implementation
├── app.py                  # Streamlit web application
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/jasonlxiao/black-scholes-project.git
cd black-scholes-project
```

2. Create and activate a virtual environment (recommended):
```bash
# On macOS/Linux:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Application

Launch the interactive Streamlit dashboard:

```bash
streamlit run app.py
```

The application will open automatically in your browser at `http://localhost:8501`

## Technologies

- **Python 3.x** - Core programming language
- **NumPy** - Numerical computations and array operations
- **SciPy** - Statistical functions (cumulative normal distribution)
- **Streamlit** - Interactive web dashboard framework
- **Matplotlib** - Chart generation and data visualization

## Technical Implementation

The Black-Scholes formula for a European call option:

```
C = S·N(d₁) - K·e^(-rT)·N(d₂)
```

Where:
```
d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d₂ = d₁ - σ√T
```

And N(x) is the cumulative standard normal distribution function.

## Future Enhancements

Potential features for future development:
- Implied volatility calculator (solving for σ given market price)
- Additional visualization: Greeks heatmaps and 3D surfaces
- American option pricing approximations
- Monte Carlo simulation capabilities
- Historical data integration for real-world examples

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Fischer Black, Myron Scholes, and Robert Merton for the Black-Scholes-Merton model
- Built as a learning project to understand option pricing theory and quantitative finance
