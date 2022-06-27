<template>
  <div class="container mt-4 shadow-lg p-3 mb-5 bg-body rounded">
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
        <tr v-for="reserva in reservas" :key="reserva.key">
          <td>{{ reserva[2] }}</td>
          <td>{{ reserva[0].inicioReserva }}</td>
          <td>{{ reserva[0].finReserva }}</td>
          <td>{{ reserva[1] }}</td>
          <td>{{ reserva[0].costoReserva }}</td>
          <td>{{ reserva[0].costoTotal }}</td>
          <td>{{ reserva[0].estadoRegistro }}</td>
          <td v-if="reserva[0].estadoRegistro == 'PEN'">
            <button
              class="btn btn-warning"
              @click="deleteReserva(reserva[0].id)"
            >
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
    name: 'reservas',
    methods : {
        deleteReserva(id){
            fetch('/reservas/'+id, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
        }
    }
};
</script>

<style></style>
