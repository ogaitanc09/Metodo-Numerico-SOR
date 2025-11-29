import { useState } from 'react'
import Sidebar from './components/Sidebar'
import InputView from './components/InputView'
import ResultView from './components/ResultView'
import './App.css'

function App() {
  const [currentView, setCurrentView] = useState('input'); // 'input' | 'result'
  const [resultData, setResultData] = useState(null);

  const handleContinue = (data) => {
    setResultData(data);
    setCurrentView('result');
  };

  const handleBack = () => {
    setCurrentView('input');
  };

  const handleSelectHistory = async (id) => {
    try {
      const response = await fetch(`http://localhost:8000/api/history/${id}/`);
      if (response.ok) {
        const data = await response.json();
        setResultData(data);
        setCurrentView('result');
      }
    } catch (error) {
      console.error("Failed to fetch attempt details:", error);
    }
  };

  return (
    <div className="app-container">
      <Sidebar onSelectHistory={handleSelectHistory} />
      <main className="main-content">
        {currentView === 'input' ? (
          <InputView onContinue={handleContinue} />
        ) : (
          <ResultView onBack={handleBack} result={resultData} />
        )}
      </main>
    </div>
  )
}

export default App
