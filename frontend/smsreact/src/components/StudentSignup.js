// StudentSignup.js
import React, { useState } from 'react';
import axios from 'axios';

const StudentSignup = () => {
  const [formData, setFormData] = useState({
    studentname: '',
    studentmobile: '',
    entryfee: '',
  });
  const [successMessage, setSuccessMessage] = useState('');

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    try {
      // Make API request to store student data in the database
      const response = await axios.post('http://127.0.0.1:8000/api/studentsignup/', formData);

      // Display success message
      setSuccessMessage('Successfully signed up student');
      console.log('Student Signup success:', response.data);
    } catch (error) {
      console.error('Student Signup failed:', error.response.data);
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
      <h1>Student Signup</h1>
      <form onSubmit={handleFormSubmit}>
        <div>
          <label htmlFor="studentname">Student Name</label>
          <input
            type="text"
            id="studentname"
            name="studentname"
            value={formData.studentname}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="studentmobile">Student Mobile</label>
          <input
            type="text"
            id="studentmobile"
            name="studentmobile"
            value={formData.studentmobile}
            onChange={handleInputChange}
          />
        </div>
        <div>
          <label htmlFor="entryfee">Entry Fee</label>
          <input
            type="text"
            id="entryfee"
            name="entryfee"
            value={formData.entryfee}
            onChange={handleInputChange}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
      {successMessage && <div>{successMessage}</div>}
    </div>
  );
};

export default StudentSignup;
