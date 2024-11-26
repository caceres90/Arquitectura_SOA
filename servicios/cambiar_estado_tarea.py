import json

def cambiar_estado_tarea(indice):
    with open('tareas.json', 'r') as file:
        tareas = json.load(file)

    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = not tareas[indice]['completada']

        with open('tareas.json', 'w') as file:
            json.dump(tareas, file)

        return tareas[indice]
    else:
        return None