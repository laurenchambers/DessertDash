import React from "react";
import "./Restaurant.css";

//will want to destructure items on line 4 as well to key into photos
const RestaurantTwoImages = ({ restaurant }) => {
  if (restaurant) {
    return (
      <div>
        <div>
          <img
            className="restaurant-top-image"
            src={restaurant?.items[1]?.image_src}
            alt=""
          />
          <img
            className="restaurant-top-image"
            src={restaurant?.items[2]?.image_src}
            alt=""
          />
          {/* <img
            className="restaurant-top-image"
            src={restaurant?.items[1]?.image_src}
            alt=""
          /> */}
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

export default RestaurantTwoImages;
