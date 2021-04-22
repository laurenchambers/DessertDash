import React from "react";
import { useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";

const LogoutButton = ({ setAuthenticated }) => {
  const dispatch = useDispatch();
  const history = useHistory();

  const onLogout = async (e) => {
    await logout();
    dispatch(logout());
    setAuthenticated(false);
    return history.push("/");
  };

  return <button onClick={onLogout}>Sign Out</button>;
};

export default LogoutButton;
