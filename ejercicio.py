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



#um round(x)redondear numero flotante

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


a=int(input("Digite su numero a"))
b=int(input("Digite su numero b"))
c=int(input("Digite su numero c"))

if a==b:
    print('Sus numeros son iguales')
elif a==c:
    print('Sus numeros son iguales')

elif b==c:
    print ('Sus numeros son iguales')
    
elif a<b or a<c:
    if b<c:
        print('El numero mayor es la variable c:' ,c)
    else:
        print ('El numero mayor es la variable b: ',b )
else:
    print('El numero mayor es es la variable a: ',a)
