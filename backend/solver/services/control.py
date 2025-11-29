import numpy as np
from .translation import EquationParser
from .sor import metodo_SOR
from .grafico import GraphGenerator
from .history import HistoryService

class SolverController:
    @staticmethod
    def solve_system(data):
        """
        Orchestrates the solving process:
        1. Parses equations.
        2. Solves using SOR.
        3. Generates convergence graph.
        4. Saves to History.
        5. Returns combined result.
        """
        equations = data.get('equations', [])
        initial_vector = data.get('initial_vector', [])
        relaxation_factor = float(data.get('relaxation_factor', 1.2))
        tolerance = float(data.get('tolerance', 0.0001))
        max_iter = int(data.get('max_iter', 100))

        if not equations:
            raise ValueError("No equations provided")

        # 1. Parse equations
        variables = ['x', 'y', 'z']
        A, b = EquationParser.parse_system(equations, variables)

        # Prepare initial vector
        if not initial_vector:
            x0 = np.zeros(len(variables))
        else:
            x0 = np.array(initial_vector, dtype=float)
            if len(x0) != len(variables):
                raise ValueError(f"Initial vector must have size {len(variables)}")

        # 2. Solve using SOR
        solution, iterations, error, history = metodo_SOR(A, b, x0, relaxation_factor, tolerance, max_iter)

        # 3. Generate Graph
        graph_base64 = GraphGenerator.generate_convergence_graph(history)

        result = {
            "solution": solution.tolist(),
            "iterations": iterations,
            "error": error,
            "history": history,
            "graph": graph_base64
        }

        # 4. Save to History
        # We need to include input data for context
        save_data = {
            **result,
            "equations": equations,
            "initial_vector": initial_vector,
            "relaxation_factor": relaxation_factor,
            "tolerance": tolerance,
            "max_iter": max_iter
        }
        try:
            attempt_id = HistoryService.save_attempt(save_data)
            result['id'] = attempt_id
        except Exception as e:
            print(f"Failed to save history: {e}")
            # Don't fail the request if saving history fails

        # 5. Return result
        return result
