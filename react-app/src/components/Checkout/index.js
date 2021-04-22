import React from "react";
import { useSelector } from "react-redux";
import CheckoutCart from "../Cart/CheckoutCart";
import "./Checkout.css";
import { GoogleMap, withGoogleMap, Marker } from "react-google-maps";
import mastercard from "../site-images/mastercard.png";

const Map = withGoogleMap(() => {
  const user = useSelector((state) => state.session.user);
  const defaultMarker = { lat: user.lat, lng: user.lng };
  return (
    <GoogleMap
      defaultZoom={14}
      defaultCenter={{ lat: user.lat, lng: user.lng }}
    >
      {<Marker key={user.id} postition={defaultMarker} />}
    </GoogleMap>
  );
});

const Checkout = () => {
  const user = useSelector((state) => state.session.user);
  const currentURL = window.location.pathname;
  const defaultMarker = { lat: user.lat, lng: user.lng };

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
            <Map
              user={user}
              googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places`}
              loadingElement={<div style={{ height: `100%` }} />}
              containerElement={<div style={{ height: "100%" }} />}
              mapElement={<div style={{ height: "100%" }} />}
            >
              {<Marker key={user.id} postition={defaultMarker} />}
            </Map>
            <div className="checkout-address-subaddress">{user.address}</div>
          </div>
        </div>
        <div className="payment-container">
          <div className="payment-title">
            <div className='payment-title-title'>PAYMENT</div>
            <div className='payment-change-add'>Change / Add</div>
          </div>
          <div className="payment-card-info">
            <img className="payment-card-img" src={mastercard} alt="" />
            <div className="payment-card-numbers">MasterCard....8783</div>
          </div>
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
