import { Component, Input, Output, OnInit, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrls: ['./topbar.component.css']
})
export class TopbarComponent implements OnInit {
  @Input() data: any[] = [];
  @Output() filterChanged = new EventEmitter<string>();
  dataCopia: any[] = [];


  ngOnInit(): void {

  }

  filterState(state: string) {
    this.filterChanged.emit(state);
  }

}