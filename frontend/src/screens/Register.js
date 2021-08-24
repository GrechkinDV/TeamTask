import React, { useState } from "react";

import { signup } from "../plugins/api-client";

function Register() {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [institution, setInstitution] = useState("");
  const [password, setPassword] = useState("");

  async function submitRegister(e) {
    e.preventDefault();
    console.log(email);
    console.log(name);
    console.log(institution);
    console.log(password);
    let resp = await signup({ email, name, institution, password });
    console.log(resp);
  }

  return (
    <div>
      <h1>Регистрация</h1>
      <form onSubmit={submitRegister} className="d-flex flex-column w-50">
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          required
          placeholder="Е-мейл*"
        />
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          type="text"
          maxLength="50"
          placeholder="Никнейм"
        />
        <input
          value={institution}
          onChange={(e) => setInstitution(e.target.value)}
          type="text"
          maxLength="500"
          placeholder="Учебное заведение"
        />
        <input
          value={password}
          required
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          placeholder="Пароль*"
        />
        <input type="submit" value="Зарегестрироваться" />
      </form>
    </div>
  );
}

export default Register;
