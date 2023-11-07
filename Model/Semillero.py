from config.bd import ma,app,bd

class Semillero(bd.Model):
    __tablename__="tblSemillero"
    codigoSemillero = bd.Column(bd.Integer, primary_key = True)
    nombre=bd.Column(bd.String(50))
    codigoColciencias=bd.Column(bd.String(50))
    facultad=bd.Column(bd.String(50))
    idProyectoFk =bd.Column(bd.Integer,bd.ForeignKey("tblProyecto.codProyecto"))#Relacion con proyecto
    idGrupoInFk =bd.Column(bd.Integer,bd.ForeignKey("tblGInvestigacion.codigoGI"))#Relacion con grupoInvestigacion

    #Constructor
    def __init__(self,nombre,codigoColciencias,facultad,idProyectoFk,idGrupoInFk):
        self.nombre=nombre
        self.codigoColciencias= codigoColciencias
        self.facultad= facultad
        self.idProyectoFk=idProyectoFk
        self.idGrupoInFk=idGrupoInFk

#Creación del contexto de la aplicación
with app.app_context():
    # Crear la tabla de unión
    bd.create_all()

#Descerializacion
class SemilleroSchema(ma.Schema):
    class Meta:
        fields = ("nombre", "codigoColciencias","facultad","idProyectoFk","idGrupoInFk")    

