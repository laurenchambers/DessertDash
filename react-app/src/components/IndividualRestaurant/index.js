import React, { useEffect, useState } from "react";
import { Modal } from "../context/Modal";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getRestaurant } from "../../store/restaurant-detail";
import "./IndividualRestaurant.css";
import ItemForm from "../ItemModal/ItemForm";
import Footer from "../Footer";
import { Link } from "react-router-dom";
import {
  GoogleMap,
  withScriptjs,
  withGoogleMap,
  Marker,
} from "react-google-maps";

function Map() {
  const eachRestaurant = useSelector(
    (state) => state?.restaurant?.currentRestaurant
  );
  console.log("lat", eachRestaurant?.lat);
  return (
    <GoogleMap
      defaultZoom={14}
      defaultCenter={{ lat: 30.26498, lng: -97.746597 }}
    >
      <Marker
        position={{ lat: eachRestaurant?.lat, lng: eachRestaurant?.lng }}
      />
    </GoogleMap>
  );
}

const WrappedMap = withScriptjs(withGoogleMap(Map));

const RestaurantDetail = ({ cart, address }) => {
  const params = useParams();
  const dispatch = useDispatch();
  const [showModal, setShowModal] = useState(null);

  const eachRestaurant = useSelector(
    (state) => state?.restaurant?.currentRestaurant
  );
  const restaurantItems = eachRestaurant?.items;

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
                <WrappedMap
                  googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=AIzaSyB3lFaDSw-OH95uJunSPk6f8EUrZGvpcx8`}
                  loadingElement={<div style={{ height: "100%" }} />}
                  containerElement={<div style={{ height: "100%" }} />}
                  mapElement={<div style={{ height: "100%" }} />}
                />
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
                      {genre.name}
                    </Link>
                    // <span>{genre.name}</span>
                  ))}
                </div>
                <div className="rating-price-container">
                  <div className="store-header-rating">
                    {eachRestaurant?.rating} ⭐️
                  </div>
                  <div className="bullet-point-between">•</div>
                  <div className="store-header-price">
                    {eachRestaurant?.price}
                  </div>
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
        <div className="footer-container">
          <Footer />
        </div>
      </>
    </>
  );
};

export default RestaurantDetail;
