import React, { useState } from "react";

import { signin } from "../plugins/api-client";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  async function submitLogin(e) {
    e.preventDefault();
    let resp = await signin({ email, password });
    console.log(resp);
  }

  return (
    <div>
      <h1>Вход</h1>
      <form onSubmit={submitLogin} className="d-flex flex-column w-50">
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          required
          placeholder="Е-мейл*"
        />
        <input
          value={password}
          required
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          placeholder="Пароль*"
        />
        <input type="submit" value="Войти" />
      </form>
    </div>
  );
}

export default Login;
