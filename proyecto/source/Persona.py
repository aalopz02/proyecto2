class Persona:
    def __init__(self,n,c,e):
        self.nombre=n
        self.cedula=c
        self.edad=e
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,n):
        if isinstance(n,str) and n != "":
            self.__nombre=n
        else:print("nombre mal")
    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self,c):
        if isinstance(c,int) and c != 0:
            self.__cedula=c
        else:print("cedula mal")
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,e):
        if isinstance(e,int) and e != 0:
            self.__edad=e
        else:print("edad mal")
