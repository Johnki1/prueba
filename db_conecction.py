from pymongo import MongoClient

client = MongoClient("mongodb://mongo:miOOkXpHHVMfhXpmbosXNPOuaimLGUCy@mongodb.railway.internal:27017")


db = client.TallerMongoDB

def set_database(nombre_db: str):
    global db
    db = client[nombre_db]
    print(f"Base de datos cambiada a '{nombre_db}' (se creará al insertar el primer documento).")

def get_database():
    return db
