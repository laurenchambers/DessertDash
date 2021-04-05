import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getRestaurant } from "../../store/restaurant-detail";
import "./IndividualRestaurant.css";
import Restaurant from "../Restaurant";

const RestaurantDetail = () => {
  const params = useParams();
  const dispatch = useDispatch();
  const eachRestaurant = useSelector(
    (state) => state?.restaurant?.currentRestaurant
  );
  const restaurantItems = eachRestaurant?.items;
  console.log("eac", eachRestaurant);

  useEffect(() => {
    dispatch(getRestaurant(params.id));
  }, [dispatch]);

  return (
    <div>
      <Restaurant restaurant={eachRestaurant} />
      <div>{restaurantItems?.map((item) => item.name)}</div>
    </div>
  );
};

export default RestaurantDetail;
