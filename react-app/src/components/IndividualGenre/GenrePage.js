import React from "react";
import GenreContainer from "../Genres/GenreContainer";
import "./GenrePage.css";

const GenrePage = ({ genre }) => {
  if (genre) {
    return (
      <>
        <div className="genre-page-title-name">{genre.name}</div>
        <GenreContainer key={genre} genre={genre} />
      </>
    );
  } else {
    return <></>;
  }
};

export default GenrePage;
