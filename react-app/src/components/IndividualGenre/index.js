import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getOneGenre } from "../../store/genres";
import "./IndividualGenre.css";
import Genre from "../Genres";
import GenrePage from "./GenrePage";

const GenreDetail = () => {
  const params = useParams();
  const dispatch = useDispatch();
  const genre = useSelector((state) => {
    return state?.genres?.currentGenre;
  });
  const restaurant = useSelector((state) => {
    return state?.genres?.currentGenre?.restaurants;
  });

  useEffect(() => {
    dispatch(getOneGenre(params.id));
  }, [params]);
  return (
    <div>
      <h1>GENRE PAGE</h1>
      replace this below with individual genre component
      <GenrePage genre={genre} />
    </div>
  );
};

export default GenreDetail;
