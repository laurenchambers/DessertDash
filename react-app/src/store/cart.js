const GET_CARTS = "carts/getCarts";
const REMOVE = "carts/remove_cart";

const getCarts = (cart) => ({
  type: GET_CARTS,
  payload: cart,
});

const remove = (cart) => ({
  type: REMOVE,
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
      return {
        ...state,
        cart: state.cart.filter((cart) => cart.id !== action.payload),
      };
    default:
      return state;
  }
};

export default cartsReducer;
