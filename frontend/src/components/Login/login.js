import React, {useState} from "react";
import axios  from  'axios';
import  './login.css'
import { useNavigate } from 'react-router-dom';


const LoginForm = () => {
  const [mail, setMail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isProfessor, setIsProfessor] = useState(false);

  const handleToggleChange = () => {
    setIsProfessor(!isProfessor);
  };

  const handleMailChange = (event) => {
    setMail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };


  const handleSubmit = async (event) => {
    event.preventDefault();
    const endpoint = isProfessor ? 'http://localhost:5000/professor_login' : 'http://localhost:5000/student_login';
    try {

    const response = await fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ mail: mail, password: password}),
    });

    const data = await response.json()

    if (response.ok) {
      // Redirect to home profile
      console.log('Login Success:', data);
      // Redirect logic here, e.g., window.location.href = '/dashboard';
    } 
    else{
      console.log('error finding data :', data)
      setError(data.message || 'Invalid credentials or server error');
    }
  } catch (err){
    console.log('error :', err)

  }
  };

  return (
    <div className={`login-form ${isProfessor ? 'professional' : 'student-friendly'}`}>
      <label className="switch">
        <input type="checkbox" checked={isProfessor} onChange={handleToggleChange} />
        <span className="slider round"></span>
      </label>
      <form onSubmit={handleSubmit}>
        <div>
          <label>
            Mail:
            <input type="mail" value={mail} onChange={handleMailChange} required />
          </label>
        </div>
        <div>
          <label>
            Password:
            <input type="password" value={password} onChange={handlePasswordChange} required />
          </label>
        </div>
        <button type="submit">Login</button>
        {error && <p className="error">{error}</p>}
      </form>
    </div>
  );
};

export default LoginForm