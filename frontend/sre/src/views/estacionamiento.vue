<template>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">         
        <title>Estacionamiento</title>
    </head>
    <body class="align-items-center">
        <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
            <symbol id="exclamation-triangle-fill" fill="currentColor" viewBox="0 0 16 16">
                <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
            </symbol>
        </svg>
        <main role="main" class="container m-auto row justify-content-center">
            <div class="pantalla min-vh-100">
                <div class="grupoEstacionamiento">
                    <div v-for="(estacionamiento, index) in estacionamientos" :key="index" class="elementoEstacionamiento"> 
                        <button v-bind:class="['lugarEstacionamiento', estacionamiento.estadoRegistro]" v-bind:data-bs-toggle="[estacionamiento.estadoRegistro=='DIS' ? 'modal':'']" type="button" data-bs-target="#modal-escoger" v-on:click="iniciarFormulario(estacionamiento.lugar)">
                            {{estacionamiento.lugar}}
                        </button>
                    </div>
                </div>
                <div class="modal fade" id="modal-escoger">
                    <div class="modal-dialog">
                        <div class="modal-content">
                                                    
                            <form id="formularioReserva" class="modal-body">
                                <div class="mb-3">
                                    <label for="lugar" class="col-form-label">Lugar de estacionamiento</label>
                                    <input class="form-control" type="text" :placeholder="lugarEstacionamientoFormulario" id="lugar" :value="lugarEstacionamientoFormulario" readonly required>
                                </div>
                                <div class="mb-3 d-flex">
                                    <div class="m-auto">
                                        <label for="fechaInicio" class="col-form-label">Fecha inicio</label>
                                        <input v-model="inicioReservaFormulario" type="datetime-local" class="form-control" id="fechaInicio" required>
                                    </div>
                                    <div class="m-auto">
                                        <label for="fechaFin" class="col-form-label">Fecha final</label>
                                        <input v-model="finReservaFormulario" type="datetime-local" class="form-control" id="fechaFin" required>
                                    </div>
                                </div>

                                <div v-if="cantidadAutos>0" id="autosDisponibles">
                                    <button v-if="alternarOpcionAutos" id="cambiarAnadirDisponible" type="button" @click="alternarOpcionAutos = !alternarOpcionAutos">Carros disponibles</button>
                                    <button v-else id="cambiarAnadirDisponible" type="button" @click="alternarOpcionAutos = !alternarOpcionAutos">Añadir auto</button>
                                    <div v-if="alternarOpcionAutos">
                                        <div class="mb-3" id="contenedorPlaca">
                                            <label for="placa" class="col-form-label">Placa</label>
                                            <input type="text" v-model="placaFormulario" class="form-control" id="placa" required>
                                        </div>
                                        <div class="mb-3" id="contenedorMarca">
                                            <label for="marca" class="col-form-label">Marca</label>
                                            <input type="text" v-model="marcaFormulario" class="form-control" id="marca" required>
                                        </div>
                                        <div class="mb-3" id="contenedorModelo">
                                            <label for="modelo" class="col-form-label">Modelo</label>
                                            <input type="text" v-model="modeloFormulario" class="form-control" id="modelo" required>
                                        </div>
                                        <div class="mb-3" id="contenedorColor">
                                            <label for="color" class="col-form-label">Color</label>
                                            <input type="text" v-model="colorFormulario" class="form-control" id="color" required>
                                        </div>
                                    </div>
                                    <div v-else>
                                        <div id="contenedorAutosDisponibles" class="mb-3">
                                            <select class="form-select" id="seleccionarAutosDisponibles" required>
                                                <option value=null>Elige un auto</option>
                                                <!-- Aqui van los autos -->
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div v-else id="autosDisponibles">
                                    <div class="mb-3" id="contenedorPlaca">
                                        <label for="placa" class="col-form-label">Placa</label>
                                        <input type="text" v-model="placaFormulario" class="form-control" id="placa" required>
                                    </div>
                                    <div class="mb-3" id="contenedorMarca">
                                        <label for="marca" class="col-form-label">Marca</label>
                                        <input type="text" v-model="marcaFormulario" class="form-control" id="marca" required>
                                    </div>
                                    <div class="mb-3" id="contenedorModelo">
                                        <label for="modelo" class="col-form-label">Modelo</label>
                                        <input type="text" v-model="modeloFormulario" class="form-control" id="modelo" required>
                                    </div>
                                    <div class="mb-3" id="contenedorColor">
                                        <label for="color" class="col-form-label">Color</label>
                                        <input type="text" v-model="colorFormulario" class="form-control" id="color" required>
                                    </div>
                                </div>

                                
                                <div class="mb-3">
                                    <label for="costoReserva" class="col-form-label">Costo de reserva</label>
                                    <input type="number" class="form-control" :placeholder="costoReservaFormulario" :value="costoReservaFormulario" id="costoReserva" readonly required>
                                </div>
                                <div class="mb-3">
                                    <label for="costoTotal" class="col-form-label">Costo total</label>
                                    <input type="number" class="form-control" :placeholder="costoTotalFormulario" :value="costoTotalFormulario" id="costoTotal" readonly required>
                                </div>
                            </form>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                <button type="submit" class="btn btn-primary" form="formularioReserva">Realizar reserva</button>
                            </div>
                            
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </body>
</template>

<script>
import * as estacionamiento from '../assets/estacionamiento/estacionamiento.js'

export default {
    name: 'app-estacionamiento',
    data(){
            return{
                lugarEstacionamientoFormulario:'--',
                inicioReservaFormulario:null,
                finReservaFormulario:null,
                placaFormulario:'',
                marcaFormulario:'',
                modeloFormulario:'',
                colorFormulario:'',
                estacionamientos:null,
                cantidadestacionamientos:null,
                cantidadAutos:1,
                alternarOpcionAutos:false
            };
    },
    async created(){
        let respuesta = await estacionamiento.obtenerEstacionamientos();
        this.estacionamientos = respuesta['estacionamientos'];
        this.cantidadestacionamientos = respuesta['total_estacionamientos'];
        let scopeself = this
        setInterval(async function () {
            let respuesta = await estacionamiento.obtenerEstacionamientos();
            scopeself.estacionamientos = respuesta['estacionamientos'];
            scopeself.cantidadestacionamientos = respuesta['total_estacionamientos'];
        }, 10000);
    },
    methods:{
        iniciarFormulario: function(lugar){
            this.lugarEstacionamientoFormulario = lugar;
        }
    },
    computed:{
        costoTotalFormulario(){
            return estacionamiento.calcularCosto(this.inicioReservaFormulario, this.finReservaFormulario);
        },
        costoReservaFormulario(){
            return estacionamiento.calcularCosto(this.inicioReservaFormulario, this.finReservaFormulario) * 5/100;
        }
    },
    watch:{
        inicioReservaFormulario(){
            var fechaInicio = document.getElementById('fechaInicio');
            var fechaFin = document.getElementById('fechaFin');
            if (fechaInicio.value)
                fechaFin.min = fechaInicio.value;
        },
        finReservaFormulario(){
            var fechaInicio = document.getElementById('fechaInicio');
            var fechaFin = document.getElementById('fechaFin');
            if (fechaFin.value)
                fechaInicio.max = fechaFin.value;
        }
    }
    }
</script>

<style scoped>

*{
    font-family: 'Roboto', sans-serif;
}
  

.titulo{
    color: white;
    text-align: center;
}  

.nav{
    padding: 3px;
}
  
.nav li:hover {
    background-color: white;
    color: black;
}

.estacionamiento{
    position: relative;
    border: solid blue 2px;
    display: grid;
    grid-template-columns: 15% 15% 15% 15% 15% ;
    grid-template-rows: 15% 15% 15% 15% 15% ;
    gap:4em;
    padding-top: 50px;
    padding-left: 100px;
}

.lugarEstacionamiento{
    width: auto;
    height: auto;
    border: 2px solid #0b1108;
    border-radius: 10px;
    padding: 3em;
}

.grupoEstacionamiento{
    display: grid;
    grid-template-columns: auto auto auto auto auto;
    gap: 10px;
    padding: 5px;
}



.DIS{
    background-color: #81e248;
    transition-duration: 0.4s;
}
.DIS:hover{
    background-color: #61ad35;
}

.RES{
    background-color: #f5b41d;
    transition-duration: 0.4s;
}
.RES:hover{
    background-color: #ce9716;
}
.RES:active{
    animation: shake 0.5s;
}


.OCU{
    background-color: #e41515;
    transition-duration: 0.4s;
}
.OCU:hover{
    background-color: #bb0f0f;
}
.OCU:active{
    animation: shake 0.5s;
}

.NOD{
    background-color: #bebeb7;
    transition-duration: 0.4s;
}
.NOD:hover{
    background-color: #8b8b87;
}
.NOD:active{
    animation: shake 0.5s;
}

@keyframes shake {
    0% { transform: translate(1px, 1px) rotate(0deg); }
    10% { transform: translate(-1px, -2px) rotate(-1deg); }
    20% { transform: translate(-3px, 0px) rotate(1deg); }
    30% { transform: translate(3px, 2px) rotate(0deg); }
    40% { transform: translate(1px, -1px) rotate(1deg); }
    50% { transform: translate(-1px, 2px) rotate(-1deg); }
    60% { transform: translate(-3px, 1px) rotate(0deg); }
    70% { transform: translate(3px, 1px) rotate(-1deg); }
    80% { transform: translate(-1px, -1px) rotate(1deg); }
    90% { transform: translate(1px, 2px) rotate(0deg); }
    100% { transform: translate(1px, -2px) rotate(-1deg); }
}

label{
    color:black !important;
    font-family: georgia, 'Times New Roman', Times, serif;
}
</style>