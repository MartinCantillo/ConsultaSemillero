from config.bd import ma , bd, app

class Objetivos(bd.Model):
 __tablename__="tblObjetivos"
 codigoOb = bd.Column(bd.Integer, primary_key = True)
 descripcion=bd.Column(bd.String(50))


#Constructor
def __inti__(self,codigoOb,descripcion):
 self.codigoOb=codigoOb
 self.descripcion=descripcion


#Creacion de la tabla 
with app.app_context():
    bd.create_all()

#Descerializacion
class ObjetivosSchema(ma.Schema):
    class Meta:
        fields=("codigoOb","descripcion")


 