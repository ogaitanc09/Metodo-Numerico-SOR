import React, { useState } from 'react';
import './VirtualKeyboard.css'; // Import the new CSS file

const VirtualKeyboard = ({ onKeyPress }) => {
    const [activeTab, setActiveTab] = useState('123');
    const [shift, setShift] = useState(false);

    // Helper to create button data
    const btn = (label, command, payload, className = '') => ({ label, command, payload, className });

    // --- 123 Tab Layout (9 columns) ---
    const keys123 = [
        // Row 1
        btn('x', 'insert', 'x'), btn('y', 'insert', 'y'), btn('z', 'insert', 'z'), btn('π', 'insert', 'π'), btn('7', 'insert', '7'), btn('8', 'insert', '8'), btn('9', 'insert', '9'), btn('×', 'insert', '*'), btn('÷', 'insert', '/'),
        // Row 2
        btn('□²', 'insert', '^2'), btn('□^□', 'insert', '^'), btn('√□', 'insert', 'sqrt('), btn('e', 'insert', 'e'), btn('4', 'insert', '4'), btn('5', 'insert', '5'), btn('6', 'insert', '6'), btn('+', 'insert', '+'), btn('-', 'insert', '-'),
        // Row 3
        btn('<', 'insert', '<'), btn('>', 'insert', '>'), btn('|□|', 'insert', '|'), btn('□/□', 'insert', '/'), btn('1', 'insert', '1'), btn('2', 'insert', '2'), btn('3', 'insert', '3'), btn('=', 'insert', '='), btn('⌫', 'command', 'deleteBackward', 'gray-btn'),
        // Row 4
        btn('(', 'insert', '('), btn(')', 'insert', ')'), btn('[ ]', 'insert', '['), btn(',', 'insert', ','), btn('0', 'insert', '0'), btn('.', 'insert', '.'), btn('←', 'command', 'moveToPreviousChar', 'gray-btn'), btn('→', 'command', 'moveToNextChar', 'gray-btn'), btn('↵', 'command', 'commit', 'gray-btn')
    ];

    // --- f(x) Tab Layout (7 columns) ---
    const keysFx = [
        // Row 1
        btn('sen', 'insert', 'sin('), btn('cos', 'insert', 'cos('), btn('tg', 'insert', 'tan('), btn('%', 'insert', '%'), btn('!', 'insert', '!'), btn('$', 'insert', '$'), btn('°', 'insert', '°'),
        // Row 2
        btn('sen⁻¹', 'insert', 'asin('), btn('cos⁻¹', 'insert', 'acos('), btn('tg⁻¹', 'insert', 'atan('), btn('{', 'insert', '{'), btn('}', 'insert', '}'), btn('≤', 'insert', '<='), btn('≥', 'insert', '>='),
        // Row 3
        btn('ln', 'insert', 'ln('), btn('log₁₀', 'insert', 'log10('), btn('log_□', 'insert', 'log('), btn('d/dx', 'insert', 'd/dx'), btn('∫', 'insert', 'int('), btn('i', 'insert', 'i'), btn('⌫', 'command', 'deleteBackward', 'gray-btn'),
        // Row 4
        btn('e^□', 'insert', 'e^'), btn('10^□', 'insert', '10^'), btn('ⁿ√□', 'insert', 'root('), btn('□_□', 'insert', '_'), btn('←', 'command', 'moveToPreviousChar', 'gray-btn'), btn('→', 'command', 'moveToNextChar', 'gray-btn'), btn('↵', 'command', 'commit', 'gray-btn')
    ];

    // --- ABC Tab Layout (10 columns) ---
    const keysABC = [
        // Row 1
        btn('q', 'insert', 'q'), btn('w', 'insert', 'w'), btn('e', 'insert', 'e'), btn('r', 'insert', 'r'), btn('t', 'insert', 't'), btn('y', 'insert', 'y'), btn('u', 'insert', 'u'), btn('i', 'insert', 'i'), btn('o', 'insert', 'o'), btn('p', 'insert', 'p'),
        // Row 2
        btn('a', 'insert', 'a'), btn('s', 'insert', 's'), btn('d', 'insert', 'd'), btn('f', 'insert', 'f'), btn('g', 'insert', 'g'), btn('h', 'insert', 'h'), btn('j', 'insert', 'j'), btn('k', 'insert', 'k'), btn('l', 'insert', 'l'), btn('ñ', 'insert', 'ñ'),
        // Row 3
        btn('⇧', 'action', 'shift', 'gray-btn'), btn('z', 'insert', 'z'), btn('x', 'insert', 'x'), btn('c', 'insert', 'c'), btn('v', 'insert', 'v'), btn('b', 'insert', 'b'), btn('n', 'insert', 'n'), btn('m', 'insert', 'm'), btn('ï', 'insert', 'ï'), btn('⌫', 'command', 'deleteBackward', 'gray-btn'),
        // Row 4
        btn('αβγ', 'action', 'greek', 'gray-btn'), btn(',', 'insert', ','), btn('SPACE', 'insert', ' ', 'space-btn'), btn('←', 'command', 'moveToPreviousChar', 'gray-btn'), btn('→', 'command', 'moveToNextChar', 'gray-btn'), btn('↵', 'command', 'commit', 'gray-btn')
    ];

    const handleKeyClick = (k) => {
        if (k.command === 'action') {
            if (k.payload === 'shift') setShift(!shift);
            // Handle greek toggle if needed, or just switch tab?
            // For now, let's just log it or do nothing as it's a visual replica request
        } else {
            let payload = k.payload;
            if (shift && k.command === 'insert' && payload.length === 1 && /[a-z]/.test(payload)) {
                payload = payload.toUpperCase();
            }
            onKeyPress(k.command, payload);
        }
    };

    const renderKeys = (keys, gridClass) => (
        <div className={`keyboard-grid ${gridClass}`}>
            {keys.map((k, i) => (
                <button
                    key={i}
                    className={`key-btn ${k.className}`}
                    onClick={() => handleKeyClick(k)}
                >
                    {k.label}
                </button>
            ))}
        </div>
    );

    return (
        <div className="virtual-keyboard-container">
            <div className="keyboard-tabs">
                <button
                    className={`tab-btn ${activeTab === '123' ? 'active' : ''}`}
                    onClick={() => setActiveTab('123')}
                >
                    123
                </button>
                <button
                    className={`tab-btn ${activeTab === 'fx' ? 'active' : ''}`}
                    onClick={() => setActiveTab('fx')}
                >
                    f(x)
                </button>
                <button
                    className={`tab-btn ${activeTab === 'abc' ? 'active' : ''}`}
                    onClick={() => setActiveTab('abc')}
                >
                    ABC
                </button>
            </div>

            <div className="keyboard-content">
                {activeTab === '123' && renderKeys(keys123, 'grid-123')}
                {activeTab === 'fx' && renderKeys(keysFx, 'grid-fx')}
                {activeTab === 'abc' && renderKeys(keysABC, 'grid-abc')}
            </div>
        </div>
    );
};

export default VirtualKeyboard;
