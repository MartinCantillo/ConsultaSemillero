from config.bd import app, bd, ma
class GInvestigacion(bd.Model):
    __Tablename__="tblGInvestigacion"
    codigoGI = bd.Column(bd.Integer, primary_key = True)
    nombre = bd.Column(bd.String(50))
    lider = bd.Column(bd.String(50))
    lineaInvestigacion = bd.Column(bd.String(50))
    idProfesorFk = bd.relationship('tblProfesor', secondary="profesor_programa") #relacion con  profesor_programa

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
