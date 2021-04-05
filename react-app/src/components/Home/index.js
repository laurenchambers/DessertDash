import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllGenres } from "../../store/genres";
import { Link } from "react-router-dom";
import { allRestaurants } from "../../store/restaurants";
import "./Home.css";
import TopRestaurants from "../TopRestaurants";
import "./Home.css";

const HomePage = ({ restaurant, genre }) => {
  const dispatch = useDispatch();
  const genresArray = useSelector((state) => state?.genres?.allGenres?.genres);
  //   let eachGenre = genresArray?.map((genre) => {
  //     return genre.name;
  //   });
  //   console.log("each genre", eachGenre);
  //   console.log("genres array", genresArray);
  const restaurants = useSelector((state) => state?.restaurants?.restaurants);
  useEffect(() => {
    dispatch(getAllGenres());
    dispatch(allRestaurants());
  }, [dispatch]);

  return (
    <div className="landing-page-container">
      <div className="landing-genres-container">
        <div className="landing-genres-header">Categories</div>
        <div className="landing-genres-subheder">49 STORES NEARBY</div>
        <div className="genres-container">
          {genresArray?.map((genre) => (
            <div className="genres-name">
              <Link to={`/genres/${genre.id}`}>
              <img className="genres-image" src={genre.img_src} />
              </Link>
              <Link to={`/genres/${genre.id}`} className="each-genre-name">
                {genre.name}
              </Link>
            </div>
          ))}
        </div>
      </div>
      <div className="landing-restaurants-container">
        <div className="landing-restaurants-list">
          <div className="all-restaurants-container">
            {restaurants?.map((restaurant) => (
              <div className="entire-restaurant-container">
                <Link
                  to={`/restaurants/${restaurant.id}`}
                  className="image-container"
                >
                  <img
                    onClick={`/restaurants/${restaurant.id}`}
                    className="landing-rest-image"
                    src={restaurant?.items[0]?.image_src}
                  />
                  <img
                    onClick={`/restaurants/${restaurant.id}`}
                    className="landing-rest-image"
                    src={restaurant?.items[1]?.image_src}
                  />
                </Link>
                <Link
                  className="restaurant-info"
                  to={`/restaurants/${restaurant.id}`}
                >
                  <span className="each-restaurant-name">
                    {restaurant.name}
                  </span>
                  <span className="each-restaurant-rating">
                    {restaurant.rating}
                  </span>
                </Link>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
export default HomePage;
