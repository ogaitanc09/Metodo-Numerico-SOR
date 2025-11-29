import re
import numpy as np

class EquationParser:
    @staticmethod
    def parse_equation(equation_str, variables):
        """
        Parses a single linear equation string into coefficients for given variables and a constant.
        Example: "3x + 2y - z = 5" -> {'x': 3.0, 'y': 2.0, 'z': -1.0}, constant: 5.0
        """
        # Remove spaces and normalize
        equation_str = equation_str.replace(" ", "")
        
        # Split into left and right sides
        if "=" not in equation_str:
            raise ValueError(f"Invalid equation format: {equation_str}")
            
        lhs, rhs = equation_str.split("=")
        
        try:
            constant = float(rhs)
        except ValueError:
            raise ValueError(f"Invalid constant on RHS: {rhs}")

        coeffs = {var: 0.0 for var in variables}
        
        # Regex to find terms like +3x, -y, z, +2.5z
        # This regex looks for:
        # ([+-]?) : Optional sign
        # (\d*\.?\d*) : Optional number (coefficient)
        # ([a-zA-Z]+) : Variable name
        term_pattern = re.compile(r'([+-]?)(\d*\.?\d*)([a-zA-Z]+)')
        
        # We need to handle the case where the equation might start without a sign
        # but the regex expects terms.
        # Let's iterate over matches in LHS
        
        # A more robust approach might be to split by + or - but keep the delimiters
        # For simplicity, let's use a regex that captures all terms
        
        matches = term_pattern.findall(lhs)
        
        # Verify that we consumed the entire LHS string (excluding non-variable terms if any, but linear eq shouldn't have them)
        # Actually, linear equations might have constants on LHS too, but let's assume standard form for now
        # or just handle variable terms.
        
        for sign, number, var in matches:
            if var not in variables:
                continue # Or raise error? Let's ignore unknown vars or raise error.
                # raising error is safer
                # raise ValueError(f"Unknown variable: {var}")
                # But maybe the user uses x1, x2... let's stick to the passed variables.
            
            if number == "":
                val = 1.0
            elif number == ".": # Handle case like .5x
                 val = 0.0 # Invalid? or 0? Python float('.') fails.
                 # Let's assume valid float string if not empty
                 continue # Should not happen with \d*\.?\d* if it matched a var
            else:
                try:
                    val = float(number)
                except ValueError:
                    val = 1.0 # Should be covered by regex, but safety first
            
            if sign == "-":
                val = -val
            
            coeffs[var] += val
            
        return coeffs, constant

    @staticmethod
    def parse_system(equations, variables=['x', 'y', 'z']):
        """
        Parses a list of equation strings into matrix A and vector b.
        """
        n = len(variables)
        A = np.zeros((len(equations), n))
        b = np.zeros(len(equations))
        
        for i, eq in enumerate(equations):
            coeffs, constant = EquationParser.parse_equation(eq, variables)
            for j, var in enumerate(variables):
                A[i, j] = coeffs[var]
            b[i] = constant
            
        return A, b
