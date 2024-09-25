import React from 'react';
import './Output.css';

interface OutputProps {
    value: string;
}

const Output: React.FC<OutputProps> = ({ value }) => {
    return (
        <div className="output-container">
            <div className="output-box">
                {value || "The solution will appear here..."}
            </div>
        </div>
    );
};

export default Output;
