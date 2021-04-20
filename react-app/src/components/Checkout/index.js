import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import {
  GoogleMap,
  withScriptjs,
  withGoogleMap,
  Marker,
} from "react-google-maps";

function Map({ user }) {
  // const user = useSelector((state) => state.session.user);
  return (
    <GoogleMap
      defaultZoom={10}
      defaultCenter={{ lat: 30.26498, lng: -97.746597 }}
    >
      {/* <Marker position={{ lat: user.lat, lng: user.lng }} /> */}
    </GoogleMap>
  );
}

const WrappedMap = withScriptjs(withGoogleMap(Map));

const Checkout = () => {
  return (
    <div>
      <h1></h1>
      <h2> hi </h2>
      <h2>Checkout Page</h2>
      <div style={{ width: "50vw", height: "50vh" }}>
        <WrappedMap
          googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyB3lFaDSw-OH95uJunSPk6f8EUrZGvpcx8`}
          loadingElement={<div style={{ height: "100%" }} />}
          containerElement={<div style={{ height: "100%" }} />}
          mapElement={<div style={{ height: "100%" }} />}
        />
      </div>
    </div>
  );
};

export default Checkout;
