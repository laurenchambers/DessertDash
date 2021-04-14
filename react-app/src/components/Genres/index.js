import React from "react";
import { GenreContainer } from "./GenreContainer";

const Genre = ({ genre }) => {
  if (genre) {
    return (
      <div>
        <GenreContainer />
        <div>
          <div className="restaurant-title">{genre.name}</div>
        </div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default Genre;
