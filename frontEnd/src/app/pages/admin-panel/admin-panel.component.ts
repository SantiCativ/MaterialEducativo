import { Component } from '@angular/core';
                                            import { SidebarComponent } from './components/sidebar/sidebar.component';

@Component({
  selector: 'app-admin-panel',
  templateUrl: './admin-panel.component.html',
  styleUrls: ['./admin-panel.component.css']
})
export class AdminPanelComponent {

  table: string = ''
  state:string=''

  constructor() { }

  onTableSelectionChange(tableName: string): void {
    this.table = tableName;
  }
  onFilterChanged(state:string): void {
    this.state=state;
  }

}

