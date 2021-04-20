const GET_USER = "/session/get_user";
const REMOVE_USER = "/session/remove_user";
const CREATE_USER = "/session/create_user";
const EDIT_USER = "/user/edit";

const edit = (user) => ({
  type: EDIT_USER,
  payload: user,
});

const getUser = (user) => ({
  type: GET_USER,
  user,
});

const removeUser = () => ({
  type: REMOVE_USER,
});

const createUser = (user) => ({
  type: CREATE_USER,
  user,
});

export const authenticate = () => async (dispatch) => {
  const response = await fetch("/api/auth/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  const user = await response.json();
  if (response.ok) {
    dispatch(getUser(user));
  }
  return user;
};

export const login = (email, password) => async (dispatch) => {
  const response = await fetch("/api/auth/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });
  let user = await response.json();
  if (!user.errors) {
    dispatch(getUser(user));
    return user;
  }
  return user;
};

export const logout = () => async (dispatch) => {
  const response = await fetch("/api/auth/logout/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  await response.json();
  dispatch(removeUser());
  return response;
};

export const signUp = (first_name, last_name, email, password) => async (
  dispatch
) => {
  const response = await fetch("/api/auth/signup/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      first_name,
      last_name,
      email,
      password,
    }),
  });
  if (response.ok) {
    let data = await response.json();
    dispatch(createUser(data));
    return response;
  }
};

export const editUser = (user) => async (dispatch) => {
  const { id, address, lat, lng } = user;
  const response = await fetch(`/api/users/edit-user/${id}/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id,
      address,
      lat,
      lng,
    }),
  });
  const editedUser = await response.json();
  if (response.ok) {
    dispatch(edit(editedUser));
    return editedUser;
  }
};

let initialState = { user: null };

const sessionReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case GET_USER:
      return { ...state, user: action.user };
    case CREATE_USER:
      newState = Object.assign({}, state);
      newState.user = action.user;
      return newState;
    case REMOVE_USER:
      newState = Object.assign({}, state);
      newState.user = null;
      return newState;
    case EDIT_USER:
      return {
        ...state,
        user: action.payload,
      };
    default:
      return state;
  }
};

export default sessionReducer;
