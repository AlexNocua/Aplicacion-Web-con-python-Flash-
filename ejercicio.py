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


lista =["lunes","martes","miercoles","jueves","viernes"]
print(lista[-1]) #manera inversa
print(lista[1])

##forma de crear subconjuntos
print(lista[0:3])#menos un dato Sub lista
print(lista[:4])#menos un dato Sub lista
print(lista[:])#muestra todo
print(lista[1:3])#
print(lista[3:])#jueves y viernes

lista=["lunes",40,5.65,[1,2,3],True,5,5,5]

lista.append(6)
#lista.insert(2,2)
lista.extend([6,7,8])
print(len(lista))

nombres = 'alex','eduardo',3
nombres2 = ['alex','eduardo',3]
print(type(nombres))
print(tuple(nombres))
nombre3 = "a"
print(ord(nombre3))
print(chr(ord(nombre3)))

#print(4 in lista[4])
print(lista.index(40)) #busca la posicion donde se encuetra este valor
print(lista.count(40)) 
print(lista.remove(5))#elimina el primer dato de la lista que sea 5
#print(lista.clear())
listanum = [1,2,4,5,3]
print(listanum.sort()) 
print(listanum)##solo numeros
print(listanum.sort(reverse=True)) ##solo numeros
print(listanum)