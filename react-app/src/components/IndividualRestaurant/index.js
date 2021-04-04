import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getRestaurant } from "../../store/restaurant-detail";
import "./IndividualRestaurant.css";

const RestaurantDetail = () => {
  const params = useParams();
  const dispatch = useDispatch();
  const restaurant = useSelector((state) => state.restaurants?.restaurant);

  useEffect(() => {
    dispatch(getRestaurant(params.id));
  });
  return <div></div>;
};

export default RestaurantDetail;
