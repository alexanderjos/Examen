class AJAProducto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_vuelto_VC(self, pago, inventario_monedas):
        if pago < self.precio:
            return "insuficiente", "Error: El pago es insuficiente."
        elif pago == self.precio:
            return "exacto", "No hay vuelto, pago exacto."
        else:
            vuelto = round(pago - self.precio, 2)
            monedas = self.calcular_monedas_VC(vuelto, inventario_monedas)
            if monedas == "Error":  # Si no se puede dar el vuelto completo
                return "sin_monedas", "Error: No hay suficientes monedas para dar el vuelto."
            elif monedas:
                return "con_vuelto", monedas
            else:
                return "sin_monedas", "Error: No se pudo calcular el vuelto con las monedas disponibles."

    def calcular_monedas_VC(self, vuelto, inventario_monedas):
        monedas_a_devolver = {}  # Diccionario para almacenar el vuelto calculado
        for valor in sorted(inventario_monedas.keys(), reverse=True):  # Ordenar por valor, de mayor a menor
            if vuelto >= valor:
                cantidad_requerida = int(vuelto // valor)  # Cuántas monedas de este valor se necesitan
                cantidad_disponible = inventario_monedas.get(valor, 0)  # Cuántas monedas hay disponibles

                cantidad_a_usar = min(cantidad_requerida, cantidad_disponible)  # Usar la menor cantidad
                if cantidad_a_usar > 0:
                    monedas_a_devolver[valor] = cantidad_a_usar

                vuelto = round(vuelto - cantidad_a_usar * valor, 2)  # Reducir el vuelto restante

        # Si el vuelto fue cubierto completamente, retornamos las monedas
        if vuelto == 0:
            return monedas_a_devolver
        else:
            return "Error"  # Retornar un mensaje de error si no se puede cubrir el vuelto
