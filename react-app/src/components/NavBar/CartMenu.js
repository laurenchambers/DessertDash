import { NavLink } from "react-router-dom";
import React, { useState, useEffect } from "react";
import greyx from "../site-images/grey-x.png";
import carticon from "../site-images/cart-icon.jpeg";
import "./CartMenu.css";
import TheCart from "../Cart";

function Cart({ authenticated }) {
  const [showCart, setShowCart] = useState(false);

  const closeCart = () => {
    setShowCart(false);
  };

  const openCart = () => {
    if (showCart) {
      setShowCart(false);
    } else {
      setShowCart(true);
    }
  };

  useEffect(() => {
    if (!showCart) return;

    document.addEventListener("mouseEnter", closeCart);

    return () => document.removeEventListener("mouseEnter", closeCart);
  }, [showCart]);

  return (
    <div className="cart-container">
      <img className="cart-image" src={carticon} alt="" onClick={openCart} />
      {showCart && (
        <div className="cart">
          <div onClick={closeCart}>
            <img src={greyx} alt="" className="menubar-x" />
          </div>
          <div>Your Order</div>
          <div>current restauran(linkto)</div>
          <div onClick={closeCart}>
            <NavLink
              to="/checkout"
              exact={true}
              className="dropdown-item-first"
            >
              <button>Checkout</button>
            </NavLink>
          </div>
          <div onClick={closeCart}>
            <NavLink to="/checkout" exact={true} className="dropdown-item">
              <img src={carticon} alt="" />
              Checkout
            </NavLink>
          </div>
          <div>
            <div className="cart-items">
              <div>1 x hummus</div>
              <div>price</div>
              <div>remove</div>
              <TheCart />
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
export default Cart;
