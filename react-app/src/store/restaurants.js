const GET_RESTAURANTS = "/restaurants/getRestaurants";

const getRestaurants = (allRestaurants) => ({
  type: GET_RESTAURANTS,
  payload: allRestaurants,
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

let initialState = { restaurants: [] };
const restaurantReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_RESTAURANTS:
      newState = Object.assign({}, state);
      newState = action.payload;
      return newState;
    default:
      return state;
  }
};

export default restaurantReducer;
