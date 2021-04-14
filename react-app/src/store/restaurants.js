const GET_RESTAURANTS = "/restaurants/getRestaurants";
const FEATURED = "restaurants/featured";

const getRestaurants = (allRestaurants) => ({
  type: GET_RESTAURANTS,
  payload: allRestaurants,
});

const getFeatured = (featured) => ({
  type: FEATURED,
  featured,
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

export const featuredRestaurants = () => async (dispatch) => {
  const response = await fetch("/api/restaurants/featured/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const featured = await response.json();
    dispatch(getFeatured(featured));
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
    case FEATURED:
      newState = Object.assign({}, state);
      newState.featured = action.featured;
      return newState;
    default:
      return state;
  }
};

export default restaurantReducer;
