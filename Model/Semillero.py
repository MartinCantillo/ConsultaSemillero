from Config import ma,app,bd

class Semillero(bd.Model):
    __tablename__="tblSemillero"
    codigoSemillero=bd.column(bd.Integer,primeary_Key=True)
    nombre=bd.column(bd.String(50))
    codigoColciencias=bd.column(bd.String(50))
    facultad=bd.column(bd.String(50))
    idProyectoFk =bd.column(bd.integer,bd.ForeignKey("tblProyecto.codProyecto"))#Relacion con proyecto
    idGrupoInFk =bd.column(bd.integer,bd.ForeignKey("tblGInvestigacion.codigoGI"))#Relacion con grupoInvestigacion

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

