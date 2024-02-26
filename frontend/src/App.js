import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import LoginPage from './components/Login/loginPage';
import 'bootstrap/dist/css/bootstrap.min.css';


<<<<<<< HEAD
// import HomeProfile from './components/profile'; // Assuming you have this component
=======
// import HomeProfile from './components/profile'; 
>>>>>>> 577e7cbaebf5665132bb958c52fd60a84ef315b7

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/loginPage" element={<LoginPage />} />
      {/* <Route path="/home_profile" element={<HomeProfile />} /> */}
    </Routes>
    </BrowserRouter>
  );
}

export default App;
