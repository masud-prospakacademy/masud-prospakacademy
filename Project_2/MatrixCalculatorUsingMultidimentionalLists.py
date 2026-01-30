# atrices (2x2)
matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

result_matrix = [
    [0, 0],
    [0, 0]
]

for row_index in range(2):
    for col_index in range(2):
        
        sum_value = matrix_a[row_index][col_index] + matrix_b[row_index][col_index]
        result_matrix[row_index][col_index] = sum_value

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

print("Matrix A:")
print_matrix(matrix_a)

print("\nMatrix B:")
print_matrix(matrix_b)

print("\nSum of Matrices (A + B):")
print_matrix(result_matrix)