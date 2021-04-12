import { NavLink } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarts, removeFromCart } from "../../store/cart";
import greyx from "../site-images/grey-x.png";
import carticon from "../site-images/cart-icon.jpeg";
import "./CartMenu.css";

function Cart({ cart, submission, authenticated }) {
  const [showCart, setShowCart] = useState(false);
  const dispatch = useDispatch();
  const cartsArray = useSelector((state) => state.carts.cart);

  // const totalPrice = cartsArray?.reduce(
  //   (a, b) => a + (b["item_price"] || 0),
  //   0
  // );
  // const totalQuanity = cartsArray?.reduce(
  //   (a, b) => a + (b["quantity"] || 0),
  //   0
  // );
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
    dispatch(getAllCarts());
    if (!showCart) return;

    document.addEventListener("mouseEnter", closeCart);

    return () => document.removeEventListener("mouseEnter", closeCart);
  }, [dispatch, showCart]);

  return (
    <>
      <img className="cart-image" src={carticon} alt="" onClick={openCart} />
      {/* <div className="cart-container"> */}
      {/* <div className="cart-image-container">
      </div> */}
      {showCart && (
        <div className="cart">
          <div onClick={closeCart}>
            <img src={greyx} alt="" className="menubar-x" />
          </div>
          <div className="cart-your-order">Your Order</div>
          <div onClick={closeCart}>
            <NavLink to="/checkout" exact={true} className="cart-checkout">
              <button className="cart-checkout-button">
                Checkout
              </button>
            </NavLink>
          </div>
          <div className="cart-current-items">
            {cartsArray?.map((cart) => (
              <>
                <div className="cart-items-container">
                  <div className="cart-current-item-quantity">
                    <span classname="current-item-quantity-cart">
                      {cart.quantity} x
                    </span>
                  </div>
                  <div className="cart-current-item-name">
                    <span className="curent-item-name-cart">
                      {cart.item_name}
                    </span>
                  </div>
                  <div className="cart-current-item-remove">
                    <button
                      onClick={() => {
                        dispatch(removeFromCart(cart.id)) &&
                          dispatch(getAllCarts());
                      }}
                      className="remove-button"
                    >
                      Remove
                    </button>
                  </div>
                  <div className="cart-current-item-price">
                    <span className="current-item-price">
                      ${(cart.item_price * cart.quantity).toFixed(2)}
                    </span>
                  </div>
                </div>
              </>
            ))}
          </div>
        </div>
      )}
      {/* </div> */}
    </>
  );
}
export default Cart;
