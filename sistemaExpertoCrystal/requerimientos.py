# requerimientos.py

def obtener_requerimientos_adicionales():
    print("Ingrese los requerimientos adicionales del proyecto:")

    # Solicitar habilidades de los integrantes
    habilidades_integrantes = input("Habilidades de los integrantes: ")

    # Solicitar tecnologías
    tecnologias = input("Tecnologías a utilizar: ")

    # Solicitar recursos disponibles
    recursos = input("Recursos disponibles: ")

    # Solicitar tolerancia al cambio con opciones específicas
    tolerancia_cambio = input("Tolerancia al cambio (Baja, Media, Alta): ").capitalize()
    while tolerancia_cambio not in ["Baja", "Media", "Alta"]:
        print("Opción inválida. Debe ser Baja, Media o Alta.")
        tolerancia_cambio = input("Tolerancia al cambio (Baja, Media, Alta): ").capitalize()

    # Solicitar áreas específicas con múltiples opciones
    print("Seleccione el área del proyecto:")
    print("Opciones: Medicina, Arquitectura, Psicología, Estudiantil, Obrero, Agricultor, Tecnología, Ingeniería, Educación, etc.")
    area = input("Área del proyecto: ").capitalize()

    # Retornar los datos en un diccionario
    return {
        "Habilidades de los integrantes": habilidades_integrantes,
        "Tecnologías": tecnologias,
        "Recursos": recursos,
        "Tolerancia al cambio": tolerancia_cambio,
        "Área": area
    }
