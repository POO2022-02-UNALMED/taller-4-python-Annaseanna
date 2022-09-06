

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
       if(lista is None):
            lista = [alumno]
            if self.listadoAlumnos is None:
                self.listadoAlumnos = lista
            else:
                self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista
        
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return "Grupo de estudiantes:" + " "+ self._grupo
    
    