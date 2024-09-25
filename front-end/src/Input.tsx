import React from 'react';
import './Input.css';

interface InputProps {
    value: string;
    onChange: (event: React.ChangeEvent<HTMLTextAreaElement>) => void;
}

const Input: React.FC<InputProps> = ({ value, onChange }) => {
    return (
        <div className="input-container">
            <textarea
                className="input-box"
                value={value}
                onChange={onChange}
                placeholder="Enter your problem here..."
            />
        </div>
    );
};

export default Input;
