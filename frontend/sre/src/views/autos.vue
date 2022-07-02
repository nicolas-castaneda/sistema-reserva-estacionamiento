<template>
  <div class="container mt-4 shadow-lg p-3 mb-5 bg-body rounded">
    <!-- boton para agregar autos -->
    <button
      type="button"
      class="btn btn-primary"
      data-bs-toggle="modal"
      data-bs-target="#modalinsertAuto"
      @click="insertAuto()"
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
              @click="updateAuto(auto.placa)"
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
                  <form id="formularioupdateAuto" method="PATCH">
                    <div class="mb-3">
                      <label for="marca" class="col-form-label">Marca</label>
                      <input
                        id="updateMarca"
                        type="text"
                        class="form-control"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="modelo" class="col-form-label">Modelo</label>
                      <input
                        id="updateModelo"
                        type="text"
                        class="form-control"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="color" class="col-form-label">Color</label>
                      <input
                        id="updateColor"
                        type="text"
                        class="form-control"
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
      id="modalinsertAuto"
      class="modal fade"
      tabindex="-1"
      aria-labelledby="modalinsertAuto"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header bg-primary text-white">
            <h5 class="modal-title" id="modalinsertAuto">Crear</h5>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <form id="formularioinsertAuto" method="POST">
              <div class="mb-3">
                <label for="placa" class="col-form-label">Placa</label>
                <input id="insertPlaca" type="text" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="marca" class="col-form-label">Marca</label>
                <input id="insertMarca" type="text" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="modelo" class="col-form-label">Modelo</label>
                <input id="insertModelo" type="text" class="form-control" />
              </div>
              <div class="mb-3">
                <label for="color" class="col-form-label">Color</label>
                <input id="insertColor" type="text" class="form-control" />
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
      autos: {},
    };
  },
  async created() {
    let idUsuario = this.$store.state.user.id;
    let token = this.$store.state.user.token;
    let respuesta = await autos.obtenerAutoUsuario(idUsuario, token);
    this.autos = respuesta["autos"];
  },
  methods: {
    insertAuto() {
      let scopeself = this;
      document
        .getElementById("formularioinsertAuto")
        .addEventListener("submit", (e) => {
          e.preventDefault();
          const placa = document.getElementById("insertPlaca").value;
          const marca = document.getElementById("insertMarca").value;
          const modelo = document.getElementById("insertModelo").value;
          const color = document.getElementById("insertColor").value;
          const estado = "DIS";
          const data = {
            idUsuario: this.$store.state.user.id,
            placa: placa,
            marca: marca,
            modelo: modelo,
            color: color,
            estado: estado,
          };
          fetch("http://localhost:5000/autos/insert", {
            method: "POST",
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
                document.getElementById("modalinsertAuto")
              );
              modalFormulario.hide();
            })
            .catch((error) => console.error("Error:", error));
        });
    },
    updateAuto(placa) {
      let scopeself = this;
      document
        .getElementById("formularioupdateAuto")
        .addEventListener("submit", (e) => {
          e.preventDefault();
          const marca = document.getElementById("updateMarca").value;
          const modelo = document.getElementById("updateModelo").value;
          const color = document.getElementById("updateColor").value;
          const data = {
            placa: placa,
            marca: marca,
            modelo: modelo,
            color: color,
          };
          fetch("http://localhost:5000/autos/update", {
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
        });
    },
    deleteAuto(placa) {
      let scopeself = this;
      const data = {
        placa: placa,
      };
      fetch("http://localhost:5000/autos/delete", {
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

<style></style>
