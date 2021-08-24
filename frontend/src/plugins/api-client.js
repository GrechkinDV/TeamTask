import axios from "axios";

export function signin(payload) {
  return callApi("token/", {}, payload, false, "POST");
}

export function signup(payload) {
  return callApi("accounts/", {}, payload, false, "POST");
}

function callApi(
  path,
  params = {},
  data = {},
  authenticated = false,
  method = "GET"
) {
  let headers = {};
  //   if (authenticated === true) {
  //     headers = {
  //       Authorization: this.state.tokenType + " " + this.state.auth_token,
  //     };
  //   }
  return axios.request({
    baseURL: "http://localhost:8000/api/0.1/",
    url: path,
    data,
    method,
    headers,
    params,
  });
}
