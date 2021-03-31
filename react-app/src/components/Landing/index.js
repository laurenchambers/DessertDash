import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllGenres } from "../../store/genres";
import { allRestaurants } from "../../store/restaurants";
import "./Landing.css";
import TopRestaurants from "../TopRestaurants";

const Landing = ({ restaurant, genre }) => {
  const dispatch = useDispatch();
  const genresArray = useSelector((state) => state?.genres?.allGenres?.genres);
  //   let eachGenre = genresArray?.map((genre) => {
  //     return genre.name;
  //   });
  //   console.log("each genre", eachGenre);
  //   console.log("genres array", genresArray);
  const restaurants = useSelector(
    (state) => state?.restaurants?.allRestaurants?.restaurants
  );

  useEffect(() => {
    dispatch(getAllGenres());
    dispatch(allRestaurants());
  }, [dispatch]);

  return (
    <div className="landing-page-container">
      <div className="landing-genres-container">
        <div className="landing-genres-header">Categories</div>
        <div className="genres-container"></div>
      </div>
      {genresArray?.map((genre) => (
        <div className="genres-name">
          <img className="genres-image" src={genre.img_src} />
          {genre.name}
        </div>
      ))}
      <div className="landing-restaurants-container">
        <div className="top-restaurants-container">
          {restaurants?.map((restaurant) => (
            <TopRestaurants key={restaurant.id} restaurant={restaurant} />
          ))}
        </div>
      </div>
    </div>
  );
};
export default Landing;
