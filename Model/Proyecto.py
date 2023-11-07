from Config import app,ma,bd

class Proyecto(bd.Model):
    __tablename__="tblProyecto"
    codProyecto =bd.column(bd.Integer,primary_key = True)
    nombreProyecto=bd.column(bd.String(50))
    fechaInicio=bd.column(bd.String(50))
    fechaFinal=bd.column(bd.String(50))
    objetivos=bd.column(bd.String(50))
    descripcion=bd.column(bd.String(50))
    resultadosObtenidos=bd.column(bd.String(50))
    idEstudianteFk =bd.column(bd.integer,bd.ForeignKey("tblEstudiante.codigoE"))

    #Constructor
    def __init__(self,nombreProyecto,fechaInicio,fechaFinal,objetivos,descripcion,resultadosObtenidos,idEstudianteFk):
        self.nombreProyecto=nombreProyecto
        self.fechaInicio=fechaInicio
        self.fechaFinal=fechaFinal
        self.objetivos=objetivos
        self.descripcion=descripcion
        self.resultadosObtenidos=resultadosObtenidos
        self.idEstudianteFk=idEstudianteFk

#Creacion de la tabla y contexto 
with app.app_context():
    bd.create_all()

#Descerializacion
class ProyectoSchema(ma.schema):
    class Meta:
        fields=("nombreProyecto","fechaInicio","fechaFinal","objetivos","descripcion","resultadosObtenidos","idEstudianteFk")
