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
        
# ===== Manejo de archivos =====
def cargar_inventario(nombre_archivo):
    inventario = {}
    try:
        with open(f"{nombre_archivo}.txt", "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    nombre, codigo, stock, precio = datos
                    inventario[nombre] = {
                        "codigo": codigo,
                        "Stock": int(stock),
                        "precio": float(precio)
                    }
    except FileNotFoundError:
        print("Archivo no encontrado, se creará uno nuevo.")
        open(f"{nombre_archivo}.txt", "w").close()
    return inventario

#Cargar y guardar ganancias
def guardar_ganancias(nombre_archivo, ganancias):
    with open(f"{nombre_archivo}_ganancias.txt", "w") as f:
        f.write(f"{ganancias:.2f}")

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
def ActualizarProducto(diccionario, archivo, dato=None, nuevo_stock=None):
    if dato is None:
        dato = input("Ingrese producto a actualizar: ")
    if dato in diccionario:
        try:
            if nuevo_stock is None:
                nuevo_stock = int(input("Ingrese nuevo stock: "))
            diccionario[dato]['Stock'] = nuevo_stock
            print('Producto actualizado.')
            guardar_inventario(archivo, diccionario)
            return True
        except ValueError:
            print('El stock debe ser numerico.')
            return False
    else:
        print('No encontrado.')
        return False
  
#Aqui va el codigo para eliminar un producto
def EliminarProducto(diccionario, archivo):
    dato = input("Ingrese producto a eliminar: ")
    if dato in diccionario:
        diccionario.pop(dato)
        print('Producto eliminado')
        guardar_inventario(archivo, diccionario)
    else:
        print('Producto no encontrado')

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
    return encontrado

#Aqui va el codigo para el calculo final de precios
def Preciototal(diccionario):
    total = sum(diccionario[p]['Stock'] * diccionario[p]['precio'] for p in diccionario)
    print(f"El presupuesto total es: ${total:.2f}")
    return total

#Aqui va el codigo para registrar las ventas
def venta(diccionario, archivo, ganancias_acumuladas):
    carrito = {}
    total_venta = 0
    while True:
        dato = input("Ingrese producto o código a vender (o 'salir' para terminar): ")
        if dato.lower().strip() == 'salir':
            break
        
        nombre_encontrado = None
        for nombre, datos in diccionario.items():
            if nombre == dato or datos['codigo'] == dato:
                nombre_encontrado = nombre
                break
        
        if not nombre_encontrado:
            print("Ese producto no existe en el inventario.")
            continue
        try:
            cantidad = int(input(f"Ingrese cantidad de '{nombre_encontrado}': "))
        except ValueError:
            print('Debe ser un número.')
            continue
        
        if cantidad <= 0:
            print("Cantidad inválida.")
            continue
        
        stock_actual = diccionario[nombre_encontrado]['Stock']
        if cantidad > stock_actual:
            print(f"Stock insuficiente (disponible: {stock_actual}).")
            continue
        
        #Actualizar el inventario (restar lo vendido)
        nuevo_stock = stock_actual - cantidad
        diccionario[nombre_encontrado]['Stock'] = nuevo_stock
        
        #Calcular las ganancias de cada venta
        precio_venta = diccionario[nombre_encontrado]['precio']
        subtotal = cantidad * precio_venta
        total_venta += subtotal
        
        #Agregar al carrito
        carrito[nombre_encontrado] = {'cantidad': cantidad, 'subtotal': subtotal}
        print(f"{cantidad} {nombre_encontrado} añadido al carrito. Subtotal: ${subtotal:.2f}")
    if carrito:
        print("\n--- RESUMEN DE VENTA ---")
        for prod, datos in carrito.items():
            print(f"{prod}: {datos['cantidad']} unidades → ${datos['subtotal']:.2f}")
        
        print(f"Total de la venta: ${total_venta:.2f}")
        
        #Sumar las ganancias de esta venta a las ganancias acumuladas
        ganancias_acumuladas += total_venta
        print(f"Ganancias acumuladas actualizadas: ${ganancias_acumuladas:.2f}")
        
        print("\n--- INVENTARIO ACTUALIZADO ---")
        MostrarInventario(diccionario)
        
                #Guardar los cambios
        guardar_inventario(archivo, diccionario)
        guardar_ganancias(archivo, ganancias_acumuladas)
        
        carrito.clear()
        print('Venta finalizada.')
    else:
        print('No se vendió nada.')
    
    return ganancias_acumuladas



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