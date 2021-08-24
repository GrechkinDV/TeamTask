import "./App.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import Login from "./screens/Login";
import Register from "./screens/Register";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/login">
          <Login />
        </Route>
        <Route path="/register">
          <Register></Register>
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
