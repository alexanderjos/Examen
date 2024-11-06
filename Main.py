from Presentacion import *
from Clase import *
def mostrar_inventario_monedas_VC(inventario_monedas):
    print("\nInventario de Monedas:")
    for valor, cantidad in inventario_monedas.items():
        print(f"S/. {valor}: {cantidad} moneda(s) disponibles")

def actualizar_inventario_monedas_VC(inventario_monedas, monedas_usadas):
    for valor, cantidad in monedas_usadas.items():
        if valor in inventario_monedas:
            inventario_monedas[valor] -= cantidad
            if inventario_monedas[valor] < 0:
                inventario_monedas[valor] = 0

try:
    inventario_monedas = {5: 1, 2: 1, 1: 1, 0.5: 1, 0.2: 1, 0.1: 1}

    productos = {
        1: AJAProducto("Pepsi", 2.50),
        2: AJAProducto("Fanta", 2.80),
        3: AJAProducto("Coca-Cola", 3.20)
    }

    movimientos = list()  # Para almacenar los movimientos

    while True:
        mostrar_menu_VC()  # Mostrar el menú principal
        opcion = int(input("Elige una opción: "))
        
        # Opción para salir
        if opcion == 4:
            break
        
        # Mostrar inventario de monedas
        elif opcion == 5:
            mostrar_inventario_monedas_VC(inventario_monedas)
        
        # Selección de productos
        elif opcion in productos:
            producto = productos[opcion]
            pago = solicitar_importeVC()

            # Calcular el vuelto
            resultado, monedas = producto.calcular_vuelto_VC(pago, inventario_monedas)
            
            if resultado == "insuficiente":
                mensaje_insuficiente_VC()
                mostrar_reporte_VC(movimientos)
                break  # Termina el programa si el pago es insuficiente
            
            elif resultado == "exacto":
                mensaje_despachado_VC()
                movimientos.append((producto.nombre, producto.precio, pago, 0))
                mostrar_reporte_VC(movimientos)
                break  # Termina si el pago es exacto

            elif resultado == "sin_monedas":
                # Mensaje de error por falta de monedas para el vuelto
                mensaje_no_monedas_VC()  # Mostrar mensaje de no hay monedas suficientes
                mostrar_reporte_VC(movimientos)
                break  # Termina el programa si no hay monedas suficientes

            elif resultado == "con_vuelto":
                # Verificar si el inventario tiene suficientes monedas
                mensaje_despachado_VC()
                mostrar_vuelto_VC(monedas)
                total_vuelto = sum(valor * cantidad for valor, cantidad in monedas.items())
                movimientos.append((producto.nombre, producto.precio, pago, total_vuelto))
                actualizar_inventario_monedas_VC(inventario_monedas, monedas)  # Actualizar inventario
        else:
            print("Opción no válida.")
except :
    print(f"Ocurrió un error")
