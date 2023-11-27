// SignupDashboard.js
import React from 'react';
import { Link } from 'react-router-dom';

const SignupDashboard = () => {
  return (
    <div>
      <h1>Signup Dashboard</h1>
      <Link to="/signup/student">
        <div>
          <h2>Student Signup</h2>
          <p>Click here to signup new students</p>
        </div>
      </Link>
      <Link to="/signup/teacher">
        <div>
          <h2>Teacher Signup</h2>
          <p>Click here to signup new teachers</p>
        </div>
      </Link>
    </div>
  );
};

export default SignupDashboard;
