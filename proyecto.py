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

#Aqui se mostrara el producto y su informacion
def layout(nombre, datos):
    print(f"Producto: {nombre:<15} Código: {datos['codigo']:<10} Stock: {datos['Stock']:<5} Precio: ${datos['precio']:<8.2f}")

#Aqui va el codigo para agregar algun producto nuevo
def AgregarProducto(diccionario):
    print("Agregar el codigo para la parte ""AgregarProducto""")

#Aqui va el codigo para mostrar el inventario
def MostrarInventario(diccionario):
    print("Agregar el codigo para la parte ""MostrarInventario""")

#Aqui va el codigo para actualizar el inventario
def ActualizarProducto(diccionario, dato=None, nuevo_stock=None):
    if dato is None:
        dato = input("Ingrese producto a actualizar: ")
    if BuscarProducto(diccionario,dato):
        try:
            if nuevo_stock is None:
                nuevo_stock = int(input("Ingrese nuevo stock: "))
            diccionario[dato]['Stock'] = nuevo_stock
            print('Producto actualizado.')
            return True
        except ValueError:
            print('El stock debe ser numerico.')
            return False
    else:
        print('No encontrado.')
        input("¿Deseas agaregarlo como nuevo? (si/no): ")
        if Opcion.lower() == 'si':
            AgregarProducto(diccionario)
        return False
  
#Aqui va el codigo para eliminar un producto
def EliminarProducto(diccionario):
    dato = input("Ingrese producto a eliminar: ")
    nuevo_dato=None
    for nombre,datos in diccionario:
        if dato==nombre or dato==datos['codigo']: 
            nuevo_dato=nombre
            diccionario.pop(nuevo_dato)
            print('"Producto eliminado."')
    else: 
        print('Producto no encontrado.')

#Aqui va el codigo para buscar un producto
def BuscarProducto(diccionario,dato=None):
    if dato is None:
        dato = input('Ingrese producto o código a buscar: ')
    encontrado = False
    for nombre, datos in diccionario.items():
        if nombre == dato or datos['codigo'] == dato:
            print('Encontrado:')
            layout(nombre, datos)
            encontrado = True
    if not encontrado:
        print('No encontrado.')
        opcion = input('¿Deseas agregarlo? (si/no): ')
        if opcion.lower().strip() == 'si':
            AgregarProducto(diccionario)
    return encontrado

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