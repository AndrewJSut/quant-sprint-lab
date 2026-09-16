from monte_carlo import monte_carlo_price
from analytical import black_scholes_price


# Parameters
S0 = 100
K = 100
T = 1
r = 0.05
sigma = 0.20
n_sims = 100_000


# Monte Carlo price
mc_price, mc_se = monte_carlo_price(
    S0=S0,
    K=K,
    T=T,
    r=r,
    sigma=sigma,
    n_sims=n_sims,
    option_type="call"
)


# Black-Scholes analytical price
bs_price = black_scholes_price(
    S0=S0,
    K=K,
    T=T,
    r=r,
    sigma=sigma,
    option_type="call"
)


# Comparison
difference = mc_price - bs_price
absolute_error = abs(difference)


print("Monte Carlo Price:", mc_price)
print("Monte Carlo Standard Error:", mc_se)
print("Black-Scholes Price:", bs_price)
print("Difference:", difference)
print("Absolute Error:", absolute_error)