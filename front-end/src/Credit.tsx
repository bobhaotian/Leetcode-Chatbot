// Credit.tsx
import React from 'react';
import './Credit.css';
import avatar1 from './assets/svgs/Avatar1.png';
import avatar2 from './assets/svgs/Avatar2.png';
import avatar3 from './assets/svgs/Avatar3.png';

const Credit = () => {
    return (
        <div className="credit-page">
            <h2>Credit</h2>
            <div className="credit-list">
                <div className="credit-item">
                    <img src={avatar1} alt="Avatar 1" className="avatar" />
                    <div className="credit-info">
                        <h2>Robert</h2>
                        <p>Developer1</p>
                    </div>
                </div>
                <div className="credit-item">
                    <img src={avatar2} alt="Avatar 2" className="avatar" />
                    <div className="credit-info">
                        <h2>Steven</h2>
                        <p>Developer2</p>
                    </div>
                </div>
                <div className="credit-item">
                    <a href="/yiyunDescription.html">
                        <img src={avatar3} alt="Avatar 3" className="avatar" />
                    </a>
                    <div className="credit-info">
                        <h2>Yiyun</h2>
                        <p>Developer3</p>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Credit;
