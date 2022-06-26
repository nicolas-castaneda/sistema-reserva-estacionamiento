<template>
  <head>
    <h1 class="text-center font-weight-bold">Reserva de estacionamiento</h1>
    <p class="text-center small">
      Bienvenido, comienza tu reserva ahora y ahorra tiempo.
    </p>
  </head>

  <div class="container">
    <div class="row">
      <div class="descripción col-md-6 align-self-center">
        <blockquote class="blockquote" style="text-align: justify">
          Las playas de estacionamiento del país gestionan de manera manual los
          espacios de estacionamiento disponibles en cada playa. El sistema de
          reserva de estacionamiento permite al usuario realizar reservas
          remotas en estacionamientos y verificar el estado de cada aparcamiento
          del establecimiento. Además permite a las empresas una gestión
          automatizada de su estacionamiento.
        </blockquote>
      </div>
      <div class="imagenes col-md-6">
        <div>
          <img
            src="../assets/reserva_1.jpg"
            class="img-fluid"
            alt="Imagen 1"
            width="200px"
            height="200px"
          />
          <img
            src="../assets/reserva_2.jpg"
            class="img-fluid"
            alt="Imagen 2"
            width="250px"
            height="200x"
          />
        </div>
        <div>
          <img
            src="../assets/reserva_3.jpg"
            class="img-fluid"
            alt="Imagen 3"
            width="250px"
            height="150px"
          />
          <img
            src="../assets/reserva_4.jpg"
            class="img-fluid"
            alt="Imagen 4"
            width="200px"
            height="150px"
          />
        </div>
      </div>
    </div>
  </div>

  <footer class="footer">Página realizada por estudiantes de UTEC</footer>
</template>

<script>
export default {
  name: "app-home",
  data() {
    return {
      msg: "Bienvenido a la aplicación de reserva de estacionamiento",
    };
  },
};
</script>

<style scoped>
p {
  padding-bottom: 1.5em;
  display: center;
  margin: 0.9%;
}

h1 {
  font-size: 2.5rem;
  font-weight: bold;
  margin: 1em;
  display: center;
  margin: 0.9%;
}

footer {
  padding: 1em;
  font-size: small;
  text-align: center;
  margin-top: 10rem;
}

img {
  margin: 10px;
  border-radius: 5px;
  margin: 0.9%;
}
</style>
