const GET_GENRES = "genres/getGenres";
const GET_GENRE = "genres/getGenre";

const getGenres = (genres) => ({
  type: GET_GENRES,
  payload: genres,
});

const getGenre = (genre) => ({
  type: GET_GENRE,
  genre,
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

export const getOneGenre = (genreId) => async (dispatch) => {
  const response = await fetch(`/api/genres/${genreId}/`);
  if (response.ok) {
    const data = await response.json();
    dispatch(getGenre(data));
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
    case GET_GENRE:
      newState = Object.assign({}, state);
      newState = action.genre;
      return newState;
    default:
      return state;
  }
};

export default genresReducer;
