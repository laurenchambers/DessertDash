import { NavLink } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarts, removeFromCart } from "../../store/cart";
import { Modal } from "../context/Modal";
import EditItemForm from "../ItemModal/EditItemForm";
import "./TheCart.css";
import "./CheckoutCart.css";

function CheckoutCart() {
  const user = useSelector((state) => state.session.user);
  const [showModal, setShowModal] = useState(null);
  const dispatch = useDispatch();
  const cartsArray = useSelector((state) => state?.carts?.cart);

  const totalPrice = cartsArray?.map((cart) =>
    (cart.item_price * cart.quantity).toFixed(2)
  );

  const totalNumbers = totalPrice?.map((price) => parseFloat(price));
  const cartTotal = totalNumbers?.reduce((a, b) => a + b, 0);

  let tip = 3;

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
        <div>
          <div className="line-divider"></div>
        </div>
        <div clasName="dasher-tip-container">
          <div className="dasher-tip-amounts">
            <div className="dasher-tip-title">Dasher Tip</div>
            <div className="dasher-tip-amount">${tip}.00</div>
          </div>
          <div className="dasher-tip-blurb">
            The recommended Dasher tip is based on the delivery distance and
            effort. 100% of the tip goes to your Dasher :)
          </div>
        </div>
        <div>
          <div className="line-divider"></div>
        </div>
        <div className="dash-total">
          <div className="dash-total-title">Total</div>
          <div className="dash-total-amount">${cartTotal + tip}</div>
        </div>
      </div>
    </>
  );
}

export default CheckoutCart;
