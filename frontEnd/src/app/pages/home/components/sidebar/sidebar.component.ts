import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sidebar-h',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponentHome implements OnInit {

  constructor() { }

  ngOnInit() {
  }
 
    
  isDropdownActive = false;

  // Alterna la visibilidad del dropdown
  toggleDropdown() {
    this.isDropdownActive = !this.isDropdownActive;
  }

}
