from Config  import ma, bd, app

class Programa(bd.Model):
    __tablename__="tblPrograma"
    codigoPrograma=bd.column(bd.Integer,primeary_Key=True)
    codigo=bd.column(bd.Integer, unique=True)
    nombre=bd.column(bd.String(50))
    facultad=bd.column(bd.String(50))

#Constructor
    def  __init_(self,codigo,nombre,facultad):
        self.codigo=codigo
        self.nombre=nombre
        self.facultad=facultad


#Creacion de la tabla 
with app.app_context():
    bd.create_all()


#Descerializacion
class ProgramaSchema(ma.schema):
    class Meta:
        fields=("codigo","nombre","facultad")
