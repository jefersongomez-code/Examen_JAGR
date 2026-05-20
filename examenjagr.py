import mysql.connector
# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="restaurante"
)
# Codigo que sirve para enviar instrucciones SQL desde Python hacia MySQL.
cursor = conexion.cursor()

# Agregamos el menu interactivo para la persona quien va a elegir la opcio q desea
while True:
    print(" ")
    print(" >>> BIENVENIDO A LA GESTION DE RESTAURANTE <<< ")
    print("👨‍🍳1 >. Agregar Platillo. ")
    print("💫2 >. Eliminar Platillo. ")
    print("👁️3 >. Mostrar Menú. ")
    print("🔏4 >. Salir del Programa. ")

# Declaramos una variable llamada opcion para que el usuario pueda ingresar su opcion
    opcion = input(">>. Elige la opcion que deseas: ")

# 1: Agregar un Platillo:
    if opcion == "1":
        plato_nuevo = input("Ingrese el nombre del platillo a agregar: ").strip()
# Codigo para poder ingresar el plato y aguardar en la base de datos
        if plato_nuevo:
            sql = "INSERT INTO platos (nombre) VALUES (%s)"
            valores = (plato_nuevo,)
            #Ejecuta la instrucción usando el valor ingresado por el usuario.
            cursor.execute(sql, valores)
            #Guardar en la base de datos.
            conexion.commit()

            print(f"Plato '{plato_nuevo}' agregado al Menu.\n")
        else:
            print("No puede agregar un plato vacío.\n")
# 2: Eliminar Plato:
    elif opcion == "2":
        plato = input("Ingrese el nombre del plato a eliminar: ").strip()
#if Plato:
    #Codigo para poder eliminar el plato y eliminarlo de la base de datos.
        sql = "DELETE FROM platos WHERE nombre = %s"
        valores = (plato,)
        #eliminar el Plato.
        cursor.execute(sql, valores)
        #Guardar en la base de datos.
        conexion.commit()
        #Verifica si se eliminó.
        if cursor.rowcount > 0:
            print(f"Plato '{plato}' eliminado del Menu.\n")
        else:
            print(f"El Plato '{plato}' no se encuentra en el menu.\n")
# 3: Ver Menu:
    elif opcion == "3":
        print(" ")
        print(" >> Este es todo el Menu del Restaurante << ")
        # Ejecutar para ver los platos.
        cursor.execute("SELECT id, nombre FROM platos")
        # Guarda en la variable platos.
        platos = cursor.fetchall()
        # Verificar si se encuntra algun plato.
        if len(platos) == 0:
            print("El Menu esta vacio. No hay platos registrados.\n")
        else:
            print("Menu de platos:")
            # Recorre uno por uno
            for plato in platos:
                # Muestra el id y el nombre.
                print(f"{plato[0]}. {plato[1]}")
            print()

    elif opcion == "4":
        print("✨ Gracias por usar el sistema del Restaurante. ¡Hasta pronto!")
        # Rompe el ciclo while y finaliza el menú.
        break