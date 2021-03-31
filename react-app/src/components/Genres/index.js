import React from "react";

const Genre = ({ genre }) => {
  if (genre) {
    return (
      <div>
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
