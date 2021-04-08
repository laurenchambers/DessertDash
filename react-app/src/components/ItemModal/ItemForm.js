import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router";
import { updateItem } from "../../store/items";
import greyx from "../site-images/grey-x.png";
import "./ItemForm.css";

const ItemForm = ({ item, setShowModal, id }) => {
  const user = useSelector((state) => state.session.user);
  //   const restaurant = useSelector((state) => state.restaurant.currentRestaurant);

  const dispatch = useDispatch();
  const history = useHistory();
  const [quantity, setQuantity] = useState(1);

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
    setShowModal(false);
    setQuantity(1);
  };
  useEffect(() => {
    setQuantity();
  }, [setQuantity]);

  const price = parseFloat(item.price) * parseFloat(quantity);

  return (
    <div className="item-form-container">
      <div className="item-form-title">
        <p>{item.name}</p>
        <div onClick={() => setShowModal(false)}>
          <img className="form-close-img" src={greyx} alt="" />
        </div>
      </div>
      <div className="item-form-description-container">
        <div className="item-form-description-box">{item.description}</div>
        <div className="item-form-picture-container">
          <div className="item-form-picture">
            <img className="item-form-picture" src={item.image_src} alt="" />
          </div>
        </div>
      </div>
      <div className="item-form-button-container">
        <div className="item-form-button">
          <button onClick={subtractOne}>minus</button>
          <button onClick={addOne}>add</button>
          <button
            className="item-form-button"
            onClick={() => handleSubmit() && setShowModal(false)}
          >
            {console.log("q", quantity)}
            Add to cart ${price}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ItemForm;
