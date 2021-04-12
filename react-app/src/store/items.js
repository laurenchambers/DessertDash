const GET_ITEMS = "/items/getItems";
const UPDATE_ITEMS = "/items/updateItems";

const getItems = (items) => ({
  type: GET_ITEMS,
  payload: items,
});

const updateItems = (cart) => ({
  type: UPDATE_ITEMS,
  cart,
});

export const getAllItems = () => async (dispatch) => {
  const response = await fetch("/api/items/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(getItems(data));
    return response;
  }
};

export const updateItem = (cart) => async (dispatch) => {
  const { id, user_id, item_id, quantity } = cart;
  const response = await fetch("/api/restaurants/add-item/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id,
      user_id,
      item_id,
      quantity,
    }),
  });
  const data = await response.json();
  if (response.ok) {
    dispatch(updateItems(data));
    return response;
  }
};

let initialState = {};
const itemsReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_ITEMS:
      newState = Object.assign({}, state);
      newState.allItems = action.payload;
      return newState;
    case UPDATE_ITEMS:
      newState = Object.assign({}, state);
      newState = action.cart;
      return newState;
    default:
      return state;
  }
};

export default itemsReducer;
