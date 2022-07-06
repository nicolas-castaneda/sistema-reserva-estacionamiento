<template>
  <div class="container mt-4 shadow-lg p-3 mb-5 bg-body rounded">
    <!-- boton para agregar autos -->
    <button
      type="button"
      class="btn btn-primary"
      data-bs-toggle="modal"
      data-bs-target="#modalinsertAuto"
    >
      Crear
    </button>
    <!-- tabla de autos -->
    <table id="tablaAutos" class="table mt-2 table-bordered table-striped">
      <thead>
        <div class="h3 text-center font-weight-bold">Mis Autos</div>
        <tr>
          <th>Placa</th>
          <th>Marca</th>
          <th>Modelo</th>
          <th>Color</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="auto in autos" :key="auto.placa">
          <td>{{ auto.placa }}</td>
          <td>{{ auto.marca }}</td>
          <td>{{ auto.modelo }}</td>
          <td>{{ auto.color }}</td>
          <td>{{ auto.estado }}</td>
          <td>
            <button
              class="btn btn-success"
              data-bs-toggle="modal"
              data-bs-target="#modalupdateAuto"
              v-on:click="getAuto(auto.placa)"
            >
              Editar
            </button>
            <button class="btn btn-warning" @click="deleteAuto(auto.placa)">
              Eliminar
            </button>
          </td>
          <!-- modal para editar autos -->
          <div
            class="modal fade"
            id="modalupdateAuto"
            tabindex="-1"
            role="dialog"
            aria-labelledby="exampleModalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header bg-primary text-white">
                  <h5 class="modal-title" id="exampleModalLabel">Editar</h5>
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <form
                    id="formularioupdateAuto"
                    method="PATCH"
                    v-on:submit="updatesubmit"
                  >
                    <div class="form-group">
                      <label for="placa" class="col-form-label">Placa</label>
                      <input
                        type="text"
                        class="form-control"
                        id="placa"
                        :placeholder="[[this.updatePlaca]]"
                        disabled
                      />
                    </div>
                    <div class="mb-3">
                      <label for="marca" class="col-form-label">Marca</label>
                      <input
                        id="marca"
                        type="text"
                        class="form-control"
                        v-model="updateMarca"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="modelo" class="col-form-label">Modelo</label>
                      <input
                        id="modelo"
                        type="text"
                        class="form-control"
                        v-model="updateModelo"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="color" class="col-form-label">Color</label>
                      <input
                        id="color"
                        type="text"
                        class="form-control"
                        v-model="updateColor"
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
                      <button type="submit" class="btn btn-primary">
                        Guardar
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </tr>
      </tbody>
    </table>
    <!-- Modal insert Auto -->
    <div
      class="modal fade"
      id="modalinsertAuto"
      tabindex="-1"
      role="dialog"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header bg-primary text-white">
            <h5 class="modal-title" id="exampleModalLabel">Crear</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <form
              id="formularioinsertAuto"
              method="POST"
              v-on:submit="insertsubmit"
            >
              <div class="mb-3">
                <label for="placa" class="col-form-label">Placa</label>
                <input
                  id="placa"
                  type="text"
                  class="form-control"
                  v-model="insertPlaca"
                />
              </div>
              <div class="mb-3">
                <label for="marca" class="col-form-label">Marca</label>
                <input
                  id="marca"
                  type="text"
                  class="form-control"
                  v-model="insertMarca"
                />
              </div>
              <div class="mb-3">
                <label for="modelo" class="col-form-label">Modelo</label>
                <input
                  id="modelo"
                  type="text"
                  class="form-control"
                  v-model="insertModelo"
                />
              </div>
              <div class="mb-3">
                <label for="color" class="col-form-label">Color</label>
                <input
                  id="color"
                  type="text"
                  class="form-control"
                  v-model="insertColor"
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
                <button type="submit" class="btn btn-primary">Guardar</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as autos from "../assets/autos/autos.js";
import { Modal } from "bootstrap";

export default {
  name: "autos",
  data() {
    return {
      idUsuario: this.$store.state.user.id,
      insertPlaca: "",
      insertMarca: "",
      insertModelo: "",
      insertColor: "",
      estado: "DIS",
      updatePlaca: "",
      updateMarca: "",
      updateModelo: "",
      updateColor: "",
      autos: [],
    };
  },
  async created() {
    let scopeself = this;
    let idUsuario = scopeself.$store.state.user.id;
    let token = scopeself.$store.state.user.token;
    let respuesta = await autos.obtenerAutoUsuario(idUsuario, token);
    this.autos = respuesta["autos"];
  },
  methods: {
    getAuto: function (placa) {
      this.updatePlaca = placa;
    },
    insertsubmit: async function (e) {
      e.preventDefault();
      let scopeself = this;
      const estado = "DIS";
      const data = {
        idUsuario: this.$store.state.user.id,
        placa: this.insertPlaca,
        marca: this.insertMarca,
        modelo: this.insertModelo,
        color: this.insertColor,
        estado: estado,
      };
      fetch("http://localhost:5000/autos", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then(async function () {
          let idUsuario = scopeself.$store.state.user.id;
          let token = scopeself.$store.state.user.token;
          let respuesta = await autos.obtenerAutoUsuario(idUsuario, token);
          scopeself.autos = respuesta["autos"];
          const modalFormulario = Modal.getInstance(
            document.getElementById("modalinsertAuto")
          );
          modalFormulario.hide();
        })
        .catch((error) => console.error("Error:", error));
    },
    updatesubmit: async function (e) {
      e.preventDefault();
      let scopeself = this;
      const data = {
        placa: this.updatePlaca,
        marca: this.updateMarca,
        modelo: this.updateModelo,
        color: this.updateColor,
      };
      fetch("http://localhost:5000/autos", {
        method: "PATCH",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then(async function () {
          console.log(scopeself);
          let idUsuario = scopeself.$store.state.user.id;
          let token = scopeself.$store.state.user.token;
          let respuesta = await autos.obtenerAutoUsuario(idUsuario, token);
          scopeself.autos = respuesta["autos"];
          const modalFormulario = Modal.getInstance(
            document.getElementById("modalupdateAuto")
          );
          modalFormulario.hide();
        })
        .catch((error) => console.error("Error:", error));
    },

    deleteAuto(placa) {
      let scopeself = this;
      const data = {
        placa: placa,
      };
      fetch("http://localhost:5000/autos", {
        method: "DELETE",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .then(async function () {
          console.log(scopeself);
          let idUsuario = scopeself.$store.state.user.id;
          let token = scopeself.$store.state.user.token;
          let respuesta = await autos.obtenerAutoUsuario(idUsuario, token);
          scopeself.autos = respuesta["autos"];
        })
        .catch((error) => console.error("Error:", error));
    },
  },
};
</script>

<style scoped>
label {
  color: black !important;
}
</style>
