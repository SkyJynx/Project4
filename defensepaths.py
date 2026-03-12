import math, random
from panda3d.core import *
import classes as classes

from math import pi, sin, cos


#BASEBALL - YELLOW
def BaseballSeams(step, numSeams, B, F = 1):
    time = step / float(numSeams) * 2 * math.pi

    F4 = 0
    R = 1

    xxx = math.cos(time) - B * math.cos(3 * time)
    yyy = math.cos(time) - B * math.cos(3 * time)
    zzz = F * math.cos(2 * time) + F4 * math.cos(4 * time)

    rrr = math.sqrt(xxx ** 2 + yyy ** 2 + zzz ** 2)
    
    x = R * xxx / rrr
    y = R * yyy / rrr
    z = R * zzz / rrr

    return Vec3(x, y, z)

def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
    unitVec = BaseballSeams(step, numSeams, B = 0.4)
    unitVec.normalize()
    enlarge = centralObject.scaleNote * 1.25
    position = unitVec * radius * 250 + centralObject.modelNode.getPos()
    classes.ColorDrone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 5,  r = 0.8, g = 0.8, b = 0.2, a = 1.0)


#CLOUD - PURPLE
def Cloud(radius = 1):
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1
    z = 2 * random.random() - 1
    unitVec = Vec3(x, y, z)
    unitVec.normalize()
    return unitVec * radius

def DrawCloudDefense(self, centralObject, droneName):
    unitVec = Cloud()
    unitVec.normalize()
    enlarge = centralObject.scaleNote * 1.5
    position = unitVec * enlarge + centralObject.modelNode.getPos()
    classes.ColorDrone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10,  r = 0.8, g = 0.2, b = 0.8, a = 1.0)


#X - RED
def CircleX(p = 0, theta = 0):
    theta = p # starting position in the circle
    x = 50.0 * math.cos(theta)
    y = 50.0 * math.sin(theta)
    z = 0.0 * math.tan(theta)
    unitVec = Vec3(x, y, z)
    return unitVec


def DrawCircleX(self, centralObject, droneName, increment = 10, p = 0, theta = 0):
    unitVec = CircleX(p, theta)
    
    position =  (unitVec + centralObject.modelNode.getPos()) * 1.5
    #position =  unitVec * 500 + centralObject.modelNode.getPos()

    classes.ColorDrone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10,  r = 0.8, g = 0.2, b = 0.2, a = 1.0)
    p = p + increment



#Y - GREEN
def CircleY(p = 0, theta = 0):
    theta = p # starting position in the circle
    x = 0.0 * math.cos(theta)
    y = 50.0 * math.sin(theta)
    z = 50.0 * math.tan(theta)
    unitVec = Vec3(x, y, z)
    return unitVec


def DrawCircleY(self, centralObject, droneName, increment = 10, p = 0, theta = 0):
    unitVec = CircleY(p, theta)
    
    position =  (unitVec + centralObject.modelNode.getPos()) * 1.5
    #position =  unitVec * 500 + centralObject.modelNode.getPos()

    classes.ColorDrone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10,  r = 0.2, g = 0.8, b = 0.2, a = 1.0)
    p = p + increment


#Z - BLUE
def CircleZ(p = 0, theta = 0):
    theta = p # starting position in the circle
    x = 50.0 * math.cos(theta)
    y = 0.0 * math.sin(theta)
    z = 50.0 * math.tan(theta)
    unitVec = Vec3(x, y, z)
    return unitVec


def DrawCircleZ(self, centralObject, droneName, increment = 10, p = 0, theta = 0):
    unitVec = CircleZ(p, theta)
    
    position =  (unitVec + centralObject.modelNode.getPos()) * 1.5
    #position =  unitVec * 500 + centralObject.modelNode.getPos()

    classes.ColorDrone(self.loader, "./Assets/DroneDefender/DroneDefender.x", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 10,  r = 0.2, g = 0.2, b = 0.8, a = 1.0)
    p = p + increment

