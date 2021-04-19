const GET_CARTS = "carts/getCarts";
const REMOVE = "carts/remove_cart";
const EDIT_ITEMS = "/items/edit";
const UPDATE_ITEMS = "/items/updateItems";

const getCarts = (cart) => ({
  type: GET_CARTS,
  payload: cart,
});

const remove = (cart) => ({
  type: REMOVE,
  payload: cart,
});

const edit = (cart) => ({
  type: EDIT_ITEMS,
  payload: cart,
});

const updateItems = (cart) => ({
  type: UPDATE_ITEMS,
  payload: cart,
});

export const getAllCarts = () => async (dispatch) => {
  const response = await fetch("/api/carts/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
    console.log("data", data.cart);
    dispatch(getCarts(data));
    return response;
  }
};

export const removeFromCart = (cartId) => async (dispatch) => {
  const response = await fetch(`/api/carts/${cartId}/delete/`);
  const deletedCart = await response.json();
  console.log("deleted", deletedCart);
  if (response.ok) {
    dispatch(remove(deletedCart.deleted));
  }
  return deletedCart;
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
    dispatch(edit(editedItem.edited));
    return editedItem;
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

let initialState = {};

const cartsReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_CARTS:
      // return { cart: [...state.cart, action.payload] };
      newState = Object.assign({}, state);
      console.log("action", action.payload);
      newState = action.payload;
      return newState;
    case REMOVE:
      console.log("load", action.payload);
      return {
        ...state,
        cart: state.cart.filter((cart) => cart.id !== action.payload),
      };
    case EDIT_ITEMS:
      console.log("state", ...state.cart);
      console.log("payload", action.payload.id);
      return {
        ...state,
        cart: [
          state.cart.filter((cart) => cart.id !== action.payload.id),
          action.payload,
        ],
      };
    case UPDATE_ITEMS:
      return { ...state, cart: [...state.cart, action.payload] };
    default:
      return state;
  }
};

export default cartsReducer;
