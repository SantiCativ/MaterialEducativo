import { Component, OnInit } from '@angular/core';
import { MaterialService } from 'src/app/services/service.service';
import { AlertService } from 'src/app/services/alertas/alert.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  username:string='';
  password:string='';

  constructor(private _Materialservice: MaterialService,private _alertService: AlertService,private router:Router ){}

  ngOnInit(): void {}

  Login():void{
    this._Materialservice.loginUser(this.username,this.password).subscribe({
      next: ()=> this.router.navigate(['/home']),
      error: ()=> this._alertService.error('Login fallido')
    })
  }
}
