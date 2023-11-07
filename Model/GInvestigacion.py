from Model.Profesor import Profesor
from config.bd import app, bd, ma

# que represente la relación muchos a muchos
profesor_programa = bd.Table(
    "profesor_programa",
    bd.Column("profesorId", bd.Integer, bd.ForeignKey("tblProfesor.codigoProfesor"),primary_key=True),
    bd.Column("programaId", bd.Integer, bd.ForeignKey("tblPrograma.codigoPrograma"),primary_key=True)
)


class GInvestigacion(bd.Model):
    __tablename__ ='tblGInvestigacion'
    codigoGI = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(50))
    lider = bd.Column(bd.String(50))
    profesores = bd.relationship(Profesor, secondary=profesor_programa)
    lineaInvestigacion = bd.Column(bd.String(50))
   # profesor = bd.relationship("tblProfesor", secondary="profesor_programa") #relacion con  profesor_programa
    
    #Constructor
    def __init__(self,nombre,lider,lineaInvestigacion,idProfesorFk):
        self.nombre=nombre
        self.lider=lider
        self.lineaInvestigacion=lineaInvestigacion
        self.idProfesorFk=idProfesorFk



#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class GrupoInvestigacion_Schema(ma.Schema):
    class Meta:
        fields=("nombre","lider","lineaInvestigacion","idProfesorFk")
