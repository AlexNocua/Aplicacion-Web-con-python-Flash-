# creacion de diccionario donde se va a almacenar cada uno de los productos registrados
almacen = {
}

# Creacion de la lista donde se va a almacenar el nombre del operario y el numero del envio recibido
registroEnvios = []
print('Sistema de gestion y contro de inventario :)')

# Inicializacion de variable que va a ser iterativa con el funcionamiento de que me deje agregar nuevos productos y sis caracteristicas en el diccionario
i = 0

while True:

    opcion = (input(
        'Digite la letra "S" si desea continuar, de lo contario pulse cualquier letra: ')).lower()
    if opcion != 's':
        # Cuando salga del Programa me muestre los funcionarios que realizaron ingresos de envios
        print(f'Registros realizados: {registroEnvios}')
        print('Gracias por utilizar el programa.')
        break

    nombre_Operario = input(
        'Por favor Digite el nombre de quiena va a realizar el informe: ')
    num_envio = int(input(
        'Por favor Digite el codigo numero de envio que recibio: '))

    # Agrega el nombre del operario
    registroEnvios.extend([nombre_Operario, num_envio])

    # verificar si no se ingreso nada en esas variables
    if nombre_Operario == None or num_envio == None:
        print(
            'No puede realizar la continuar si no asigna un nombre o un numero de registro.')

    while True:

        # variable de opciones
        opcion = int(input("""
        1.Ingresar producto recibido.
        2.Modificar datos de productos.
        3.Eliminar registro de productos recibidos.
        4.Muestra productos ingresados.
        5.Generar informe.
        6.Cambiar de Operario o salir. 
            
                    """))

        # si la opcion es igual a:
        if opcion == 1:

            while True:
                # i va a ser la encargada de cambiar el nombre de la clave con el fin de que me cree diccionarios dentro del diccionario
                i += 1

                # Variables
                nombre = input('Digite el nombre del producto: ')
                id = int(input('Digite el id del producto: '))
                h_ingreso = input(
                    'Digite el hora de ingreso en formato 24  horas del producto: ')

                # En el diccionario almacen se va a almacenar el diccionario porducto
                almacen[f'Producto {i}'] = {
                    'nombre_product': nombre,
                    'id': id,
                    'horaIngreso': h_ingreso
                }

                break

        # si la opcion es igual a:
        elif opcion == 2:

            # se obtienen las claves de el diccionario almacen
            print('Los producto ingresados son: ', almacen.keys(),
                  '\n Recuerde digitar el nombre exactamente como esta')

            # Variable importante para el modificar los valores de el diccionario producto
            nombre_product = input(
                'Digite el nombre del producto que desea modificar: ')

            if nombre_product in almacen:
                while True:

                    # Variables de Opcion
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

                    # se va a acceder al diccionario almacen, especificamente a la clave producto y se actualizan los valores de las claves
                    almacen[nombre_product] = {
                        'nombre_product': nombre,
                        'id': id,
                        'horaIngreso': h_ingreso
                    }

            else:
                # si no se encuentra la clave ingresada que me muestre este mensaje.
                print(
                    f'Su producto "{nombre_product}" no se encuentra en registrado, verifique e ingrese de nuevo.')

        # si la opcion es igual a:
        elif opcion == 3:
            while True:
                print('Los producto ingresados son: ', almacen.keys(),
                      '\n Recuerde digitar el nombre exactamente como esta.')

                # Variable importante para el modificar los valores de el diccionario producto
                nombre_product = input(
                    'Digite el nombre del producto que desea eliminar: ')

                # se verifica que la clave de porducto que queremos eliminar este en nuestro diccionario.
                if nombre_product in almacen:

                    # se utiliza el metodo pop para eliminar la clave
                    almacen.pop(nombre_product)
                    break
                else:
                    # si no se encuentra la clave ingresada que me muestre este mensaje.
                    print(
                        f'Su producto "{nombre_product}" no se encuentra en registrado, verifique e ingrese de nuevo.')
                    break

        # si la opcion es igual a:
        elif opcion == 4:
            print('Sus productos ingresados son:')

            # si el diccionario almacen no tiene valores
            if not almacen:
                print('No se encuentra ningun producto.')
            else:
                # para que me itere las claves de claves del almacen con la funcion items, este mismo los guarde en la variable items creada y muestre los valores de cada una de esas llaves.
                for items in almacen.items():
                    print(items)

        # si la opcion es igual a:
        elif opcion == 5:
            
            #recupere los datos de mi almacen en formato tupla.
            print(f'''Informe de productos Ingresados
                
                
                Esta es la lista de todos los productos que ingreso: {tuple(almacen)}
                
                Informe presentado por: {nombre_Operario}
                Codigo de envio: {num_envio}
                ''')

        # si la opcion es igual a:
        elif opcion == 6:
            
            # i se iguala a 0 para que cuente desde uno el ingreso de productos de otro operario
            i = 0
            # se reicicia el diccionario almacen con el fin de que no guarde los productos ingresados por el operario.
            almacen = {}
            break

        # si la opcion no es igual a ninguna de las seleccionadas:
        else:
            print('por favor digite una de las opciones establecidas.')
