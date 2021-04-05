import React, { useState } from "react";
import { Redirect, Link } from "react-router-dom";
import { signUp } from "../../store/session";
import { useDispatch } from "react-redux";
import NavBar from "../NavBar/NavBar";

const SignUpForm = ({ authenticated, setAuthenticated }) => {
  const dispatch = useDispatch();
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [errors, setErrors] = useState([]);

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const user = await dispatch(
        signUp(first_name, last_name, email, password)
      );
      if (!user.errors) {
        setAuthenticated(true);
      } else {
        setErrors(user.errors);
      }
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updateFirstName = (e) => {
    setFirstName(e.target.value);
  };

  const updateLastName = (e) => {
    setLastName(e.target.value);
  };

  if (authenticated) {
    return <Redirect to="/home" />;
  }

  return (
    <div className="signin-form-container">
      <NavBar />
      <form className="signin-form" onSubmit={onSignUp}>
        <div className="signin-title">Sign Up</div>
        <div className="signup_link_text">
          Already have an account?
          <Link to="/login" className="signup_page_link">
            Sign In
          </Link>
        </div>
        <div>
          {errors.map((error) => (
            <div key={error}>{error}</div>
          ))}
        </div>
        <div className="input-name-container">
          <div className="first-name-container">
            <div className="login-name-text">First Name</div>
            <input
              type="text"
              name="firstName"
              onChange={updateFirstName}
              value={first_name}
              placeholder=""
              className="form-email-name-input"
            ></input>
          </div>
          <div>
            <div className="login-lastname-text">Last Name</div>
            <input
              type="text"
              name="lastName"
              onChange={updateLastName}
              value={last_name}
              placeholder=""
              className="form-email-lastname-input"
            ></input>
          </div>
        </div>
        <div className="login-email-text">Email</div>
        <div>
          <input
            type="text"
            name="email"
            onChange={updateEmail}
            value={email}
            className="form-email-input"
          ></input>
        </div>
        <div className="login-email-text">Password</div>
        <div>
          <input
            type="password"
            name="password"
            onChange={updatePassword}
            value={password}
            className="form-email-input"
          ></input>
        </div>
        <div className="login-email-text">Repeat Password</div>
        <div>
          <input
            type="password"
            name="repeat_password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
            className="form-email-input"
          ></input>
        </div>
        <button className="login-button" type="submit">
          Sign Up
        </button>
      </form>
    </div>
  );
};

export default SignUpForm;
