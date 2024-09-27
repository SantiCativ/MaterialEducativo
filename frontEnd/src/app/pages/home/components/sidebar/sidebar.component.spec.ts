/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { SidebarComponentHome } from './sidebar.component';

describe('SidebarComponent', () => {
  let component: SidebarComponentHome;
  let fixture: ComponentFixture<SidebarComponentHome>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SidebarComponentHome ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SidebarComponentHome);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
