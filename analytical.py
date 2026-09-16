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
def black_scholes_delta(S0, K, T, r, sigma, option_type="call"):
    d1 = (
        math.log(S0 / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    if option_type == "call":
        return normal_cdf(d1)
    elif option_type == "put":
        return normal_cdf(d1) - 1
    else:
        raise ValueError("option_type must be 'call' or 'put'")
def black_scholes_gamma(S0, K, T, r, sigma):
    d1 = (
        math.log(S0 / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    normal_pdf_d1 = math.exp(-0.5 * d1**2) / math.sqrt(2 * math.pi)

    gamma = normal_pdf_d1 / (S0 * sigma * math.sqrt(T))

    return gamma
def black_scholes_vega(S0, K, T, r, sigma):
    d1 = (
        math.log(S0 / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    normal_pdf_d1 = math.exp(-0.5 * d1**2) / math.sqrt(2 * math.pi)

    vega = S0 * normal_pdf_d1 * math.sqrt(T)

    return vega
def black_scholes_theta(S0, K, T, r, sigma, option_type="call"):
    d1 = (
        math.log(S0 / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    d2 = d1 - sigma * math.sqrt(T)

    normal_pdf_d1 = math.exp(-0.5 * d1**2) / math.sqrt(2 * math.pi)

    if option_type == "call":
        theta = (
            -(S0 * normal_pdf_d1 * sigma) / (2 * math.sqrt(T))
            - r * K * math.exp(-r * T) * normal_cdf(d2)
        )
    elif option_type == "put":
        theta = (
            -(S0 * normal_pdf_d1 * sigma) / (2 * math.sqrt(T))
            + r * K * math.exp(-r * T) * normal_cdf(-d2)
        )
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return theta
def black_scholes_rho(S0, K, T, r, sigma, option_type="call"):
    d1 = (
        math.log(S0 / K)
        + (r + 0.5 * sigma**2) * T
    ) / (sigma * math.sqrt(T))

    d2 = d1 - sigma * math.sqrt(T)

    if option_type == "call":
        rho = K * T * math.exp(-r * T) * normal_cdf(d2)
    elif option_type == "put":
        rho = -K * T * math.exp(-r * T) * normal_cdf(-d2)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return rho
if __name__ == "__main__":
    price = black_scholes_price(
        S0=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20
    )

    print("Black-Scholes Price:", price)
    print("Delta:", black_scholes_delta(100, 100, 1, 0.05, 0.20))
print("Gamma:", black_scholes_gamma(100, 100, 1, 0.05, 0.20))
print("Vega:", black_scholes_vega(100, 100, 1, 0.05, 0.20))
print("Theta:", black_scholes_theta(100, 100, 1, 0.05, 0.20))
print("Rho:", black_scholes_rho(100, 100, 1, 0.05, 0.20))