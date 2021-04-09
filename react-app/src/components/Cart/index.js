import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getAllCarts } from "../../store/cart";

const TheCart = () => {
  const dispatch = useDispatch();

  const cart = useSelector((state) => state.carts.cart);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    dispatch(getAllCarts());
  }, [dispatch]);
  if (cart?.user_id === user.id) {
    return (
      <>
        <div>{cart.item}</div>
      </>
    );
  } else {
    return <></>;
  }
};

export default TheCart;
