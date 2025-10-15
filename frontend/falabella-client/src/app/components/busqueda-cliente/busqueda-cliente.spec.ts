import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BusquedaCliente } from './busqueda-cliente';

describe('BusquedaCliente', () => {
  let component: BusquedaCliente;
  let fixture: ComponentFixture<BusquedaCliente>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BusquedaCliente]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BusquedaCliente);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
