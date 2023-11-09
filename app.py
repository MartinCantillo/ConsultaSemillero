
from flask import Flask, request, jsonify, render_template
from config.bd import app, bd, ma
from Model.Estudiante import Estudiante, estudianteSchema
from Model.Profesor import ProfesorSchema
from Model.Programa import ProgramaSchema
from Model.GInvestigacion import GrupoInvestigacion_Schema
from Model.Semillero import Semillero, SemilleroSchema
from Model.Proyecto import Proyecto, ProyectoSchema
from Model.Objetivos import Objetivos ,ObjetivosSchema




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
        "codigoSemillero":s.codigoSemillero,
        'nombre' :s.nombre, 
        'facultad':s.facultad,  

        }
      
     print(s.nombre )  
    
     return jsonify(dato)

@app.route("/Semillero", methods=['GET'])
def GoSemilleros():  
  return render_template("Semillero.html")

@app.route('/FiltroSemillero', methods=['POST'])
def GetData():
   idSemillero=request.json["idSemillero"]
   print(idSemillero)
    # Verifica si idSemillero está presente en la solicitud JSON
   if idSemillero is None:
       return {"error": "Se requiere el campo 'idSemillero' en la solicitud JSON"}, 400

    # Consulta con filtro entre las tres entidades para hacer el filtro
   results = bd.session.query(Semillero, Proyecto, Estudiante)\
        .join(Proyecto, Semillero.idProyectoFk == Proyecto.codProyecto)\
        .join(Estudiante, Proyecto.idEstudianteFk == Estudiante.codigoE)\
        .filter(Semillero.codigoSemillero == idSemillero).all()

    # Diccionario donde se almacena los datos de la info consultada
   dato = {}

    # Contador para ir recorriendo los datos
   i = 0

   for semillero, proyecto, estudiante in results:
        # Incremento i
        i+=1

        # Creo el diccionario con la info de results
        dato[i] = {
            "Semillero": {
                "codigoSemillero": semillero.codigoSemillero,
                "idProyectoFk": semillero.idProyectoFk
            },
            "Proyecto": {
                "codProyecto": proyecto.codProyecto,
                "nombreProyecto": proyecto.nombreProyecto,
                "objetivos": proyecto.objetivos,
                "resultadosObtenidos": proyecto.resultadosObtenidos,
            },
            "Estudiante": {
                "codigoE": estudiante.codigoE,
                "nombre": estudiante.nombre,
                "apellido": estudiante.apellido,
            }
        }

   
   return dato

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9566)