import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { Redirect, Link } from "react-router-dom";
import { login } from "../../store/session";
import "./Login.css";

const LoginForm = ({ authenticated, setAuthenticated }) => {
  const dispatch = useDispatch();
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const user = await dispatch(login(email, password));
    if (!user.errors) {
      setAuthenticated(true);
    } else {
      setErrors(user.errors);
    }
  };

  const signInDemoUser = async (e) => {
    e.preventDefault();
    await dispatch(login("demo@desserts.com", "password"));
    setAuthenticated(true);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/home" />;
  }

  return (
    <div className="signin-form-container">
      <form className="signin-form" onSubmit={onLogin}>
        <div className="signin-title">Sign In</div>
        <div className="signup_link_text">
          New to DessertDash?
          <Link to="/signup" className="signup_page_link">
            Sign up
          </Link>
        </div>
        <div>
          {errors.map((error) => (
            <div>{error}</div>
          ))}
        </div>
        <div className="login-email-text">Email</div>
        <div>
          <label htmlFor="email"></label>
          <input
            name="email"
            type="text"
            placeholder=""
            value={email}
            onChange={updateEmail}
            className="form-email-input"
          />
        </div>
        <div className="login-email-text">Password</div>
        <div>
          <label htmlFor="password"></label>
          <input
            name="password"
            type="password"
            placeholder=""
            value={password}
            onChange={updatePassword}
            className="form-email-input"
          />
          <div className='signin-button-space'>
          <button className="login-button" type="submit">
            Sign In
          </button>
          </div>
          <div className='demo-button-space'></div>
          <button
            type="button"
            className="login-button"
            onClick={signInDemoUser}
          >
            Sign In as Demo
          </button>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
