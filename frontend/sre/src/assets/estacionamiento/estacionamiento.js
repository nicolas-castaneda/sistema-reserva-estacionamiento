export async function obtenerEstacionamientos(){
    let respuesta = await
    fetch('http://127.0.0.1:5000/estacionamiento',{
        method:'GET'
    }).then(function (response) {
        return response.json();
    }).then(function (responseJson){  
        return responseJson;
    }).catch(error => console.log(error));
    return respuesta;
}

export function calcularCosto(fechaInicio, fechaFin){
    if(fechaInicio != null && fechaFin != null){
        let valorFechaFin = Date.parse(fechaFin)
        let valorFechaInicio = Date.parse(fechaInicio)

        let horasTotales = (valorFechaFin - valorFechaInicio) / 1000 / 60 / 60;
        horasTotales = Math.floor(horasTotales) + 1*(horasTotales - Math.floor(horasTotales) > 0); 
        const costo = horasTotales * 3;
        return costo;
    }else{
        return 0;
    }
}