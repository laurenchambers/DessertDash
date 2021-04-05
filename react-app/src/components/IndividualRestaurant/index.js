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
  console.log("eac", restaurantItems);

  useEffect(() => {
    dispatch(getRestaurant(params.id));
  }, [dispatch]);

  return (
    <div className="store-info-container">
      <header>
        <div className="store-header-container">
          <div className="store-header-information">
            <div className="store-header-name">{eachRestaurant?.name}</div>
            <div className="store-header-dashpass"></div>
            <div className="store-header-hours">{eachRestaurant?.hours}</div>
            <div className="store-header-genres">
              {eachRestaurant?.genres?.map((genre) => (
                <span>{genre.name}</span>
              ))}
            </div>
            <div className="rating-price-container">
              <div className="store-header-rating">
                {eachRestaurant?.rating} ⭐️
              </div>
              <div className="bullet-point-between">•</div>
              <div className="store-header-price">{eachRestaurant?.price}</div>
            </div>
          </div>
        </div>
        <div className="delivery-header-info">DEVLIERY INFO</div>
      </header>
      <div className="menu-container">

        <div className="restaurant-menu-items">
          {restaurantItems?.map((item) => (
            <>
              <span>
                <h1>{item.name}</h1>
                <h2>{item.description}</h2>
                <p>${item.price}</p>
                <img
                  className="restaurant-menu-item-img"
                  src={item.image_src}
                />
              </span>
            </>
          ))}
        </div>
      </div>
    </div>
  );
};

export default RestaurantDetail;
