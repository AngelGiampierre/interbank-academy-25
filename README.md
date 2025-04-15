# Reporte de Transacciones Bancarias

## Introducción
Aplicación CLI que procesa transacciones bancarias desde un archivo CSV y genera un reporte con balance final, transacción de mayor monto y conteo por tipo de transacción (Crédito/Débito).

## Instrucciones de Ejecución
No requiere dependencias externas, solo Python 3.

```bash
# Asegúrate de tener un archivo data.csv en el mismo directorio
python reporte_transacciones.py
```

## Enfoque y Solución
- Lectura del archivo CSV usando el módulo csv de Python
- Procesamiento de datos en memoria para calcular métricas
- Diseño modular con funciones independientes para cada cálculo
- Manejo básico de errores para archivos inexistentes o formato incorrecto
- Enfoque simple sin dependencias externas

## Estructura del Proyecto
- `reporte_transacciones.py`: Script principal con toda la lógica
- `data.csv`: Archivo de datos de ejemplo
  
El formato del CSV debe ser:
```
id,tipo,monto
1,Crédito,100.00
2,Débito,50.00
...
```