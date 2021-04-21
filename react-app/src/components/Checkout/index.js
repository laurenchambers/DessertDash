import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import CheckoutCart from "../Cart";
import "./Checkout.css";
import {
  GoogleMap,
  withScriptjs,
  withGoogleMap,
  Marker,
} from "react-google-maps";

function Map() {
  const user = useSelector((state) => state.session.user);
  return (
    <GoogleMap
      defaultZoom={14}
      defaultCenter={{ lat: 30.26498, lng: -97.746597 }}
    >
      <Marker position={{ lat: user.lat, lng: user.lng }} />
    </GoogleMap>
  );
}

const WrappedMap = withScriptjs(withGoogleMap(Map));

const Checkout = () => {
  const user = useSelector((state) => state.session.user);
  const currentURL = window.location.pathname;
  console.log("URL", currentURL);

  return (
    <div className="checkout-page">
      <div className="checkout-page-rows">
        <div className="checkout-page-time">
          <div className="time-title">TIME</div>
          <div className="time-amount-time">30mins</div>
        </div>
        <div className="checkout-page-address-container">
          <div className="checkout-address-title">ADDRESS</div>
          <div className="checkout-address-map">
            <WrappedMap
              googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyB3lFaDSw-OH95uJunSPk6f8EUrZGvpcx8`}
              loadingElement={<div style={{ height: "100%" }} />}
              containerElement={<div style={{ height: "100%" }} />}
              mapElement={<div style={{ height: "100%" }} />}
            />
            <div className="checkout-address-subaddress">{user.address}</div>
          </div>
        </div>
        <div className="payment-container">
          <div className="payment-title">PAYMENT</div>
          <div className="payment-card-info">card info</div>
        </div>
        <div className="place-order-container">
          <button className="place-order-button">Place Order</button>
        </div>
        <div>
          <CheckoutCart />
        </div>
      </div>
    </div>
  );
};

export default Checkout;
