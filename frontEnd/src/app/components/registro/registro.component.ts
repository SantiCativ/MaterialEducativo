import { Component, OnInit } from '@angular/core';//no se usa pero que quede por si acaso
import { MaterialService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';
import { NgForm } from '@angular/forms';


@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit {
  //user es un objeto que declaro, este objeto tendra los campos 4 campos que defino, uso este objeto para luego cargarlo al form
  user = {
    nombre: '',
    email: '',
    contrasenia: '',
    certificado: null as File | null
  };

  certificadoError = false;

  constructor(
    private _Materialservice:MaterialService,
    private _alertService: AlertService) { }

  ngOnInit(): void {

  }

  SelectFile(event: any) {
    const file = event.target.files[0];
    if (file && file.type === 'application/pdf') {
      this.user.certificado = file;
      this.certificadoError = false;
    } else {
      this.user.certificado = null;
      this.certificadoError = true;
      this._alertService.error('Selecciona un archivo PDF y no haga perder tiempo');
    }
  }

  Registro(form: NgForm) {

   //pregunto por separado las validaciones ya que ng model no se puede enlazar con un input de tipo file. Si algunos de los campos no se completo entra a la funcion
    if (form.invalid || !this.user.certificado) {
      //Basicamente recorremos todos los controles y seteamos que fueron tocados, de esta manera el cartel se va a mostrar cuando el usuario haga el registro y no antes.
      Object.keys(form.controls).forEach(field => {
        const control = form.control.get(field);
        control?.markAsTouched({ onlySelf: true });
      });

      //verifico el certificado, necesario esta comprobacion porque no sabemos si entramos a la funcion porque el usuario ingreso el nombre,email,contraseña o por el certificado
      if (!this.user.certificado) {
        this.certificadoError = true;
      }

      //retornamos, ya que el formulario fue invalido
      return;
    }

    const dataUser = new FormData();
    dataUser.append('nombre', this.user.nombre);
    dataUser.append('email', this.user.email);
    dataUser.append('contrasenia', this.user.contrasenia);
    dataUser.append('certificado', this.user.certificado, this.user.certificado.name);

    this._Materialservice.registrarUsuario(dataUser).subscribe((response: any) => {
      console.log('Registro exitoso', response);
      this._alertService.success('Usuario registrado exitosamente!');
      //reedirigir a por ejemplo la pantalla principal
    }, error => {
      this._alertService.error('Ocurrió un error.');
      console.error('Error en el registro', error);
    });
  }
}