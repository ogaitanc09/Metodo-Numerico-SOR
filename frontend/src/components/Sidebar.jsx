import React from 'react';
import '../App.css';

const Sidebar = ({ onSelectHistory }) => {
    const [historyItems, setHistoryItems] = React.useState([]);

    const fetchHistory = async () => {
        try {
            const response = await fetch('http://localhost:8000/api/history/');
            if (response.ok) {
                const data = await response.json();
                setHistoryItems(data);
            }
        } catch (error) {
            console.error("Failed to fetch history:", error);
        }
    };

    React.useEffect(() => {
        fetchHistory();
        // Poll every 5 seconds to keep history updated
        const interval = setInterval(fetchHistory, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <aside className="sidebar">
            <div className="sidebar-header">
                <button className="menu-btn">☰</button>
                <h2>Historial</h2>
            </div>
            <div className="history-list">
                {historyItems.map((item) => (
                    <div
                        key={item.id}
                        className="history-item"
                        onClick={() => onSelectHistory(item.id)}
                    >
                        <div style={{ fontSize: '12px', color: '#888' }}>
                            {new Date(item.timestamp).toLocaleString()}
                        </div>
                        <div>Iteraciones: {item.iterations}</div>
                        <div style={{ fontSize: '12px' }}>Error: {item.error ? item.error.toExponential(2) : 'N/A'}</div>
                    </div>
                ))}
            </div>
        </aside>
    );
};

export default Sidebar;
