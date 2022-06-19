<template>
    <div class="container p-5 shadow-lg">
        <!-- boton para agregar autos -->
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalinsertAuto" @click="insertAuto()">Crear</button>
        <!-- tabla de autos -->
        <table id="tablaAutos" class="table mt-2 table bordered table-striped">
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
                    <tr v-for="auto in autos">
                        <td scope="col">{{auto.placa}}</td>
                        <td>{{auto.marca}}</td>
                        <td>{{auto.modelo}}</td>
                        <td>{{auto.color}}</td>
                        <td>{{auto.estado}}</td>
                        <td>
                            <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#modalupdateAuto" @click="updateAuto(auto.id)">Editar</button>
                            <button class="btn btn-warning" @click="deleteAuto(auto.id)">Eliminar</button>
                        </td>
                        <!-- modal para editar autos -->
                        <div class="modal fade" id="modalupdateAuto" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header bg-primary text-white">
                                        <h5 class="modal-title" id="exampleModalLabel">Editar</h5>
                                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                    </div>
                                    <div class="modal-body">
                                        <div class="mb-3">
                                            <label for="placa" class="col-form-label">Placa</label>
                                            <input id="updatePlaca" type="text" class="form-control">
                                        </div>
                                        <div class="mb-3">
                                            <label for="marca" class="col-form-label">Marca</label>
                                            <input id="updateMarca" type="text" class="form-control">
                                        </div>
                                        <div class="mb-3">
                                            <label for="modelo" class="col-form-label">Modelo</label>
                                            <input id="updateModelo" type="text" class="form-control">
                                        </div>
                                        <div class="mb-3">
                                            <label for="color" class="col-form-label">Color</label>
                                            <input id="updateColor" type="text" class="form-control">
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                                            <button type="submit" class="btn btn-primary">Guardar</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div> 
                    </tr>
                </tbody>
        </table>
        <!-- Modal insert Auto --> 
        <div id="modalinsertAuto" class="modal fade" tabindex="-1" aria-labelledby="modalinsertAuto" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header bg-primary text-white">
                        <h5 class="modal-title" id="modalinsertAuto">Crear</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="formularioinsertAuto" method="POST">
                            <div class="mb-3">
                                <label for="placa" class="col-form-label">Placa</label>
                                <input id="insertPlaca" type="text" class="form-control">
                            </div>
                            <div class="mb-3">
                                <label for="marca" class="col-form-label">Marca</label>
                                <input id="insertMarca" type="text" class="form-control">
                            </div>
                            <div class="mb-3">
                                <label for="modelo" class="col-form-label">Modelo</label>
                                <input id="insertModelo" type="text" class="form-control">
                            </div>
                            <div class="mb-3">
                                <label for="color" class="col-form-label">Color</label>
                                <input id="insertColor" type="text" class="form-control">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
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
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";

export default {
    name: 'autos',
    data() {
        return {
            autos : [
                {
                    placa: '',
                    marca: '',
                    modelo: '',
                    color: '',
                    estado: '',
                }
            ],
        }
    },
    methods: {
        insertAuto(){
            document.getElementById('formularioinsertAuto').addEventListener('submit', (e) => {
                e.preventDefault();
                const placa = document.getElementById('insertPlaca').value;
                const marca = document.getElementById('insertMarca').value;
                const modelo = document.getElementById('insertModelo').value;
                const color = document.getElementById('insertColor').value;
                const estado = 'DIS';
                const data = {
                    placa: placa,
                    marca: marca,
                    modelo: modelo,
                    color: color,
                    estado: estado,
                }
                fetch('/autos/insert', {
                    method: 'POST',
                    body: JSON.stringify(data),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log('Success:', response));
            });
        },
        updateAuto(id){
            document.getElementById('formularioupdateAuto').addEventListener('submit', (e) => {
                e.preventDefault();
                const marca = document.getElementById('updateMarca').value;
                const modelo = document.getElementById('updateModelo').value;
                const color = document.getElementById('updateColor').value;
                const data = {
                    idAuto: id,
                    marca: marca,
                    modelo: modelo,
                    color: color,
                }
                fetch('/autos/update/'+id, {
                    method: 'PUT',
                    body: JSON.stringify(data),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log('Success:', response));
            });
        },
        deleteAuto(id){
            const data = {
                idAuto: id,
            }
            fetch('/autos/delete/'+id, {
                method: 'DELETE',
                body: JSON.stringify(data),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(res => res.json())
            .catch(error => console.error('Error:', error))
            .then(response => console.log('Success:', response));
        }
    }
};


</script>

<style>
</style>


