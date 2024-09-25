import React, { useEffect, useState } from 'react';

function History() {
    const [history, setHistory] = useState<string[]>([]);

    useEffect(() => {
        const storedHistory = JSON.parse(localStorage.getItem('inputHistory') || '[]');
        setHistory(storedHistory);
    }, []);

    return (
        <div style={{ height: '50vh', width: '90vw', padding: '20px', backgroundColor: '#fffbc3' }}>
            <h2 style={{ color: '#333', fontFamily: 'Arial, sans-serif' }}>Input History</h2>
            <ul style={{ listStyleType: 'none', padding: 0 }}>
                {history.map((input, index) => (
                    <li
                        key={index}
                        style={{
                            height: '100%',
                            backgroundColor: '#242423',
                            margin: '10px 0',
                            padding: '10px',
                            borderRadius: '4px',
                            boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
                        }}
                    >
                        {input}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default History;
