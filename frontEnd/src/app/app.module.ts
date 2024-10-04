import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RegistroComponent } from './pages/registro/registro.component'; 
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { NgxPaginationModule} from 'ngx-pagination';
                                    import { MatIconModule } from '@angular/material/icon';
//componentes
import { HomeComponent } from './pages/home/home.component'; 
import { AdminPanelComponent } from './pages/admin-panel/admin-panel.component';
import { TopbarComponent } from './pages/admin-panel/components/topbar/topbar.component'; 
import { SidebarComponent } from './pages/admin-panel/components/sidebar/sidebar.component';

import { UsersTableComponent } from './pages/admin-panel/components/users-table/users-table.component'; 
import { DocumentsTableComponent } from './pages/admin-panel/components/documents-table/documents-table.component'; 
import { LoginComponent } from './pages/login/login.component';
import { NavbarComponent } from './pages/home/components/navbar/navbar.component';
import { SidebarComponentHome } from './pages/home/components/sidebar/sidebar.component';
import { TableComponentHome } from './pages/home/components/table/table.component';

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
    SidebarComponentHome,
    TableComponentHome
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    NgxPaginationModule,
    MatIconModule,
  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
