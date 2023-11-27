// TeacherSignup.js
import React, { useState } from 'react';
import axios from 'axios';

const TeacherSignup = () => {
  const [formData, setFormData] = useState({
    teachername: '',
    teachermobile: '',
    entrysalary: '',
  });
  const [successMessage, setSuccessMessage] = useState('');

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    try {
      // Make API request to store teacher data in the database
      const response = await axios.post('http://127.0.0.1:8000/api/teachersignup/', formData);

      // Display success message
      setSuccessMessage('Successfully signed up teacher');
      console.log('Teacher Signup success:', response.data);
    } catch (error) {
      console.error('Teacher Signup failed:', error.response.data);
    }
  };

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  return (
    <div>
      <h1>Teacher Signup</h1>
      <form onSubmit={handleFormSubmit}>
        <div>
          <label htmlFor="teachername">Teacher Name</label>
          <input
            type="text"
            id="teachername"
            name="teachername"
            value={formData.teachername}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="teachermobile">Teacher Mobile</label>
          <input
            type="text"
            id="teachermobile"
            name="teachermobile"
            value={formData.teachermobile}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="entrysalary">Entry Salary</label>
          <input
            type="text"
            id="entrysalary"
            name="entrysalary"
            value={formData.entrysalary}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {successMessage && <div>{successMessage}</div>}
    </div>
  );
};

export default TeacherSignup;
