import math

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        distance = math.sqrt(((self.coor2[0] - self.coor1[0])**2) + ((self.coor2[1] - self.coor1[1])**2))
        print('distance: ' + str(distance))
        return distance
    
    def slope(self):
        slope = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])
        print('slope: ' + str(slope))
        return slope


class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        volumen = self.height * 3.14 * (self.radius**2)
        print('volumen:' + str(volumen))
        return volumen
           
    def surface_area(self):
        top = 3.14 * (self.radius**2)
        area = (2*top) + (2*3.14*self.radius*self.height)
        print('area: ' + str(area))
        return area


#Line
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()



#cylinder
c = Cylinder(2,3)

c.volume()

c.surface_area()



import math
coor1 = (3,2)
coor2 = (8,10)
distance = math.sqrt(((coor2[0] - coor1[0])**2) + ((coor2[1] - coor1[1])**2))

height = 2
radius = 3
area = 2*(height * radius) + 2*(radius**2)
volumen = (radius**2)*height