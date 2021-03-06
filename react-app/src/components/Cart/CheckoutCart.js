import { NavLink, useHistory } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarts, removeFromCart } from "../../store/cart";
import { Modal } from "../context/Modal";
import EditItemForm from "../ItemModal/EditItemForm";
import "./TheCart.css";
import "./CheckoutCart.css";

function CheckoutCart() {
  const history = useHistory();
  const [tip, setTip] = useState(0);
  const [showModal, setShowModal] = useState(null);
  const dispatch = useDispatch();
  const deliveryFee = 2.99;
  const user = useSelector((state) => state.session.user);

  const cartsArray = useSelector((state) => state?.carts?.cart);

  const totalPrice = cartsArray?.map((cart) =>
    (cart.item_price * cart.quantity).toFixed(2)
  );

  const totalNumbers = totalPrice?.map((price) => parseFloat(price));
  const cartTotal = totalNumbers?.reduce((a, b) => a + b, 0);
  const cartFee = cartTotal * 0.15 + cartTotal * 0.063;

  const redirect = () => {
    history.push("/order-complete");
  };

  useEffect(() => {
    dispatch(getAllCarts());
    if (!cartsArray?.length) {
      return [];
    }
  }, [dispatch, cartsArray?.length]);

  return (
    <>
      <div className="the-cart">
        <div className="the-cart-your-order">Your Order</div>
        <div className="checkout-container">
          <div className="cart-checkout">
            <button onClick={redirect} className="cart-checkout-button">
              Place Order
            </button>
          </div>
        </div>
        <div className="cart-current-items">
          {cartsArray?.map((cart) => (
            <>
              <div className="cart-items-container">
                <div className="cart-current-item-quantity">
                  <span className="current-item-quantity-cart">
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
                      <EditItemForm
                        key={cart.id}
                        cart={cart}
                        setShowModal={setShowModal}
                      />
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
        <div className="price-total-container">
          <div className="subtotal-container">
            <div className="subtotal-title">Subtotal</div>
            <div className="subtotal-amount">${cartTotal?.toFixed(2)}</div>
          </div>
          <div className="delivery-fee-info-container">
            <div className="delivery-fee-info-title">Delivery Fee</div>
            <div className="deliver-fee-info-amount">${deliveryFee}</div>
          </div>
          <div className="taxes-fee-container">
            <div className="taxes-fee-title">Fees {`&`} Estimated Tax</div>
            <div className="taxes-fee-amount">${cartFee.toFixed(2)}</div>
          </div>
        </div>
        <div>
          <div className="line-divider"></div>
        </div>

        <div className="dasher-tip-container">
          <div className="dasher-tip-amounts">
            <div className="dasher-tip-title">Dasher Tip</div>
            <div className="dasher-tip-amount">${tip}.00</div>
          </div>
          <div className="dasher-tip-selection-container">
            <button onClick={() => setTip(2)} className="tip-selection-one">
              $2
            </button>
            <button onClick={() => setTip(4)} className="tip-selection-two">
              $4
            </button>
            <button onClick={() => setTip(6)} className="tip-selection-three">
              $6
            </button>
            <button onClick={() => setTip(8)} className="tip-selection-four">
              $8
            </button>
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
          <div className="dash-total-amount">
            ${(cartTotal + tip + cartFee + deliveryFee).toFixed(2)}
          </div>
        </div>
      </div>
    </>
  );
}

export default CheckoutCart;
