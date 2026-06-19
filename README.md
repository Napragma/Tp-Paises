# Sistema de Gestión de Países

Este programa es una aplicación de consola desarrollada en Python para la administración, filtrado, ordenamiento y análisis estadístico de un dataset de países. Permite gestionar datos demográficos y geográficos almacenados en un archivo de persistencia CSV.

## Funcionalidades Mínimas

- **Mostrar todos los países:** Listado completo alineado en formato de tabla.
- **Agregar un nuevo país:** Captura y validación de campos obligatorios para evitar registros vacíos o duplicados.
- **Actualizar datos:** Modificación de población y superficie de un país existente.
- **Buscar un país:** Búsqueda flexible por coincidencia exacta o parcial.
- **Filtrar países:** Búsqueda segmentada por continente, rango de población o rango de superficie.
- **Ordenar países:** Clasificación alfabética o numérica en sentido ascendente o descendente.
- **Mostrar estadísticas:** Cálculo automático de promedios, valores máximos, mínimos y conteo por continente.

## Ejemplos de Entrada y Salida

### Ejemplo 1: Filtrar países por Continente (Tolerante a tildes y minúsculas)
**Entrada del usuario:**
```text
Elegí una opción: 5
Elegí una opción: a
Ingresá el continente a filtrar: africa
```
**Salida del sistema:**
```text
--- PAÍSES EN EL CONTINENTE: AFRICA ---

País: Nigeria       | Población: 206139589 | Superficie: 923768
País: Egipto        | Población: 102334404 | Superficie: 1002450
País: Sudáfrica     | Población: 59308690  | Superficie: 1221037
```

### Ejemplo 2: Validación de datos en la Búsqueda
**Entrada del usuario:**
```text
Elegí una opción (1-8): 4
Ingresá el nombre del país a buscar: marruecos
```
**Salida del sistema:**
```text
--- RESULTADOS DE LA BÚSQUEDA ---

No se encontraron países que coincidan con 'marruecos'.
Ingresá el nombre del país a buscar: 
```

## Instrucciones de Uso

Para iniciar la aplicación, se deben seguir las siguientes indicaciones técnicas:

1. Verificar que el entorno local cuente con **Python 3** instalado.
2. Asegurar que el archivo de datos `paises.csv` se encuentre ubicado en el mismo directorio (carpeta) que el script principal de la aplicación.
3. Ejecutar el archivo de código fuente principal denominado `Integrador_Cóceres_Natalia.py` desde la consola de comandos o terminal del sistema operativo.
4. Al iniciar, el sistema realizará la lectura automatizada del dataset y desplegará de forma inmediata el menú interactivo en la terminal.
   
## Integrantes del Proyecto
- Cóceres Natalia

## Enlaces Obligatorios
- **Video Demostrativo:** [LINK DE VIDEO]
- **Documentación Técnica (PDF):** [PDF]

