import numpy as np

def de(matrix):
    return np.linalg.det(matrix)

def matr(coeff_matrix, const_matrix, column_index):
    t_matrix = coeff_matrix.copy()
    for row_index in range(len(coeff_matrix)):
        t_matrix[row_index][column_index] = const_matrix[row_index]
    return t_matrix

def solve_system(coeff_matrix, const_matrix):
    n = len(coeff_matrix)
    D = de(coeff_matrix)

    if D == 0:
        return "Система не имеет единственного решения"

    result = []
    for i in range(n):
        temp_matrix = matr(coeff_matrix, const_matrix, i)
        D_i = de(temp_matrix)
        x_i = D_i / D
        result.append(x_i)

    return result

coeff_matrix = [[2 + 2j, 3], [2, 2 + 3j]]
const_matrix = [2 + 2j, 3]

solutions = solve_system(np.array(coeff_matrix, dtype=complex), np.array(const_matrix, dtype=complex))

print("Решения системы")
for i, sol in enumerate(solutions):
    print(f"x_{i+1} = {sol}")




 
