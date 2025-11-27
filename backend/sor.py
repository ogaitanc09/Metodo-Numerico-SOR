import numpy as np

class MetodoSor:

    def __init__(self,A,b,w,tol):
        self.A = A # Ecuaciones almacenada en matriz
        self.b = b # Valores independientes
        self.w = w # Factor de relajación 
        self.tol = tol # Tolerancia
        self.x0 = np.zeros_like(self.b) # Vector inicial (x0 = [0,0,0])
        self.max_iter = 100 # Máximo de iteraciones
    


    def metodo_SOR(self):
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
        """
        

        n = len(self.A)
        x = self.x0.copy()

        for k in range(self.max_iter):
            x_old = x.copy()

            for i in range(n):
                # Suma de los términos anteriores (ya actualizados)
                suma1 = np.dot(self.A[i, :i], x[:i])
                # Suma de los términos posteriores (de la iteración anterior)
                suma2 = np.dot(self.A[i, i+1:], x_old[i+1:])

                # Fórmula del método SOR
                x[i] = (1 - self.w) * x_old[i] + (self.w / self.A[i, i]) * (self.b[i] - suma1 - suma2)

            # Calcular el error como norma infinito (máxima diferencia entre iteraciones)
            error = np.linalg.norm(x - x_old, ord=np.inf)

            print(f"Iteración {k+1}: x = {x}, error = {error:.6f}")

            # Verificar criterio de parada
            if error < self.tol:
                print("\n Convergencia alcanzada.")
                return x, k+1

        print("\n No se alcanzó la convergencia en el número máximo de iteraciones.")
        return x, self.max_iter

'''# EJEMPLO

A = np.array([[4, -1, 0],
              [0, -1, 6],
              [-1, 5, -1]], dtype=float)

b = np.array([3, 2, -3], dtype=float)

x0 = np.zeros_like(b)    # Vector inicial (x0 = [0,0,0])
w = 1.2                 # Factor de relajación
tol = 0.001              # Tolerancia
max_iter = 100           # Máximo de iteraciones

# Ejecutar método
solucion, iteraciones = metodo_SOR(A, b, x0, w, tol, max_iter)

print("\n----------------------------------")
print("Solución aproximada:", solucion)
print("Iteraciones realizadas:", iteraciones)
print("----------------------------------")
'''