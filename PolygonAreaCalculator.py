class Rectangle():

    def __init__(self, width, height):
        self.width = width
        self.height =  height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
        


    def set_width(self,new_width):
        self.width = new_width

    def set_height(self,new_height):
        self.height = new_height

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return  (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        pict = ''
        if self.width <= 50 and self.height <= 50:
            for _ in range(self.height):
                pict += '*'* self.width + '\n'
            return pict        
        else:
            return "Too big for picture."
    
    def get_amount_inside(self,shape):
        return  self.get_area() // shape.get_area()
        

"""
class Square:

    def __init__(self,side):
        self.side = side
        self.square = Rectangle(self.side,self.side)
        #self.get_perimeter = self.square.get_perimeter()

    def __str__(self):
        return f'Square(side={self.side})'

    def set_side(self,new_side):
        self.side = new_side

    def set_width(self,new_width):
        self.square.set_width(new_width)
        self.square.set_height(new_width)
    
    def set_height(self,new_height):
        self.square.set_width(new_height)
        self.square.set_height(new_height)

    def get_area(self):
        return self.square.get_area()
        
    def get_perimeter(self):
        return self.square.get_perimeter()

    def get_diagonal(self):
        return self.square.get_diagonal()

    def get_picture(self):
        return self.square.get_picture()

    def get_amount_inside(self,shape):
        return self.square.get_amount_inside(shape)
"""
class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"
rect = Rectangle(10,15)
rect2 = Square(5)
#rect.set_height(5)
print(rect.width)
print(rect.height)
print(rect.get_picture())
print(rect.height)
print(rect.get_amount_inside(rect2))
print(rect.get_area())
print(rect2.get_area())
print(rect2.get_picture())
print(rect2.get_perimeter())