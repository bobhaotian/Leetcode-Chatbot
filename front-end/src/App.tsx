import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import './App.css';

import TitleIcon from './assets/svgs/LeetBot your problem-solver chatbot for LeetCode.svg';
import ButtonIcon from './assets/svgs/Button.svg';

function App() {
    const [inputValue, setInputValue] = useState('');
    const [outputValue, setOutputValue] = useState('');

    const handleGenerate = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/api/generate', { prompt: inputValue });
            setOutputValue(response.data.code);

            // Store the input in localStorage
            const history = JSON.parse(localStorage.getItem('inputHistory') || '[]');
            history.unshift(inputValue);
            if (history.length > 10) {
                history.pop(); // Keep only the latest 10 inputs
            }
            localStorage.setItem('inputHistory', JSON.stringify(history));
        } catch (error) {
            console.error('Error generating response:', error);
            setOutputValue('Error generating response.');
        }
    };

    return (
        <div className="app">
            <header className="header">
                <img src={TitleIcon} alt="LeetBot" className="title-icon" />
            </header>
            <div className="content">
                <div className="input-container">
                    <textarea
                        className="input-box"
                        placeholder="Enter your problem here..."
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                    />
                </div>
                <div className="divider"></div>
                <div className="output-container">
                    <textarea
                        className="output-box"
                        placeholder="The solution will appear here..."
                        value={outputValue}
                        readOnly
                    />
                </div>
            </div>
            <footer className="footer">
                <button className="generate-button" onClick={handleGenerate}>
                    Generate
                </button>
                <Link to="/credit" className="credit-button">
                    Credit
                </Link>
                <Link to="/history" className="history-button">
                    History
                </Link>
            </footer>
        </div>
    );
}

export default App;
