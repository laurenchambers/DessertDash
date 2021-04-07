import React, { useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getOneGenre } from "../../store/genres";

import "./IndividualGenre.css";
// import Genre from "../Genres";
import GenrePage from "./GenrePage";
import Footer from "../Footer";
// import RestaurantTwoImages from "../Restaurant/";

const GenreDetail = () => {
  const params = useParams();
  const dispatch = useDispatch();
  const genre = useSelector((state) => {
    return state?.genres?.currentGenre;
  });
  const restaurantArray = useSelector((state) => {
    return state?.genres?.currentGenre?.restaurants;
  });

  useEffect(() => {
    dispatch(getOneGenre(params.id));
  }, [dispatch, params]);
  return (
    <>
      <div className="genre-page-container">
        <div className="genre-twoboxes-container">
          <div className="genre-box-left">
            <GenrePage key={genre} genre={genre} />
          </div>
          <div className="genre-side-container">
            <div className="genre-side-images">
              {restaurantArray?.map((restaurant) => (
                <>
                  <img
                    className="genre-image-one"
                    src={restaurant?.items[1]?.image_src}
                    alt=""
                  />
                  <img
                    className="genre-image-two"
                    src={restaurant?.items[2]?.image_src}
                    alt=""
                  />
                </>
              ))}
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

export default GenreDetail;
