
from flask import Flask, request, jsonify
from config.bd import app, ma, bd
from Model.Estudiante import estudianteSchema
from Model.GInvestigacion import GrupoInvestigacion_Schema
from Model.Profesor import ProfesorSchema
from Model.Programa import ProgramaSchema
from Model.Proyecto import ProyectoSchema
from Model.Semillero import SemilleroSchema
from Model.RelacionProfPro import ProfesorProgramaSchema


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

profesorProgramaSchema = ProfesorProgramaSchema()
profesoresProgramas_schema = ProfesorProgramaSchema(many=True)

semilleroSchema = SemilleroSchema()
semilleros_schema = SemilleroSchema(many=True)

profesorProgramaSchema = ProfesorProgramaSchema()
profesorsProgramaSchema = ProfesorProgramaSchema(many=True)

@app.route("/", methods=["GET"])
def consultarSemillero():
   
    diccionario={
        "Nombre":"Martin"
    }
    return jsonify(diccionario)  


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)