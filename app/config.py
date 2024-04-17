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