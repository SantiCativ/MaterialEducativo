import { Component, OnInit } from '@angular/core';//no se usa pero que quede por si acaso
import { ServiceService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';



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
    certificado: null as File | null //no entiendo muy bien esto, pero es la unica forma en que anda
  };

  constructor(
    private _Materialservice: ServiceService,
    private _alertService: AlertService) { }

  ngOnInit(): void {

  }

  SelectFile(event: any)//este evento se activa cuando se selecciona un archivo en el campo certificado
  {
    const file = event.target.files[0];//obtiene el certificado que se haya elegido y se lo asigna a file
    if (file && file.type === 'application/pdf') {//verifica que sea un archivo PDF
      this.user.certificado = file;
    } else
      this._alertService.error('Selecciona un archivo PDF y no haga perder tiempo');

  }

  Registro()//este metodo se ejecuta cuando se oprime el boton registrar
  {
    if (!this.user.certificado)// verifica si se cargo un archivo
    {
      alert('Por favor, carga un archivo PDF');
      return;//detiene la ejecucion del metodo y no sigue con las siguientes lineas de codigo
    }

    //aqui creo el formdata que se enviara al backend en django, formdata permite enviar archivos pdf por eso lo uso
    const dataUser = new FormData();
    dataUser.append('nombre', this.user.nombre);//agrego el campo al dataUser
    dataUser.append('email', this.user.email);
    dataUser.append('contrasenia', this.user.contrasenia);
    dataUser.append('certificado', this.user.certificado, this.user.certificado.name);


    this._Materialservice.registrarUsuario(dataUser).subscribe((response: any) => {
        console.log('Registro exitoso', response);
        this._alertService.success('Usuario registrado exitosamente!');
      }, error => {
        this._alertService.error('Ocurrió un error.');
        console.error('Error en el registro', error);
      });
  }

}
