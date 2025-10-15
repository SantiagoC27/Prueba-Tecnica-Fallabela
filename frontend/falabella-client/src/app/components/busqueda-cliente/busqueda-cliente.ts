import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-busqueda-cliente',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './busqueda-cliente.html',
  styleUrls: ['./busqueda-cliente.css']
})
export class BusquedaCliente {
  tipoDocumento = 'CC';
  numeroDocumento = '';
  cliente: any = null;
  compras: any[] = [];

  constructor(private http: HttpClient) {}

  buscarCliente(event: Event) {
    event.preventDefault();

    this.http.get<any>(`http://127.0.0.1:5000/api/clientes/${this.tipoDocumento}/${this.numeroDocumento}`)
      .subscribe({
        next: (data) => {
          this.cliente = data.cliente;
          this.compras = data.compras;
        },
        error: () => {
          alert('Cliente no encontrado');
          this.limpiarFormulario();
        }
      });
  }

  exportar() {
    window.open(`http://127.0.0.1:5000/api/reporte_fidelizacion`, '_blank');
  }

  limpiarFormulario() {
    this.numeroDocumento = '';
    this.tipoDocumento = 'CC';
    this.cliente = null;
    this.compras = [];
  }
}
