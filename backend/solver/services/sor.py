import numpy as np

def metodo_SOR(A, b, x0, w, tol, max_iter):
    """
    Parámetros:
    A : matriz de coeficientes (numpy array)
    b : vector de términos independientes (numpy array)
    x0 : vector inicial (numpy array)
    w : factor de relajación (float)
    tol : tolerancia del error (float)
    max_iter : número máximo de iteraciones (int)

    Retorna:
    x : solución aproximada
    iteraciones : número de iteraciones realizadas
    error : error final
    history : lista de diccionarios con el estado de cada iteración
    """

    n = len(A)
    x = x0.copy()
    history = []

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            # Suma de los términos anteriores (ya actualizados)
            suma1 = np.dot(A[i, :i], x[:i])
            # Suma de los términos posteriores (de la iteración anterior)
            suma2 = np.dot(A[i, i+1:], x_old[i+1:])

            # Fórmula del método SOR
            if A[i, i] == 0:
                raise ValueError(f"El elemento diagonal A[{i},{i}] es cero. El método no puede continuar.")
                
            x[i] = (1 - w) * x_old[i] + (w / A[i, i]) * (b[i] - suma1 - suma2)

        # Calcular el error como norma infinito (máxima diferencia entre iteraciones)
        error = np.linalg.norm(x - x_old, ord=np.inf)

        history.append({
            "iteration": k + 1,
            "x": x.tolist(),
            "error": error
        })

        # Verificar criterio de parada
        if error < tol:
            return x, k+1, error, history

    return x, max_iter, error, history
