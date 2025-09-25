#Variables a mostrar
Contraseña=''
intentos=0
Producto=0
Opcion = ''

#---FUNCIONES PARA EL INVENTARIO---

#Mostrar el menu
def Menu():
    print('\n--- MENÚ INVENTARIO ---')
    print('1. Mostrar inventario')
    print('2. Agregar producto')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Buscar producto')
    print('6. Presupuesto total')
    print('7. Venta')
    print('8. Salir')
    try:
        Opcion = int(input("Seleccione una opción: "))
        return Opcion
    except ValueError: 
        print("Opción inválida.")
        return 
    
#Aqui se va el codigo para el inventario
def cargar_inventario(nombre_archivo):
    print("Agregar el codigo para la parte ""cargar_inventario""" )

#Aqui va el codigo para guardar el inventario
def guardar_inventario(nombre_archivo, inventario):
    print("Aqui va el codigo de la parte ""guardar_inventario""")

#Aqui va el codigo para cargar las ganancias
def cargar_ganancias(nombre_archivo):
    print("Aqui va el codigo para la parte ""cargar_ganancias""")

#Aqui va el codigo para guardar las ganancias
def guardar_ganancias(nombre_archivo, ganancias):
    print("Agregar el codigo para la parte ""guardar_ganancias""")

#Aqui se mostrara el producto y su informacion
def layout(nombre, datos):
    print("Agregar el codigo para la parte ""layout""")

#Aqui va el codigo para agregar algun producto nuevo
def AgregarProducto(diccionario):
    print("Agregar el codigo para la parte ""AgregarProducto""")

#Aqui va el codigo para mostrar el inventario
def MostrarInventario(diccionario):
    print("Agregar el codigo para la parte ""MostrarInventario""")

#Aqui va el codigo para actualizar el inventario
def ActualizarProducto(diccionario, dato=None, nuevo_stock=None):
    print("Agregar el codigo para la parte ""ActualizarProducto""")

#Aqui va el codigo para eliminar un producto
def EliminarProducto(diccionario):
    print("Agregar el codigo para la parte ""EliminarProducto""")

#Aqui va el codigo para buscar un producto
def BuscarProducto(diccionario,dato=None):
    print("Agregar el codigo para la parte ""BuscarProducto""")

#Aqui va el codigo para el calculo final de precios
def Preciototal(diccionario):
    print("Agregar el codigo para la parte ""Preciototal""")

#Aqui va el codigo para registrar las ventas
def venta(diccionario):
    print("Agregar el codigo para la parte ""venta""")

#---PROGRAMA PRINCIPAL---
Contraseña=''
intentos=0
Precio_total=0
Productos ={}
Opcion=0
while intentos < 3 and Contraseña != 'OXXO':
    Contraseña=input("Ingrese la contraseña: ")
    if Contraseña=='OXXO':
        while Opcion !=8:
            Opcion=Menu()
            if Opcion == 1:
                MostrarInventario(Productos)
            elif Opcion == 2:
                AgregarProducto(Productos)
            elif Opcion == 3:
                ActualizarProducto(Productos)
            elif Opcion == 4:
                EliminarProducto(Productos)
            elif Opcion == 5:
                BuscarProducto(Productos)
            elif Opcion == 6:
                Precio_total(Productos)
            elif Opcion == 7:
                venta(Productos)
            elif Opcion == 8:
                print('Saliendo...')
                print(Productos)
    else:
        print("Contraseña incorrecta. No se pueden agregar o eliminar productos.")
        intentos += 1


