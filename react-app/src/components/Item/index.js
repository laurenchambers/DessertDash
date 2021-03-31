import React from "react";

//will want to destructure items on line 4 as well to key into photos
const Item = ({ item }) => {
  if (item) {
    return (
      <div>
        <div>
          <div className="restaurant-title">{item.name}</div>
          <div className="restaurant rating">{item.description}</div>
          <div>${item.price}</div>
          <img src={item.image_src} alt="" />
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Item;
