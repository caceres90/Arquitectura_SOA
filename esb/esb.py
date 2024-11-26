from servicios.crear_tarea import crear_tarea
from servicios.obtener_tareas import obtener_tareas
from servicios.cambiar_estado_tarea import cambiar_estado_tarea

def procesar_peticion(accion, datos=None):
    try:
        if accion == "crear_tarea":
            titulo = datos.get("titulo")
            descripcion = datos.get("descripcion")
            return {"status": "success", "data": crear_tarea(titulo, descripcion)}

        elif accion == "obtener_tareas":
            tareas = obtener_tareas()
            return {"status": "success", "data": tareas}

        elif accion == "cambiar_estado_tarea":
            indice = datos.get("indice")
            tarea_modificada = cambiar_estado_tarea(indice)
            if tarea_modificada:
                return {"status": "success", "data": tarea_modificada}
            else:
                return {"status": "error", "message": "Índice de tarea no válido"}

        else:
            return {"status": "error", "message": "Acción no reconocida"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
