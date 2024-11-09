# Aquí van las otras funciones que ya tienes

def obtener_recomendacion_por_categoria(categoria, criticidad=None, duracion=None, tipo_proyecto=None, requerimientos_adicionales=None):
    recomendaciones = {
        "Crystal Clear": """Recomendaciones para Crystal Clear:
        - Alta comunicación: Reuniones informales, pero frecuentes.
        - Entregas frecuentes: Ciclos de desarrollo cortos (cada 1-2 semanas).
        - Flexibilidad en roles y mínima documentación.
        - Prototipos frecuentes basados en retroalimentación.
        - Fomentar la autoorganización dentro del equipo.
        - Utilizar herramientas de colaboración simples y efectivas.
        - Adaptarse rápidamente a cambios en los requisitos.""",
        
        "Crystal Yellow": """Recomendaciones para Crystal Yellow:
        - Reuniones diarias más estructuradas y revisiones semanales.
        - Entregas intermedias cada 2-4 semanas.
        - Documentación ligera y especialización de roles.
        - Retroalimentación formal del cliente.
        - Fomentar la comunicación efectiva entre los equipos.
        - Utilizar técnicas de planificación de sprints.
        - Evaluar el progreso regularmente con revisiones retrospectivas.""",
        
        "Crystal Orange": """Recomendaciones para Crystal Orange:
        - Reuniones planificadas diarias en cada subequipo.
        - Entregas grandes cada 4-6 semanas.
        - Roles formalizados y documentación moderada.
        - Sistemas de retroalimentación formales.
        - Incorporar revisiones de código y pruebas regulares.
        - Establecer un marco claro para la gestión de riesgos.
        - Mantener la flexibilidad para adaptarse a cambios en los requisitos del cliente.""",
        
        "Crystal Red": """Recomendaciones para Crystal Red:
        - Reuniones semanales con subequipos.
        - Entregas grandes cada 4-6 semanas.
        - Alta formalización de roles y documentación exhaustiva.
        - Pruebas exhaustivas de seguridad.
        - Realizar análisis de riesgos detallados y gestión de cambios.
        - Establecer métricas claras de éxito y evaluación del rendimiento.
        - Fomentar una cultura de mejora continua dentro del equipo.""",
        
        "Crystal Marrón": """Recomendaciones para Crystal Marrón:
        - Para equipos extremadamente grandes y alta criticidad.
        - Enfoque en la gestión del riesgo y la planificación exhaustiva.
        - Formalización de todos los procesos de desarrollo.
        - Evaluaciones frecuentes del estado del proyecto con todos los interesados.
        - Uso de metodologías ágiles combinadas con prácticas tradicionales.
        - Mantener un alto nivel de comunicación y colaboración entre equipos.
        - Implementar procesos de auditoría y control de calidad rigurosos."""
    }

    recomendacion = recomendaciones.get(categoria, "Categoría no válida. Por favor, verifica los datos ingresados.")
    
    # Ajuste según niveles de criticidad
    if criticidad in ["Alta", "Muy Alta"]:
        recomendacion += "\n- Aumentar el enfoque en pruebas de seguridad y análisis de riesgos."
    elif criticidad == "Media":
        recomendacion += "\n- Considerar evaluaciones periódicas de riesgos y ajustes en la planificación."
    elif criticidad == "Baja":
        recomendacion += "\n- Enfocar en eficiencia y entregas rápidas, sin necesidad de pruebas de alto rigor."

    # Ajuste según la duración del proyecto
    if duracion:
        if duracion > 6:
            recomendacion += "\n- Considerar estrategias de escalabilidad y mantenimiento debido a la duración prolongada."
        elif duracion <= 6:
            recomendacion += "\n- Priorizar la velocidad y eficiencia en el desarrollo debido a la duración más corta."

    # Ajuste según el tipo de proyecto
    if tipo_proyecto == "Web":
        recomendacion += "\n- Ajuste específico para desarrollo web: Optimizar para rendimiento y disponibilidad."
    elif tipo_proyecto == "Móvil":
        recomendacion += "\n- Recomendación especial para desarrollo móvil: Pruebas exhaustivas en distintos dispositivos."
    elif tipo_proyecto == "Software":
        recomendacion += "\n- Desarrollar con un enfoque en pruebas de integración y modularidad."
    elif tipo_proyecto == "Crítico":
        recomendacion += "\n- Ajustes en rendimiento y seguridad debido a la criticidad del proyecto."

    # Agregar recomendaciones basadas en los requerimientos adicionales
    if requerimientos_adicionales:
        if 'Tolerancia al cambio' in requerimientos_adicionales:
            tolerancia = requerimientos_adicionales['Tolerancia al cambio']
            if tolerancia == 'alta':
                recomendacion += "\n- El proyecto tiene alta tolerancia al cambio. Se recomienda mantener una alta flexibilidad y adaptabilidad."
            elif tolerancia == 'media':
                recomendacion += "\n- Tolerancia media al cambio: equilibrar estabilidad con flexibilidad para adaptarse según sea necesario."
            elif tolerancia == 'baja':
                recomendacion += "\n- El proyecto tiene baja tolerancia al cambio. Se debe priorizar la estabilidad y control de cambios."

        if 'Tecnologías' in requerimientos_adicionales:
            tecnologias = requerimientos_adicionales['Tecnologías']
            recomendacion += f"\n- Tecnologías recomendadas para este proyecto: {tecnologias}"

        if 'Recursos' in requerimientos_adicionales:
            recursos = requerimientos_adicionales['Recursos']
            recomendacion += f"\n- Recursos disponibles: {recursos}"

        if 'Áreas' in requerimientos_adicionales:
            areas = requerimientos_adicionales['Áreas']
            recomendacion += f"\n- Áreas específicas de aplicación del proyecto: {areas}"

    return recomendacion


# Aquí va la nueva función que debes agregar

def validar_tamano_equipo(equipo, categoria):
    """
    Valida si el tamaño del equipo es adecuado para la categoría de Crystal seleccionada.
    """
    if categoria == "Crystal Clear" and equipo <= 6:
        return True
    elif categoria == "Crystal Yellow" and 7 <= equipo <= 20:
        return True
    elif categoria == "Crystal Orange" and 21 <= equipo <= 50:
        return True
    elif categoria == "Crystal Red" and 51 <= equipo <= 100:
        return True
    elif categoria == "Crystal Marrón" and equipo > 100:
        return True
    else:
        return False
