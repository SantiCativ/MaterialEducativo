import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RegistroComponent } from './components/registro/registro.component';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
//componentes
import { HomeComponent } from './components/home/home.component';
import { AdminPanelComponent } from './components/admin-panel/admin-panel.component';
import { TopbarComponent } from './components/admin-panel/topbar/topbar.component';
import { SidebarComponent } from './components/admin-panel/sidebar/sidebar.component';
import { TableComponent } from './components/admin-panel/table/table.component';

@NgModule({
  
  declarations: [
    
    AppComponent,
    HomeComponent,
    RegistroComponent,
    AdminPanelComponent,
    TopbarComponent,
    SidebarComponent,
    TableComponent,
  
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
   
  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
