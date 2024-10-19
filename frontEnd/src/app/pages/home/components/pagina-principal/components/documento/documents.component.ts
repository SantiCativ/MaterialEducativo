import { Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';
import { MaterialService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';

@Component({
  selector: 'app-documents',
  templateUrl: './documents.component.html',
  styleUrls: ['./documents.component.css']
})
export class DocumentsComponent implements OnInit {
  displayedColumns: string[] = ['nombre', 'creado', 'propietario'];
  documents :any

  @ViewChild(MatSort) sort!: MatSort;

  constructor(private _Materialservice: MaterialService, private _alertService: AlertService) { }

  ngOnInit() {
    this.getUser();
  }

  getUser() {
    this._Materialservice.getUser().then(usuario => {
      if (usuario) {
        this.getDocuments(usuario.id);
      }
    }).catch(error => {
      console.error('Error al obtener el usuario', error);
    });
  }

  getDocuments(idUser: string) {
    this._Materialservice.getSuggestedDocuments(idUser).subscribe({
      next: (response: any) => {
        console.log("documentos", response);
        this.documents= response;  
      },
      error: () => this._alertService.error('Respuesta Fallida')
    });
  }
  
}
