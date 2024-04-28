#el primer parametro de referencia a una clase es "self"
class Profesor:
    def __init__(self, el_nombre, el_email):
        self.__nombre__ = el_nombre
        self.__email__ = el_email

    def dame_tu_nombre(self):
        return self.__nombre__


class Alumno:
    def __init__(self, el_nombre_del_alumno):
        self.__nombre__ = el_nombre_del_alumno
        self.__inasistencias__ = 0
        self.__dieta__ = ""
        self.__mentor__ = None

    def mentoria(self, profesor):
        self.__mentor__ = profesor

    def falta(self):
        self.__inasistencias__ += 1

    def elegir_dieta_especial(self, la_dieta):
        self.__dieta__ = la_dieta

    def es_vegano(self):
        self.__dieta__ = "vegano"

    def esta_libre(self):
        if self.__inasistencias__ >= 5:
            return "ESTA LIBRE"
        else:
            return "OK"


profe_elio = Profesor("Elio", "elio@gmail.com")
profe_gabi = Profesor("Gabriel", "gabriel@um.edu.ar")

# print(profe_elio.dame_tu_nombre())
# print(profe_gabi.dame_tu_nombre())

alumno_juan = Alumno("Juancito")
alumno_Maria = Alumno("Maria")

alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
alumno_juan.falta()
print(alumno_juan.esta_libre())
alumno_juan.falta()
print(alumno_juan.esta_libre())

alumno_Maria.elegir_dieta_especial("vegetariana")
print(alumno_Maria.__dieta__)

alumno_juan.es_vegano()
print(alumno_juan.__dieta__)

alumno_juan.mentoria(profe_elio)
print(alumno_juan.__mentor__.__nombre__)

alumno_Maria.mentoria(profe_gabi)
print(alumno_Maria.__mentor__.__nombre__)

#los_alumnos = [alumno_juan, alumno_maria]  se pueden hacer listas de los objetos

#import ipdb; ipdb.set_trace()

