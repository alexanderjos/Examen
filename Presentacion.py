#Presentacion.py
def mostrar_menu_VC():
    print("Seleccione un producto:")
    print("[1] Pepsi (S/. 2.50)")
    print("[2] Fanta (S/. 2.80)")
    print("[3] Coca-Cola (S/. 3.20)")
    print("[4] Salir")

def mensaje_insuficiente_VC():
    print("Importe insuficiente. Gracias.")

def mensaje_despachado_VC():
    print("Despachando...")

def mostrar_vuelto_VC(monedas):
    print("Vuelto entregado:")
    for valor, cantidad in monedas.items():
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de S/. {valor}")

def mensaje_no_monedas_VC():
    print("Lo sentimos, no contamos con monedas para el vuelto.")
    
def solicitar_importeVC():
    monto = 0.0
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            if monto < 0:
                print("El monto ingresado no puede ser menor a 0")
                continue
            break
        except :
            print("Ingrese un valor numerico")
    return monto

def mostrar_reporte_VC(movimientos):
    print("\nReporte de Movimientos:")
    for movimiento in movimientos:
        producto, precio, pago, vuelto = movimiento
        vuelto_mostrar = vuelto if vuelto else 0
        print(f"Producto: {producto}, Precio: S/. {precio}, Importe: S/. {pago}, Vuelto: S/. {round(vuelto_mostrar, 2)}")