import { useHistory, Redirect } from "react-router-dom";
import React from "react";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { allRestaurants } from "../../store/restaurants";
import "./SearchBar.css";
import searchicon from "../site-images/search-icon.png";

const SearchBar = () => {
  //   const history = useHistory();
  const dispatch = useDispatch();
  const [input, setInput] = useState("");
  const [showResults, setShowResults] = useState([]);
  const restaurantArray = useSelector(
    (state) => state?.restaurants?.restaurants
  );

  const handleInput = (e) => {
    setInput(e.target.value);
    setShowResults(dynamicSearch(e.target.value));
    if (e.target.value === "") {
      setShowResults([]);
    }
  };

  const dynamicSearch = (value) => {
    return restaurantArray?.filter((restaurant) =>
      restaurant?.name?.toLowerCase().includes(value?.toLowerCase())
    );
  };

  useEffect(() => {
    dispatch(allRestaurants());
  }, [dispatch]);

  //   const showAllResults = () => {
  //     while (input) {
  //       return showResults;
  //     }
  //   };

  return (
    <div className="entire-search-container">
      <div className="search-container">
        <img src={searchicon} alt="" />
        <input
          type="search"
          value={input}
          onChange={handleInput}
          placeholder="Search"
          className="search-input"
        />
      </div>
      {showResults && (
        <div className="search-bar-original-results">
          {showResults.map((result) => (
            <div className="search-bar-results">
              {" "}
              <a
                className="search-bar-name-results"
                href={`/restaurants/${result.id}`}
              >
                {result.name}
              </a>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default SearchBar;
