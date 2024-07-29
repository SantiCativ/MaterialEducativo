import { Component, Output, Input,EventEmitter } from '@angular/core';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrls: ['./topbar.component.css']
})
export class TopbarComponent {

  @Output() filterChanged = new EventEmitter<string>();
  @Input() table: string = '';
  nameAndEmail:string=''

  filterState(state: string) {
    this.filterChanged.emit(state);
  }

}