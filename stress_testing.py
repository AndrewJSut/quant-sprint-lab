from analytical import black_scholes_price


def stress_test(S0, K, T, r, sigma, option_type="call"):
    """
    Run simple stress scenarios on the Black-Scholes option price.
    """

    base_price = black_scholes_price(S0, K, T, r, sigma, option_type)

    scenarios = {
        "Base": (S0, sigma),
        "Spot -10%": (S0 * 0.90, sigma),
        "Spot +10%": (S0 * 1.10, sigma),
        "Volatility -20%": (S0, sigma * 0.80),
        "Volatility +20%": (S0, sigma * 1.20),
    }

    print("Base Price:", base_price)
    print("\nStress Test Results:")

    for name, (stressed_S0, stressed_sigma) in scenarios.items():
        stressed_price = black_scholes_price(
            stressed_S0,
            K,
            T,
            r,
            stressed_sigma,
            option_type
        )

        pnl = stressed_price - base_price

        print(
            name,
            "| Price:", round(stressed_price, 4),
            "| P&L:", round(pnl, 4)
        )


if __name__ == "__main__":
    stress_test(
        S0=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.20,
        option_type="call"
    )