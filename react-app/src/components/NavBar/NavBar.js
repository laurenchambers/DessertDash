import React from "react";
import { NavLink } from "react-router-dom";
import LogoutButton from "../auth/LogoutButton";
import "./NavBar.css";
import dessertdash_logo from "../site-images/desssertdash-logo.jpg";
import MeunBar from "./MenuBar";
import AddressSearch from "./AddressSearch";

const NavBar = ({ setAuthenticated }) => {
  return (
    <div>
      <div className="navbar-container">
        <nav className="navbar-navgation">
          <div>
            <div className="navbar-toggle-menu">
              <MeunBar />
            </div>
          </div>
          <div className="navbar-address">
            <div className="navbar-preset-address">ASAP </div>
            <div className="navbar-to-address">to</div>
            <div className="navbar-preset-address">
              <AddressSearch />
            </div>
          </div>
          <div className="navbar-logo">
            <NavLink
              className="navbar-logo"
              to="/home"
              exact={true}
              activeClassName="active"
            >
              <img className="navbar-image" src={dessertdash_logo} alt="" />
              DESSERTDASH
            </NavLink>
          </div>
          <div className="narbar-search-container">SEARCH BAR</div>
          <div className="navbar-cart-container">CART</div>
          {/* <ul>
            <li>
            </li>
            <li>
              <NavLink to="/login" exact={true} activeClassName="active">
                Login
              </NavLink>
            </li>
            <li>
              <NavLink to="/sign-up" exact={true} activeClassName="active">
                Sign Up
              </NavLink>
            </li>
            <li>
              <NavLink to="/users" exact={true} activeClassName="active">
                Users
              </NavLink>
            </li>
            <li>
              <LogoutButton setAuthenticated={setAuthenticated} />
            </li>
          </ul> */}
        </nav>
      </div>
      {/* div below goes with navbar container */}
    </div>
  );
};

export default NavBar;
