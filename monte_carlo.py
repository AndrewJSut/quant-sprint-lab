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

    # Antithetic variates
    half_sims = n_sims // 2

    Z = np.random.normal(0, 1, half_sims)
    Z_antithetic = -Z

    # Simulate terminal prices for Z and -Z
    ST_1 = S0 * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z
    )

    ST_2 = S0 * np.exp(
        (r - 0.5 * sigma**2) * T
        + sigma * np.sqrt(T) * Z_antithetic
    )

    # Calculate option payoffs
    if option_type == "call":
        payoff_1 = np.maximum(ST_1 - K, 0)
        payoff_2 = np.maximum(ST_2 - K, 0)

    elif option_type == "put":
        payoff_1 = np.maximum(K - ST_1, 0)
        payoff_2 = np.maximum(K - ST_2, 0)

    else:
        raise ValueError("option_type must be 'call' or 'put'")

    # Average each antithetic pair
    pair_payoff = (payoff_1 + payoff_2) / 2

    # Discount to present value
    discounted_payoff = np.exp(-r * T) * pair_payoff

    # Monte Carlo price and standard error
    estimated_price = np.mean(discounted_payoff)
    standard_error = (
        np.std(discounted_payoff, ddof=1) / np.sqrt(half_sims)
    )

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