# a=float(input("Digite el valor de a"))
# b=float(input("Digite el valor de b"))
# c=float( input("digite el valord e c"))

# # c casteo


# result = ((a**3)*((b**2)-2*(a)*(c)))/(2*b)
# print ("la multiplicacion es: " )
# print(str(result))


# parcial1 =float(input("Coloque la nota de su parcial 1: "))
# parcial2=float(input("Coloque la nota de su parcial 2: "))
# parcial3=float(input("Coloque la nota de su parcial 3: "))
# parcial4=float(input("Coloque la nota de su parcial 4: "))

# promedioParciales = (parcial1+parcial2+parcial3+parcial4)/4

# print("Promedio parciales: ", promedioParciales)

# notaParcial =promedioParciales*0.55
# proyectoFinal = float(input("Ingrese la calificacion de los parciales "))*0.3
# calificacionFinal = float(input("Ingrese la calificacion final de trabajos "))*0.15

# calificacionGeneral = notaParcial +proyectoFinal + calificacionFinal

# print("Su calificacion es:", calificacionGeneral)


# um round(x)redondear numero flotante

# import math

# tamañoDisco = float(input("Ingrese el tamaño del disco: "))

# cd_virgen = 700
# gigabite = 1024

# numDiscos = tamañoDisco / cd_virgen
# cantidadGigabytes = tamañoDisco /1024


# print(cantidadGigabytes)
# print(f"Usted necesita {math.ceil(numDiscos)} discos para alamcenar {tamañoDisco}")
# print(f"Usted necesita {round(numDiscos)} discos para alamcenar {tamañoDisco}")


# alturaPersona = float (input("Digite la alutura de la persona en metros: "))
# convercion = alturaPersona*100
# print(convercion)

# if convercion<=150:
#     print('Persona de altura baja')

# elif 151<=convercion<=190:
#     print('Persona alta')

# elif 191<=convercion <=230:
#     print('Persona Muy alta')
# else:
#     print('Persona demaciado alta')


# a=int(input("Digite su numero a"))
# b=int(input("Digite su numero b"))
# c=int(input("Digite su numero c"))

# if a==b:
#     print('Sus numeros son iguales')
# elif a==c:
#     print('Sus numeros son iguales')

# elif b==c:
#     print ('Sus numeros son iguales')

# elif a<b or a<c:
#     if b<c:
#         print('El numero mayor es la variable c:' ,c)
#     else:
#         print ('El numero mayor es la variable b: ',b )
# else:
#     print('El numero mayor es es la variable a: ',a)

# convercion de mayusculas a minujsculas
# letra = input("ingrese una letra: ").lower()
# if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' or letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U'):
#     print(f'Su letra {letra} es una vocal')
# else:
#     print(f'Su letra {letra} no es una vocal')


# saldo = 1000
# salir = False


# while salir==False:
#     opcion = int(input(f"""
#                 Bienvenido al banco BBVA
#                 Su saldo es : { saldo}
#                 ingrese por numero alguna de las siguientes opciones:
#                 1.Ingresar dinero a la cuenta
#                 2.Retirar deinero de la cuenta
#                 3.Mostrar dinero disponible
#                 4.Salir
#                 """))
#     if opcion == 1:
#         ingresarSaldo = int(input('Ingrese la cantidad que desee ingresar: '))
#         saldo = saldo + ingresarSaldo
#         ingresarSaldo = 0
#     elif (opcion == 2):
#         retirarSaldo = int(input('Digite el saldo a retirar: '))
#         if (retirarSaldo > saldo):
#             print(f'Su saldo es {saldo} por consiguiente no puede retirar')
#         else:
#             saldo = saldo - retirarSaldo
#             print(
#                 f'Usted retiro {retirarSaldo}, su saldo dsiponible es {saldo}. ')
#             retirarSaldo = 0
#     elif (opcion == 3):
#         print(f'Su saldo es {saldo}.')
#     elif (opcion == 4):
#         print('Muchas gracias por utilizar nuestros servicios')
#         salir == True
#         break
#     else:
#         print('Su opcion no es valida, digite de nuevo')


# lista =["lunes","martes","miercoles","jueves","viernes"]
# print(lista[-1]) #manera inversa
# print(lista[1])

# ##forma de crear subconjuntos
# print(lista[0:3])#menos un dato Sub lista
# print(lista[:4])#menos un dato Sub lista
# print(lista[:])#muestra todo
# print(lista[1:3])#
# print(lista[3:])#jueves y viernes

# lista=["lunes",40,5.65,[1,2,3],True,5,5,5]

# lista.append(6)
# #lista.insert(2,2)
# lista.extend([6,7,8])
# print(len(lista))

# nombres = 'alex','eduardo',3
# nombres2 = ['alex','eduardo',3]
# print(type(nombres))
# print(tuple(nombres))
# nombre3 = "a"
# print(ord(nombre3))
# print(chr(ord(nombre3)))

# #print(4 in lista[4])
# print(lista.index(40)) #busca la posicion donde se encuetra este valor
# print(lista.count(40))
# print(lista.remove(5))#elimina el primer dato de la lista que sea 5
# #print(lista.clear())
# listanum = [1,2,4,5,3]
# print(listanum.sort())
# print(listanum)##solo numeros
# print(listanum.sort(reverse=True)) ##solo numeros
# print(listanum)

# list_ProductAliments = []
# list_ProductsAseo = []
# list_Productlicores = []
# list_total = []

# while True:
#     opcion = (input(f"""
#         --Buen dia--

#         Informacion de las listas:
#         Lista de productos de alimentos
#         {list_ProductAliments}
#         Lista de porductos de aseo:
#         {list_ProductsAseo}
#         Lista de productos de licores:
#         {list_Productlicores}

#         Digita la opcion que desees
#         1. Adicionar un producto
#         2. Buscar algun producto
#         3. Eliminar un producto
#         4. Mostrar productos ingresados
#         5.Generar factura
#         6. Salir
#     """))
#     if opcion == '1':
#         while True:
#             categoria_Producto = (input("""
#         Seleccione la categora de producto a ingresar:
#         1.Alimentos
#         2.Aseo
#         3.Licores
#         4.No adicionar producto
#         """))

#             if categoria_Producto == '1':
#                 # ingresar producto  de alimento
#                 producto = input("Digite su producto de alimento: ")
#                 list_ProductAliments.append(producto)
#                 # Eliminar producto ingresado
#                 producto = ''
#             elif categoria_Producto == '2':
#                 # ingresar producto  de aseo
#                 producto = input("Digite su producto de aseo: ")
#                 list_ProductsAseo.append(producto)
#                 # Eliminar producto ingresado
#                 producto = ''
#             elif categoria_Producto == '3':
#                 # ingresar producto  de licor
#                 producto = input("Digite su producto de licor: ")
#                 list_Productlicores.append(producto)
#                 # Eliminar producto ingresado
#                 producto = ''
#             elif categoria_Producto == '4':
#                 print("No adiciono ningun producto")
#                 break
#             else:
#                 print('Opcion no valida, por favor digite una opcion valida.')

#     elif opcion == '2':
#         while True:
#             producto_Buscado = input("Digita el producto a buscar: ")
#             if producto_Buscado in list_ProductAliments:
#                 print(
#                     f'Su producto esta en su lista de alimentos en la posicion numero {(list_ProductAliments.index(producto_Buscado)+1)}.')
#             elif producto_Buscado in list_ProductsAseo:
#                 print(
#                     f'Su producto esta en su lista de productos de aseo en la posicion numero {(list_ProductsAseo.index(producto_Buscado)+1)}.')

#             elif producto_Buscado in list_Productlicores:
#                 print(
#                     f'Su producto esta en su lista de licores en la posicion numero {(list_Productlicores.index(producto_Buscado)+1)}.')
#             else:
#                 print(
#                     f"El producto buscado '{producto_Buscado}' no se encuentra en ninguna de las listas.")

#             op_Busq_Producto = input(
#                 "¿Desea buscar otro producto? Digite 's' o 'n'").lower()
#             if op_Busq_Producto == 'n':
#                 break
#             else:
#                 if op_Busq_Producto != 's':
#                     print('Opcion no valida, redireccion al menu...')
#                     break
#     elif opcion == '3':
#         while True:
#             producto_aEliminar = input(
#                 "Digite el nombre del producto que desea eliminar: ")
#             if producto_aEliminar in list_ProductAliments:
#                 list_ProductAliments.remove(producto_aEliminar)
#                 print(
#                     f'Se elimino el producto "{producto_aEliminar}" de su lista de alimentos')
#             elif producto_aEliminar in list_ProductsAseo:
#                 list_ProductsAseo.remove(producto_aEliminar)
#                 print(
#                     f'Se elimino el producto "{producto_aEliminar}" de su lista de productos de aseo')

#             elif producto_aEliminar in list_Productlicores:
#                 list_Productlicores.remove(producto_aEliminar)
#                 print(
#                     f'Se elimino el producto "{producto_aEliminar}" de su lista de licores')
#             else:
#                 print(
#                     f"No se encontro el producto que deseas eliminar")

#             op_delete_Product = input(
#                 "¿Desea eliminar otro producto? Digite 's' o 'n'").lower()
#             if op_delete_Product == 'n':
#                 break
#             else:
#                 if op_delete_Product != 's':
#                     print('Opcion no valida, redireccion al menu...')
#                     break
#     elif opcion == '4':
#         print(f"""Estos son los productos que usted ha ingresado:
#             Alimentos: {list_ProductAliments}
#             Productos de aseo: {list_ProductsAseo}
#             Licores: {list_Productlicores}
#               """)
#     elif opcion == '5':
#         list_total.extend([(list_ProductAliments),(list_ProductsAseo),(list_Productlicores)])
#         print(f"Su generacion de factura: " , tuple(list_total))

#     elif opcion == '6':
#         print("")
#         print('Gracias por utilizar nuestro servicio.\nHasta luego.')
#         break
#     else:
#         print("Por favor, rectifique su opcion ingresada")


# curso = {
#     'estudiante': {
#         'Nombre': 'Alex',
#         'id': '123'
#     }
# }

# print(curso['estudiante']['id'])
# print(curso['estudiante'].get('id', 'No se encontro '))

# curso = {
#     'estudiante': {
#         'Nombre': 'Alex',
#         'id': {
#             'par': '2'
#         }
#     }
# }

# print(curso['estudiante']['id']['par'])

# agendaTelefonicaubate = {
#     'Alex': '1234',
#     'Eduardo': '4567',
#     'Nocua': '8901',
#     'Sema': '2345',
#     'Baquero': '6789'
# }
# agendaTelefonica={}


# while True:
#     opcion=int(input('''Seleccione alguna de las opciones
#           1. Mostrar datos
#           2. Mostrar telefono
#           3. Consulta de numeros
#           4. Obtener el total de personas
#           5. Agregar personas
#           6. Salir
#           '''))
#     if opcion == 1:
#         print(agendaTelefonica)
#     elif opcion ==2:
#         print(agendaTelefonica.values())
#     elif opcion ==3:
#         nombrePersona = input('Digite el nombred e la persona: ')
#         print(agendaTelefonica.get(nombrePersona,f'No se encontro ningun numero para la persona {nombrePersona}'))
#     elif opcion ==4:
#         print('Cantidad de Personas: ')
#         print(len(agendaTelefonica))
#     elif opcion ==5:
#         cantidad = int(input('Digite la cantidad de perosnas que quiere ingresar'))
#         for i in range(cantidad):
#             nombre =input(f'Digite el Nombre de la persona {i+1}: ')
#             tel = (input(f'Digite el numero de la persona {nombre} :'))
#             agendaTelefonica[nombre]=tel


#             print(agendaTelefonica)
#     elif opcion ==6:
#         print('Gracias')
#         break
#     else:
#         print('Seleccione alna de las opciones')


# Sistema de contlo y gestion de inventario

almacen = {

}
print('Sistema de gestion y contro de inventario')

list_productos = []
list_Infproductos = []
i = 0
codigo_encriptado = 0
while True:
    opcion = (input(
        'Digite la letra "S" si desea continuar, le do contario pulce cualquier letra'))
    if opcion != 's':
        print('Gracias por utilizar el programa.').lowe()
        break

    nombre_Operario = input(
        'Por favor Digite el nombre de quiena va a realizar el informe: ')
    num_envio = int(input(
        'Por favor Digite el codigo numero de envio que recibio: '))

    while True:

        opcion = int(input("""
        1.Ingresar producto recibido.
        2.Modificar datos de productos.
        3.Eliminar registro de productos recibidos.
        4.Muestra productos ingresados.
        5.Limpiar ingreso de productos.
        6.Generar informe.
        7.Mostrar operarios.
        8.Cambiar de Operario o salir. 
            
                    """))

        if opcion == 1:

            while True:
                i += 1
                nombre = input('Digite el nombre del producto: ')
                id = int(input('Digite el id del producto: '))
                h_ingreso = input(
                    'Digite el hora de ingreso en formato 24  horas del producto: ')

                almacen[f'Producto {i}'] = {
                    'nombre_product': nombre,
                    'id': id,
                    'horaIngreso': h_ingreso
                }

                break
        elif opcion == 2:
            print('Los producto ingresados son: ', almacen.keys(),
                  '\n Recuerde digitar el nombre exactamente como esta')
            nombre_product = input(
                'Digite el nombre del producto que desea modificar: ')
            while True:

                opcion = int(input('''Digita al informacion que deseas modificar: 
                      
                        1. Nombre del producto.
                        2. Id del producto:
                        3. Hora de ingreso del producto.
                        4. No modificar el producto.'''))
                if opcion == 1:
                    nombre = input('Digite el nombre del producto: ')

                elif opcion == 2:
                    id = int(input('Digite el id del producto: '))
                elif opcion == 3:
                    h_ingreso = input(
                        'Digite el hora de ingreso en formato 24  horas del producto: ')
                elif opcion == 4:
                    break
                else:
                    print('Por favor digite una opcion correcta. \n')

                almacen[nombre_product] = {
                    'nombre_product': nombre,
                    'id': id,
                    'horaIngreso': h_ingreso
                }
        elif opcion == 3:
            print('Los producto ingresados son: ', almacen.keys(),
                  '\n Recuerde digitar el nombre exactamente como esta.')
            nombre_product = input(
                'Digite el nombre del producto que desea eliminar: ')
        elif opcion == 4:
            print('Sus productos ingresados son:')
            for items in almacen.items():
                print(items)

        elif opcion == 5:
            list_Infproductos.clear()
            list_productos.clear()

        elif opcion == 6:
            print(f'''Informe de productos Ingresados
                
                Esta es la lista de todos los productos que ingreso: {tuple(list_productos)}
                
                Informe presentado por: {nombre_Operario}
                Codigo de envio: {codigo_encriptado}
                ''')
        elif opcion == 7:

            while True:
                almacen[f'Operario {nombre_Operario}'] = f'Codigo encriptado de recibida de envio: {codigo_encriptado}'
                print(almacen)
                break
        elif opcion == 8:
            break
        else:
            print('por favor digite una de las opciones estableidas')
