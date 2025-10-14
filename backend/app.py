from datetime import date, timedelta
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from config import Config
from database import db
from models import Cliente, Compra
import pandas as pd
import io
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

@app.route('/api/clientes/<string:tipo_documento>/<string:documento>', methods=['GET'])
def obtener_cliente(tipo_documento, documento):
    cliente = Cliente.query.filter(
        Cliente.numero_documento == documento,
        Cliente.tipo_documento.has(nombre=tipo_documento)
    ).first()
    
    if not cliente:
        return jsonify({'mensaje': 'Cliente no encontrado'}), 404
    compras = [c.to_dict() for c in cliente.compras]
    return jsonify({'cliente': cliente.to_dict(), 'compras': compras})

@app.route('/api/reporte_fidelizacion', methods=['GET'])
def reporte_fidelizacion():
    hoy = date.today()
    hace_un_mes = hoy - timedelta(days=30)

    resultados = (
        db.session.query(
            Cliente.id,
            Cliente.nombre,
            Cliente.apellido,
            Cliente.email,
            Cliente.telefono,
            Cliente.numero_documento,
            Cliente.tipo_documento_id,
            db.func.sum(Compra.total).label("total_compras")
        )
        .join(Compra, Cliente.id == Compra.cliente_id)
        .filter(Compra.fecha >= hace_un_mes)
        .group_by(Cliente.id)
        .having(db.func.sum(Compra.total) > 5000000)
        .all()
    )

    if not resultados:
        return jsonify({'mensaje': 'No se encontraron clientes para fidelizar en el último mes.'}), 404
    
    data = []
    for r in resultados:
        data.append({
            "Nombre": f"{r.nombre} {r.apellido}",
            "Correo": r.email,
            "Teléfono": r.telefono,
            "Número Documento": r.numero_documento,
            "Monto Total Compras": r.total_compras
        })

    df = pd.DataFrame(data)

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Clientes Fidelización')
        worksheet = writer.sheets['Clientes Fidelización']

        for i, col in enumerate(df.columns):
            max_len = max(df[col].astype(str).map(len).max(), len(col))
            worksheet.set_column(i, i, max_len + 2)

    output.seek(0)

    return send_file(
        output,
        as_attachment=True,
        download_name=f'reporte_fidelizacion_{hoy}.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    
if __name__ == '__main__':
    app.run(debug=True)