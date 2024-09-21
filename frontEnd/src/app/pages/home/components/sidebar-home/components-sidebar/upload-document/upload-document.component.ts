import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-upload-document',
  templateUrl: './upload-document.component.html',
  styleUrls: ['./upload-document.component.css']
})
export class UploadDocumentComponent {
  @Input() ModalActivo: boolean = false;
  @Output() closeModal = new EventEmitter<void>();

  onCloseModal() {
    this.closeModal.emit();
  }
  file: File | null = null;

  OncloseModal() {
    this.closeModal.emit();
  }

  DocumentChange(event: any) {}
  Subir() {}
}
