import React, {useState} from "react";
import axios  from  'axios';
import  './login.css'
import { useNavigate } from 'react-router-dom';


function LoginPage() {
  const [mail, setMail] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate()


  const [isProfessor,setIsProfessor] = useState(false)

  const handleSubmit = async (e)=>{
    e.preventDefault();
    try {
      // const backendURL = process.env.REACT_APP_BACKEND_URL;
      const response = await axios.post(`https://localhost:5000s/login`, {
        mail:mail,
        password:password,
      })

      if (response.data.success) {
        // Handle successful login here
        console.log(response.data.message);
        navigate('/home_profil');
        // Redirect the professor or store login state
      } else {
        // Update your state to show an error message
        setErrorMessage(response.data.message);
      }
      
    }catch(error){
      setErrorMessage('An error occurred. Please try again later.');

    }}

    return (
      <div className="login-container">
      <form onSubmit={handleSubmit} className="login-form">
        {/* <label className="switch"> */}
          {/* <input
            type="checkbox"
            checked={isProfessor}
            onChange={() => setIsProfessor(!isProfessor)}
          />
          <span className="slider round"></span>
        </label>
         */}
        <div className="switch-container">
        <label className="switch-label">
          <span className="switch-description">{isProfessor ? 'Professor' : 'Student'}</span>
          <input
            type="checkbox"
            checked={isProfessor}
            onChange={() => setIsProfessor(!isProfessor)}
          />
          <h2>{isProfessor ? 'Professor' : 'Student'} Login</h2>
    <span className="switch-slider round"></span>
  </label>
</div>
          <div>
              <label>MAIL:</label>
              <input
                  type="email"
                  value={mail}
                  onChange={(e) => setMail(e.target.value)}
              />
          </div>
          <div>
              <label>Password:</label>
              <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
              />
          </div>
          {errorMessage && <p>{errorMessage}</p>}
          <button type="submit">Login</button>
      </form>
      </div>
  );
}


export default LoginPage