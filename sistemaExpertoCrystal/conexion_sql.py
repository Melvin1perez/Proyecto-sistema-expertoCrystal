import pyodbc

# Establecer la conexión con la base de datos SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=DESKTOP-NIOSHCM;'
    'DATABASE=SistemaExperto;'
    'Trusted_Connection=yes;'
)

# Función para ejecutar una consulta de inserción
def insertar_datos_usuario(nombre, apellidos, habilidades):
    cursor = conn.cursor()
    query = """
    INSERT INTO Usuarios (nombre, apellidos, habilidades)
    VALUES (?, ?, ?)
    """
    cursor.execute(query, nombre, apellidos, habilidades)
    conn.commit()

def insertar_datos_proyecto(nombre_proyecto, equipo, criticidad, duracion, categoria):
    cursor = conn.cursor()
    query = """
    INSERT INTO Proyectos (nombre_proyecto, equipo, criticidad, duracion, categoria)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, nombre_proyecto, equipo, criticidad, duracion, categoria)
    conn.commit()

def insertar_requerimientos_proyecto(habilidades_integrantes, tecnologias, recursos, tolerancia_cambio, areas):
    cursor = conn.cursor()
    query = """
    INSERT INTO Requerimientos (habilidades_integrantes, tecnologias, recursos, tolerancia_cambio, areas)
    VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, habilidades_integrantes, tecnologias, recursos, tolerancia_cambio, areas)
    conn.commit()

def cerrar_conexion():
    conn.close()
