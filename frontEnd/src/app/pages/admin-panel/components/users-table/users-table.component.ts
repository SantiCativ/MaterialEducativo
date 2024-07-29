import { Component, OnInit, Input, OnChanges, SimpleChanges } from '@angular/core';
import { MaterialService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';


@Component({
  selector: 'app-users-table',
  templateUrl: './users-table.component.html',
  styleUrls: ['./users-table.component.css']
})
export class UsersTableComponent implements OnInit, OnChanges {

  pagina: number = 1
  users: any;
  filteredUsers: any;
  @Input() state: string = '';

  constructor(private _Materialservice: MaterialService, private _alertService: AlertService) { }

  ngOnInit() {
    this.getUsers();
  }

  getUsers() {
    this._Materialservice.getUsers().subscribe({
      next: (response) => { console.log(response); this.users = response; this.filteredUsers = response },
      error: () => this._alertService.error('Respuesta Fallida')
    })
  }

  //Este método es un hook del ciclo de vida de Angular que se ejecuta cada vez que se detecta un cambio en las propiedades de entrada (@Input) del componente.
  ngOnChanges() {
    if (this.state) {
      if (this.state ==="1" || this.state=== "2" || this.state=== "3") {
        this.filteredUsers = this.users.filter((user: any) => user.estado == this.state);
      } else {
        const filtroLowerCase = this.state.toLocaleLowerCase();
        this.filteredUsers = this.users.filter((user: any) => {
          const usernameLowerCase = user.username.toLocaleLowerCase();
          const emailLowerCase = user.email.toLocaleLowerCase();
          return usernameLowerCase.includes(filtroLowerCase) || emailLowerCase.includes(filtroLowerCase)
        });
      }
    } else {
      this.filteredUsers = this.users;
    }

  }

  async updatedState(id: string, state: string, accion: string) {
    try {
      const result = await this._alertService.confirmed("¿Está seguro/a de " + accion + " el registro?", "Esto es irreversible");
      if (result.isConfirmed) {
        const dataState = { estado: state };
        this._Materialservice.updateEstado(id, dataState).subscribe({
          next: () => {
            this._alertService.success("¡Estado cambiado!");
            this.ngOnInit();
          },
          error: () => this._alertService.error('Respuesta fallida')
        });
      } else {
        this._alertService.error("La acción a sido cancelada...", "Cancelado");
      }
    } catch (error) {
      this._alertService.error("Hubo un error en la confirmación");
    }
  }

}
