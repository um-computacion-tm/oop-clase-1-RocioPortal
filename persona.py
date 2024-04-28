class Persona:

    def __init__(self, nombre: str = "John", apellido: str = "Doe", du: int = 1234567):
        self.__nombre__= nombre
        self.__apellido__= apellido
        self.__du__ = du

    def __str__(self):  #no tengo que mandarle parametros pq ya estan dentro del objeto
        return f'Mis datos son: nombre = {self.__nombre__}, apellido = {self.__apellido__}, documento = {self.__du__}'  #aca puedo poner print