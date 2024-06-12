import { Component, OnInit } from '@angular/core';//no se usa pero que quede por si acaso
import { UserService } from 'src/app/services/api-calls/user.service';//importo el serivicio que cree

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent  {
  //user es un objeto que declaro, este objeto tendra los campos 4 campos que defino, uso este objeto para luego cargarlo al form
  user = {
    nombre: '',
    email: '',
    contrasenia: '',
    certificado: null as File | null //no entiendo muy bien esto, pero es la unica forma en que anda
  };

  constructor(private userService: UserService) //infecto el servicio ala clase registroComponent mediante su constructor
  {}

  SelectFile(event: any)//este evento se activa cuando se selecciona un archivo en el campo certificado
  {
    const file = event.target.files[0];//obtiene el certificado que se haya elegido y se lo asigna a file
    if (file && file.type === 'application/pdf') 
    {//verifica que sea un archivo PDF
      this.user.certificado = file;
    } else 
       alert('Selecciona un archivo PDF y no haga perder tiempo');
    
  }

  RegisterButton()//este metodo se ejecuta cuando se oprime el boton registrar
  {
    if (!this.user.certificado)// verifica si se cargo un archivo
      {
       alert('Por favor, carga un archivo PDF');
       return;//detiene la ejecucion del metodo y no sigue con las siguientes lineas de codigo
      }

    //aqui creo el formdata que se enviara al backend en django, formdata permite enviar archivos pdf por eso lo uso
    const formData=new FormData();
    formData.append('nombre',this.user.nombre);//agrego el campo al formdata
    formData.append('email',this.user.email);
    formData.append('contrasenia',this.user.contrasenia);
    formData.append('certificado',this.user.certificado,this.user.certificado.name);
    

    this.userService.registrarUsuario(formData)//llamo al metodo del servicio que importe para enviar el formdata
      .subscribe(response => {
        console.log('Registro exitoso', response);
      }, error => {
        console.error('Error en el registro', error);
      });
  }

}
