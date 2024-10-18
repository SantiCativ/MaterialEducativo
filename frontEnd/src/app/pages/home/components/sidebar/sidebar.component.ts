import { Component, OnInit } from '@angular/core';
import { AlertService } from 'src/app/services/alertas/alert.service';
import { MaterialService } from 'src/app/services/service.service';

@Component({
  selector: 'app-sidebar-h',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponentHome implements OnInit {
  isDropdownActive = false;
  idUser:string="";
  constructor(private _alertService: AlertService, private _materialService: MaterialService) { }

  ngOnInit() {
    this.getUser();
  }

  getUser() {
    this._materialService.getUser().then(usuario => {
      if (usuario) {
        this.idUser=usuario.id;
      }
    }).catch(error => {
      console.error('Error al obtener el usuario', error);
    });
  }




  // Alterna la visibilidad del dropdown
  toggleDropdown() {
    this.isDropdownActive = !this.isDropdownActive;
  }

  async crearCarpeta() {

    const nombre = await this._alertService.form(
      "carpeta sin titulo",
      "Carpeta Nueva",
      "ingrese nombre",
      "ingrese un nombre"
    );

    if (nombre) {
      const dataFolder = new FormData();
      dataFolder.append('nombre', nombre);
      dataFolder.append('idUser', this.idUser);
      this._materialService.createFolder(dataFolder).subscribe({
        next: (response) => { console.log(response); this._alertService.success("Carpeta Creada Exitosamente"," "); /* reedireccionar a mi unidad*/ },
        error: () => this._alertService.error('Respuesta Fallida')
      })
    }
  }



}
