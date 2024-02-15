def symmetry(matrix):  # definition of Cholesky Method
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False

        return True


def positive_definite(matrix):
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                temp_sum = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = (matrix[i][j] - temp_sum) ** 0.5
            else:
                temp_sum = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - temp_sum) / L[j][j]

    for i in range(n):
        if L[i][i] <= 0:
            return False
    return True


A = [[4, 2, 4, 0],
     [2, 2, 3, 2],
     [4, 3, 6, 3],
     [0, 2, 3, 9]]

print("Matrix A:")
for row in A:
    print(row)

if symmetry(A):
    print("Matrix A is symmetric.")
else:
    print("Matrix A is not symmetric.")

if positive_definite(A):
    print("Matrix A is positive definitive.")
else:
    print("Matrix is is not positive definitive.")