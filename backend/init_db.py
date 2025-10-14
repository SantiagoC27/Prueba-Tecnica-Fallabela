from datetime import date
from app import db, app
from models import TipoDocumento, Cliente, Producto, Compra, DetalleCompra

with app.app_context():
    print("Eliminando base de datos existente...")
    db.drop_all()

    print("Creando tablas...")
    db.create_all()

    # =============================
    #   TIPOS DE DOCUMENTO
    # =============================
    print("Cargando tipos de documento...")
    tipos = [
        TipoDocumento(nombre='CC'),
        TipoDocumento(nombre='NIT'),
        TipoDocumento(nombre='PAS')
    ]
    db.session.add_all(tipos)
    db.session.commit()

    # =============================
    #   CLIENTES
    # =============================
    print("Creando clientes...")
    cliente1 = Cliente(
        tipo_documento_id=tipos[0].id,
        numero_documento='12345678',
        nombre='Juan',
        apellido='Pérez',
        email='juan.perez@example.com',
        telefono='3001234567'
    )

    cliente2 = Cliente(
        tipo_documento_id=tipos[0].id,
        numero_documento='87654321',
        nombre='María',
        apellido='López',
        email='maria.lopez@example.com',
        telefono='3009876543'
    )

    cliente3 = Cliente(
        tipo_documento_id=tipos[1].id,
        numero_documento='900456789',
        nombre='Comercial ABC S.A.S.',
        apellido='',
        email='contacto@abc.com',
        telefono='6015554321'
    )

    cliente4 = Cliente(
        tipo_documento_id=tipos[0].id,
        numero_documento='11223344',
        nombre='Carlos',
        apellido='Gómez',
        email='carlos.gomez@example.com',
        telefono='3011122334'
    )

    cliente5 = Cliente(
        tipo_documento_id=tipos[2].id,
        numero_documento='A987654',
        nombre='Laura',
        apellido='Torres',
        email='laura.torres@example.com',
        telefono='3029988776'
    )

    db.session.add_all([cliente1, cliente2, cliente3, cliente4, cliente5])
    db.session.commit()

    # =============================
    #   PRODUCTOS
    # =============================
    print("Cargando productos...")
    producto1 = Producto(nombre='Celular Samsung Galaxy', precio=1500000)
    producto2 = Producto(nombre='Audífonos Bluetooth', precio=200000)
    producto3 = Producto(nombre='Televisor LG 50"', precio=2500000)
    producto4 = Producto(nombre='Portátil Lenovo', precio=3200000)
    producto5 = Producto(nombre='Consola PlayStation 5', precio=4000000)
    producto6 = Producto(nombre='Silla Ergonómica', precio=800000)
    producto7 = Producto(nombre='Smartwatch Huawei', precio=900000)

    db.session.add_all([producto1, producto2, producto3, producto4, producto5, producto6, producto7])
    db.session.commit()

    # =============================
    #   COMPRAS
    # =============================
    print("Creando compras...")
    compra1 = Compra(cliente_id=cliente1.id, fecha=date(2025, 9, 10), total=1700000)
    compra2 = Compra(cliente_id=cliente2.id, fecha=date(2025, 9, 12), total=6700000)
    compra3 = Compra(cliente_id=cliente3.id, fecha=date(2025, 9, 15), total=20000000)
    compra4 = Compra(cliente_id=cliente4.id, fecha=date(2025, 9, 18), total=5800000)
    compra5 = Compra(cliente_id=cliente5.id, fecha=date(2025, 9, 22), total=2500000)

    db.session.add_all([compra1, compra2, compra3, compra4, compra5])
    db.session.commit()

    # =============================
    #   DETALLES DE COMPRA
    # =============================
    print("Añadiendo detalles de compra...")

    detalles = [
        DetalleCompra(compra_id=compra1.id, producto_id=producto1.id, cantidad=1, precio_unitario=1500000),
        DetalleCompra(compra_id=compra1.id, producto_id=producto2.id, cantidad=1, precio_unitario=200000),

        DetalleCompra(compra_id=compra2.id, producto_id=producto3.id, cantidad=1, precio_unitario=2500000),
        DetalleCompra(compra_id=compra2.id, producto_id=producto4.id, cantidad=1, precio_unitario=3200000),
        DetalleCompra(compra_id=compra2.id, producto_id=producto6.id, cantidad=1, precio_unitario=1000000),

        DetalleCompra(compra_id=compra3.id, producto_id=producto5.id, cantidad=5, precio_unitario=4000000),

        DetalleCompra(compra_id=compra4.id, producto_id=producto4.id, cantidad=1, precio_unitario=3200000),
        DetalleCompra(compra_id=compra4.id, producto_id=producto7.id, cantidad=1, precio_unitario=900000),
        DetalleCompra(compra_id=compra4.id, producto_id=producto3.id, cantidad=1, precio_unitario=1700000),

        DetalleCompra(compra_id=compra5.id, producto_id=producto1.id, cantidad=1, precio_unitario=1500000),
        DetalleCompra(compra_id=compra5.id, producto_id=producto2.id, cantidad=1, precio_unitario=200000),
        DetalleCompra(compra_id=compra5.id, producto_id=producto7.id, cantidad=1, precio_unitario=800000),
    ]

    db.session.add_all(detalles)
    db.session.commit()

    print("Base de datos inicializada correctamente.")
