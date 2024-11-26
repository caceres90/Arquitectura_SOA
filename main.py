from esb.esb import procesar_peticion

def main():
    while True:
        print("1. Crear tarea")
        print("2. Obtener tareas")
        print("3. Cambiar estado de tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            respuesta = procesar_peticion("crear_tarea", {"titulo": titulo, "descripcion": descripcion})
            print(respuesta.get("data") if respuesta["status"] == "success" else respuesta["message"])

        elif opcion == '2':
            respuesta = procesar_peticion("obtener_tareas")
            if respuesta["status"] == "success":
                for idx, tarea in enumerate(respuesta["data"]):
                    estado = "Completada" if tarea['completada'] else "Pendiente"
                    print(f"{idx + 1}. {tarea['titulo']} - {estado}")
            else:
                print(respuesta["message"])

        elif opcion == '3':
            indice = int(input("Ingrese el número de la tarea a cambiar de estado: ")) - 1
            respuesta = procesar_peticion("cambiar_estado_tarea", {"indice": indice})
            print(respuesta.get("data") if respuesta["status"] == "success" else respuesta["message"])

        elif opcion == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
