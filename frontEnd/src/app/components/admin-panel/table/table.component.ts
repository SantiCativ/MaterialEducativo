import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})


export class TableComponent {
  isModalActive: boolean = false;
  selectedCertificateUrl = "";

  pdfSrc = "https://vadimdez.github.io/ng2-pdf-viewer/assets/pdf-test.pdf";

  @Input() columns: string[] = [];
  @Input() data: any[] = [];

  constructor() {}

  openModal(certificadoUrl: string): void {
    this.selectedCertificateUrl = certificadoUrl;
    this.isModalActive = true;
    console.log("contenido del modal:", this.selectedCertificateUrl);
  }

  closeModal(): void {
    this.isModalActive = false;
    this.selectedCertificateUrl= '';
  }
}
