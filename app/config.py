# # Dejar conexion local para hacer pruebas
# import pymongo
# from pymongo import MongoClient
# import certifi


# def Conexion():
#     try:
#         client = pymongo.MongoClient("mongodb://localhost:27017/")
#         db = client["Red_social"]
#         print('Conecto')
#     except ConnectionError:
#         print('Error de conexion')
#     return db


# Conexion()


# descomentar con control+k+u
# comentar con control+k+c


# coneccion baquuero#############################################################################
from pymongo import MongoClient
import certifi

MONGO='mongodb+srv://bbaqueroalonso:brayanbaquero@cluster0.7hl6pdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'#string de mongo
certificado=certifi.where()

def conexion ():
    try:
        client= MongoClient(MONGO,tlsCAFile=certificado)
        bd = client["Bd_seguridad"]
        print('conexion exitosa')
    except ConnectionError:
        print('error de conexion')
    return bd


conexion()
