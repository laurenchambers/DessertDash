const GET_ITEMS = "/items/getItems";

const getItems = (items) => ({
  type: GET_ITEMS,
  payload: items,
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
  const { user_id, item_id, quantity } = cart;
  await fetch("/api/restaurants/add-item/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id,
      item_id,
      quantity,
    }),
  });
};

let initialState = {};
const itemsReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_ITEMS:
      newState = Object.assign({}, state);
      newState.allItems = action.payload;
      return newState;
    default:
      return state;
  }
};

export default itemsReducer;
