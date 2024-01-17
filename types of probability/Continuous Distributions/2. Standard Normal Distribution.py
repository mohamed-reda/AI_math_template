"""
Normal Distribution:
bell curve–shaped distribution that is symmetric about the mean.

- It is completely determined by two parameters: its mean μ (mu) and its standard deviation σ (sigma).
STD = √(σ^2) = σ

f(x) = (1/√(2πσ^2)) * e^([-(x-μ)^2]/2σ^2)

- 1/√(2πσ^2) is the normalizing constant, which makes the probability density function integrate to 1.
- e is the mathematical constant approximately equal to 2.71828.
- e^([-(x-μ)^2]/2σ^2) exponential function which gives the distribution its characteristic bell shape.

"""

import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)


def normal_pdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))


import matplotlib.pyplot as plt

xs = [x / 10.0 for x in range(-50, 50)]

# plt.plot(xs, [normal_pdf(x, mu=1, sigma=1) for x in xs], '-.', label='mu=1, sigma=1')
# plt.plot(xs, [normal_pdf(x, mu=0, sigma=.9) for x in xs], ':', label='mu=0, sigma=.9')

plt.plot(xs, [normal_pdf(x, mu=0, sigma=1) for x in xs], '-',
         label='standard normal dist')  # standard normal distribution, μ = 0 and σ = 1, it’s called
"""
the normal distribution like the formula X=σZ+μ, so Z = ( X - μ ) / σ
allows us to convert a normal distribution into a standard normal distribution (with any mean μ and standard deviation σ).
"""

plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')

plt.legend()
plt.title("Various Normal pdfs")
plt.show()
