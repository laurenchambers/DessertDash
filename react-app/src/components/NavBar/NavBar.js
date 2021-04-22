import React from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";
import dessertdash_logo from "../site-images/desssertdash-logo.jpg";
import MeunBar from "./MenuBar";
import AddressSearch from "./AddressSearch";
import SearchBar from "./SearchBar";
import Cart from "./CartMenu";

const NavBar = ({ authenticated, setAuthenticated }) => {
  const currentURL = window.location.pathname;

  if (authenticated && currentURL === "/checkout") {
    return (
      <div>
        <div className="navbar-container">
          <nav className="navbar-navgation">
            <div>
              <div className="navbar-toggle-menu">
                <MeunBar setAuthenticated={setAuthenticated} />
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
          </nav>
        </div>
      </div>
    );
  } else if (authenticated) {
    return (
      <div>
        <div className="navbar-container">
          <nav className="navbar-navgation">
            <div>
              <div className="navbar-toggle-menu">
                <MeunBar setAuthenticated={setAuthenticated} />
              </div>
            </div>
            <div className="navbar-address">
              <div className="navbar-preset-address">ASAP </div>
              <div className="navbar-to-address">to</div>
              <div className="navbar-preset-address-2">
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
            <div className="narbar-search-container">
              <SearchBar />
            </div>
            <Cart className="nav-cart-area" />
          </nav>
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default NavBar;
