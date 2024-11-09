from conexion_sql import insertar_datos_usuario, insertar_datos_proyecto
from logica import obtener_recomendacion_por_categoria, validar_tamano_equipo

from requerimientos import obtener_requerimientos_adicionales
def solicitar_datos_usuario():
    print("Ingrese los datos del usuario:")
    nombres = input("Nombres del usuario: ")
    apellidos = input("Apellidos del usuario: ")
    habilidades_usuario = input("Habilidades del usuario (separadas por comas): ")

    # Inserción de los datos del usuario en la base de datos
    insertar_datos_usuario(nombres, apellidos, habilidades_usuario)
    return nombres, apellidos, habilidades_usuario

def solicitar_datos_proyecto():
    print("\nIngrese los datos del proyecto:")
    nombre_proyecto = input("Nombre del proyecto: ")
    equipo = int(input("Tamaño del equipo (Ej: hasta 6 para Crystal Clear, 7-20 para Crystal Yellow, etc.): "))
    criticidad = input("Criticidad del proyecto (Baja, Media, Alta, Muy Alta): ")
    duracion = int(input("Duración estimada del proyecto (en meses): "))

    # Determinación de la categoría Crystal según el tamaño del equipo
    if equipo <= 6:
        categoria = "Crystal Clear"
    elif 7 <= equipo <= 20:
        categoria = "Crystal Yellow"
    elif 21 <= equipo <= 50:
        categoria = "Crystal Orange"
    elif 51 <= equipo <= 100:
        categoria = "Crystal Red"
    elif equipo > 100:
        categoria = "Crystal Marrón"
    else:
        print("Tamaño de equipo no válido. Intente de nuevo.")
        return solicitar_datos_proyecto()

    # Validación del tamaño del equipo y la categoría
    if not validar_tamano_equipo(equipo, categoria):
        print(f"El tamaño del equipo no coincide con la categoría {categoria}. Intente de nuevo.")
        return solicitar_datos_proyecto()

    # Inserción del proyecto en la base de datos
    insertar_datos_proyecto(nombre_proyecto, equipo, criticidad, duracion, categoria)
    return nombre_proyecto, equipo, criticidad, duracion, categoria

def solicitar_requerimientos():
    print("\nIngrese los requerimientos adicionales del proyecto:")
    habilidades_integrantes = input("Habilidades de los integrantes (separadas por comas): ")
    tecnologias = input("Tecnologías a utilizar en el proyecto: ")
    recursos = input("Recursos disponibles para el proyecto: ")
    tolerancia_al_cambio = input("Tolerancia al cambio (Alta, Media, Baja): ")
    
    # Opciones para áreas del proyecto
    areas_posibles = [
        "Medicina", "Arquitectura", "Psicología", "Estudiantil", "Obrero", 
        "Agricultor", "Ingeniería", "Diseño Gráfico", "Energía", "Educación", 
        "Administración", "Finanzas", "Transporte", "Tecnología", "Comercio",
        "Ambiental", "Seguridad", "Deporte", "Turismo", "Arte", "Otros"
    ]
    print("Seleccione las áreas del proyecto (puede elegir múltiples, separadas por comas):")
    print(", ".join(areas_posibles))
    areas = input("Áreas del proyecto: ")

    # Consolidación de los requerimientos en un diccionario
    requerimientos_adicionales = {
        "Habilidades de los integrantes": habilidades_integrantes,
        "Tecnologías": tecnologias,
        "Recursos": recursos,
        "Tolerancia al cambio": tolerancia_al_cambio,
        "Áreas": areas
    }
    return requerimientos_adicionales

def mostrar_recomendacion(categoria, criticidad, duracion, tipo_proyecto, requerimientos_adicionales):
    # Obtener la recomendación según la categoría y los datos adicionales
    recomendacion = obtener_recomendacion_por_categoria(categoria, criticidad, duracion, tipo_proyecto, requerimientos_adicionales)
    print("\nRecomendaciones para la categoría seleccionada:\n")
    print(recomendacion)

    # Mostrar los requerimientos adicionales
    print("\nRequerimientos adicionales del proyecto:")
    for req, valor in requerimientos_adicionales.items():
        print(f"{req}: {valor}")

def preguntar_otro_proyecto():
    respuesta = input("\n¿Tienes algún otro proyecto que organizar? (si/no): ").strip().lower()
    return respuesta == 'si'

def main():
    print("Bienvenido al Sistema Experto basado en Crystal")

    while True:
        # Solicitar los datos del usuario y el proyecto
        nombres, apellidos, habilidades_usuario = solicitar_datos_usuario()
        nombre_proyecto, equipo, criticidad, duracion, categoria = solicitar_datos_proyecto()
        
        # Solicitar los requerimientos adicionales del proyecto
        requerimientos_adicionales = solicitar_requerimientos()

        # Mostrar las recomendaciones con los datos obtenidos
        mostrar_recomendacion(categoria, criticidad, duracion, nombre_proyecto, requerimientos_adicionales)

        # Preguntar si desea ingresar otro proyecto
        if not preguntar_otro_proyecto():
            print("\nGracias por usar el sistema. ¡Adiós!")
            break

if __name__ == "__main__":
    main()
#ESTE ES EL MOTOR DE INFERENCIA