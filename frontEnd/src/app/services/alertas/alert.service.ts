import { Injectable } from '@angular/core';
import Swal, { SweetAlertOptions } from 'sweetalert2';

@Injectable({
  providedIn: 'root'
})
export class AlertService {

  constructor() { }

  success(message: string, title?: string) {
    Swal.fire({
      title: title || 'Success',
      text: message,
      icon: 'success',
      confirmButtonText: 'OK'
    });
  }

  error(message: string, title?: string) {
    Swal.fire({
      title: title || 'Error',
      text: message,
      icon: 'error',
      confirmButtonText: 'OK'
    });
  }

  info(message: string, title?: string) {
    Swal.fire({
      title: title || 'Info',
      text: message,
      icon: 'info',
      confirmButtonText: 'OK'
    });
  }

  warning(message: string, title?: string) {
    Swal.fire({
      title: title || 'Warning',
      text: message,
      icon: 'warning',
      confirmButtonText: 'OK'
    });
  }

  custom(options: SweetAlertOptions) {
    Swal.fire(options);
  }



  confirmed(title: string, text?: string): Promise<any> {
    return Swal.fire({
      title: title,
      text: text,
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Si",
      cancelButtonText: "No, cancelar!",
      customClass: {
        confirmButton: 'btn btn-success',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: true
    });
  }
}

