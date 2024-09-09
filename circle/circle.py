import math

class Circle():
    def __init__(self,radius):
        if(radius<=0):
            raise ValueError("El valor del radio tiene que ser mayor a 0")
        
        self.radius=radius
    
    def get_radius(self):
        return self.radius
    
    def get_area(self):
        return math.pi * math.pow(self.radius,2)
    
    def get_perimeter(self):
        return 2 *math.pi * self.radius
    
    def __mul__(self, n):
        
        if(n<=0):
            raise ValueError("El valor del multiplo tiene que ser mayor a 0")
        newCircle = Circle(self.radius * n)
        
        return newCircle
    
    def __str__(self):
        return f"Soy un Circulo de radio {self.radius}"
        
    pass
