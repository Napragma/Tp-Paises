# Alumna: Cóceres Natalia
# Tp Integrador: Gestión de Datos de Países en Python:
#========================================================

import csv

def normalizar(texto):
    """Pasa el texto a minúsculas y le quita las tildes"""
    texto = texto.lower()
    for con, sin in [('á','a'),('é','e'),('í','i'),('ó','o'),('ú','u')]:
        texto = texto.replace(con, sin)
    return texto

def cargar_datos_csv(nombre_archivo):
    """Abre el archivo csv, y los guarda en una lista de diccionarios"""
    lista_paises = []
    try:
        with open(nombre_archivo, mode="r", encoding="utf-8-sig", newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    lista_paises.append({
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    })
                except ValueError:
                    print(f"Error: datos numéricos inválidos en '{fila.get('nombre')}', se omite esa fila.")
        # Confirma que la carga fue exitosa
        print("\nArchivo cargado correctamente")
        return lista_paises
    
    except FileNotFoundError:
        print(f"\nError: No se pudo encontrar el archivo llamado '{nombre_archivo}'")
        print("Se iniciará el sistema con una lista vacía de forma segura.")
        return lista_paises
    
    except Exception as e:
        print(f"\nOcurrió un problema inesperado al cargar el archivo: {e}")    
        return lista_paises
    
def mostrar_paises(lista_paises):
    """Recorre la lista de paises y los muestra en la pantalla"""
    try:
        if len(lista_paises) == 0:
            print("No hay países cargados")
        else: 
            print(f"\n{'Nombre':<15} | {'Población':<12} | {'Superficie':<12} | {'Continente'}")  
            print("-" * 60)          
        
        for pais in lista_paises:
           print(f"{pais['nombre']:<15} | {pais['poblacion']:<12} | {pais['superficie']:<12} | {pais['continente']}")
        print("-" * 60)          
    except KeyError:
        print("\n")
    except Exception as e:
        print(f"\nOcurrió un problema inesperado al mostrar los países: {e}")

def buscar_pais(lista_paises):
    """Busca países usando la normalización del profesor (ignora tildes y mayúsculas)"""
    while True:
        busqueda = input("Ingresá el nombre del país a buscar: ").strip()
        if busqueda == "":
            print("Error: No ingresaste ningún nombre para buscar.")
            continue

        encontrado = False
        print("\n--- RESULTADOS DE LA BÚSQUEDA ---\n")
        for pais in lista_paises:

            if normalizar(busqueda) in normalizar(pais["nombre"]):     
                print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} | Continente: {pais['continente']}")    
                encontrado = True 
                
        if not encontrado:
            print(f"No se encontraron países que coincidan con '{busqueda}'.")
            continue
        break

def agregar_pais(lista_paises):
    """Pide los datos al usuario y agrega un nuevo país evitando repetidos con tildes"""
    print("\n--- AGREGAR NUEVO PAÍS ---\n")
    nombre = input("Nombre del país: ").strip()
    while nombre == "":
        print("Error: El nombre no puede estar vacío.")
        nombre = input("Nombre del país: ").strip()

    repetido = False
    for pais in lista_paises:

        if normalizar(pais["nombre"]) == normalizar(nombre):
            print(f"\nError: '{nombre}' ya está en la lista (como '{pais['nombre']}'). No se agregó.")
            repetido = True
            break
    
    if repetido:
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
            print("Error: Ingresá únicamente números enteros para la superficie.")
        
    lista_paises.append({
        "nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente
    })
    print(f"\n{nombre} se agregó correctamente a la lista")
        
def actualizar_pais(lista_paises):
    """Busca un país ignorando tildes y actualiza su población y superficie."""
    while True: 
        print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---\n")
        busqueda = input("Ingresá el nombre del país a modificar: ").strip()
        if busqueda == "":
            print("Error: No ingresaste ningún nombre.")
            continue 

        encontrado = False
        for pais in lista_paises:

            if normalizar(pais["nombre"]) == normalizar(busqueda):
                encontrado = True
                print(f"\nPaís encontrado: {pais['nombre'].upper()}")
                print(f"Datos actuales -> Población: {pais['poblacion']} | Superficie: {pais['superficie']}")

                while True:
                    nueva_pob = input("\nNueva población: ").strip()
                    if nueva_pob == "":
                        print("Error: La población no puede estar vacía.")
                        continue
                    try:
                        nueva_poblacion = int(nueva_pob)
                        break
                    except ValueError:
                        print("Error: Ingresá únicamente números enteros, sin puntos ni comas")

                while True:
                    nueva_sup = input("Nueva superficie en km²: ").strip()
                    if nueva_sup == "":
                        print("Error: La superficie no puede estar vacía.")
                        continue
                    try: 
                        nueva_superficie = int(nueva_sup)
                        break
                    except ValueError:
                        print("Error: Ingresá únicamente números enteros para la superficie.")

                pais["poblacion"] = nueva_poblacion
                pais["superficie"] = nueva_superficie
                print(f"\nLos datos de {pais['nombre']} se actualizaron correctamente")
                break 
                    
        if not encontrado:
            print(f"\nNo se encontró ningún país con el nombre '{busqueda}'.")
            continue 
        break
                
def filtrar_paises(lista_paises):
    """Muestra un submenú para filtrar países por continente (sin tildes), población o superficie."""
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

                if normalizar(continente_buscado) in normalizar(pais["continente"]): 
                    print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en ese continente.")
            break

        elif sub_opcion == "b":
            while True:
                try:
                    min_pob = int(input("Ingresá la población mínima: ").strip())
                    max_pob = int(input("Ingresá la población máxima: ").strip())
                    break
                except ValueError:
                    print("Error: Ingresá solo números enteros para los rangos.")

            encontrado = False
            print(f"\n--- PAÍSES CON POBLACIÓN ENTRE {min_pob} Y {max_pob} ---\n")
            for pais in lista_paises:
                if pais["poblacion"] >= min_pob and pais["poblacion"] <= max_pob:
                    print(f"País: {pais['nombre']} | Población: {pais['poblacion']} | Continente: {pais['continente']}")
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en este rango de población.")
            break

        elif sub_opcion == "c":
            while True:
                try:
                    min_sup = int(input("Ingresá la superficie mínima (km²): ").strip())
                    max_sup = int(input("Ingresá la superficie máxima (km²): ").strip())
                    break
                except ValueError:
                    print("Error: Ingresá solo números enteros para los rangos.")

            encontrado = False
            print(f"\n--- PAÍSES CON SUPERFICIE ENTRE {min_sup} Y {max_sup} ---\n")
            for pais in lista_paises:
                if pais["superficie"] >= min_sup and pais["superficie"] <= max_sup:
                    print(f"País: {pais['nombre']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en este rango de superficie.")
            break
        else:
            print("Opción inválida. Elegí a, b o c.")

def ordenar_paises(lista_paises):
    """Muestra un submenu para odenar países,
    por nombre, población o superficie"""

    while True:
        print("\n--- ORDENAR PAÍSES ---")
        print("1. Ordenar por Nombre")
        print("2. Ordenar por Población")
        print("3. Ordenar por Superficie")
        
        orden = input("Elegí el criterio de orden (1-3): ").strip() 

        if orden not in ["1, 2, 3"]:
            print("Error: Opción de orden inválido")
            continue

        print("\n¿Cómo deseas ordenar?")
        print("A- Ascendente(Menor a mayor/A-Z)")
        print("B- Ascendente(Menor a mayor/A-Z)")

        sentido = input("Elegí el sentido (A o D): ").strip().lower()
        if sentido not in ["A", "D"]:
            print("Error: Sentido inválido")

        try:
            if len(lista_paises) == 0:
                print("No hay países cargados para ordenar.")
            else:
                total_paises = len(lista_paises)

                for i in range(total_paises):
                    for j in range(0, total_paises - i -1):

                        if orden == "1":
                            valor_actual = lista_paises[j]["nombre"].lower()
                            valor_siguiente = lista_paises[j+1]["nombre"].lower()
                        elif orden == "2":
                            valor_actual = lista_paises[j]["poblacion"].lower()
                            valor_siguiente = lista_paises[j+1]["poblacion"].lower()
                        elif orden == "3":
                            valor_actual = lista_paises[j]["superficie"].lower()
                            valor_siguiente = lista_paises[j+1]["superficie"].lower()

                        intercambio = False
                        if sentido == "a" and valor_actual > valor_siguiente:
                            intercambio = True
                        elif sentido == "d" and valor_actual < valor_siguiente:
                            intercambio = True

                        if intercambio:
                            temporal = lista_paises[j]
                            lista_paises[j] = lista_paises[j+1]
                            lista_paises[j+1] = temporal

                print("\nLista ordenada correctamente")
        except Exception as e:
                print(f"\nOcurrió un problema inesperado al ordenar: {e}")
                print("Elegí la opción 1 del menú principal para ver el resultado")
        break
            
def mostrar_estadisticas(lista_paises):
    """Calcula y muestra los indicadores estadísticos exigidos por la consigna."""
    print("\n--- ESTADÍSTICAS DEL SISTEMA ---\n")
    
    try:
        if len(lista_paises) == 0:
            print("No hay países cargados para calcular estadísticas.")
        else:
            total_paises = len(lista_paises)
            suma_poblacion = 0
            suma_superficie = 0
            
            pais_mayor_pob = lista_paises[0]
            pais_menor_pob = lista_paises[0]
            
            conteo_continentes = {}

            # El bucle recorre los países y hace todos los cálculos juntos
            for pais in lista_paises:
                suma_poblacion = suma_poblacion + pais["poblacion"]
                suma_superficie = suma_superficie + pais["superficie"]
                
                # Compara para encontrar el valor de población más alto                
                if pais["poblacion"] > pais_mayor_pob["poblacion"]:
                    pais_mayor_pob = pais
                    
                # Compara para encontrar el valor de población más bajo
                if pais["poblacion"] < pais_menor_pob["poblacion"]:
                    pais_menor_pob = pais
                    
                # Cuenta cuántos países hay por continente
                continente = pais["continente"]
                if continente in conteo_continentes:
                    conteo_continentes[continente] = conteo_continentes[continente] + 1
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
                
    except Exception as e:
        print(f"\nOcurrió un problema inesperado al calcular las estadísticas: {e}")

def guardar_datos_en_csv(nombre_archivo, lista_paises):
    """Escribe el dato actualizado de la lista de regreso en el archivo CSV."""
    try:
        if len(lista_paises) == 0:
            print("No hay países cargados en la lista para poder guardar.")
        else:
            with open(nombre_archivo, mode='w', encoding='utf-8', newline='') as archivo:
                archivo.write("nombre,poblacion,superficie,continente\n")
                
                # El bucle recorre cada país para registrar su información
                for pais in lista_paises:
                    nombre = pais["nombre"]
                    poblacion = pais["poblacion"]
                    superficie = pais["superficie"]
                    continente = pais["continente"]
                    
                    # Guarda el registro en formato de texto separado por coma
                    archivo.write(f"{nombre},{poblacion},{superficie},{continente}\n")
                    
            print("\nLos cambios guardados correctamente.")
            
    except Exception as e:
        print(f"\nError: No se pudieron guardar los datos: {e}")

#========================================
# MENÚ PRINCIPAL DEL PROGRAMA 
#========================================
 
def mostrar_menu_principal(lista_paises):
    """Mantiene el programa abierto en un bucle y llama a la función elegida."""
    continuar = True

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
                print("\nGuardando la información antes de cerrar...")
             
                # Guarda el registro actual en el archivo de texto 
                guardar_datos_en_csv("paises.csv", lista_paises)

                print("Saliendo del sistema...")
                continuar = False
            else:
                print("\nError: Opción inválida. Por favor, ingresá un número del 1 al 8.")
        
        except Exception as e:
            print(f"\nOcurrió un problema inesperado en el menú: {e}")
                    
# Realiza la carga inicial desde el archivo de texto
mis_paises = cargar_datos_csv("paises.csv")
# Inicia el bucle de la consola interactiva
mostrar_menu_principal(mis_paises)

