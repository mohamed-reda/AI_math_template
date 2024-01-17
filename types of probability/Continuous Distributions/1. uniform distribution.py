"""
Uniform Distribution:

Idea: Every outcome is equally likely.
Example: Rolling a fair six-sided die.

"""


def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x: float) -> float:
    """Returns the probability that a uniform random variable is <= x"""
    if x < 0:
        return 0  # uniform random is never less than 0
    elif x < 1:
        return x  # e.g. P(X <= 0.4) = 0.4
    else:
        return 1  # uniform random is always less than


print(uniform_pdf(2))
print(uniform_cdf(2))
