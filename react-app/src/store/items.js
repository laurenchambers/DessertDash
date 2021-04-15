const GET_ITEMS = "/items/getItems";
const UPDATE_ITEMS = "/items/updateItems";
const EDIT_ITEMS = "/items/edit";

const getItems = (items) => ({
  type: GET_ITEMS,
  payload: items,
});

const updateItems = (cart) => ({
  type: UPDATE_ITEMS,
  cart,
});

const edit = (cart) => ({
  type: EDIT_ITEMS,
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
  const { id, user_id, item_id, quantity, preferences } = cart;
  const response = await fetch("/api/restaurants/add-item/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id,
      user_id,
      item_id,
      quantity,
      preferences,
    }),
  });
  const data = await response.json();
  if (response.ok) {
    dispatch(updateItems(data));
    return response;
  }
};

export const editItem = (cart) => async (dispatch) => {
  const { id, user_id, quantity, preferences } = cart;
  const response = await fetch(`/api/restaurants/edit-item/${id}/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id,
      user_id,
      quantity,
      preferences,
    }),
  });
  const editedItem = await response.json();
  if (response.ok) {
    dispatch(edit(editedItem));
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
    case EDIT_ITEMS:
      newState = Object.assign({}, state);
      newState.cart = newState?.cart?.filter((cart) => cart.id === action.cart);
      return newState;
    default:
      return state;
  }
};

export default itemsReducer;
