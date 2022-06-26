<template>
  <div class="pantalla min-vh-100">
    <div class="grupoEstacionamiento">
      <div
        v-for="(estacionamiento, index) in estacionamientos"
        :key="index"
        class="elementoEstacionamiento"
      >
        <button
          v-bind:class="[
            'lugarEstacionamiento',
            estacionamiento.estadoRegistro,
          ]"
          v-bind:data-bs-toggle="[
            estacionamiento.estadoRegistro == 'DIS' ? 'modal' : '',
          ]"
          type="button"
          data-bs-target="#modal-escoger"
          v-on:click="
            [iniciarFormulario(estacionamiento.lugar), autosUsuario()]
          "
        >
          {{ estacionamiento.lugar }}
        </button>
      </div>
    </div>
    <div class="modal fade" id="modal-escoger">
      <div class="modal-dialog">
        <div class="modal-content">
          <form id="formularioReserva" class="modal-body" v-on:submit="submit">
            <div class="mb-3">
              <label for="lugar" class="col-form-label"
                >Lugar de estacionamiento</label
              >
              <input
                class="form-control"
                type="text"
                :placeholder="lugarEstacionamientoFormulario"
                id="lugar"
                :value="lugarEstacionamientoFormulario"
                readonly
                required
              />
            </div>
            <div class="mb-3 d-flex">
              <div class="m-auto">
                <label for="fechaInicio" class="col-form-label"
                  >Fecha inicio</label
                >
                <input
                  v-model="inicioReservaFormulario"
                  type="datetime-local"
                  class="form-control"
                  id="fechaInicio"
                  required
                />
              </div>
              <div class="m-auto">
                <label for="fechaFin" class="col-form-label">Fecha final</label>
                <input
                  v-model="finReservaFormulario"
                  type="datetime-local"
                  class="form-control"
                  id="fechaFin"
                  required
                />
              </div>
            </div>
            <div id="autosDisponibles">
              <button
                v-if="alternarOpcionAutos && cantidadAutosDisponibles > 0"
                id="cambiarAnadirDisponible"
                type="button"
                @click="
                  alternarOpcionAutos = !alternarOpcionAutos;
                  placaFormulario = '';
                "
              >
                Carros disponibles
              </button>
              <button
                v-else-if="
                  alternarOpcionAutos == false && cantidadAutosDisponibles > 0
                "
                id="cambiarAnadirDisponible"
                type="button"
                @click="
                  alternarOpcionAutos = !alternarOpcionAutos;
                  placaFormulario = '';
                "
              >
                Añadir auto
              </button>
              <div v-if="alternarOpcionAutos || cantidadAutosDisponibles == 0">
                <div class="mb-3" id="contenedorPlaca">
                  <label for="placa" class="col-form-label">Placa</label>
                  <input
                    type="text"
                    v-model="placaFormulario"
                    class="form-control"
                    id="placa"
                    required
                  />
                </div>
                <div class="mb-3" id="contenedorMarca">
                  <label for="marca" class="col-form-label">Marca</label>
                  <input
                    type="text"
                    v-model="marcaFormulario"
                    class="form-control"
                    id="marca"
                    required
                  />
                </div>
                <div class="mb-3" id="contenedorModelo">
                  <label for="modelo" class="col-form-label">Modelo</label>
                  <input
                    type="text"
                    v-model="modeloFormulario"
                    class="form-control"
                    id="modelo"
                    required
                  />
                </div>
                <div class="mb-3" id="contenedorColor">
                  <label for="color" class="col-form-label">Color</label>
                  <input
                    type="text"
                    v-model="colorFormulario"
                    class="form-control"
                    id="color"
                    required
                  />
                </div>
              </div>
              <div
                v-else-if="
                  alternarOpcionAutos == false && cantidadAutosDisponibles > 0
                "
              >
                <div id="contenedorAutosDisponibles" class="mb-3">
                  <select
                    v-model="placaFormulario"
                    class="form-select"
                    id="seleccionarAutosDisponibles"
                    required
                  >
                    <option disabled value="">Seleccione un vehiculo</option>
                    <option
                      v-for="(auto, index) in autosDisponibles"
                      :key="index"
                      :value="auto.placa"
                    >
                      {{ auto.placa }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
            <div class="mb-3">
              <label for="costoReserva" class="col-form-label"
                >Costo de reserva</label
              >
              <input
                type="number"
                class="form-control"
                :placeholder="costoReservaFormulario"
                :value="costoReservaFormulario"
                id="costoReserva"
                readonly
                required
              />
            </div>
            <div class="mb-3">
              <label for="costoTotal" class="col-form-label">Costo total</label>
              <input
                type="number"
                class="form-control"
                :placeholder="costoTotalFormulario"
                :value="costoTotalFormulario"
                id="costoTotal"
                readonly
                required
              />
            </div>
            <div class="modal-footer">
              <button
                type="button"
                class="btn btn-secondary"
                data-bs-dismiss="modal"
              >
                Cerrar
              </button>
              <button
                type="submit"
                class="btn btn-primary"
                form="formularioReserva"
              >
                Realizar reserva
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as estacionamiento from "../assets/estacionamiento/estacionamiento.js";
import { Modal } from "bootstrap";

export default {
  name: "app-estacionamiento",
  data() {
    return {
      usuario: "a@a.com",
      lugarEstacionamientoFormulario: "--",
      inicioReservaFormulario: null,
      finReservaFormulario: null,
      placaFormulario: "",
      marcaFormulario: "",
      modeloFormulario: "",
      colorFormulario: "",
      estacionamientos: null,
      cantidadestacionamientos: null,
      autos: [],
      cantidadAutos: 0,
      alternarOpcionAutos: false,
      error: null,
    };
  },
  async created() {
    let respuesta = await estacionamiento.obtenerEstacionamientos();
    this.estacionamientos = respuesta["estacionamientos"];
    this.cantidadestacionamientos = respuesta["total_estacionamientos"];
    let scopeself = this;
    setInterval(async function () {
      let respuesta = await estacionamiento.obtenerEstacionamientos();
      scopeself.estacionamientos = respuesta["estacionamientos"];
      scopeself.cantidadestacionamientos = respuesta["total_estacionamientos"];
    }, 10000);
  },
  methods: {
    iniciarFormulario: function (lugar) {
      this.lugarEstacionamientoFormulario = lugar;
      this.alternarOpcionAutos = true;
      this.placaFormulario = "";
    },
    autosUsuario: async function () {
      let respuesta = await estacionamiento.obtenerAutoUsuario(this.usuario);
      this.autos = respuesta["autos"];
      this.cantidadAutos = respuesta["total_autos"];
    },
    submit: function (event) {
      event.preventDefault();
      this.error = null;
      fetch("http://127.0.0.1:5000/reserva", {
        method: "POST",
        body: JSON.stringify({
          usuario: this.usuario,
          lugar: this.lugarEstacionamientoFormulario,
          inicioReserva: this.inicioReservaFormulario,
          finReserva: this.finReservaFormulario,
          placa: this.placaFormulario,
          marca: this.marcaFormulario,
          modelo: this.modeloFormulario,
          color: this.colorFormulario,
          costoReserva: this.costoReservaFormulario,
          costoTotal: this.costoTotalFormulario,
          opcion: this.alternarOpcionAutos,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            this.lugarEstacionamientoFormulario = "--";
            this.inicioReservaFormulario = null;
            this.finReservaFormulario = null;
            this.placaFormulario = "";
            this.marcaFormulario = "";
            this.modeloFormulario = "";
            this.colorFormulario = "";
            const modalFormulario = Modal.getInstance(
              document.getElementById("modal-escoger")
            );
            modalFormulario.hide();
          } else {
            this.error = data.message;
            console.log(this.error);
          }
        });
    },
  },
  computed: {
    costoTotalFormulario() {
      return estacionamiento.calcularCosto(
        this.inicioReservaFormulario,
        this.finReservaFormulario
      );
    },
    costoReservaFormulario() {
      return (
        (estacionamiento.calcularCosto(
          this.inicioReservaFormulario,
          this.finReservaFormulario
        ) *
          5) /
        100
      );
    },
    cantidadAutosDisponibles() {
      return this.autos.filter((auto) => auto.estado == "DIS").length;
    },
    autosDisponibles() {
      return this.autos.filter((auto) => auto.estado == "DIS");
    },
  },
  watch: {
    inicioReservaFormulario() {
      var fechaInicio = document.getElementById("fechaInicio");
      var fechaFin = document.getElementById("fechaFin");
      if (fechaInicio.value) fechaFin.min = fechaInicio.value;
    },
    finReservaFormulario() {
      var fechaInicio = document.getElementById("fechaInicio");
      var fechaFin = document.getElementById("fechaFin");
      if (fechaFin.value) fechaInicio.max = fechaFin.value;
    },
  },
};
</script>

<style scoped>
.titulo {
  color: white;
  text-align: center;
}

.nav {
  padding: 3px;
}

.nav li:hover {
  background-color: white;
  color: black;
}

.estacionamiento {
  position: relative;
  border: solid blue 2px;
  display: grid;
  grid-template-columns: 15% 15% 15% 15% 15%;
  grid-template-rows: 15% 15% 15% 15% 15%;
  gap: 4em;
  padding-top: 50px;
  padding-left: 100px;
}

.lugarEstacionamiento {
  width: auto;
  height: auto;
  border: 2px solid #0b1108;
  border-radius: 10px;
  padding: 3em;
}

.grupoEstacionamiento {
  display: grid;
  grid-template-columns: auto auto auto auto auto;
  gap: 10px;
  padding: 5px;
}

.DIS {
  background-color: #81e248;
  transition-duration: 0.4s;
}
.DIS:hover {
  background-color: #61ad35;
}

.RES {
  background-color: #f5b41d;
  transition-duration: 0.4s;
}
.RES:hover {
  background-color: #ce9716;
}
.RES:active {
  animation: shake 0.5s;
}

.OCU {
  background-color: #e41515;
  transition-duration: 0.4s;
}
.OCU:hover {
  background-color: #bb0f0f;
}
.OCU:active {
  animation: shake 0.5s;
}

.NOD {
  background-color: #bebeb7;
  transition-duration: 0.4s;
}
.NOD:hover {
  background-color: #8b8b87;
}
.NOD:active {
  animation: shake 0.5s;
}

@keyframes shake {
  0% {
    transform: translate(1px, 1px) rotate(0deg);
  }
  10% {
    transform: translate(-1px, -2px) rotate(-1deg);
  }
  20% {
    transform: translate(-3px, 0px) rotate(1deg);
  }
  30% {
    transform: translate(3px, 2px) rotate(0deg);
  }
  40% {
    transform: translate(1px, -1px) rotate(1deg);
  }
  50% {
    transform: translate(-1px, 2px) rotate(-1deg);
  }
  60% {
    transform: translate(-3px, 1px) rotate(0deg);
  }
  70% {
    transform: translate(3px, 1px) rotate(-1deg);
  }
  80% {
    transform: translate(-1px, -1px) rotate(1deg);
  }
  90% {
    transform: translate(1px, 2px) rotate(0deg);
  }
  100% {
    transform: translate(1px, -2px) rotate(-1deg);
  }
}

label {
  color: black !important;
  font-family: georgia, "Times New Roman", Times, serif;
}
</style>
