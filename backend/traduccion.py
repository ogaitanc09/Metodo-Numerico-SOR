import numpy as np

class Traduccion:

    def __init__(self, ecuacion):
        self.ecuacion = ecuacion
    

    def leer(self):
        lista_ecuacion = self.ecuacion.split('\n')
        return lista_ecuacion


    def separar(self):
        lista_ecuacion = self.leer()

        matrix = []
        for i in range(len(lista_ecuacion)):
            matrix.append(lista_ecuacion[i].split('='))

        A = []
        b = []

        for i in range(len(matrix)):
            A.append(matrix[i][0].strip())
            b.append(float(matrix[i][1].strip()))

        return A, b


    def extraer_coeficientes(self):
        A, b = self.separar()

        # Extrae variables x1, x2, x3...
        variables = set()

        for ecuacion in A:
            ecuacion = ecuacion.replace(" ", "")
            j = 0
            while j < len(ecuacion):
                if ecuacion[j] == 'x':
                    j += 1
                    num = ""
                    while j < len(ecuacion) and ecuacion[j].isdigit():
                        num += ecuacion[j]
                        j += 1
                    variables.add("x" + num)
                else:
                    j += 1

        variables = sorted(list(variables), key=lambda x: int(x[1:]))

        # Matriz de ceros
        A_matrix = np.zeros((len(A), len(variables)))

        # Convertir ecuaciones a coeficientes
        for i, ecuacion in enumerate(A):
            ecuacion = ecuacion.replace(" ", "")
            terminos = ecuacion.replace('-', '+-').split('+')

            for t in terminos:
                if 'x' in t:
                    coef = t.split('x')[0]
                    if coef == '' or coef == '+': coef = 1
                    elif coef == '-': coef = -1
                    else: coef = float(coef)

                    var = 'x' + t.split('x')[1]
                    idx = variables.index(var)
                    A_matrix[i][idx] = coef

        return A_matrix, np.array(b), variables


    