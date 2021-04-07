import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router";
import { updateItem } from "../../store/items";
import greyx from "../site-images/grey-x.png";
import "./ItemForm.css";

const ItemForm = ({ item, setShowModal }) => {
  const user = useSelector((state) => state.session.user);
  //   const restaurant = useSelector((state) => state.restaurant.currentRestaurant);

  const dispatch = useDispatch();
  const history = useHistory();
  const [quantity, setQuantity] = useState(1);

  //   useEffect(() => {
  //     setQuantity;
  //   }, [quantity]);

  const handleSubmit = () => {
    const submission = {
      user_id: user.id,
      item_id: item.id,
      quantity,
    };
    console.log("submission", submission);
    dispatch(updateItem(submission));
  };

  return (
    <div className="item-form-container">
      <div className="item-form-title">
        <p>{item.name}</p>
        <div>
          <img
            className="form-close-img"
            onClick={() => setShowModal(false)}
            src={greyx}
            alt=""
          />
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
          <button className="item-form-button" onClick={handleSubmit}>
            Add to cart ${item.price}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ItemForm;
