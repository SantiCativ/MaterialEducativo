import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RegistroComponent } from './pages/registro/registro.component'; 
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';

import { NgxPaginationModule} from 'ngx-pagination';

//componentes

import { AdminPanelComponent } from './pages/admin-panel/admin-panel.component';
import { TopbarComponent } from './pages/admin-panel/components/topbar/topbar.component'; 
import { SidebarComponent } from './pages/admin-panel/components/sidebar/sidebar.component';
import { UsersTableComponent } from './pages/admin-panel/components/users-table/users-table.component'; 
import { DocumentsTableComponent } from './pages/admin-panel/components/documents-table/documents-table.component'; 
import { LoginComponent } from './pages/login/login.component';

//home
import { HomeComponent } from './pages/home/home.component'; 
import { PaginaPrincipalComponent } from './pages/home/components/pagina-principal/pagina-principal.component';
import { DocumentsComponent } from './pages/home/components/pagina-principal/components/documento/documents.component';
import { FiltersComponent } from './pages/home/components/pagina-principal/components/filters/filters.component';
import { SidebarComponentHome } from './pages/home/components/sidebar/sidebar.component';
import { NavbarComponent } from './pages/home/components/navbar/navbar.component';
import { FoldersComponent } from './pages/home/components/pagina-principal/components/folders/folders.component';
import { FavoritoComponent } from './pages/home/components/favorito/favorito.component';
import { RecientesComponent } from './pages/home/components/recientes/recientes.component';
import { MiUnidadComponent } from './pages/home/components/mi-unidad/mi-unidad.component';


import { BrowserAnimationsModule } from '@angular/platform-browser/animations'; 
//componentes angular material
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatDividerModule } from '@angular/material/divider';
import { MatButtonModule } from '@angular/material/button';
import { MatMenuModule } from '@angular/material/menu';
import { MatTableModule } from '@angular/material/table';
import { MatSortModule } from '@angular/material/sort';
import { MatPaginatorModule } from '@angular/material/paginator';


@NgModule({
  
  declarations: [
    
    AppComponent,
    HomeComponent,
    RegistroComponent,
    AdminPanelComponent,
    TopbarComponent,
    SidebarComponent,
    UsersTableComponent,
    DocumentsTableComponent,
    LoginComponent,
    NavbarComponent,
    FoldersComponent,
    DocumentsComponent,
    SidebarComponentHome,
    FiltersComponent,
    PaginaPrincipalComponent,
    MiUnidadComponent,
    FavoritoComponent,
    RecientesComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgxPaginationModule,
    BrowserAnimationsModule,
    MatListModule,
    MatIconModule,
    MatDividerModule,
    MatButtonModule,
    MatMenuModule,
    MatTableModule,
    MatSortModule,
    MatPaginatorModule,
    MatIconModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
