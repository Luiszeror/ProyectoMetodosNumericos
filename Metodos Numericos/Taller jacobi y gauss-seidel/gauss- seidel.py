def gauss_seidel(A, b, x0, tol, maxiter):
    """
    Implementación del método de Gauss-Seidel para resolver el sistema Ax = b
    """

    A = np.array([4, 0, -0.33, 0], [-2, 5, 0, -0.33], [0, 3.33, 9, -1.5], [-0.66, 0, 2, 6])
    b = ([0.5, 0.25, 0.16, 0.33])
    x0 = np.zeros(4)
    tol = 1e-6
    max_iter = 10
    x, iter = gauss_seidel(A, b, x0, tol, max_iter)



    while iter < maxiter and err > tol:
        for i in range(n):
            s = 0
            for j in range(n):
                if j != i:
                    s += A[i][j] * x[j]
            x[i] = (b[i] - s) / A[i][i]

        err = max(abs(A @ x - b))
        iter += 1

    if iter == maxiter and err > tol:
        print("El método de Gauss-Seidel no converge en", maxiter, "iteraciones.")
    else:
        print("El método de Gauss-Seidel converge a la solución:\n", x)

    return x

 print("Solución:", x)
print("Iteraciones:", iter)
