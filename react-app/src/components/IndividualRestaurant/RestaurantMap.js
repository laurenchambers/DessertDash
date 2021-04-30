import { GoogleMap, withGoogleMap, Marker } from "react-google-maps";
import React from "react";
import { useSelector } from "react-redux";

const RestaurantMap = withGoogleMap(() => {
  const currRestaurant = useSelector(
    (state) => state?.restaurant?.currentRestaurant
  );
  const locations = [
    {
      name: "Location 1",
      location: {
        lat: currRestaurant?.lat,
        lng: currRestaurant?.lng,
      },
    },
    {
      name: "Location 2",
      location: {
        lat: 41.3917,
        lng: 2.1649,
      },
    },
  ];

  return (
    <GoogleMap
      defaultZoom={14}
      defaultCenter={{ lat: currRestaurant?.lat, lng: currRestaurant?.lng }}
    >
      {locations.map((item) => {
        return <Marker key={item.name} position={item.location} />;
      })}
    </GoogleMap>
  );
});

export default RestaurantMap;
