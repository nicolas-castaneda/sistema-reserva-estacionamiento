<template>
  <html lang="en">
    <head>
      <br />
      <h1 class="font-weight-bold">S-R-E</h1>
      <br />
    </head>
    <body>
      <div class="container">
        <div class="descripcion">
          <br />
          <h1>Error interno del servidor</h1>
          <br />
          <p>
            Ha ocurrido un error inesperado en el servidor. Por favor revisa la
            dirección y prueba de nuevo.
          </p>
          <p>
            Se le redirigirá a la página principal en 10 segundos. <br />Dele
            click en el siguiente enlace:
            <router-link to="/" class="nav-link">Home</router-link>
            en caso no se le rediriga automáticamente.
          </p>
        </div>
        <div class="imagenes col-sm-6">
          <div>
            <img
              src="../assets/Error_500.jpg"
              class="img-fluid"
              alt="Imagen 1"
            />
          </div>
        </div>
      </div>

      <footer class="footer">Página realizada por estudiantes de UTEC</footer>
    </body>
  </html>
</template>

<script>
function devolverInicio() {
  window.location.href = "/";
}
setInterval(devolverInicio, 10000);
</script>

<style>
* {
  padding: 0;
  margin: 0;
}

div {
  color: white;
  margin: 0.9%;
}

p {
  padding-bottom: 1.5em;
  margin: 0.9%;
  text-align: justify;
}

h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin: 1em;
  margin: 0.9%;
}

footer {
  color: white;
  padding: 1em;
  font-size: small;
  text-align: center;
  margin-top: 10rem;
}

img {
  margin: 10px;
  border-radius: 5px;
  margin: 0.9%;
  border: 5px;
}

body {
  color: white;
  font-size: 1.2rem;
  line-height: 1.6em;
  margin: auto 0;
  padding: 0;
}

.header {
  background: #f5f5f5;
  padding: 1em;
  float: end;
  position: fixed;
  left: 0;
  top: 0;
  right: 0;
}

.container {
  display: flex;
  flex-direction: row;
  justify-items: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
  width: 60%;
}

.descripcion {
  color: black;
  margin: 10px;
  border-radius: 10px;
  border-color: black;
  margin: 0.9%;
}

.font-weight-bold {
  color: white;
}
</style>
