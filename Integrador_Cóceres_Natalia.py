# Alumna: Cóceres Natalia
# Tp Integrador: Gestión de Datos de Países en Python:
#  filtros, ordenamientos y estadísticas
#========================================================

import csv

def cargar_datos_csv(nombre_archivo):
    """Abre el archivo csv,
      y los guarda en una lista de diccionarios"""
    
    lista_paises = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8-sig", newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                print(f"Leyendo: {fila.get('nombre')}")
                try:
                    pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                    }
                    lista_paises.append(pais)
                except ValueError:
                    print(f"Error: datos numéricos inválidos en '{fila.get('nombre')}', se omite esa fila.")

        print("\nTodos los países se cargaron correctamente")
    
    except FileNotFoundError:
      print(f"\nError: No se pudo encontrar el archivo llamado '{nombre_archivo}'")
      print(f"Asegurate de que esté en la misma carpeta que tu código")
      return False
    
    return lista_paises

def mostrar_paises(lista_paises):
  """
  Recorre la lista de paises
   y los muestra en la pantalla"""

  try:
    if len(lista_paises) == 0:
        print("No hay países cargados")
    else: 
        print()
        print(f"{'Nombre':<15} | {'Población':<12} | {'Superficie':<12} | {'Continente'}")  
        print("------------------------------------------------------------")          

        for pais in lista_paises:
            print(f"{pais['nombre']:<15} | {pais['poblacion']:<12} | {pais['superficie']:<12} | {pais['continente']}")
        print("------------------------------------------------------------")          
            
  except KeyError:
     print("\nLos datos no son correctos")
  except Exception as e:
     print(f"\nOcurrió un problema inesperado al mostar los países: {e}")

def buscar_pais(lista_paises):
    """Busca países en la lista por el nombre ingresado
      por el usuario, permite coincidencias parciales"""

    while True:
        busqueda = input("Ingresá el nombre del país a buscar: ").strip()
   
        if busqueda == "":
            print("Error: No ingresaste ningún nombre para buscar.")
            continue

        encontrado = False
    
        try:
            print("\n--- RESULTADOS DE LA BÚSQUEDA ---\n")
            for pais in lista_paises:
                if busqueda.lower() in pais["nombre"].lower():     
                    print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")    
                    encontrado = True 
                    
            if not encontrado:
                print(f"No se encontraron países que coincidan con '{busqueda}'.")
                continue

            break

        except KeyError:
            print("\nError: Se buscó una etiqueta de diccionario que no existe.")
            continue

def agregar_pais(lista_paises):
    """
    Pide los datos al usuario y agrega un nuevo país a la lista.
    """
    print("\n--- AGREGAR NUEVO PAÍS ---\n")
    
    nombre = input("Nombre del país: ").strip()

    while nombre == "":
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Nombre del país: ").strip()

    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"\nError: '{nombre}' ya está en la lista (como '{pais['nombre']}'). No se agregó.")
            return
        
    continente = input("Continente: ").strip()
    while continente == "":
        print("Error: El continente no puede estar vacío.")
        continente = input("Continente: ").strip()

    while True:
        poblacion = input("Población: ").strip()
        
        if poblacion == "":
            print("Error: La población no puede estar vacía.")
            continue
        try:
            poblacion = int(poblacion)
            break
        except ValueError:
            print("Error: Ingresá únicamente números enteros, sin puntos ni comas")
    
    while True:
        superficie = input("Superficie en km²: ").strip()
        if superficie == "":
            print("Error: La superficie no puede estar vacia")
            continue
        try:
            superficie = int(superficie)
            break
        except ValueError:
            print("Error: La superficie no puede estar vacia")
            superficie = input("Superficie en km²: ").strip()
        
    nuevo_pais = {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente
    }
        
    lista_paises.append(nuevo_pais)
    print(f"\n{nombre} se agregó correctamente a la lista")
    
def actualizar_pais(lista_paises):
    """
    Busca un país por nombre y actualiza su población y superficie.
    """
    while True: 
        print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---\n")
        
        busqueda = input("Ingresá el nombre del país a modificar: ").strip()
        if busqueda == "":
            print("Error: No ingresaste ningún nombre.")
            continue 

        encontrado = False

        for pais in lista_paises:
            if pais["nombre"].lower() == busqueda.lower():
                encontrado = True
                print(f"\nPaís encontrado: {pais['nombre'].upper()}")
                print(f"Datos actuales -> Población: {pais['poblacion']} | Superficie: {pais['superficie']}")

                # Pedir nueva población
                nueva_pob = input("\nNueva población: ").strip()
                if nueva_pob == "":
                    print("Error: La población no puede estar vacía.")
                    break 
                try:
                    nueva_poblacion = int(nueva_pob)
                except ValueError:
                    print("Error: Ingresá únicamente números enteros, sin puntos ni comas")
                    nueva_pob = "" 
                    break
                
                # Pedir nueva superficie
                nueva_sup = input("Nueva superficie en km²: ").strip()
                if nueva_sup == "":
                    print("Error: La superficie no puede estar vacía.")
                    nueva_pob = "" 
                    break
                try: 
                    nueva_superficie = int(nueva_sup)
                except ValueError:
                    print("Error: Ingresá únicamente números enteros para la superficie.")
                    nueva_pob = ""
                    break

                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie
                    
                print(f"\nLos datos de {pais['nombre']} se actualizaron correctamente")
                break 
                    
        if not encontrado or nueva_pob == "":
            if not encontrado:
                print(f"\nNo se encontró ningún país con el nombre '{busqueda}'.")
            continue 
        break
        
def filtrar_paises(lista_paises):
    """
    Muestra un submenú para filtrar países por continente, población o superficie.
    """
    while True:
        print("\n--- FILTRAR PAÍSES ---")
        print("a. Filtrar por Continente")
        print("b. Filtrar por Rango de Población")
        print("c. Filtrar por Rango de Superficie")
        
        sub_opcion = input("Elegí una opción: ").strip().lower()

        if sub_opcion == "a":
            continente_buscado = input("Ingresá el continente a filtrar: ").strip()
            encontrado = False
            
            print(f"\n--- PAÍSES EN EL CONTINENTE: {continente_buscado.upper()} ---\n")
            for pais in lista_paises:

                if continente_buscado.lower() in pais["continente"].lower(): 
                    print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
                    encontrado = True
                    
            if not encontrado:
                print(f"No se encontraron países en el continente '{continente_buscado}'.")
                continue
                
            break

        elif sub_opcion == "b":
            try:
                min_pob = input("Ingresá la población mínima: ").strip()
                max_pob = input("Ingresá la población máxima: ").strip()
                
                if min_pob == "" or max_pob == "":
                    print("Error: Los rangos no pueden estar vacíos.")
                    continue
                    
                min_pob = int(min_pob)
                max_pob = int(max_pob)
                encontrado = False
                
                print(f"\n--- PAÍSES CON POBLACIÓN ENTRE {min_pob} Y {max_pob} ---\n")
                for pais in lista_paises:
                    if min_pob <= pais["poblacion"] <= max_pob:
                        print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Continente: {pais['continente']}")
                        encontrado = True
                        
                if not encontrado:
                    print("No se encontraron países en ese rango de población.")
                    continue                
                break
                    
            except ValueError:
                print("\nError: Ingrese únicamente números enteros para los rangos.")
                continue

        elif sub_opcion == "c":
            try:
                min_sup = input("Ingresá la superficie mínima en km²: ").strip()
                max_sup = input("Ingresá la superficie máxima en km²: ").strip()
                
                if min_sup == "" or max_sup == "":
                    print("Error: Los rangos no pueden estar vacíos.")
                    continue
                    
                min_sup = int(min_sup)
                max_sup = int(max_sup)
                encontrado = False
                
                print(f"\n--- PAÍSES CON SUPERFICIE ENTRE {min_sup} Y {max_sup} km² ---\n")
                
                for pais in lista_paises:
                    if min_sup <= pais["superficie"] <= max_sup:
                        print(f"País: {pais['nombre']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")
                        encontrado = True
                        
                if not encontrado:
                    print("No se encontraron países en ese rango de superficie.")
                    continue
                    
                break
                    
            except ValueError:
                print("\nError: Ingrese únicamente números enteros para los rangos.")
                continue
                
        else:
            print("\nError: Opción de filtrado inválida.")
            continue

def ordenar_paises(lista_paises):
    """
    Muestra un submenú para ordenar países por nombre, población o superficie
    """
    while True: 
        print("\n--- ORDENAR PAÍSES ---")
        print("1. Ordenar por Nombre")
        print("2. Ordenar por Población")
        print("3. Ordenar por Superficie")
        
        criterio = input("Elegí el criterio de ordenamiento (1-3): ").strip()
        
        if criterio not in ["1", "2", "3"]:
            print("Error: Opción de ordenamiento inválida.")
            continue 

        print("\n¿Cómo deseas ordenar?")
        print("A. Ascendente (Menor a Mayor / A-Z)")
        print("D. Descendente (Mayor a Menor / Z-A)")
        
        sentido = input("Elegí el sentido (a o d): ").strip().lower() 
        
        if sentido not in ["a", "d"]:
            print("Error: Sentido inválido.")
            continue 

        try:
            total_paises = len(lista_paises)
            
            for i in range(total_paises):
                for j in range(0, total_paises - i - 1):
                    
                    if criterio == "1":
                        valor_actual = lista_paises[j]["nombre"]
                        valor_siguiente = lista_paises[j+1]["nombre"]
                    elif criterio == "2":
                        valor_actual = lista_paises[j]["poblacion"]
                        valor_siguiente = lista_paises[j+1]["poblacion"]
                    elif criterio == "3":
                        valor_actual = lista_paises[j]["superficie"]
                        valor_siguiente = lista_paises[j+1]["superficie"]

                    debe_intercambiar = False
                    if sentido == "a" and valor_actual > valor_siguiente:
                        debe_intercambiar = True
                    elif sentido == "d" and valor_actual < valor_siguiente:
                        debe_intercambiar = True

                    if debe_intercambiar:
                        temporal = lista_paises[j]
                        lista_paises[j] = lista_paises[j+1]
                        lista_paises[j+1] = temporal

            print("\nLista ordenada correctamente")
            print("Elegí la opción 1 del menú principal para ver el resultado.")
            break 

        except KeyError:
            print("\nError: Se buscó una etiqueta de diccionario que no existe.")
            continue 

def mostrar_estadisticas(lista_paises):
    """
    Calcula y muestra indicadores estadísticos de los países.
    """
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---\n")
    
    total_paises = len(lista_paises)
    
    if total_paises == 0:
        print("No hay países cargados para calcular estadísticas.")
        return

    suma_poblacion = 0
    suma_superficie = 0
    
    pais_mayor_pob = lista_paises[0]
    pais_menor_pob = lista_paises[0]
    
    conteo_continentes = {}

    try:
        for pais in lista_paises:
            suma_poblacion += pais["poblacion"]
            suma_superficie += pais["superficie"]
            
            if pais["poblacion"] > pais_mayor_pob["poblacion"]:
                pais_mayor_pob = pais
                
            if pais["poblacion"] < pais_menor_pob["poblacion"]:
                pais_menor_pob = pais
                
            continente = pais["continente"]
            if continente in conteo_continentes:
                conteo_continentes[continente] += 1
            else:
                conteo_continentes[continente] = 1

        promedio_pob = suma_poblacion / total_paises
        promedio_sup = suma_superficie / total_paises

        print(f"País con mayor población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']} hab.)")
        print(f"País con menor población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']} hab.)")
        print()
        print(f"Promedio de población general: {int(promedio_pob)} habitantes")
        print(f"Promedio de superficie general: {int(promedio_sup)} km²")
        
        print("\nCantidad de países por continente:")
        for cont, cantidad in conteo_continentes.items():
            print(f"- {cont}: {cantidad}")
            
    except KeyError:
        print("\nError: Se buscó una etiqueta de diccionario que no existe.")
        return
    
def guardar_datos_en_csv(nombre_archivo, lista_paises):
    """
    Escribe los datos actualizados de la lista de regreso en el archivo CSV.
    """
    try:
        with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            archivo.write("nombre,poblacion,superficie,continente\n")
            
            for pais in lista_paises:
                nombre = pais["nombre"]
                poblacion = pais["poblacion"]
                superficie = pais["superficie"]
                continente = pais["continente"]
                
                archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")
                
        print("\nLos cambios se guardaron correctamente en el archivo CSV.")
        
    except Exception as e:
        print(f"\nError: No se pudieron guardar los datos: {e}")

def mostrar_menu_principal(lista_paises):
    """
    Mantiene el programa abierto en un bucle y llama a las funciones elegidas.
    """
    continuar = True
    opcion = 0

    while continuar:
        print()
        print(" ------- SISTEMA DE GESTIÓN DE PAÍSES ------- ")
        print("1. Mostrar todos los países")
        print("2. Agregar un nuevo país")
        print("3. Actualizar datos de un país")
        print("4. Buscar un país por nombre")
        print("5. Filtrar países")
        print("6. Ordenar países")
        print("7. Mostrar estadísticas")
        print("8. Salir del sistema")
        print("---------------------------------------------")
        
        try:
            opcion = input("Elegí una opción (1-8): ").strip()

            if opcion == "1":
                mostrar_paises(lista_paises)                
            elif opcion == "2":
                agregar_pais(lista_paises)                
            elif opcion == "3":
                actualizar_pais(lista_paises)                
            elif opcion == "4":
                buscar_pais(lista_paises)                
            elif opcion == "5":
                filtrar_paises(lista_paises)                
            elif opcion == "6":
                ordenar_paises(lista_paises)                
            elif opcion == "7":
                mostrar_estadisticas(lista_paises)            
            elif opcion == "8":
                print("\nGuardando los datos antes de cerrar...")
                guardar_datos_en_csv("paises.csv", lista_paises)
                print("¡Gracias por usar el sistema! Saliendo...")
                continuar = False
            else:
                print("\nError: Opción inválida. Por favor, ingresá un número del 1 al 8.")
        
        except ValueError:
            print("Error: Ingrese solo un número entero.")
            opcion = 0
                    
mis_paises = cargar_datos_csv("paises.csv")
mostrar_menu_principal(mis_paises)