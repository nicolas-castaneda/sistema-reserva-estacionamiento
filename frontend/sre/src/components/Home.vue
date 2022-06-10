<template>
    <h1 class="text-center font-weight-bold">Reserva de estacionamiento </h1>
    <p class="text-center small">Bienvenido, comienza tu reserva ahora y ahorra tiempo.</p>
    <div class="container row" >
        <div class="descripción col-sm-6 d-flex align-items-center">
            <blockquote class="blockquote " style="text-align:justify">
                
                    Las playas de estacionamiento del país gestionan de manera manual los espacios de estacionamiento disponibles en cada playa. El sistema de reserva de estacionamiento permite al usuario realizar reservas remotas en estacionamientos y verificar el estado de cada aparcamiento del establecimiento. Además permite a las empresas una gestión automatizada de su estacionamiento.
                
            </blockquote>
        </div>
    </div>  
   <div class="imagenes col-sm-6">
        <img src="../assets/reserva_1.png" class="img-fluid" alt="Imagen 1">
        <img src="../assets/reserva_2.png" class="img-fluid" alt="Imagen 2">
        <img src="../assets/reserva_3.png" class="img-fluid" alt="Imagen 3">
        <img src="../assets/reserva_4.png" class="img-fluid" alt="Imagen 4">
   </div>
   <footer class="footer">
        Página realizada por estudiantes de UTEC
   </footer>
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

body{
    background: black;

}
div{
    display: flex;
    flex-direction: column;
    color:white;
    margin:0.9%;
    font-family: georgia, 'Times New Roman', Times, serif;
}

.container{
    width: 50%;

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
    display: flex;
    flex-direction: row;
    margin:0.9%;
}
</style>