import { Component } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent {
  //genero dinamicamente los datos para la tabla, data es una lista que contiene diccionarios
  //SOLO SIRVE PARA PROBAR QUE LA TABLA ES DINAMICA Y NO ESTATICA
  data=[
    {estado:"activo", nombre: "Juan Pérez", certificado: "certificado-juan_perez.pdf" },
    {estado:"pendiente", nombre: "María Gómez", certificado: "certificado-maria_gomez.pdf" },
    {estado:"rechazado", nombre: "Carlos Rodríguez", certificado: "certificado-carlos_rodriguez.pdf" }];
  
  columns=['Estado','Nombre','Certificado de Alumno Regular','Acción'];

}
