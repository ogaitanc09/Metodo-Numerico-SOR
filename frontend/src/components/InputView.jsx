import React, { useState } from 'react';
import './InputView.css';
import VirtualKeyboard from './VirtualKeyboard';

const InputView = ({ onContinue }) => {
  const [initialVector, setInitialVector] = useState('');
  const [relaxationFactor, setRelaxationFactor] = useState('');
  const [tolerance, setTolerance] = useState('');

  const [eq1, setEq1] = useState('');
  const [eq2, setEq2] = useState('');
  const [eq3, setEq3] = useState('');

  const [showKeyboard, setShowKeyboard] = useState(false);
  const [activeInput, setActiveInput] = useState(null);

  const handleKeyPress = (command, payload) => {
    if (!activeInput) return;

    if (command === 'insert') {
      activeInput((prev) => prev + payload);
      if (payload === 'deleteBackward') {
        activeInput((prev) => prev.slice(0, -1));
      } else if (payload === 'commit') {
        setShowKeyboard(false);
      }
    }
  };

  const handleContinue = async () => {
    const payload = {
      equations: [eq1, eq2, eq3].filter(eq => eq.trim() !== ''),
      initial_vector: initialVector ? initialVector.replace(/[\[\]]/g, '').split(',').map(Number) : [0, 0, 0],
      relaxation_factor: parseFloat(relaxationFactor) || 1.2,
      tolerance: parseFloat(tolerance) || 0.0001,
      max_iter: 100
    };

    try {
      const response = await fetch('http://localhost:8000/api/solve/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Error en la solicitud');
      }

      const data = await response.json();
      onContinue(data);
    } catch (error) {
      alert(`Error: ${error.message}`);
    }
  };

  return (
    <div className="input-view">

      {/* Inputs superiores */}
      <div className="top-inputs">
        <div className="input-group">
          <label>Vector Inicial</label>
          <input
            type="text"
            value={initialVector}
            onChange={(e) => setInitialVector(e.target.value)}
            placeholder="[0, 0, 0]"
            onFocus={() => setShowKeyboard(false)}
          />
        </div>

        <div className="input-group">
          <label>Factor de Relajación</label>
          <input
            type="text"
            value={relaxationFactor}
            onChange={(e) => setRelaxationFactor(e.target.value)}
            placeholder="1.2"
            onFocus={() => setShowKeyboard(false)}
          />
        </div>

        <div className="input-group">
          <label>Tolerancia</label>
          <input
            type="text"
            value={tolerance}
            onChange={(e) => setTolerance(e.target.value)}
            placeholder="0.0001"
            onFocus={() => setShowKeyboard(false)}
          />
        </div>
      </div>

      {/* Ecuaciones */}
      <div className="equations-section">
        <label>Ecuaciones (3×3)</label>

        <div className="math-input-wrapper">
          <input
            className="equation-input"
            type="text"
            value={eq1}
            onChange={(e) => setEq1(e.target.value)}
            onFocus={() => setActiveInput(() => setEq1)}
            placeholder="Ej: 3x + 2y - z = 5"
          />
          <button
            className="keyboard-toggle-btn"
            onClick={() => { setActiveInput(() => setEq1); setShowKeyboard(!showKeyboard); }}
          >⌨️</button>
        </div>

        <div className="math-input-wrapper">
          <input
            className="equation-input"
            type="text"
            value={eq2}
            onChange={(e) => setEq2(e.target.value)}
            onFocus={() => setActiveInput(() => setEq2)}
            placeholder="Ej: x - y + 4z = 8"
          />
          <button
            className="keyboard-toggle-btn"
            onClick={() => { setActiveInput(() => setEq2); setShowKeyboard(!showKeyboard); }}
          >⌨️</button>
        </div>

        <div className="math-input-wrapper">
          <input
            className="equation-input"
            type="text"
            value={eq3}
            onChange={(e) => setEq3(e.target.value)}
            onFocus={() => setActiveInput(() => setEq3)}
            placeholder="Ej: 2x + y + z = 3"
          />
          <button
            className="keyboard-toggle-btn"
            onClick={() => { setActiveInput(() => setEq3); setShowKeyboard(!showKeyboard); }}
          >⌨️</button>
        </div>
      </div>

      {showKeyboard && (
        <VirtualKeyboard onKeyPress={handleKeyPress} />
      )}

      <div className="actions">
        <button className="continue-btn" onClick={handleContinue}>
          Continuar
        </button>
      </div>
    </div>
  );
};

export default InputView;
