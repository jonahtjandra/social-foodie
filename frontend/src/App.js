import logo from './logo.svg';
import './App.css';
import React from 'react';
import { GoogleLogin } from 'react-google-login';

function App() {
  const responseGoogle = (response) => {
    console.log(response);
  }
  return (
    <div className="App">
      <h1>Social Foodie</h1>
      <GoogleLogin
        clientId="353050019892-dhaegvs5p5b0rjue8v9umcs14m7mveo3.apps.googleusercontent.com"
        buttonText="Login"
        onSuccess={responseGoogle}
        onFailure={responseGoogle}
        cookiePolicy={'single_host_origin'}
      />
    </div>
  );
}

export default App;
