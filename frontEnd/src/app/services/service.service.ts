import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

  private url = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  registrarUsuario(formData: any) {
    const url=this.url+'/registro/';
    return this.http.post( url,formData);
  }

}