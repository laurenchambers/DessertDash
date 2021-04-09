const GET_CARTS = "carts/getCarts";

const getCarts = (carts) => ({
  type: GET_CARTS,
  carts,
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

let initialState = {};

const cartsReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_CARTS:
      newState = Object.assign({}, state);
      newState = action.carts;
      return newState;
    default:
      return state;
  }
};

export default cartsReducer;
