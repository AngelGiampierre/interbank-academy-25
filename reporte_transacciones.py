"""
Aplicación CLI para procesar transacciones bancarias desde un archivo CSV y generar un reporte con balance final, transacción de mayor monto y conteo por tipo.
"""

import csv
import os

def leer_archivo_csv(nombre_archivo):
    """
    Lee un archivo CSV y devuelve una lista de diccionarios con los datos.
    
    Args:
        nombre_archivo: Ruta al archivo CSV a leer
        
    Returns:
        Lista de diccionarios con los datos del archivo CSV
    """
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return []

def calcular_balance_final(transacciones):
    """
    Calcula el balance final sumando los créditos y restando los débitos.
    
    Args:
        transacciones: Lista de transacciones
        
    Returns:
        Balance final
    """
    balance = 0.0
    for transaccion in transacciones:
        monto = float(transaccion['monto'])
        if transaccion['tipo'] == 'Crédito':
            balance += monto
        elif transaccion['tipo'] == 'Débito':
            balance -= monto
    return balance

def encontrar_transaccion_mayor_monto(transacciones):
    """
    Encuentra la transacción con el mayor monto.
    
    Args:
        transacciones: Lista de transacciones
        
    Returns:
        Tupla con el ID y el monto de la transacción de mayor monto
    """
    if not transacciones:
        return "", 0.0
    
    transaccion_mayor = max(transacciones, key=lambda t: float(t['monto']))
    return transaccion_mayor['id'], float(transaccion_mayor['monto'])

def contar_transacciones_por_tipo(transacciones):
    """
    Cuenta el número de transacciones por tipo.
    
    Args:
        transacciones: Lista de transacciones
        
    Returns:
        Diccionario con el conteo de transacciones por tipo
    """
    conteo = {"Crédito": 0, "Débito": 0}
    for transaccion in transacciones:
        tipo = transaccion['tipo']
        if tipo in conteo:
            conteo[tipo] += 1
    return conteo

def generar_reporte(transacciones):
    """
    Genera y muestra el reporte de transacciones.
    
    Args:
        transacciones: Lista de transacciones
    """
    balance_final = calcular_balance_final(transacciones)
    id_mayor, monto_mayor = encontrar_transaccion_mayor_monto(transacciones)
    conteo = contar_transacciones_por_tipo(transacciones)
    
    print("Reporte de Transacciones")
    print("---------------------------------------------")
    print(f"Balance Final: {balance_final:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {monto_mayor:.2f}")
    print(f"Conteo de Transacciones: Crédito: {conteo['Crédito']} Débito: {conteo['Débito']}")

def main():
    """Función principal del programa."""
    # Por defecto, leer el archivo data.csv
    archivo_csv = "data.csv"
    
    # Comprobar si el archivo existe
    if not os.path.exists(archivo_csv):
        print(f"Error: No se encontró el archivo '{archivo_csv}'")
        return
    
    # Leer transacciones y generar reporte
    transacciones = leer_archivo_csv(archivo_csv)
    if transacciones:
        generar_reporte(transacciones)

if __name__ == "__main__":
    main()
