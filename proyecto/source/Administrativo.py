from Persona import Persona

class Administrativo(Persona):
    def __init__(self,n,c,e,dep,pues):
        super().__init__(n,c,e)
        self.departamento=dep
        self.puesto=pues
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self,dep):
        if isinstance(dep,str) and dep != "":
            self.__departamento=dep
        else:print("departamento mal")
    @property
    def puesto(self):
        return self.__puesto
    @puesto.setter
    def puesto(self,pues):
        if isinstance(pues,str) and pues != "":
            self.__puesto=pues
    
    
