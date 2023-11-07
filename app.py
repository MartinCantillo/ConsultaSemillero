from Config import app, ma, bd
from flask import Flask, request, jsonify, json
from Model import Estudiante ,GruppoInvestigacion,Semillero,Profesor,Programa,Proyecto,SemilleroSchema,Profesor_Programa,ProyectoSchema,ProfesorProgramaSchema,GruppoInvestigacion_Schema,ProgramaSchema, estudianteSchema,ProfesorSchema

Estudiante_schema = estudianteSchema()
Estudiantes_schema = estudianteSchema(many=True)

GruppoInvestigacion_Schema=GruppoInvestigacion_Schema()
GruppoInvestigacion_Schema=GruppoInvestigacion_Schema(many=True)

ProfesorSchema=ProfesorSchema()
ProfesorSchema=ProfesorSchema(many=True)

ProgramaSchema=ProgramaSchema()
ProgramaSchema=ProgramaSchema(many=True)

ProyectoSchema=ProyectoSchema()
ProyectoSchema=ProyectoSchema(many=True)

ProfesorProgramaSchema=ProfesorProgramaSchema()
ProfesorProgramaSchema=ProfesorProgramaSchema(many=True)

SemilleroSchema=SemilleroSchema()
SemilleroSchema=SemilleroSchema(many=True)







