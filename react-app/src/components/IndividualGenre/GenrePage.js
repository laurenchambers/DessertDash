import React from "react";

const GenrePage = ({ genre }) => {
  if (genre) {
    return (
      <div>
        <div>{genre.restaurants[0].image_src}</div>
        <div>{genre.name}</div>
      </div>
    );
  } else {
    return <></>;
  }
};

export default GenrePage;
