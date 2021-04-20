import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { useHistory } from "react-router";
import { updateItem } from "../../store/cart";
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
  const [preferences, setPreferences] = useState("");
  const [textLength, setTextLength] = useState(0);

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
      preferences,
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
    setTextLength(500 - preferences.length);
  }, [dispatch, cart, quantity, preferences, textLength]);

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
        <div className="item-form-price">${item.price.toFixed(2)}</div>
      </div>
      <div className="item-form-picture-container">
        <div className="item-form-picture">
          <img className="item-form-picture" src={item.image_src} alt="" />
        </div>
      </div>
      <div className="preferences-container">
        <div clasname="preferences-titles">
          <div className="preferences">
            <label className="extra-instructions">Extra Instructions</label>
            <span className="special-requests">List any special requests</span>
          </div>
        </div>
        <div>
          <textarea
            className="preferences-text-area"
            onChange={(e) => setPreferences(e.target.value)}
            placeholder="Add any special requests (e.g., food allergies, extra icing, etc.) and the store wil do its best to accomodate you."
            value={preferences}
          />
          <span className="preferences-character-count">
            {textLength} characters left
          </span>
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
            Add to cart - ${price.toFixed(2)}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ItemForm;
