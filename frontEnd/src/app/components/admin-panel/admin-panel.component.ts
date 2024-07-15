import { Component } from '@angular/core';
import { MaterialService } from 'src/app/services/service.service';

@Component({
  selector: 'app-admin-panel',
  templateUrl: './admin-panel.component.html',
  styleUrls: ['./admin-panel.component.css']
})
export class AdminPanelComponent {
  columns: string[] = [];
  data: any[] = [];
  filteredData: any[] = [];

  constructor(private _MaterialService: MaterialService) { }

  onTableSelectionChange(tableName: string): void {
    this.loadTableData(tableName);
  }

  getUsers() {
    this._MaterialService.getUsers().subscribe(data => {
      console.log('Received data:', data); // Verifica la estructura de los datos
      if (Array.isArray(data) && data.length > 0) {
        this.columns = Object.keys(data[0]);
        this.data = data;
        this.filteredData = data;
      } else {
        console.error('Formato de datos inesperado:', data);
      }
    }, error => {
      console.error('Error fetching data:', error);
    });
  }

  getDocumentos() {

  }

  loadTableData(tableName: string): void {
    switch (tableName) {
      case 'Usuarios':
        this.getUsers();
        break;
      case 'Documentos':
        this.getDocumentos();
        break;
      // Agrega más casos según sea necesario
      default:
        console.error('Tabla no encontrada:', tableName);
    }
  }


  onFilterChanged(state: string): void {
    this.filteredData = this.data.filter(user => user.estado === state);
  }

}

