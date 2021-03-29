import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { BrowserRouter } from "react-router-dom";
import "./index.css";
import App from "./App";
import configureStore from "./store";
// import * as sessionActions from "./store/session";

const store = configureStore();

if (process.env.NODE_ENV !== "production") {
  window.store = store;
  // window.sessionActions = sessionActions;
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
