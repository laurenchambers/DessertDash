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
