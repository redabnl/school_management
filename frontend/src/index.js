import App from './App';
import { createRoot } from 'react-dom/client';


const container = document.getElementById('root');
const root = createRoot(container); // create a root.
root.render(<App />);
