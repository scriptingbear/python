#experimenting with overloading magic methods

import math

class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y
         

    @property
    def length(self):
        return math.sqrt(self._x**2 + self._y**2)
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if value > 0:
            self._x = value
        else:
            raise ValueError("{} is not valid for x.".format(value))

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value > 0:
            self._y = value
        else:
            raise ValueError("{} is not valid for y.".format(value))


    #overload the + and - operators
    def __add__(self, other):
        return Vector(self._x + other.x, self._y + other.y)

    def __sub__(self, other):
        #can subtract bigger from smaller
        #it means vector now points in the opposite direction
        #this works out well since the constructor doesn't
        #raise an error when passed a negative parameter value

        return Vector(self._x - other.x, self._y - other.y)




'''
v1 = Vector(1,1)
print("v1 length is {:.2f}".format(v1.length))

#try to instantiate a Vector object with a negative number
v2 = Vector(-3.5, 4)
print("v2 length is {:.2f}".format(v2.length))

#no errors raised; perhaps errors raised only when directly accessing the
#x or y property??

v1.x = 10
v1.y = 5
print("v1 length is {:.2f}".format(v1.length))


v1.x = 10
v1.y = 5.6
print("v1 length is {:.2f}".format(v1.length))
'''
#try "adding" Vector objects

v1 = Vector(4, 9)
v2 = Vector(6, 5)
v3 = v1 + v2
print("v3.x = {0:.2f}.\nv3.y = {1:.2f}\n v3.length = {2:.2f}".format(v3.x, v3.y, v3.length))
 

#try "subtracting" Vector objects

v1 = Vector(50, 100)
v2 = Vector(30, 70)
v3 = v1 - v2
print("v3.x = {0:.2f}.\nv3.y = {1:.2f}\nv3.length = {2:.2f}".format(v3.x, v3.y, v3.length))
    
v1 = Vector(50, 100)
v2 = Vector(30, 70)
v3 = v2 - v1
print("v3.x = {0:.2f}.\nv3.y = {1:.2f}\nv3.length = {2:.2f}".format(v3.x, v3.y, v3.length))
