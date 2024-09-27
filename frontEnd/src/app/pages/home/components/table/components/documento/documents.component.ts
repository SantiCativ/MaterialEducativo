import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';

export interface PeriodicElement {
  creado: string;
  nombre: string;
  propietario: string;
  ubicacion: string;
}

const ELEMENT_DATA: PeriodicElement[] = [
  { nombre: 'parcialMate', creado: '2020-09-20', propietario: 'santiago', ubicacion: 'H' },
  { nombre: 'parcialMate', creado: '2020-09-20', propietario: 'santiago', ubicacion: 'H' },
  { nombre: 'parcialMate', creado: '2020-09-20', propietario: 'santiago', ubicacion: 'H' },
  { nombre: 'parcialMate', creado: '2021-03-20', propietario: 'santiago', ubicacion: 'He' },
  { nombre: 'parcialMate', creado: '2022-09-20', propietario: 'santiago', ubicacion: 'Li' },
  { nombre: 'parcialMate', creado: '2026-09-20', propietario: 'santiago', ubicacion: 'Be' },
  { nombre: 'parcialMate', creado: '2027-09-20', propietario: 'santiago', ubicacion: 'B' },
  { nombre: 'parcialMate', creado: '2027-09-20', propietario: 'santiago', ubicacion: 'C' },
  { nombre: 'parcialMate', creado: '2028-09-20', propietario: 'santiago', ubicacion: 'N' },
  { nombre: 'parcialMate', creado: '2029-09-20', propietario: 'santiago', ubicacion: 'O' },
  { nombre: 'parcialMate', creado: '2030-09-20', propietario: 'santiago', ubicacion: 'F' },
  { nombre: 'parcialMate', creado: '2120-09-20', propietario: 'santiago', ubicacion: 'Ne' },
];
@Component({
  selector: 'app-documents',
  templateUrl: './documents.component.html',
  styleUrls: ['./documents.component.css']
})
export class DocumentsComponent implements OnInit {
  displayedColumns: string[] = ['nombre', 'creado', 'propietario', 'ubicacion'];
  dataSource = new MatTableDataSource(ELEMENT_DATA);

  @ViewChild(MatSort) sort!: MatSort;

  ngOnInit() { }

  ngAfterViewInit() {
    this.dataSource.sort = this.sort;
  }
}
