import math


def normal_cdf(x):
    """Cumulative distribution function of the standard normal distribution."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def black_scholes_price(S0, K, T, r, sigma, option_type="call"):
    """
    Analytical Black-Scholes price for a European call or put.
    """

    d1 = (
        math.log(S0 / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        price = (
            S0 * normal_cdf(d1)
            - K * math.exp(-r * T) * normal_cdf(d2)
        )

    elif option_type == "put":
        price = (
            K * math.exp(-r * T) * normal_cdf(-d2)
            - S0 * normal_cdf(-d1)
        )

    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price


if __name__ == "__main__":
    price = black_scholes_price(
        S0=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20
    )

    print("Black-Scholes Price:", price)