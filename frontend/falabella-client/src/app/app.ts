import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BusquedaCliente } from './components/busqueda-cliente/busqueda-cliente';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, BusquedaCliente],
  template: `
    <div class="container mt-4">
      <h2 class="text-center mb-4 text-primary">Sistema de Consulta de Clientes</h2>
      <app-busqueda-cliente></app-busqueda-cliente>
    </div>
  `
})
export class App {}
