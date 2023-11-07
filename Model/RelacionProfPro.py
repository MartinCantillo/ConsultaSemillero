from Config import app, bd, ma

#Relacion muchos a muchos nueva entidad
Profesor_Programa=bd.Table(
  "profesor_programa",
  bd.column("profesorId",bd.Integer,bd.ForeignKey("tblProfesor.codigoProfesor")),
  bd.column("programaId",bd.Integer,bd.ForeignKey("tblPrograma.codigoPrograma"))
)

# Creación del contexto de la aplicación
with app.app_context():
    # Crear la tabla de unión
    bd.create_all()

#Descerializacion
class ProfesorProgramaSchema(ma.Schema):
    class Meta:
        fields = ("profesorId", "programaId")    