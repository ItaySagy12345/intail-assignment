import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

// Global styling
import "@/styles/reset.scss";
import "@/styles/themes.css";

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
