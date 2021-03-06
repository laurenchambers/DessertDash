import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch } from "react-redux";
import { authenticate } from "./store/session";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/NavBar/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import Landing from "./components/Landing";
import HomePage from "./components/Home";
import RestaurantDetail from "./components/IndividualRestaurant";
import GenreDetail from "./components/IndividualGenre";
import Checkout from "./components/Checkout";
import OrderComplete from "./components/OrderComplete";

function App() {
  const dispatch = useDispatch();
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    const func = async () => {
      const user = await dispatch(authenticate());
      if (!user.errors) {
        setAuthenticated(true);
      }
      setLoaded(true);
    };
    func();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar
        authenticated={authenticated}
        setAuthenticated={setAuthenticated}
      />
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/signup" exact={true}>
          <SignUpForm
            authenticated={authenticated}
            setAuthenticated={setAuthenticated}
          />
        </Route>
        <Route path="/" exact={true} authenticated={authenticated}>
          <Landing authenticated={authenticated} />
        </Route>
        <ProtectedRoute path="/home" exact={true} authenticated={authenticated}>
          <HomePage authenticated={authenticated} />
        </ProtectedRoute>
        <ProtectedRoute
          path="/restaurants/:id"
          exact={true}
          authenticated={authenticated}
        >
          <RestaurantDetail />
        </ProtectedRoute>
        <ProtectedRoute
          path="/genres/:id"
          exact={true}
          authenticated={authenticated}
        >
          <GenreDetail />
        </ProtectedRoute>
        <ProtectedRoute
          path="/checkout"
          exact={true}
          authenticated={authenticated}
        >
          <Checkout />
        </ProtectedRoute>
        <ProtectedRoute
          path="/order-complete"
          exact={true}
          authenticated={authenticated}
        >
          <OrderComplete />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
