<template>
  <div class="container mt-4 shadow-lg p-3 mb-5 bg-body rounded">
    <!-- tabla de reservas -->
    <table id="tablaReservas" class="table mt-2 table-bordered table-striped">
      <thead>
        <div class="h3 text-center font-weight-bold">Mis Reservas</div>
        <tr class="text-center">
          <th>Lugar</th>
          <th>Fecha Inicio</th>
          <th>Fecha Fin</th>
          <th>Placa</th>
          <th>Costo Reserva(S/.)</th>
          <th>Costo Total(S/.)</th>
          <th>Estado</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <!-- Eliminar reserva -->
        <tr v-for="reserva in reservas" :key="reserva.idReserva">
          <td>{{ reserva.inicioReserva }}</td>
          <td>{{ reserva.inicioReserva }}</td>
          <td>{{ reserva.finReserva }}</td>
          <td>{{ reserva.inicioReserva }}</td>
          <td>{{ reserva.costoReserva }}</td>
          <td>{{ reserva.costoTotal }}</td>
          <td>{{ reserva.estadoRegistro }}</td>
          <td v-if="reserva.estadoRegistro == 'PEN'">
            <button
              class="btn btn-warning"
              @click="deleteReserva(reserva.idReserva)"
            >
              Anular
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import * as reservas from "../assets/reservas/reservas.js";
export default {
  name: "reservas",
  data() {
    return {
      reservas: {},
    };
  },
  async created() {
    let idUsuario = this.$store.state.user.id;
    let token = this.$store.state.user.token;
    let respuesta = await reservas.getReservas(idUsuario, token);
    console.log(respuesta);
    this.reservas = respuesta["reservas"];
  },
  methods: {
    deleteReserva(id) {
      let scopeself = this;
      const data = {
        idReserva: id,
      };
      fetch("http://localhost:5000/reservas/delete", {
        method: "DELETE",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then(async function () {
          let idUsuario = scopeself.$store.state.user.id;
          let token = scopeself.$store.state.user.token;
          let respuesta = await reservas.getReservas(idUsuario, token);
          scopeself.reservas = respuesta["reservas"];
        })
        .catch((error) => console.log("Error:", error));
    },
  },
};
</script>

<style></style>
