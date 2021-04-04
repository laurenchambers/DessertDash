const LOAD = "restaurant/load";

const load = (restaurant) => ({
  type: LOAD,
  restaurant,
});

export const getRestaurant = (restaurantId) => async (dispatch) => {
  const response = await fetch(`/api/restaurants/${restaurantId}/`);

  if (response.ok) {
    const restaurant = await response.json();
    dispatch(load(restaurant));
    return response;
  }
};

let initialState = {};

const restaurantDetailReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case LOAD:
      newState = Object.assign({}, state);
      newState = action.restaurant;
      return newState;
    default:
      return state;
  }
};

export default restaurantDetailReducer;
