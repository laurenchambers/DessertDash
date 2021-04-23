import React, { useEffect, useState } from "react";
import { Modal } from "../context/Modal";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getRestaurant } from "../../store/restaurant-detail";
import "./IndividualRestaurant.css";
import ItemForm from "../ItemModal/ItemForm";
import Footer from "../Footer";
import { Link } from "react-router-dom";
import TheCart from "../Cart";
import greystar from "../site-images/grey-star.png";
import { getDistance } from "geolib";

const RestaurantDetail = ({ cart, address }) => {
  const user = useSelector((state) => state?.session?.user);
  const params = useParams();
  const dispatch = useDispatch();
  const [showModal, setShowModal] = useState(null);

  const eachRestaurant = useSelector(
    (state) => state?.restaurant?.currentRestaurant
  );
  const restaurantItems = eachRestaurant?.items;

  const userLat = user?.lat;
  const userLng = user?.lng;
  const restaurantLat = eachRestaurant?.lat;
  const restaurantLng = eachRestaurant?.lng;
  console.log("user", parseFloat(userLat));

  const distanceMeters = getDistance(
    { latitude: parseFloat(userLat), longitude: parseFloat(userLng) },
    {
      latitude: parseFloat(restaurantLat),
      longitude: parseFloat(restaurantLng),
    },
    1
  );
  const distanceMiles = distanceMeters * 0.000621371;

  useEffect(() => {
    dispatch(getRestaurant(params.id));
  }, [params, dispatch, cart]);

  return (
    <>
      <>
        <div className="store-info-container">
          <header>
            <div className="store-header-container">
              <div className="store-header-information">
                <div className="store-header-name">{eachRestaurant?.name}</div>
                <div className="store-header-dashpass"></div>
                <div className="store-header-hours">
                  {eachRestaurant?.hours}
                </div>
                <div className="store-header-genres">
                  {eachRestaurant?.genres?.map((genre) => (
                    <Link
                      to={`/genres/${genre.id}`}
                      className="store-header-genres"
                    >
                      {genre.name} •
                    </Link>
                    // <span>{genre.name}</span>
                  ))}
                </div>
                <div className="rating-price-container">
                  <div className="store-header-rating">
                    {eachRestaurant?.rating}{" "}
                    <img className="grey-star" src={greystar} alt="" />
                  </div>
                  <div className="bullet-point-between">•</div>
                  <div className="store-distance">
                    {distanceMiles.toFixed(1)} mi
                  </div>
                  <div className="bullet-point-between">•</div>
                  <div className="store-header-price">
                    {eachRestaurant?.price}
                  </div>
                </div>
              </div>
            </div>
            <div className="delivery-header-info-container">
              <div className="delivery-fee-container">
                <div className="delivery-fee-amount-dollar">$2.99</div>
                <div className="delivery-fee-amount-name">delivery fee</div>
              </div>
              <div className="line-between"></div>
              <div className="delivery-time-container">
                <div className="delivery-amount-time">25-35</div>
                <div className="delivery-amount-time-name">minutes</div>
              </div>
            </div>
          </header>
          <div className="menu-container">
            <div className="restaurant-menu-items">
              {restaurantItems?.map((item) => (
                <>
                  <span>
                    <div className="restaurant-menu-items-container">
                      <div
                        className="restaurant-menu-items-name"
                        onClick={() => setShowModal(item.id)}
                      >
                        {item.name}
                      </div>
                      <div className="restaurant-menu-items-description">
                        {item.description}
                      </div>
                      <div className="restaurant-menu-items-price">
                        ${item.price.toFixed(2)}
                      </div>
                    </div>
                    {item.id === showModal && (
                      <Modal onClose={() => setShowModal(null)}>
                        <ItemForm
                          key={item.id}
                          item={item}
                          setShowModal={setShowModal}
                        />
                      </Modal>
                    )}
                    <img
                      className="restaurant-menu-item-img"
                      src={item.image_src}
                      alt=""
                    />
                  </span>
                </>
              ))}
            </div>
          </div>
        </div>
        <div>
          <TheCart />
        </div>
        <div className="footer-container">
          <Footer />
        </div>
      </>
    </>
  );
};

export default RestaurantDetail;
