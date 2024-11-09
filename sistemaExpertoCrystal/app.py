from flask import Flask, render_template, request, redirect, url_for, session
from conexion_sql import insertar_datos_usuario, insertar_datos_proyecto
from logica import obtener_recomendacion_por_categoria

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Para manejar la sesión de forma segura

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
    if request.method == 'POST':
        session['nombres'] = request.form['nombres']
        session['apellidos'] = request.form['apellidos']
        session['habilidades_usuario'] = request.form['habilidades_usuario']
        
        
        insertar_datos_usuario(session['nombres'], session['apellidos'], session['habilidades_usuario'])
        
        return redirect(url_for('proyecto'))
    return render_template('usuario.html')

@app.route('/proyecto', methods=['GET', 'POST'])
def proyecto():
    if request.method == 'POST':
        session['nombre_proyecto'] = request.form['nombre_proyecto']
        session['equipo'] = int(request.form['equipo'])
        session['criticidad'] = request.form['criticidad']
        session['duracion'] = int(request.form['duracion'])
        
        equipo = session['equipo']
        if equipo <= 6:
            session['categoria'] = "Crystal Clear"
        elif 7 <= equipo <= 20:
            session['categoria'] = "Crystal Yellow"
        elif 21 <= equipo <= 50:
            session['categoria'] = "Crystal Orange"
        elif 51 <= equipo <= 100:
            session['categoria'] = "Crystal Red"
        else:
            session['categoria'] = "Crystal Marrón"
        
        # Inserta datos del proyecto
        insertar_datos_proyecto(
            session['nombre_proyecto'],
            session['equipo'],
            session['criticidad'],
            session['duracion'],
            session['categoria']
        )
        
        return redirect(url_for('requerimientos'))
    return render_template('proyecto.html')


@app.route('/requerimientos', methods=['GET', 'POST'])
def requerimientos():
    if request.method == 'POST':
        session['habilidades_integrantes'] = request.form['habilidades_integrantes']
        session['tecnologias'] = request.form['tecnologias']
        session['recursos'] = request.form['recursos']
        session['tolerancia_al_cambio'] = request.form['tolerancia_al_cambio']
        session['areas'] = request.form.getlist('areas')
        
 

        return redirect(url_for('recomendaciones'))
    return render_template('requerimientos.html')


@app.route('/recomendaciones')
def recomendaciones():
    categoria = session.get('categoria')
    criticidad = session.get('criticidad')
    duracion = session.get('duracion')
    tipo_proyecto = session.get('nombre_proyecto')
    requerimientos_adicionales = {
        "Habilidades de los integrantes": session.get('habilidades_integrantes'),
        "Tecnologías": session.get('tecnologias'),
        "Recursos": session.get('recursos'),
        "Tolerancia al cambio": session.get('tolerancia_al_cambio'),
        "Áreas": session.get('areas')
    }
    
    recomendacion = obtener_recomendacion_por_categoria(
        categoria, criticidad, duracion, tipo_proyecto, requerimientos_adicionales
    )
    
    return render_template('recomendaciones.html', recomendacion=recomendacion)

if __name__ == '__main__':
    app.run(debug=True)
