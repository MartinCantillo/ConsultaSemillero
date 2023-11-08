
from flask import Flask, request, jsonify, render_template
from config.bd import app, ma, bd
from Model.Estudiante import Estudiante, estudianteSchema
from Model.Profesor import ProfesorSchema
from Model.Programa import ProgramaSchema
from Model.Proyecto import Proyecto, ProyectoSchema
from Model.GInvestigacion import GrupoInvestigacion_Schema
from Model.Semillero import Semillero, SemilleroSchema


Estudiante_schema = estudianteSchema()
Estudiantes_schema = estudianteSchema(many=True)

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
        'nombre' :s.nombre, 
        'facultad':s.facultad          
        }
      
     print(s.nombre )  
    
     return jsonify(dato)

@app.route("/GetSemillero", methods=["GET"])
def consultarSemillero():
    semilleros = Semillero.query.all()
    resultado = []

    for semillero in semilleros:
        proyectos = Proyecto.query.filter_by(idProyectoFk=semillero.idProyectoFk).all()
        estudiantes = [estudiante.nombre for proyecto in proyectos for estudiante in Estudiante.query.filter_by(idEstudianteFk=proyecto.idEstudianteFk)]

        info_semillero = {
            "Nombre del Grupo de Investigación": semillero.idGrupoInFk.nombre,
            "Líder del Grupo de Investigación": semillero.idGrupoInFk.lider,
            "Nombre del Semillero": semillero.nombre,
            "Periodo Académico": semillero.periodo_academico,
            "Docente líder del semillero": semillero.idProyectoFk.docente_lider,
            "Proyectos": [proyecto.nombreProyecto for proyecto in proyectos],
            "Objetivos": [proyecto.objetivos for proyecto in proyectos],
            "Resultados Obtenidos": [proyecto.resultadosObtenidos for proyecto in proyectos],
            "Estudiantes": estudiantes,
            "Profesores": [profesor.nombre for profesor in semillero.idGrupoInFk.profesores]
        }
        resultado.append(info_semillero)

    return jsonify({"semilleros_investigacion": resultado})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)