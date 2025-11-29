import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

class GraphGenerator:
    @staticmethod
    def generate_convergence_graph(history):
        """
        Generates a convergence graph (Error vs Iteration) and returns it as a base64 string.
        """
        if not history:
            return None

        # Extract data
        iterations = [entry['iteration'] for entry in history]
        errors = [entry['error'] for entry in history]

        # Create DataFrame for easier plotting (optional but good practice)
        df = pd.DataFrame({'Iteration': iterations, 'Error': errors})

        # Create plot
        plt.figure(figsize=(10, 6))
        plt.plot(df['Iteration'], df['Error'], marker='o', linestyle='-', color='b')
        plt.title('Convergencia del Método SOR')
        plt.xlabel('Iteración')
        plt.ylabel('Error')
        plt.grid(True)
        plt.yscale('log') # Log scale is often better for convergence plots

        # Save to buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        # Encode to base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return f"data:image/png;base64,{image_base64}"
