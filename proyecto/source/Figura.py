class Fig:
    def __init__(self,x1,y1):
        self.x=x1
        self.y=y1
    @property
    def x(self):
        return self.__x# "__.variable" para hacerlo privado
    @x.setter
    def x(self,x):
        if x>=0 and x<=1023:
            self.__x=x
        else:print("no")
    @property#Consultar valor
    def y(self):
        return self.__y
    @y.setter#setear valor
    def y(self,y):
        if y>=0 and y<=1023:
            self.__y=y
        else:print("no")
    
