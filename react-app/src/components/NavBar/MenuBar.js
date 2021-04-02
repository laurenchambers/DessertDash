import { NavLink } from "react-router-dom";
import React, { useState, useEffect } from "react";
import menubar from "../site-images/menu-bar.png";
import greyx from "../site-images/grey-x.png";
import homeicon from "../site-images/home-icon.png";
import profileicon from "../site-images/profile-icon.jpeg";
import carticon from "../site-images/cart-icon.jpeg";
import "./MenuBar.css";
import LogoutButton from "../auth/LogoutButton"

function MeunBar({ setAuthenticated }) {
  const [showMenu, setShowMenu] = useState(false);

  const closeMenu = () => {
    setShowMenu(false);
  };

  const openMenu = () => {
    if (showMenu) {
      setShowMenu(false);
    } else {
      setShowMenu(true);
    }
  };

  useEffect(() => {
    if (!showMenu) return;

    document.addEventListener("mouseEnter", closeMenu);

    return () => document.removeEventListener("mouseEnter", closeMenu);
  }, [showMenu]);

  return (
    <div className="menubar-container">
      <img className="menu-bar-img" src={menubar} alt="" onClick={openMenu} />
      {showMenu && (
        <div className="menu">
          <div onClick={closeMenu}>
            <img src={greyx} alt="" className="menubar-x" />
          </div>
          <div onClick={closeMenu}>
            <NavLink to="/home" exact={true} className="dropdown-item-first">
              <img className="menubar-image" src={homeicon} alt="" />
              Home
            </NavLink>
          </div>
          <div onClick={closeMenu} >
            <NavLink to="/checkout" exact={true} className="dropdown-item">
              <img src={carticon} alt="" />
              Checkout
            </NavLink>
          </div>
          <div onClick={closeMenu}>
            <div className="dropdown-item">
              <img className="menubar-image" src={profileicon} alt="" />
            <LogoutButton className="dropdown-item" setAuthenticated={setAuthenticated} />
            </div>
          </div>
          {/* <div className="logout-button-nav">
            <LogoutButton setAuthenticated={setAuthenticated} />
          </div> */}
        </div>
      )}
    </div>
  );
}
export default MeunBar;
