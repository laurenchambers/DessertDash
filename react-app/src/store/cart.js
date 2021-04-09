const GET_CARTS = "carts/getCarts";
const REMOVE = "carts/remove_cart";

const getCarts = (carts) => ({
  type: GET_CARTS,
  carts,
});

const remove = (cart) => ({
  type: REMOVE,
  cart,
});

export const getAllCarts = () => async (dispatch) => {
  const response = await fetch("/api/carts/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
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

let initialState = {};

const cartsReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_CARTS:
      newState = Object.assign({}, state);
      newState = action.carts;
      return newState;
    case REMOVE:
      newState = Object.assign({}, state);
      newState = newState.cart.filter((cart) => cart.id !== action.cart);
      return newState;
    default:
      return state;
  }
};

export default cartsReducer;
