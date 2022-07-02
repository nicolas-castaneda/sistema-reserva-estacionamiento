export async function getReservas(usuario, token) {
  let respuesta = await fetch("http://127.0.0.1:5000/reservas" + usuario, {
    method: "GET",
    headers: {
      Authorization: "Bearer " + token,
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (responseJson) {
      return responseJson;
    })
    .catch((error) => console.log(error));
  return respuesta;
}
