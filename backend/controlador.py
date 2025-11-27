from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import numpy as np


def metodo_sor(A, b, omega, x0=None, tol=1e-6, max_iter=1000):
    """
    Implementación del método SOR (Successive Over-Relaxation)
    para resolver A x = b.

    Parámetros:
        A: matriz de coeficientes (lista de listas o np.array)
        b: vector independiente (lista o np.array)
        omega: parámetro de relajación (0 < ω < 2)
        x0: vector inicial (opcional)
        tol: tolerancia para el criterio de parada
        max_iter: número máximo de iteraciones

    Retorna:
        x: aproximación de la solución
        k: iteraciones realizadas
        convergio: True/False
    """

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = b.shape[0]

    if A.shape != (n, n):
        raise ValueError("La matriz A debe ser cuadrada y compatible con el tamaño de b.")

    # Vector inicial
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)

    for k in range(1, max_iter + 1):
        x_old = x.copy()

        for i in range(n):
            # sumas parciales usando valores ya actualizados (j < i)
            sigma1 = np.dot(A[i, :i], x[:i])
            # y valores antiguos (j > i)
            sigma2 = np.dot(A[i, i + 1:], x_old[i + 1:])

            if A[i, i] == 0:
                raise ZeroDivisionError(f"Elemento diagonal nulo en A[{i},{i}]")

            x[i] = (1 - omega) * x_old[i] + (omega / A[i, i]) * (b[i] - sigma1 - sigma2)

        # Criterio de parada con norma infinito
        error = np.linalg.norm(x - x_old, ord=np.inf)
        if error < tol:
            return x, k, True

    # Si llega aquí, no convergió en max_iter iteraciones
    return x, max_iter, False


class SORController(APIView):
    """
    Controlador REST para resolver sistemas lineales Ax = b usando el método SOR.
    Espera un JSON con la siguiente estructura:

    {
        "matriz": [[...], [...], ...],
        "vector": [...],
        "omega": 1.2,
        "tolerancia": 1e-6,
        "max_iter": 100
    }
    """

    def post(self, request):
        data = request.data

        # 1. Validar que están las claves necesarias
        campos_obligatorios = ["matriz", "vector", "omega"]
        faltantes = [c for c in campos_obligatorios if c not in data]

        if faltantes:
            return Response(
                {
                    "detalle": "Faltan campos en el cuerpo de la petición.",
                    "faltantes": faltantes,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        matriz = data.get("matriz")
        vector = data.get("vector")
        omega = data.get("omega")
        tolerancia = data.get("tolerancia", 1e-6)
        max_iter = data.get("max_iter", 1000)
        x0 = data.get("x0", None)

        # 2. Validaciones básicas de tipos
        try:
            omega = float(omega)
            tolerancia = float(tolerancia)
            max_iter = int(max_iter)
        except (TypeError, ValueError):
            return Response(
                {
                    "detalle": "omega, tolerancia y max_iter deben ser numéricos.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not (0 < omega < 2):
            return Response(
                {
                    "detalle": "El parámetro omega debe estar en el intervalo (0, 2).",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 3. Intentar ejecutar el método SOR
        try:
            x, iteraciones, convergio = metodo_sor(
                A=matriz,
                b=vector,
                omega=omega,
                x0=x0,
                tol=tolerancia,
                max_iter=max_iter,
            )

            respuesta = {
                "solucion": x.tolist(),
                "iteraciones": iteraciones,
                "convergio": convergio,
            }

            if convergio:
                respuesta["mensaje"] = "El método SOR convergió correctamente."
            else:
                respuesta["mensaje"] = (
                    "El método SOR NO convergió en el número máximo de iteraciones."
                )

            return Response(respuesta, status=status.HTTP_200_OK)

        except Exception as e:
            # Cualquier error numérico o de forma de los datos
            return Response(
                {
                    "detalle": "Ocurrió un error al ejecutar el método SOR.",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )