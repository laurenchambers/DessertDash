import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { allRestaurants } from "../../store/restaurants";
import { getAllItems } from "../../store/items";
import Restaurant from "../Restaurant";

const ShowRestaurant = () => {
  const dispatch = useDispatch();
  const restaurantArray = useSelector(
    (state) => state?.restaurants?.restaurants
  );

  // const itemsArray = useSelector((state) => state?.items?.allItems?.items);

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
    </>
  );
};

export default ShowRestaurant;
