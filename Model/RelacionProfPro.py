from config.bd import app, bd, ma

# Definición de la tabla de unión como una clase de modelo
class ProfesorPrograma(bd.Model):
    __tablename__ = "profesor_programa"
    profesorId = bd.Column(bd.Integer, bd.ForeignKey("tblProfesor.codigoProfesor"), primary_key=True)
    programaId = bd.Column(bd.Integer, bd.ForeignKey("tblPrograma.codigoPrograma"), primary_key=True)

    #Constructor
    def __init__(self,profesorId,programaId):
        self.codigo=profesorId
        self.telefono=profesorId
        


# Creación del contexto de la aplicación
with app.app_context():
    # Crear la tabla de unión
    bd.create_all()

# Deserialización
class ProfesorProgramaSchema(ma.Schema):
    class Meta:
        fields = ("profesorId", "programaId")
