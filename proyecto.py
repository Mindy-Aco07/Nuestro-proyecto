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

#Guardar inventario
def guardar_inventario(nombre_archivo, inventario):
    with open(f"{nombre_archivo}.txt", "w") as f:
        for nombre, datos in inventario.items():
            f.write(f"{nombre},{datos['codigo']},{datos['Stock']},{datos['precio']}\n")

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
    if not diccionario:
        print('Inventario vacío.')
    else:
        print('\n--- Inventario ---')
        for nombre, datos in diccionario.items(): 
            layout(nombre, datos)


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
        
        #Esta funcion nos sirve para actualizar el inventario de manera correcta y restarle la cantidad que se vendió.
        nuevo_stock = stock_actual - cantidad
        diccionario[nombre_encontrado]['Stock'] = nuevo_stock
        
        #Esta funcion nos sirve para calcular las ganancias de cada venta que se hace.
        precio_venta = diccionario[nombre_encontrado]['precio']
        subtotal = cantidad * precio_venta
        total_venta += subtotal
        
        #Esta funcion sirve para agregar los productos que son escritos se envian al carrito de compras.
        carrito[nombre_encontrado] = {'cantidad': cantidad, 'subtotal': subtotal}
        print(f"{cantidad} {nombre_encontrado} añadido al carrito. Subtotal: ${subtotal:.2f}")
    if carrito:
        print("\n--- RESUMEN DE VENTA ---")
        for prod, datos in carrito.items():
            print(f"{prod}: {datos['cantidad']} unidades → ${datos['subtotal']:.2f}")
        
        print(f"Total de la venta: ${total_venta:.2f}")
        
        #Esta funcion nos sirve para Sumar las ganancias de esta venta a las ganancias acumuladas.
        ganancias_acumuladas += total_venta
        print(f"Ganancias acumuladas actualizadas: ${ganancias_acumuladas:.2f}")
        
        print("\n--- INVENTARIO ACTUALIZADO ---")
        MostrarInventario(diccionario)
        
                #esta nos sirve para guardar los cambios de manera correcta y al instante.
        guardar_inventario(archivo, diccionario)
        guardar_ganancias(archivo, ganancias_acumuladas)
        
        carrito.clear()
        print('Venta finalizada.')
    else:
        print('No se vendió nada.')
    
    return ganancias_acumuladas


# ===== Programa principal =====
Contraseña = ''
intentos = 0
Opcion = 0

#Nombre de variable corregido (nomrbre_archivo - nombre_archivo)
nombre_archivo = input('¿Qué nombre tiene el archivo?: ').strip()
Productos = cargar_inventario(nombre_archivo)

#Esta funcion nos sirve para agregar correctamente las ganancias al archivo.
ganancias_totales = cargar_ganancias(nombre_archivo)
print(f"Ganancias acumuladas cargadas: ${ganancias_totales:.2f}")

while intentos < 3:
    Contraseña = input("Ingrese la contraseña: ")
    if Contraseña == 'OXO':
        while True: #para controlar de mejor manera el bucle (mientras la opcion sea Menu() creara el bucle infinito) y que al salir del programa, el usuario del programa completamente
            Opcion = Menu()
            
            #Verificar si "Opcion es None(nada o vacio)" (ahora el programa verifica None)--- if Opcion is None verifica especificamente si Menu() retorno Nonee
            if Opcion is None: #En el programa no corregido si el usuario ingresaba un valor invalido Menu() mostraba None lo que hacia que todas las demas opciones (Opcion == 1, etc dieran "false")
                continue
            #while Opcion != 8 posible error: Si "Opcion" empieza en 8, el bucle nunca funciona - Si despues de salir del programa el usuario elige 8, "Opcion" queda en 8 para siempre
                
            if Opcion == 1:
                MostrarInventario(Productos)
            elif Opcion == 2:
                AgregarProducto(Productos, nombre_archivo)
            elif Opcion == 3:
                ActualizarProducto(Productos, nombre_archivo)
            elif Opcion == 4:
                EliminarProducto(Productos, nombre_archivo)
            elif Opcion == 5:
                BuscarProducto(Productos)
            elif Opcion == 6:
                Preciototal(Productos, ganancias_totales)
            elif Opcion == 7:
                ganancias_totales = venta(Productos, nombre_archivo, ganancias_totales)
            elif Opcion == 8:
                print('Saliendo...')
                guardar_inventario(nombre_archivo, Productos)
                guardar_ganancias(nombre_archivo, ganancias_totales)
                break
        break  #break par salir del bucle de contraseña cuando se sale del programa
    else:
        print("Contraseña incorrecta.")
        intentos += 1
        if intentos >= 3: #En caso de que se excedan los intentos
            print("Demasiados intentos fallidos. Saliendo del programa.") #Mensaje de que se excedieron los intentos
            break