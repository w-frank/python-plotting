"""Python Plotting Example

This shows an example of a Poisson distribution with various parameters. The
custom plotting class is used to style the figure.

To install LaTeX on Ubuntu 20.04 Focal Fossa Linux:
    sudo apt install texlive-latex-extra
    sudo apt install cm-super
    sudo apt install dvipng

    usage: python3 plotting_example.py

"""

import numpy as np
from scipy.stats import poisson
from matplotlib import pyplot as plt
from plotting import custom_plotting


custom_plotting = custom_plotting()
custom_plotting.setup_plots(fontsize=10, usetex=True)

# Define the distribution parameters to be plotted
mu_values = [1, 5, 15]
linestyles = ['-', '--', ':']

"""
plot the distributions
we generate it using scipy.stats.poisson(). Once the distribution object is
created, we have many options: for example:
    - dist.pmf(x) evaluates the probability mass function in the case of
      discrete distributions.
    - dist.pdf(x) evaluates the probability density function for
      evaluates
"""
fig, ax = plt.subplots(figsize=(5, 3.75))

for mu, ls in zip(mu_values, linestyles):
    """
    create a poisson distribution
    we could generate a random sample from this distribution using, e.g.
    rand = dist.rvs(1000)
    """
    dist = poisson(mu)
    x = np.arange(-1, 200)

    plt.plot(x, dist.pmf(x), color='black', ds='steps-mid', ls=ls,
                label=r'$\mu=%i$' % mu)

plt.xlim(-0.5, 30)
plt.ylim(0, 0.4)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|\mu)$')
plt.legend()
plt.show()
