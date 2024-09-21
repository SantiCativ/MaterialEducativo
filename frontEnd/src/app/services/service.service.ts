import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
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

  constructor(private http: HttpClient, private route: Router) { }

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
  getDocuments(){
    const url=this.url+'/documents/'
    return this.http.get(url);
  }

  updateEstado(id: string,dataState:any) {
    const url = this.url + '/update/estado/' + id
    return this.http.put(url,dataState);
  }

  updateStateDocument(id:string,dataState:any){
    const url = this.url + '/update/state/' + id
    return this.http.put(url,dataState);
  }

  loginUser(username: string, password: string): Observable<any> {
    const url = this.url + '/login/';
    return this.http.post<any>(url, { username, password }).pipe(tap(response => {
      if (response.access && response.refresh) {
        this.setTokens(response.access, response.refresh);
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
    this.route.navigate(['/login']);//aqui me redirecciona ala pantalla login
  }
}