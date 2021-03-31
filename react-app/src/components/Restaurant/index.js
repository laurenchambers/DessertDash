import React from "react";

//will want to destructure items on line 4 as well to key into photos
const Restaurant = ({ restaurant }) => {
  if (restaurant) {
    return (
      <div>
        <div>
          <div className="restaurant-title">{restaurant.name}</div>
          <div className="restaurant-price">{restaurant.price}</div>
          <div className="restaurant rating">{restaurant.rating}</div>
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Restaurant;
