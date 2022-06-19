<template>
<html lang="en">
    <head>
    <h1 class="text-center font-weight-bold">Reserva de estacionamiento </h1>
    <p class="text-center small">Bienvenido, comienza tu reserva ahora y ahorra tiempo.</p>
    </head>
    <body>
    <div class="container row" >
        <div class="descripción col-sm-6 d-flex align-items-center" >
            <blockquote class="blockquote " style="text-align:justify">

                    Las playas de estacionamiento del país gestionan de manera manual los espacios de estacionamiento disponibles en cada playa. El sistema de reserva de estacionamiento permite al usuario realizar reservas remotas en estacionamientos y verificar el estado de cada aparcamiento del establecimiento. Además permite a las empresas una gestión automatizada de su estacionamiento.
            </blockquote>
        </div>
        <div class="imagenes col-sm-6" >
          <div>
             <img src="../assets/reserva_1.jpg" class="img-fluid" alt="Imagen 1" width="200px" height="200px">
             <img src="../assets/reserva_2.jpg" class="img-fluid" alt="Imagen 2" width="250px" height="200x">
          </div>
          <div>
              <img src="../assets/reserva_3.jpg" class="img-fluid" alt="Imagen 3" width="250px" height="150px" >
              <img src="../assets/reserva_4.jpg" class="img-fluid" alt="Imagen 4" width="200px" height="150px">
          </div>
        </div>

    </div>


   <footer class="footer">
        Página realizada por estudiantes de UTEC
   </footer>
   </body>
</html>
</template>

<script>
export default {
  name: 'app-home',
  data(){
    return {
        msg: 'Bienvenido a la aplicación de reserva de estacionamiento'
    }
  }
}
</script>

<style >
*{
    padding: 0;
    margin:0;
}

div{
    color:white;
    margin:0.9%;
    font-family: georgia, 'Times New Roman', Times, serif;
}

p {
    color:white;
    padding-bottom: 1.5em;
    display: center;
    margin:0.9%;
}

h1{
    color:white;
    font-size: 2.5rem;
    font-weight: bold;
    margin: 1em;
    display: center;
    margin:0.9%;
    font-family: georgia, 'Times New Roman', Times, serif;


}

footer{
    color:white;
    padding: 1em;
    font-size: small;
    text-align: center;
    margin-top: 10rem;
}

img{
    margin:10px;
    border-radius: 5px;
    margin:0.9%;
}

body{
    background: black;
    font-family: georgia, 'Times New Roman', Times, serif;
    color:white;
    font-size: 1.2rem;
    line-height: 1.6em;
    margin: 0;
}

.header{
    background: #f5f5f5;
    padding: 1em;
    float: end;
    position: fixed;
    left: 0;
    top:0;
    right: 0;
}

.container{
    display: flex;
    flex-direction: row;
}
</style>
