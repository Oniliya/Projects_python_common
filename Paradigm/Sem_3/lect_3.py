import math
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calc_area(self):
        self.area = self.width*self.length
        return self.area
    
    def calc_perimetr(self):
        self.perimetr = 2* (self.width+self.length)
        return self.perimetr
    
    def calc_diag_len(self):
        self.diag = (self.width**2 + self.length**2) **0.5
        return self.diag
    
    def calc_diag_angels(self):
        if not hasattr(self, 'diag'):
            self.calc_diag_len

        cos_diag_length = self.length / self.diag
        angle_diag_length = math.acos(cos_diag_length)
        angle_diag_length = math.degrees(angle_diag_length)
        first_angle = 90 - angle_diag_length
        second_angle = (180 - 2*first_angle)/2
        assert first_angle+second_angle == 90
        return first_angle, second_angle

    def __add__(self, other):
        return self.calc_area() + other.calc_area()

    def __eq__(self,other):
        return self.calc_area() == other.calc_area()


r = Rectangle(3, 4)
print(r.width, r.length)
print(r.calc_area())
print(r.calc_perimetr())
print(r.calc_diag_len())
print(r.calc_diag_angels())

r1 = Rectangle(1, 2)
r2 = Rectangle(2, 1)
print(r1+r2)
print(r1==r2)
