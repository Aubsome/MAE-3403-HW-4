#Chat.gpt was used as a resource to help create this code
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

def equation1(x):
    """
    This function takes a numerical argument and performs the mathematical function, 'equation1' on the argument before
    returning it.
    :param x: A numerical value.
    :return: The numerical value after equation1 has been applied to it.
    """
    return x - 3 * np.cos(x)

def equation2(x):
    """
    This function takes a numerical argument and performs the mathematical function, 'equation2' on the argument before
    returning it.
    :param x: A numerical value.
    :return:  The numerical value after equation2 has been applied to it.
    """
    return np.cos(2 * x) * x**3

def find_unique_roots_in_range(equation, x_range):
    """
    This function will determine the unique roots of an equation within a specific range.
    :param equation: The equation whose roots are to be found.
    :param x_range: The range of x values in which to search for roots.
    :returns: A sorted list of unique roots rounded to 3 decimals.
    """
    # Use a set to store unique roots
    roots = set()

    # Use a for loop to try different values of x. If a value of x produces a true case for a root, that value will be
    # stored in a list called roots.
    for x_guess in x_range:
        sol = root(equation, x_guess)
        if sol.success:
            roots.add(round(sol.x[0], 3))
    return sorted(list(roots))

# Find roots of each equation in the range -3 to 3
roots_equation1 = find_unique_roots_in_range(equation1, np.linspace(-3, 3, 1000))
roots_equation2 = find_unique_roots_in_range(equation2, np.linspace(-3, 3, 1000))
# Remove the first and last root because they are outside of our scope.
roots_equation2 = roots_equation2[1:-1]


# Find intersection points in the range -3 to 3
def intersection_equations(x):
    """Define the system of equations for finding intersection points."""
    return equation1(x) - equation2(x)

# Use a larger range for initial guesses
all_guesses = np.linspace(-3, 3, 1000)
intersection_points = find_unique_roots_in_range(intersection_equations, all_guesses)
# Remove first and last point because they are outside of our scope
intersection_points = intersection_points[1:-1]


# Print the values of the roots and intersection points
print("Roots of Equation 1:", roots_equation1)
print("Roots of Equation 2:", roots_equation2)
print("Intersection Points:", intersection_points)

# Plot the equations, roots, and intersection points
x_values = np.linspace(-3, 3, 1000)
plt.plot(x_values, equation1(x_values), label='x - 3*cos(x)')
plt.plot(x_values, equation2(x_values), label='cos(2*x)*x^3')
plt.scatter(roots_equation1, np.zeros_like(roots_equation1), color='red', marker='o', label='Roots of Equation 1')
plt.scatter(roots_equation2, np.zeros_like(roots_equation2), color='blue', marker='x', label='Roots of Equation 2')
plt.scatter(intersection_points, equation1(intersection_points), color='green', marker='*', label='Intersection Points')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.title('Equations and Intersection Points')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
# This next bit allows for annotation of values above their respective positions in the plot. Python does not have an
# easy way to do this, so it is done with for loops and if statements.
rootlist1 = list(roots_equation1)
for x in range(len(rootlist1)):
    if x%2==0:
        y=-4
    else:
        y=2
    plt.annotate(str(rootlist1[x]), xy=(rootlist1[x],y), ha='center', c='red')
rootlist2 = list(roots_equation2)
for x in range(len(rootlist2)):
    if x%2==0:
        y=-4
    else:
        y=2
    plt.annotate(str(rootlist2[x]), xy=(rootlist2[x],y), ha='center', c='blue')
for x in range(len(intersection_points)):
    plt.annotate('Intersection point', xy=(intersection_points[x], equation1(intersection_points[x])), xytext=(0,20),
             arrowprops=dict(facecolor='green', shrink=0.05),
             )
    if x%2==0:
        y = 6
    else:
        y = -6
    plt.annotate(str(intersection_points[x]), xy=(intersection_points[x], equation1(intersection_points[x])+y), ha='center',
            c='green')
plt.show()
