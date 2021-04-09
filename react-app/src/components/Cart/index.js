import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarts } from "../../store/cart";

const TheCart = ({ items }) => {
  const dispatch = useDispatch();

  const cartsArray = useSelector((state) => state.carts.cart);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(getAllCarts());
  }, [dispatch]);

  const cartUserId = cartsArray?.map((cart) => cart.user_id);

  console.log("i", cartUserId);

  return (
    <>
      <div>hi</div>
    </>
  );
};

export default TheCart;
