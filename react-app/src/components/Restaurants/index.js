import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { allRestaurants } from "../../store/restaurants";
import { getAllItems } from "../../store/items";
import Restaurant from "../Restaurant";
import Item from "../Item";

const ShowRestaurant = () => {
  const dispatch = useDispatch();
  const restaurantArray = useSelector(
    (state) => state?.restaurants?.allRestaurants?.restaurants
  );

  const itemsArray = useSelector((state) => state?.items?.allItems?.items);
  console.log("ITEMs", itemsArray);

  console.log("ARRAY", restaurantArray);
  useEffect(() => {
    dispatch(allRestaurants());
    dispatch(getAllItems());
  }, [dispatch]);

  return (
    <>
      <h1>
        {restaurantArray?.map((restaurant) => (
          <Restaurant key={restaurant.id} restaurant={restaurant} />
        ))}
      </h1>
      <h2>
        {itemsArray?.map((item) => (
          <Item key={item.id} item={item} />
        ))}
      </h2>
    </>
  );
};

export default ShowRestaurant;
