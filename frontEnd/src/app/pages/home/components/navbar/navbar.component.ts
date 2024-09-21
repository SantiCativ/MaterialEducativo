import { Component,OnInit } from '@angular/core';
import { MaterialService } from 'src/app/services/service.service';
import { Router } from '@angular/router';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  constructor(private _Materialservice: MaterialService,private router:Router){}
  ngOnInit(): void {}

  Logout():void{
    this._Materialservice.logout();}
    
  Login():void{
    this.router.navigate(['/login']);
  }
}
