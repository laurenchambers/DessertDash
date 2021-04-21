import { NavLink } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarts, removeFromCart } from "../../store/cart";
import { Modal } from "../context/Modal";
import EditItemForm from "../ItemModal/EditItemForm";
import "./TheCart.css";

function CheckoutCart() {
  const [showModal, setShowModal] = useState(null);
  const dispatch = useDispatch();
  const cartsArray = useSelector((state) => state?.carts?.cart);

  useEffect(() => {
    dispatch(getAllCarts());
    if (!cartsArray?.length) {
      return [];
    }
  }, [dispatch]);

  return (
    <>
      <div className="the-cart">
        <div className="the-cart-your-order">Your Order</div>
        <div className="checkout-container">
          <NavLink to="/checkout" exact={true} className="cart-checkout">
            <button className="cart-checkout-button">Place Order</button>
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
                  <div className="cart-current-item-preferences">
                    {cart.preferences}
                  </div>
                </div>
                <div className="cart-current-item-remove">
                  <button
                    onClick={() => {
                      dispatch(removeFromCart(cart.id));
                    }}
                    className="remove-button"
                  >
                    Remove
                  </button>
                  <button
                    onClick={() => setShowModal(cart.id)}
                    className="edit-item-button"
                  >
                    Edit
                  </button>
                </div>
                <div>
                  {cart.id === showModal && (
                    <Modal onClose={() => setShowModal(null)}>
                      <EditItemForm cart={cart} setShowModal={setShowModal} />
                    </Modal>
                  )}
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
    </>
  );
}

export default CheckoutCart;
