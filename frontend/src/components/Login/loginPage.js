import React, { useState } from 'react';
import './loginPage.css'; // Make sure you link the CSS file

function LoginPage() {
  const [isStudent, setIsStudent] = useState(true);

  const toggleRole = () => {
    setIsStudent(!isStudent);
  };


  const handleSubmit = async (event) => {
    event.preventDefault();
    // Extract the form data
    const formData = new FormData(event.target);
    const loginDetails = {
      mail: formData.get('mail'), // Assuming the input has a name attribute "email"
      password: formData.get('password'), // Assuming the input has a name attribute "password"
    };
  
    const role = isStudent ? 'student' : 'professor';
    const baseUrl = 'http://localhost:5000'; // Change this to the URL of your Flask app
    const endpoint = role === 'student' ? `${baseUrl}/student_login` : `${baseUrl}/professor_login`;
  
    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(loginDetails),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      console.log('Login successful:', data);
      // Here you could redirect the user or perform other actions upon successful login
    } catch (error) {
      console.error('Login failed:', error);
    }
  };
  return (
    <div className="login-container">
      <div className="home-section">
        {/* Home section content goes here */}
        <button className="library-btn">Public Library</button>
      </div>
      <div className="form-section">
        <button onClick={toggleRole} className="toggle-btn">
          {isStudent ? 'Switch to Professor' : 'Switch to Student'}
        </button>
        <form onSubmit={handleSubmit}>
          <input type="email" placeholder="Mail"name="mail" required />
          <input type="password" placeholder="Password" name="password" required />
          <button type="submit" className="submit-btn">
            Sign In as {isStudent ? 'Student' : 'Professor'}
          </button>
        </form>
      </div>
    </div>
  );
  

}
export default LoginPage