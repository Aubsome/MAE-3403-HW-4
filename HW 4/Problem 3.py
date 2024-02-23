#Chat.gpt was used as a resource to help create this code
import numpy as np

def solve_linear_system(matrix, rhs):
    """
    Solve a system of linear equations.

    Parameters:
    :param matrix: Coefficient matrix of the system of equations.
    :param rhs: Right-hand side vector of the system.
    :returns:Solution vector for the system of equations.
    """
    solution = np.linalg.solve(matrix, rhs)
    return solution

# Define the matrices
matrix1 = np.array([[3, 1, -1],
                    [1, 4, 1],
                    [2, 1, 2]])

matrix2 = np.array([[1, -10, 2, 4],
                    [3, 1, 4, 12],
                    [9, 2, 3, 4],
                    [-1, 2, 7, 3]])

# Define the right-hand sides
rhs1 = np.array([2, 12, 10])
rhs2 = np.array([2, 12, 21, 37])

# Solve the systems of equations
solution1 = solve_linear_system(matrix1, rhs1)
solution2 = solve_linear_system(matrix2, rhs2)

# Round the solutions to 2 decimals
solution1 = np.round(solution1, decimals=2)
solution2 = np.round(solution2, decimals=2)

# Print the rounded solutions
print("Solution for the first system:")
print("x_1 =", solution1[0])
print("x_2 =", solution1[1])
print("x_3 =", solution1[2])

print("\nSolution for the second system:")
print("x_1 =", solution2[0])
print("x_2 =", solution2[1])
print("x_3 =", solution2[2])
print("x_4 =", solution2[3])
