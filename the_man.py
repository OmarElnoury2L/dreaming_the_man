class Vettore:
    def __init__(self,x1,y1):
        self.x1 = x1
        self.y1 = y1
    def modulo(self):
        m = (((self.x1)**2+(self.y1)**2)**(1/2))
        return m
    def somma(self, v2):
        v2.x1 = self.x1+v2.x1
        v2.y1 = self.y1+v2.y1
        return v2 
v1 = Vettore(5,3)
v2 = Vettore(-2,1)
v2 = v1.somma(v2)
print(v2.modulo())
