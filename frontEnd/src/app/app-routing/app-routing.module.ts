import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { AppRoutingRoutingModule } from './app-routing-routing.module';
import { AdminPanelComponent } from '../components/admin-zone/admin-panel/admin-panel.component';
import { RegistroComponent } from '../components/registro/registro.component';
import { LoginComponent } from '../components/login/login.component';
import { HomeComponent } from '../components/home/home.component';

//defino en routes las rutas de mi proyecto
const routes: Routes = [
  { path: 'admin', component: AdminPanelComponent },
  { path: 'registro', component: RegistroComponent },
  { path: 'login',component: LoginComponent},
  { path: 'home',component: HomeComponent}
];

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    AppRoutingRoutingModule,
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
