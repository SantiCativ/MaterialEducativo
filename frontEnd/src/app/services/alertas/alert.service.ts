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

  async form(messageDefault: string, title: string, label: string, warning: string): Promise<string | undefined>{
    const inputValue = messageDefault;
    const { value: name } = await Swal.fire({
      title: title,
      input: "text",
      inputLabel: label,
      inputValue,
      showCancelButton: true,
      inputValidator: (value) => {
        if (!value) {
          return warning;
        }
        //Retornar null le indica a SweetAlert2 que no hay error y que todo está bien.
        return null;
      }
      
    });
    return name;
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
  
  customDialog(title:string){
    return Swal.fire({
      position: "center",
      icon: "success",
      title: title,
      showConfirmButton: false,
      timer: 1500
    });
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

