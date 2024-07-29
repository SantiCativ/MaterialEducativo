import { Component, EventEmitter, Output } from '@angular/core';
@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {

  @Output() tableSelectionChange = new EventEmitter<string>();

  constructor() { }

  selectTable(tableName: string): void {
    this.tableSelectionChange.emit(tableName);
  }
}


