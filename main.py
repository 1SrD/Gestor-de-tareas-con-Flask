from flask import Flask, render_template, request, redirect, url_for
from models import Tarea
import db
from datetime import datetime as dt


app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    for i in todas_las_tareas:
        print(i)
    return render_template("index.html", lista_de_tareas = todas_las_tareas)


@app.route("/crear-tarea", methods=["POST"])
def crear():
    try:
        fechaLimite = dt.strptime(request.form['fecha'], '%Y-%m-%d').date()
    except ValueError:
        fechaLimite = dt.now().date()

    tarea = Tarea(contenido=request.form['nombre'],
                  fecha=fechaLimite,
                  hecha=False)
    db.session.add(tarea)  # añadir el objeto de Tarea a la base de datos
    db.session.commit()  # ejecuta la operación pendiente de la base de datos
    return redirect(url_for('home'))

@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id=id).delete()
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home")) #Mensaje de log para ver a través del navegador

@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos
    db.session.close()
    return redirect(url_for("home")) #Mensaje de log para ver a través del navegador

@app.route('/editar-tarea/<id>')
def get_tarea(id):
    tarea_selecionada = db.session.query(Tarea).filter_by(id=id)
    return render_template('/update.html', tarea=tarea_selecionada[0])

@app.route('/update/<id>', methods = ['POST'])
def update(id):
    try:
        fechaLimite = dt.strptime(request.form['fecha'], '%Y-%m-%d').date()
    except ValueError:
        fechaLimite = dt.now().date()

    contenido = request.form['nombre']
    fecha = fechaLimite
    db.session.query(Tarea).filter(Tarea.id == id).update({Tarea.contenido:contenido, Tarea.fecha:fechaLimite})
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) #Creamos el modelo de datos
    app.run(debug=True)