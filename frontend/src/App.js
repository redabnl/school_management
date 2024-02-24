import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom';
import LoginPage from './components/Login/login';

// import HomeProfile from './components/profile'; // Assuming you have this component

function App() {
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      {/* <Route path="/home_profile" element={<HomeProfile />} /> */}
    </Routes>
    </BrowserRouter>
  );
}

export default App;
