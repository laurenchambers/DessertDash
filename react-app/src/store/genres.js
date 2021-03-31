const GET_GENRES = "genres/getGenres";

const getGenres = (genres) => ({
  type: GET_GENRES,
  payload: genres,
});

export const getAllGenres = () => async (dispatch) => {
  const response = await fetch("/api/genres/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(getGenres(data));
    return response;
  }
};

let initialState = {};

const genresReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_GENRES:
      newState = Object.assign({}, state);
      newState.allGenres = action.payload;
      return newState;
    default:
      return state;
  }
};

export default genresReducer;
