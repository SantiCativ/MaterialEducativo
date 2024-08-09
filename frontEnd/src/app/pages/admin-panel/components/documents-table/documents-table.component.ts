import { Component, OnInit, Input, OnChanges, SimpleChanges} from '@angular/core';
import { MaterialService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';

@Component({
  selector: 'app-documents-table',
  templateUrl: './documents-table.component.html',
  styleUrls: ['./documents-table.component.css']
})
export class DocumentsTableComponent implements OnInit,OnChanges {

  pagina: number = 1
  documents: any;
  filteredDocuments: any;
  @Input() state: string = '';
  constructor(private Material_service:MaterialService,private alerts:AlertService) { }

  ngOnInit() {
    this.getDocuments();
  }

  getDocuments()
  {
   this.Material_service.getDocuments().subscribe({
    next:(response)=>{console.log(response);this.documents=response;this.filteredDocuments=response;},
    error:()=>this.alerts.error('Respuesta fallida')
   })
  }

  //Este método es un hook del ciclo de vida de Angular que se ejecuta cada vez que se detecta un cambio en las propiedades de entrada (@Input) del componente.
  ngOnChanges() {
    if (this.state) {
      if (this.state === '1' || this.state === '2') {
        this.filteredDocuments = this.documents.filter((doc: any) => doc.state == this.state);
      } else {
        const filtroLowerCase = this.state.toLocaleLowerCase();
        this.filteredDocuments = this.documents.filter((doc: any) => {
          const titleLowerCase = doc.title.toLocaleLowerCase();
          const ownerLowerCase = doc.owner.username.toLocaleLowerCase();
          return titleLowerCase.includes(filtroLowerCase) || ownerLowerCase.includes(filtroLowerCase);
        });
      }
    } else {
      this.filteredDocuments = this.documents;
    }
  }

  async updatedState(id: string, state: number, accion: string) {
    try {
      const result = await this.alerts.confirmed("¿Está seguro/a de " + accion + " el registro?", "Esto es irreversible");
      if (result.isConfirmed) {
        const dataState = { state: state };
        this.Material_service.updateStateDocument(id, dataState).subscribe({
          next: () => {
            this.alerts.success("¡Estado cambiado!");
            this.ngOnInit();
          },
          error: () => this.alerts.error('Respuesta fallida')
        });
      } else {
        this.alerts.error("La acción a sido cancelada...", "Cancelado");
      }
    } catch (error) {
      this.alerts.error("Hubo un error en la confirmación");
    }
  }

}
