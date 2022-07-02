<template>
  <div class="container">
    <div class="descripcion">
      <br />
      <h1>Página no encontrada</h1>
      <br />
      <p>
        Es posible que haya escrito mal la dirección o que la página se haya
        movido
      </p>
      <p>
        Se le redirigirá a la página principal en 10 segundos. <br />Dele click
        en el siguiente enlace:
        <router-link to="/" class="nav-link">Home</router-link>
        en caso no se le rediriga automáticamente.
      </p>
    </div>
    <div class="imagenes col-sm-6">
      <div>
        <img src="../assets/errores.png" class="img-fluid" alt="Imagen 1" />
      </div>
    </div>
  </div>
</template>

<script>
function devolverInicio() {
  window.location.href = "/";
}
setInterval(devolverInicio, 10000);
</script>

<style scoped>
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

img {
  margin: 10px;
  border-radius: 5px;
  margin: 0.9%;
  border: 5px;
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
  margin: 10px;
  border-radius: 10px;
  border-color: black;
  margin: 0.9%;
}

.font-weight-bold {
  color: white;
}
</style>
