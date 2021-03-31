const GET_RESTAURANTS = "/restaurants/getRestaurants";

const getRestaurants = (restaurants) => ({
  type: GET_RESTAURANTS,
  payload: restaurants,
});

export const allRestaurants = () => async (dispatch) => {
  const response = await fetch("/api/restaurants/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const restaurant = await response.json();
    dispatch(getRestaurants(restaurant));
    return response;
  }
};

let initialState = {};
const restaurantReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_RESTAURANTS:
      newState = Object.assign({}, state);
      newState.allRestaurants = action.payload;
      return newState;
    default:
      return state;
  }
};

export default restaurantReducer;
