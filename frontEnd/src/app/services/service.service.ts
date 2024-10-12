import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, tap, throwError } from 'rxjs';
import { Router } from '@angular/router';
import { catchError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MaterialService {

  private url = 'http://127.0.0.1:8000/api';
  private accessTokenKey = 'access';
  private refreshTokenKey = 'refresh';
  private userKey = 'user';  // Clave para almacenar la información del usuario
  private user: any = null; // Guardar el perfil del usuario en memoria

  constructor(private http: HttpClient, private route: Router) { }



  getDocuments() {
    const url = this.url + '/documents/'
    return this.http.get(url);
  }
  
  getSuggestedDocuments(id:string){
    const url = this.url + '/documents_suggested/' + id
    return this.http.get(url);
  }

  getFolders(id:string) {
    const url = this.url + '/last_folders_modified/' + id
    return this.http.get(url);
  }

  updateEstado(id: string, dataState: any) {
    const url = this.url + '/update/estado/' + id
    return this.http.put(url, dataState);
  }

  updateStateDocument(id: string, dataState: any) {
    const url = this.url + '/update/state/' + id
    return this.http.put(url, dataState);
  }



  //*? de aca para abajo esta todo relacionado con los Usuarios, deberiamos Colocarlo en otro servicio 
  //? apartado que sea por ejemplo UsuarioService

  registrarUsuario(formData: any): Observable<any> {//ESTO ES NUEVO, MANEJO LOS ERRORES EN EL POST
    const url = this.url + '/registro/';
    return this.http.post(url, formData).pipe(
      catchError((error: HttpErrorResponse) => {
        return throwError(error);
      })
    );
  }

  getUsers() {
    const url = this.url + '/users/';
    return this.http.get(url);
  }

  getUserProfile(id: number): Observable<any> {
    const url = this.url + '/user_profile/' + id;
    const headers = this.getHeader(); //obtengo el header
    return this.http.get(url, { headers }); //agrego el header en la peticion para la autenticacion
  }

  loginUser(username: string, password: string): Observable<any> {
    const url = this.url + '/login/';
    return this.http.post<any>(url, { username, password }).pipe(tap(response => {
      if (response.access && response.refresh) {
        this.setTokens(response.access, response.refresh);
        this.loadUser();
      }
    }
    ));;
  }

  private setTokens(access: string, refresh: string): void {
    localStorage.setItem(this.accessTokenKey, access);//seteo el valor del accessTokenKey con el valor del parametro access
    localStorage.setItem(this.refreshTokenKey, refresh);
  }

  private getAccessTokenKey(): string | null {
    return localStorage.getItem(this.accessTokenKey);
  }

  private getRefreshTokenKey(): string | null {
    return localStorage.getItem(this.refreshTokenKey);
  }

  isAuthenticated(): boolean {
    const token = this.getAccessTokenKey();
    if (!token)
      return false;
    const payload = JSON.parse(atob(token.split('.')[1]));
    const exp = payload.exp * 1000;
    return Date.now() < exp;
  }

  logout(): void {
    localStorage.removeItem(this.accessTokenKey);
    localStorage.removeItem(this.refreshTokenKey);
    localStorage.removeItem(this.userKey);
    this.user = null; // Limpiar los datos del usuario de la memoria
    this.route.navigate(['/login']);//aqui me redirecciona ala pantalla login
  }

  //NUEVO
  getUserIdToken(): number | null {//este metodo me devuelve el id del user que esta en el access token
    const token = this.getAccessTokenKey();
    if (token) {
      const payload = JSON.parse(atob(token.split('.')[1]));  // Decodifica la parte del payload del token
      return payload.user_id;//el JWT tiene el id del usuario en el campo 'user_id'
    }
    return null;
  }

  //NUEVO
  private getHeader(): HttpHeaders {
    const token = this.getAccessTokenKey();//obtiene el token de acceso almacenado en localStorage
    if (token) {
      return new HttpHeaders({
        'Authorization': `Bearer ${token}`//si el token existe, lo agrego en el header authorization como bearer <token>
      });
    } else {
      return new HttpHeaders();  // Si no hay token, devuelve un objeto HttpHeaders vacío
    }
  }



  private loadUser(): Promise<void> {
    return new Promise((resolve, reject) => {
      const userId = this.getUserIdToken(); // Obtener el ID del token
  
      if (userId) {
        this.getUserProfile(userId).subscribe(
          (userData: any) => {
            this.user = userData; // Guardar solo en memoria
            resolve(); // Resuelve la promesa
          },
          (error) => {
            console.error('Error al cargar el perfil del usuario', error);
            reject(error); // Rechaza la promesa
          }
        );
      } else {
        console.error('No se pudo obtener el id del usuario del token');
        reject(new Error('ID de usuario no disponible'));
      }
    });
  }


  getUserLocalStorage(): any {//obtengo los datos del usuario desde el localStorage
    return JSON.parse(localStorage.getItem(this.userKey)!);
  }

  getUser(): Promise<any> {
     // const user = this.getUserLocalStorage();
    return this.loadUser().then(() => this.user);
  }
}