class Doctor():

    def __init__(self,id,nombre,correo,foto): #Metodo constructor de medico 
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.foto = foto

    def to_json(self): #metodo para retornar cada uno de los objetos como un diccionario (JSON)
        return {
            'id': self.id,
            'nombre' : self.nombre,
            'correo': self.correo,
            'foto': self.foto
        }

        