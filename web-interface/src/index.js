import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import AudioInputAndDisplay from './AudioRecorder';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AudioInputAndDisplay />
  </React.StrictMode>
);
