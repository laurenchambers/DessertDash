import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getAllGenres } from "../../store/genres";
import { Link } from "react-router-dom";

const GenreContainer = ({ genre }) => {
  const dispatch = useDispatch();
  const genresArray = useSelector((state) => state?.genres?.allGenres?.genres);
  const currentGenreRestaurantsArray = useSelector(
    (state) => state?.genres?.currentGenre?.restaurants
  );
  console.log("curr", currentGenreRestaurantsArray?.length);
  useEffect(() => {
    dispatch(getAllGenres());
    // setGetGenres(genresArray);
  }, [dispatch, genre]);
  return (
    <div>
      <div className="genres-genres-header">Categories</div>
      <div className="genres-genres-subheder">
        {currentGenreRestaurantsArray
          ? currentGenreRestaurantsArray?.length
          : 32}{" "}
        STORES NEARBY
      </div>
      <div className="genres-container">
        {genresArray?.map((genre) => (
          <div className="genres-name">
            <Link to={`/genres/${genre.id}`}>
              <img className="genres-image" src={genre.img_src} alt="" />
            </Link>
            <Link to={`/genres/${genre.id}`} className="each-genre-name">
              {genre.name}
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GenreContainer;
