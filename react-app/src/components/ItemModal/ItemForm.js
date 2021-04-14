import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { useHistory } from "react-router";
import { updateItem } from "../../store/items";
import greyx from "../site-images/grey-x.png";
import plus from "../site-images/plus.png";
import minus from "../site-images/minus.png";
import "./ItemForm.css";
import { getAllCarts } from "../../store/cart";

const ItemForm = ({ item, setShowModal }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const [quantity, setQuantity] = useState(1);
  const [cart, setCart] = useState(null);

  const addOne = () => {
    setQuantity(quantity + 1);
  };

  const subtractOne = () => {
    setQuantity(quantity - 1);
  };

  const handleSubmit = () => {
    const submission = {
      user_id: user.id,
      item_id: item.id,
      quantity,
    };
    console.log("submission", submission);
    dispatch(updateItem(submission));
    dispatch(getAllCarts());
    setShowModal(false);
    setQuantity(1);
    setCart(submission);
  };
  useEffect(() => {
    setQuantity(quantity);
    setCart(cart);
    dispatch(getAllCarts());
  }, [dispatch, cart, quantity]);

  const price = parseFloat(item.price) * parseFloat(quantity);

  return (
    <div className="item-form-container">
      <div className="item-form-title">
        <button
          className="item-form-x-button"
          onClick={() => setShowModal(false)}
        >
          <img className="form-close-img" src={greyx} alt="" />
        </button>
      </div>
      <div>
        <div className="item-form-title">{item.name}</div>
        <div className="item-form-description">{item.description}</div>
        <div className="item-form-price">${item.price}.00</div>
      </div>
      <div className="item-form-picture-container">
        <div className="item-form-picture">
          <img className="item-form-picture" src={item.image_src} alt="" />
        </div>
      </div>

      <div className="item-form-button-container">
        <div className="item-form-button">
          <button
            className="form-add-minus-button"
            onClick={subtractOne}
            disabled={quantity === 1}
          >
            <img className="form-minus" src={minus} alt="" />
          </button>
          <div className="item-form-current-quantity">{quantity}</div>
          <button className="form-add-minus-button" onClick={addOne}>
            <img className="form-plus" src={plus} alt="" />
          </button>
          <button
            className="item-form-button-add"
            onClick={() => handleSubmit() && setShowModal(false)}
          >
            {/* {console.log("q", quantity)} */}
            Add to cart - ${price}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ItemForm;
