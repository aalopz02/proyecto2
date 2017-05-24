from Persona import Persona

class Profesor:
    def __init__(self,n,c,e,es,cur):
        self.escuela=es
        self.curso=cur
    @property
    def escuela(self):
        return self.__escuela
    @escuela.setter
    def escuela(self,es):
        if isinstance(es,str) and es != "":
            self.__escuela=es
        else:print("escuela mal")
    @property
    def curso(self):
        return self.__curso
    @curso.setter
    def curso(self,cur):
        if isinstance(cur,str) and cur != "":
            self.__curso=cur
    
