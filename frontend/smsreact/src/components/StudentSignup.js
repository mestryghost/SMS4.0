import React, { useState } from 'react';
import axios from 'axios';

const StudentSignup = () => {
  const [formData, setFormData] = useState({
    firstname: '',
    lastname: '',
    email: '',
    username: '',
    password: '',
    confirmPassword: '',
  });
  const [successMessage, setSuccessMessage] = useState('');

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    try {
      // Make API request to store student data in the database
      const response = await axios.post('http://127.0.0.1:8000/api/studentsignup/', {
        first_name: formData.firstname, // Match the field names here
        last_name: formData.lastname,   // Match the field names here
        email: formData.email,
        username: formData.username,
        password: formData.password,
        confirmPassword: formData.confirmPassword,
      });

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
    <div className="flex justify-center items-center h-screen">
      <div className="w-96 p-8 bg-white rounded-md shadow-md">
        <h1 className="text-2xl font-bold mb-4">Student Signup</h1>
        <form onSubmit={handleFormSubmit}>
          <div className="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
            <input
              className="pl-2 outline-none border-none flex-1"
              type="text"
              name="firstname"
              placeholder="First Name"
              value={formData.firstname}
              onChange={handleInputChange}
            />
          </div>
          <div className="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
            <input
              className="pl-2 outline-none border-none flex-1"
              type="text"
              name="lastname"
              placeholder="Last Name"
              value={formData.last_name}
              onChange={handleInputChange}
            />
          </div>
          <div className="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
            <input
              className="pl-2 outline-none border-none flex-1"
              type="text"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleInputChange}
            />
          </div>
          <div className="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
            <input
              className="pl-2 outline-none border-none flex-1"
              type="text"
              name="username"
              placeholder="Username"
              value={formData.username}
              onChange={handleInputChange}
            />
          </div>
          <div className="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
            <input
              className="pl-2 outline-none border-none flex-1"
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleInputChange}
            />
          </div>
          <div className="flex items-center border-2 py-2 px-3 rounded-2xl mb-4">
            <input
              className="pl-2 outline-none border-none flex-1"
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              value={formData.confirmPassword}
              onChange={handleInputChange}
            />
          </div>
          <br></br>
          <button type="submit" className="block w-full bg-blue-500 text-white py-2 rounded-2xl">
            Submit
          </button>
        </form>
        {successMessage && <div className="mt-4 text-green-500">{successMessage}</div>}
      </div>
    </div>
  );
};

export default StudentSignup;
