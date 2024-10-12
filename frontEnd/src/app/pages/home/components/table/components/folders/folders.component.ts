import { Component, OnInit } from '@angular/core';
import { MaterialService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';

export interface Section {
  name: string;
  updated: Date;
}

@Component({
  selector: 'app-folders',
  templateUrl: './folders.component.html',
  styleUrls: ['./folders.component.css']
})
export class FoldersComponent implements OnInit {

  folders: any
  
  constructor(private _Materialservice: MaterialService, private _alertService: AlertService) { }

  ngOnInit() {
    this.getUser();
  }

  getUser() {
    this._Materialservice.getUser().then(usuario => {
      if (usuario) {
        this.getFolders(usuario.id);
      }
    }).catch(error => {
      console.error('Error al obtener el usuario', error);
    });
  }

  getFolders(idUser:string){
    this._Materialservice.getFolders(idUser).subscribe({
      next: (response) => { console.log(response); this.folders = response;  },
      error: () => this._alertService.error('Respuesta Fallida')
    })
  }

}
