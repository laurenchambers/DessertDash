import React from "react";
import checkoutImage from "../site-images/checkout-image.jpg";
import "./OrderComplete.css";

function OrderComplete() {
  return (
    <>
      <div className="order-complete-words">
        Thank you! Your order will be delivered shortly
      </div>
      <img className="order-complete-image" src={checkoutImage} alt="" />
    </>
  );
}

export default OrderComplete;
