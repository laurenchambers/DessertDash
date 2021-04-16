import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";

const LogoutButton = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const [authenticated, setAuthenticated] = useState(false);

  const onLogout = async (e) => {
    await logout();
    setAuthenticated(false);
    dispatch(logout());
    return history.push("/");
  };

  return <button onClick={onLogout}>Sign Out</button>;
};

export default LogoutButton;
