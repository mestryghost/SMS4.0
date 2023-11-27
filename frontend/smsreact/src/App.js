import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import AdminLogin from './components/AdminLogin';
import SignupDashboard from './components/SignupDashboard';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Function to handle successful login
  const handleLogin = () => {
    // For simplicity, let's assume successful login sets isLoggedIn to true
    setIsLoggedIn(true);
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={isLoggedIn ? <Navigate to="/signup-dashboard" /> : <AdminLogin onLogin={handleLogin} />} />
        <Route path="/signup-dashboard" element={isLoggedIn ? <SignupDashboard /> : <Navigate to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;