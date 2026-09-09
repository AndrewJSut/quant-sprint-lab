import numpy as np


def monte_carlo_price(
    S0: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    n_sims: int = 100_000,
    option_type: str = "call"
) -> tuple[float, float]:
    """Returns a tuple: (estimated_price, standard_error)."""

    # Generate random standard normal variables
    Z = np.random.normal(0, 1, n_sims)

    # Simulate terminal stock prices
    ST = S0 * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z
    )

    # Calculate option payoff
    if option_type == "call":
        payoff = np.maximum(ST - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - ST, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    # Discount payoff to present value
    discounted_payoff = np.exp(-r * T) * payoff

    # Monte Carlo price and standard error
    estimated_price = np.mean(discounted_payoff)
    standard_error = np.std(discounted_payoff, ddof=1) / np.sqrt(n_sims)

    return estimated_price, standard_error


if __name__ == "__main__":
    price, se = monte_carlo_price(
        S0=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20,
        n_sims=100_000
    )

    print("Monte Carlo Price:", price)
    print("Standard Error:", se)