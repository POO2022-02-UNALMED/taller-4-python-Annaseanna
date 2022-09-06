class Asignatura:

    def __init__(self, nombre, salon="remoto"):
        self._nombre = nombre
        self._salon = salon
    def __str__(self):
        return str(self.nombre)+" "+str(self.salon)
