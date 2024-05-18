# Dejar conexion local para hacer pruebas
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient
import pymongo
from pymongo import MongoClient
import certifi


def Conexion():
    try:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["Red_social"]
        print('Conecto')
    except ConnectionError:
        print('Error de conexion')
    return db


Conexion()


# MONGO = "mongodb+srv://dbAdmin:JmD3syv14nYqUdUo@redsocial.pejsc3e.mongodb.net/?retryWrites=true&w=majority&appName=Redsocial"
# certificado = certifi.where()
# # Create a new client and connect to the server

# # Send a ping to confirm a successful connection


# def Conexion():
#     try:
#         client = MongoClient(MONGO, server_api=ServerApi('1'))
#         db = client["Red_social"]
#         print('Conecto la coneccion Virtual')
#         print(db)
#     except ConnectionError:
#         print('Error de conexion')

#     return db


# Conexion()

# descomentar con control+k+u
# comentar con control+k+c


# coneccion baquuero#############################################################################
# from pymongo import MongoClient
# import certifi

# MONGO='mongodb+srv://bbaqueroalonso:brayanbaquero@cluster0.7hl6pdy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'#string de mongo
# certificado=certifi.where()

# def conexion ():
#     try:
#         client= MongoClient(MONGO,tlsCAFile=certificado)
#         bd = client["Bd_seguridad"]
#         print('conexion exitosa')
#     except ConnectionError:
#         print('error de conexion')
#     return bd


# conexion()
