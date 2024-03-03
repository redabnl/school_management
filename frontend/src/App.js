import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import LoginPage from './components/Login/loginPage';
import 'bootstrap/dist/css/bootstrap.min.css';


// import HomeProfile from './components/profile'; 


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
