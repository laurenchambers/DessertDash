import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { editItem } from "../../store/cart";
import greyx from "../site-images/grey-x.png";
import plus from "../site-images/plus.png";
import minus from "../site-images/minus.png";
import "./ItemForm.css";
import cartsReducer, { getAllCarts } from "../../store/cart";

const EditItemForm = ({ cart, item, setShowModal }) => {
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();
  const { quantity, preferences } = cart;

  const [newQuantity, setNewQuantity] = useState(quantity ? quantity : null);
  const [newPreferences, setNewPreferences] = useState(
    preferences ? preferences : ""
  );
  const [textLength, setTextLength] = useState(
    preferences ? preferences.length : 0
  );

  const addOne = () => {
    setNewQuantity(newQuantity + 1);
  };

  const subtractOne = () => {
    setNewQuantity(newQuantity - 1);
  };

  const handleSubmit = () => {
    const submission = {
      id: cart.id,
      user_id: user.id,
      quantity: newQuantity,
      preferences: newPreferences,
    };
    console.log("submission", submission);
    dispatch(editItem(submission));
    dispatch(getAllCarts());
    setShowModal(false);
    // setCart(submission);
  };

  useEffect(() => {
    setNewQuantity(newQuantity);
    // setCart(cart);
    // dispatch(getAllCarts());
    setTextLength(500 - newPreferences.length);
  }, [dispatch, cart, quantity, newPreferences, textLength]);

  const price = parseFloat(cart.item_price) * parseFloat(newQuantity);

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
        <div className="item-form-title">{cart.item_name}</div>
        <div className="item-form-description">{cart.item_description}</div>
        <div className="item-form-price">${cart.item_price}</div>
      </div>
      <div className="item-form-picture-container">
        <div className="item-form-picture">
          <img className="item-form-picture" src={cart.item_image_src} alt="" />
        </div>
      </div>
      <div className="preferences-container">
        <div classname="preferences-titles">
          <div className="preferences">
            <label className="extra-instructions">Extra Instructions</label>
            <span className="special-requests">List any special requests</span>
          </div>
        </div>
        <div>
          <textarea
            className="preferences-text-area"
            onChange={(e) => setNewPreferences(e.target.value)}
            placeholder="Add any special requests (e.g., food allergies, extra icing, etc.) and the store wil do its best to accomodate you."
            value={newPreferences}
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
            disabled={newQuantity === 1}
          >
            <img className="form-minus" src={minus} alt="" />
          </button>
          <div className="item-form-current-quantity">{newQuantity}</div>
          <button className="form-add-minus-button" onClick={addOne}>
            <img className="form-plus" src={plus} alt="" />
          </button>
          <button
            className="item-form-button-add"
            onClick={() => handleSubmit() && setShowModal(false)}
          >
            {/* {console.log("q", quantity)} */}
            Update cart - ${price.toFixed(2)}
          </button>
        </div>
      </div>
    </div>
  );
};

export default EditItemForm;
