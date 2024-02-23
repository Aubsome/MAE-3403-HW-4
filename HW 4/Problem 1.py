#Chat.gpt was used as a resource to help create this code
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def plot_normal_distribution_and_probability(mean, std_dev, x_range, probability_condition, label):
    """
    Plot a normal distribution and shade the area under the curve based on a given probability condition.

    :param mean: Mean of the normal distribution.
    :param std_dev: Standard deviation of the normal distribution.
    :param x_range: Range of x values for plotting.
    :param probability_condition: Function defining the probability condition.
    :param label: Label for the distribution in the legend.
    :return: The plotted graph in the range -5 to 5.
    """
    distribution = stats.norm(mean, std_dev)

    # Generate x values for plotting
    x_values = np.linspace(x_range[0], x_range[1], 100)

    # Calculate the probability condition
    probability = probability_condition(x_values, mean, std_dev)

    # Plot the normal distribution
    plt.plot(x_values, distribution.pdf(x_values), label=f'{label}')

    # Fill the area under the curve based on the probability condition
    plt.fill_between(x_values, distribution.pdf(x_values), where=probability, alpha=1, label=f'P({probability_condition.__name__})')

# Set up the figure
plt.figure(figsize=(10, 10))

# Plot the first normal distribution (N(0, 1))
plot_normal_distribution_and_probability(mean=0, std_dev=1, x_range=(-5, 5),
                                         probability_condition=lambda x_values, mean, std_dev: (x_values < 1),
                                         label='N(0, 1)')

# Plot the second normal distribution (N(175, 3))
plot_normal_distribution_and_probability(mean=175, std_dev=3, x_range=(-5, 5),
                                         probability_condition=lambda x_values, mean, std_dev: (x_values > mean + 2 * std_dev),
                                         label='N(175, 3)')

# Customize the plot
plt.title('Normal Distributions and Probabilities')
plt.xlabel('x')
plt.ylabel('Probability Density Function')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()


