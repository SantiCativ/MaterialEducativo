import { Component, OnInit } from '@angular/core';
import { UploadDocumentComponent } from './components-sidebar/upload-document/upload-document.component';
@Component({
  selector: 'app-sidebar-home',
  templateUrl: './sidebar-home.component.html',
  styleUrls: ['./sidebar-home.component.css']
})
export class SidebarHomeComponent implements OnInit{
  ngOnInit(): void {}
  modalActivo: boolean = false;
  openModal() {
    this.modalActivo = true;
  }
  closeModal() {
    this.modalActivo = false;
  }
}
