from config.bd import app,ma,bd

class Proyecto(bd.Model):
    __tablename__="tblProyecto"
    codProyecto =bd.Column(bd.Integer,primary_key=True)
    nombreProyecto=bd.Column(bd.String(50))
    fechaInicio=bd.Column(bd.String(50))
    fechaFinal=bd.Column(bd.String(50))
    objetivos=bd.Column(bd.String(50))
    descripcion=bd.Column(bd.String(50))
    resultadosObtenidos=bd.Column(bd.String(50))
    idEstudianteFk =bd.Column(bd.Integer,bd.ForeignKey("tblEstudiante.codigoE"))

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
class ProyectoSchema(ma.Schema):
    class Meta:
        fields=("nombreProyecto","fechaInicio","fechaFinal","objetivos","descripcion","resultadosObtenidos","idEstudianteFk")
