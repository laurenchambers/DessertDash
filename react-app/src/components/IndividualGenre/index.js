import React, { useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getOneGenre, getAllGenres } from "../../store/genres";
import "./IndividualGenre.css";
import GenrePage from "./GenrePage";
import Footer from "../Footer";

const GenreDetail = () => {
  const params = useParams();
  const dispatch = useDispatch();
  const genre = useSelector((state) => {
    return state?.genres?.currentGenre;
  });
  const genresArray = useSelector((state) => state?.genres?.allGenres?.genres);
  console.log("genresarray", genresArray);
  const restaurantArray = useSelector((state) => {
    return state?.genres?.currentGenre?.restaurants;
  });

  useEffect(() => {
    dispatch(getOneGenre(params.id));
    dispatch(getAllGenres());
  }, [dispatch, params]);
  return (
    <>
      <div className="genre-page-container">
        <div className="genre-twoboxes-container">
          <div className="genre-box-left">
            <GenrePage key={genre} genre={genre} />
          </div>
          <div className="genre-side-container">
            <div className="all-restaurants-container">
              {restaurantArray?.map((restaurant) => (
                <div className="entire-restaurant-container">
                  <Link
                    to={`/restaurants/${restaurant.id}`}
                    className="image-container"
                  >
                    <img
                      onClick={`/restaurants/${restaurant.id}`}
                      className="landing-rest-image"
                      src={restaurant?.items[0]?.image_src}
                      alt=""
                    />
                    <img
                      onClick={`/restaurants/${restaurant.id}`}
                      className="landing-rest-image"
                      src={restaurant?.items[1]?.image_src}
                      alt=""
                    />
                  </Link>
                  <Link
                    className="restaurant-info"
                    to={`/restaurants/${restaurant.id}`}
                  >
                    <div className="each-restaurant-name">
                      {restaurant.name}
                    </div>
                    {/* <span className="each-restaurant-rating">
                      {restaurant.rating}
                    </span> */}
                  </Link>
                </div>
              ))}
            </div>

            {/* <div className="genre-side-images">
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
            </div> */}
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
