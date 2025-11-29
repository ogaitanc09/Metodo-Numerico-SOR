import React from 'react';
import '../App.css';

const ResultView = ({ onBack, result }) => {
    if (!result) return null;

    const { history, solution, error, graph } = result;

    return (
        <div className="result-view">
            <div className="result-header">
                <h2>Resultados del Método SOR</h2>
                <button className="back-btn" onClick={onBack}>
                    Volver
                </button>
            </div>

            <div className="result-content">
                <div className="section iterations-section">
                    <h3>Iteraciones</h3>
                    <table className="iterations-table">
                        <thead>
                            <tr>
                                <th>k</th>
                                <th>x</th>
                                <th>y</th>
                                <th>z</th>
                                <th>Error</th>
                            </tr>
                        </thead>
                        <tbody>
                            {history.map((iter) => (
                                <tr key={iter.iteration}>
                                    <td>{iter.iteration}</td>
                                    <td>{iter.x[0].toFixed(6)}</td>
                                    <td>{iter.x[1].toFixed(6)}</td>
                                    <td>{iter.x[2].toFixed(6)}</td>
                                    <td>{iter.error.toFixed(6)}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>

                <div className="section solution-section">
                    <h3>Solución Aproximada</h3>
                    <div className="solution-box">
                        <p>x = {solution[0].toFixed(6)}</p>
                        <p>y = {solution[1].toFixed(6)}</p>
                        <p>z = {solution[2].toFixed(6)}</p>
                        <p className="final-error">Error final: {error.toFixed(6)}</p>
                    </div>
                </div>

                <div className="section graph-section">
                    <h3>Gráfica de Convergencia</h3>
                    <div className="graph-placeholder">
                        {graph ? (
                            <img src={graph} alt="Gráfica de Convergencia" style={{ maxWidth: '100%', height: 'auto' }} />
                        ) : (
                            <p>No se pudo generar la gráfica.</p>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ResultView;
