import json

def crear_tarea(titulo, descripcion):
    with open('tareas.json', 'r') as file:
        tareas = json.load(file)

    nueva_tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'completada': False
    }

    tareas.append(nueva_tarea)

    with open('tareas.json', 'w') as file:
        json.dump(tareas, file)

    return nueva_tarea