import React, { useState, useEffect } from "react";
import { Redirect, useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { featuredRestaurants } from "../../store/restaurants";
import "./Landing.css";
import { Link } from "react-router-dom";
import dessertdash_logo from "../site-images/desssertdash-logo.jpg";
import brownie from "../site-images/brownie.jpg";
import donut from "../site-images/donut.jpg";
import Footer from "../Footer";

const Landing = ({ restaurant, genre, authenticated }) => {
  const dispatch = useDispatch();
  const featuredArray = useSelector(
    (state) => state?.restaurants?.featured?.restaurants
  );

  useEffect(() => {
    dispatch(featuredRestaurants());
  }, [dispatch]);

  const history = useHistory();
  if (authenticated) {
    return <Redirect to="/home" />;
  }
  return (
    <>
      <div className="landing-all-container">
        <div className="landing-top-container">
          <div className="landing-button-container">
            <div
              onClick={() => history.push("/login")}
              className="landing-button-div-login"
            >
              Sign In
            </div>
            <div
              onClick={() => history.push("/signup")}
              className="landing-button-div-signup"
            >
              Sign Up
            </div>
            {/* <div className="landing-logo">
              <img className="logo" src={dessertdash_logo} alt="" />
            </div> */}
            <div className="landing-site-title">DESSERTDASH</div>
          </div>

          <div className="landing-subtitle">
            <div>Restaurants and more, </div>
            <div>delivered to your door</div>
          </div>
        </div>
        <div className="landing-lower-section">
          <div className="landing-second-section-message">
            <div>Local Favorites</div></div>
            <div className="featured-restaurants-container">
              {featuredArray?.map((featured) => (
                <div className="featured-restaurant-list">
                  <Link
                    to={`/restaurants/${featured.id}`}
                    className="featured-image-container"
                  >
                    <img
                      onClick={`/restaurants/${featured.id}`}
                      className="featured-rest-image"
                      src={featured?.items[2]?.image_src}
                      alt=""
                    />
                  </Link>
                  <Link
                    className="restaurant-info"
                    to={`/restaurants/${featured.id}`}
                  >
                    <div className="featured-restaurant-name">
                      {featured.name}
                    </div>
                  </Link>
                </div>
              ))}
            </div>

        </div>
        <div className="landing-third-container">
          <div className="landing-lower-section">
            <div className="landing-third-section-message">
              <div className="landing-third-section-header">It’s all here.</div>
              <div className="third-secion-sub-message">
                Discover local, on-demand dessert delivery from restaurants,
                nearby grocery and convenience stores, and more... yum!
              </div>
              <img className="donut-image" src={donut} alt="" />
            </div>
          </div>
        </div>
        <div className="landing-fourth-container">
          <div className="landing-fourth-section">
            <img className="brownie-image" src={brownie} alt="" />
            <div className="landing-fourth-section-message">
              Every Flavor Welcome
            </div>
            <div className="fourth-section-sub-message">
              From your neighborhood cupcake spot to the ice cream you crave,
              choose from tons of local and national favorites to satisfy your
              sweet tooth.
            </div>
          </div>
        </div>
      </div>
      <div>{<br></br>}</div>
      <div className="footer-container">
        <Footer />
      </div>
    </>
  );
};
export default Landing;
