
import json
from datetime import datetime
from db_connection import get_database, set_database

def crear_base_de_datos():
    nombre_db = input("Ingrese el nombre de la base de datos: ")
    set_database(nombre_db)

def crear_coleccion():
    db = get_database()
    nombre_coleccion = input("Ingrese el nombre de la colección a crear: ")
    if nombre_coleccion in db.list_collection_names():
        print(f"La colección '{nombre_coleccion}' ya existe.")
    else:
        db.create_collection(nombre_coleccion)
        print(f"Colección '{nombre_coleccion}' creada exitosamente.")

def insertar_documento():
    db = get_database()
    nombre_coleccion = input("Ingrese el nombre de la colección donde insertar: ")
    if nombre_coleccion not in db.list_collection_names():
        print("La colección no existe. Primero créala.")
        return

    print("Ingrese el documento en formato JSON (ejemplo: {\"nombre\": \"Producto A\", \"precio\": 100}):")
    entrada = input()
    try:
        documento = json.loads(entrada)
    except json.JSONDecodeError:
        print("El formato JSON no es válido.")
        return

    resultado = db[nombre_coleccion].insert_one(documento)
    print(f"Documento insertado con _id: {resultado.inserted_id}")

def ver_documentos():
    db = get_database()
    nombre_coleccion = input("Ingrese el nombre de la colección a consultar: ")
    if nombre_coleccion not in db.list_collection_names():
        print("La colección no existe.")
        return

    filtro_input = input("Ingrese el filtro en formato JSON (o presione Enter para sin filtro): ")
    if filtro_input.strip() == "":
        filtro = {}
    else:
        try:
            filtro = json.loads(filtro_input)
        except json.JSONDecodeError:
            print("Filtro JSON inválido. Se usará sin filtro.")
            filtro = {}

    proyeccion_input = input("Ingrese la proyección en formato JSON (o presione Enter para todos los campos): ")
    if proyeccion_input.strip() == "":
        proyeccion = None
    else:
        try:
            proyeccion = json.loads(proyeccion_input)
        except json.JSONDecodeError:
            print("Proyección JSON inválida. Se mostrarán todos los campos.")
            proyeccion = None

    cursor = db[nombre_coleccion].find(filtro, proyeccion)
    print(f"Documentos en la colección '{nombre_coleccion}':")
    for doc in cursor:
        print(doc)

def actualizar_documento():
    db = get_database()
    nombre_coleccion = input("Ingrese el nombre de la colección a actualizar: ")
    if nombre_coleccion not in db.list_collection_names():
        print("La colección no existe.")
        return

    print("Ingrese el filtro para seleccionar el documento en formato JSON:")
    filtro_input = input()
    try:
        filtro = json.loads(filtro_input)
    except json.JSONDecodeError:
        print("Filtro JSON inválido.")
        return

    print("Ingrese los campos a actualizar en formato JSON (ejemplo: {\"precio\": 150}):")
    update_input = input()
    try:
        update_fields = json.loads(update_input)
    except json.JSONDecodeError:
        print("Formato JSON inválido para actualización.")
        return

    opcion = input("¿Desea actualizar un solo documento (1) o múltiples documentos (2)? [1/2]: ")
    if opcion == "1":
        resultado = db[nombre_coleccion].update_one(filtro, {"$set": update_fields})
        print(f"Documentos modificados: {resultado.modified_count}")
    elif opcion == "2":
        resultado = db[nombre_coleccion].update_many(filtro, {"$set": update_fields})
        print(f"Documentos modificados: {resultado.modified_count}")
    else:
        print("Opción no válida.")

def eliminar_documento():
    db = get_database()
    nombre_coleccion = input("Ingrese el nombre de la colección para eliminar documentos: ")
    if nombre_coleccion not in db.list_collection_names():
        print("La colección no existe.")
        return

    print("Ingrese el filtro en formato JSON para eliminar (ejemplo: {\"nombre\": \"Producto A\"}):")
    filtro_input = input()
    try:
        filtro = json.loads(filtro_input)
    except json.JSONDecodeError:
        print("Filtro JSON inválido.")
        return

    opcion = input("¿Desea eliminar un solo documento (1) o múltiples documentos (2)? [1/2]: ")
    if opcion == "1":
        resultado = db[nombre_coleccion].delete_one(filtro)
        print(f"Documentos eliminados: {resultado.deleted_count}")
    elif opcion == "2":
        resultado = db[nombre_coleccion].delete_many(filtro)
        print(f"Documentos eliminados: {resultado.deleted_count}")
    else:
        print("Opción no válida.")

def eliminar_coleccion():
    db = get_database()
    nombre_coleccion = input("Ingrese el nombre de la colección a eliminar: ")
    if nombre_coleccion not in db.list_collection_names():
        print("La colección no existe.")
        return

    confirmacion = input(f"¿Está seguro de eliminar la colección '{nombre_coleccion}'? [s/n]: ")
    if confirmacion.lower() == "s":
        db[nombre_coleccion].drop()
        print(f"Colección '{nombre_coleccion}' eliminada.")
    else:
        print("Operación cancelada.")
