from Figura import Fig
class Rectangulo(Fig):
    def ___init___(self,x,y,a,b):
        super().__init__(x,y)
        self.base=b
        self.alto=a
        @property
        def base(self):
            return self.__base
        @base.setter
        def base(self,base):
            if base>=0 and base<=1023:
                self.__base=b
            else:print("no")
        @property
        def alto(self):
            return self.__alto 
        @alto.setter
        def altura(self,alto):
            if alto>=0 and alto<=1023:
                self.__alto=a
            else:print("no")
        @property
        def area(self):
            return self.calc_area
        def calc_area(self):
            area=self.__base*self.__alto
        
            
