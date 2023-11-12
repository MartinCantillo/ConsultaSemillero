
from flask import Flask, request, jsonify, render_template
from config.bd import app, bd, ma
from Model.Estudiante import Estudiante, EstudianteSchema
from Model.Profesor import ProfesorSchema
from Model.Programa import ProgramaSchema
from Model.GInvestigacion import GrupoInvestigacion_Schema
from Model.Semillero import Semillero, SemilleroSchema

from Model.Proyecto import Proyecto, ProyectoSchema
from Model.Objetivos import Objetivos ,ObjetivosSchema
from Model.ResultadosOb import ResultadosOb,ResultadosObSchema
from Model.EstudianteP import EstudianteP ,EstudiantePSchema





Estudiante_schema = EstudianteSchema()
Estudiantes_schema = EstudianteSchema(many=True)

GruppoInvestigacion_Schema = GrupoInvestigacion_Schema()
GrupposInvestigacion_schema = GrupoInvestigacion_Schema(many=True)

passrofesorSchema = ProfesorSchema()
profesores_schema = ProfesorSchema(many=True)

programaSchema = ProgramaSchema()
programas_schema = ProgramaSchema(many=True)

proyectoSchema = ProyectoSchema()
proyectos_schema = ProyectoSchema(many=True)


semilleroSchema = SemilleroSchema()
semilleros_schema = SemilleroSchema(many=True)


@app.route("/", methods=['GET'])
def index():
    nombre= "Login"
    return render_template('index.html')


@app.route("/traerSemilleros", methods=['GET'])
def GetSemilleros():
     results = bd.session.query(Semillero).all() 
     dato={}   
     i=0
     for s in results:
        i+=1	       
        dato[i] = {
        "codigoSemillero":s.codigoSemillero,
        'nombre' :s.nombre, 
        'facultad':s.facultad,  

        }
      
     print(dato)
    
     return jsonify(dato)

@app.route("/Semillero", methods=['GET'])
def GoSemilleros():  
  return render_template("Semillero.html")


@app.route('/FiltroSemillero', methods=['GET'])
def GetData():
    idSemillero = request.json["idSemillero"]

    # Verifica si idSemillero está presente en la solicitud JSON
    if idSemillero is None:
        return {"error": "Se requiere el campo 'idSemillero' en la solicitud JSON"}, 400

    # Consulta con filtro entre las tres entidades para hacer el filtro
    results = bd.session.query(Semillero, Proyecto, EstudianteP,Estudiante, Objetivos, ResultadosOb) \
        .join(Proyecto, Semillero.codigoSemillero == Proyecto.idSemilleroFk) \
        .join(EstudianteP, Proyecto.codProyecto == EstudianteP.codProyectoFk) \
        .join(Estudiante, EstudianteP.codigoEstudianteP == Estudiante.codigoE) \
        .join(Objetivos, Proyecto.codProyecto == Objetivos.idProyectoOFk) \
        .join(ResultadosOb, Proyecto.codProyecto == ResultadosOb.idProyectoObFk) \
        .filter(Semillero.codigoSemillero == idSemillero).all()

    # Listas donde se almacenarán los datos de cada entidad
    estudiantes_list = []
    estudiantesP_list = []
    semilleros_list = []
    proyectos_list = []
    objetivos_list = []
    resultadosOb_list = []
    print(results)

    for semillero, proyecto,estudiantep,estudiante,objetivos, resultadosOb in results:
         semilleros_list.append({
        "codigoSemillero":semillero.codigoSemillero,
        'nombre' :semillero.nombre, 
        'facultad':semillero.facultad,  
        })
         
         estudiantesP_list.append({
            "codigoEstudianteP": estudiantep.codigoEstudianteP,
            "codProyectoFk": estudiantep.codProyectoFk,
            "idEstudianteFk": estudiantep.idEstudianteFk,
        })

         estudiantes_list.append({
            "codigoE": estudiante.codigoE,
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
        })
         proyectos_list.append({
            "codProyecto": proyecto.codProyecto,
            "nombreProyecto": proyecto.nombreProyecto,
        })

         objetivos_list.append({
            "codigoOb": objetivos.codigoOb,
            "descripcion": objetivos.descripcion,
        })

         resultadosOb_list.append({
            "codigoRO": resultadosOb.codigoRO,
            "descripcionOb": resultadosOb.descripcionOb,
        })

    # Eliminar duplicados de las listas
    estudiantes_list = [dict(t) for t in {tuple(d.items()) for d in estudiantes_list}]
    estudiantesP_list = [dict(t) for t in {tuple(d.items()) for d in estudiantesP_list}]
    semilleros_list = [dict(t) for t in {tuple(d.items()) for d in semilleros_list}]
    proyectos_list = [dict(t) for t in {tuple(d.items()) for d in proyectos_list}]
    objetivos_list = [dict(t) for t in {tuple(d.items()) for d in objetivos_list}]
    resultadosOb_list = [dict(t) for t in {tuple(d.items()) for d in resultadosOb_list}]

    return jsonify({
        "Estudiantes": estudiantes_list,
        "EstudiantesP":estudiantesP_list,
        "Proyectos": proyectos_list,
        "Objetivos": objetivos_list,
        "ResultadosOb": resultadosOb_list
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)