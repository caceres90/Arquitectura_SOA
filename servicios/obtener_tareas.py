import json

def obtener_tareas():
    with open('tareas.json', 'r') as file:
        tareas = json.load(file)
    return tareas