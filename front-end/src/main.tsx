import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Auth from './Auth';
import App from './App';
import Credit from './Credit';
import History from './history';
import './index.css';


const rootElement = document.getElementById('root') as HTMLElement;
const root = ReactDOM.createRoot(rootElement);

root.render(
    <React.StrictMode>
        <Router>
            <Routes>
                <Route path="/" element={<Auth />} />
                <Route path="/app" element={<App />} />
                <Route path="/credit" element={<Credit />} />
                <Route path="/history" element={<History />} />
            </Routes>
        </Router>
    </React.StrictMode>
);
