// SignupDashboard.js
import React from 'react';
import { useNavigate } from 'react-router-dom';

const SignupDashboard = () => {
  const navigate = useNavigate();

  const handleStudentSignupClick = () => {
    navigate('/signup-dashboard/StudentSignup');
  };

  const handleTeacherSignupClick = () => {
    // Adjust this function if you have a separate route for teacher signup
    navigate('/signup-dashboard/TeacherSignup');
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="mx-4">
        <div
            className="block rounded-lg bg-white shadow-[0_4px_20px_-5px_rgba(0,0,0,0.1),0_10px_25px_-5px_rgba(0,0,0,0.1)] dark:bg-neutral-700"
            onClick={handleStudentSignupClick}
        >
          <img
            className="rounded-t-lg"
            src="https://tecdn.b-cdn.net/img/new/standard/nature/184.jpg"
            alt=""
          />
          <div className="p-4">
            <h5 className="mb-2 text-lg font-medium leading-tight text-neutral-800 dark:text-neutral-50">
              Student Admission
            </h5>
            <p className="mb-2 text-sm text-neutral-600 dark:text-neutral-200">
              Click here to signup new students.
            </p>
          </div>
        </div>
      </div>

      <div className="mx-4">
        <div
          className="block rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700"
          onClick={handleTeacherSignupClick}
        >
          <img
            className="rounded-t-lg"
            src="https://tecdn.b-cdn.net/img/new/standard/nature/184.jpg"
            alt=""
          />
          <div className="p-4">
            <h5 className="mb-2 text-lg font-medium leading-tight text-neutral-800 dark:text-neutral-50">
              Teacher's Admission
            </h5>
            <p className="mb-2 text-sm text-neutral-600 dark:text-neutral-200">
              Click here to signup new teachers.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SignupDashboard;
