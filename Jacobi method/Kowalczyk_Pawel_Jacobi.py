import math
import numpy as np

def if_dominant_matrix(A):
    for rows in range(0, A.shape[0]):
        for columns in range(0, A.shape[1]):
            if abs(A[rows, rows]) < A[rows, columns]:
                print("Macierz nie jest dominująca wierszowo! Metoda nie jest zbieżna")
                break

def kowalczyk_pawel_jacobi(A,b,eps):
    if_dominant_matrix(A)
    xk=np.ones(A.shape[1])
    x0=np.zeros(A.shape[1])
    while np.linalg.norm(xk-x0) >= eps:
        x0 = list(xk)
        for i in range(0, A.shape[0]):
            sum_ax0 = 0
            for j in range(0, A.shape[1]):
                if i != j:
                    sum_ax0 += A[i, j] * x0[j]
            xk[i] = (b[i]-sum_ax0) / A[i, i]
    return xk


#test case

A = np.array([[4.0, -1, -1, 0], [-1, 4, 0, -1], [-1, 0, 4, -1], [0, -1, -1, 4]])
b = [-1, 2, 0, 1]

print(kowalczyk_pawel_jacobi(A, b, 0.5))
