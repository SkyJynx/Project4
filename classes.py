from direct.showbase.ShowBase import ShowBase
from panda3d.core import * 
from direct.task import Task

from CollideObjectBase import *


class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName:str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 0.9)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.scaleNote = scaleVec

class Planet(SphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName:str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Planet, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.scaleNote = scaleVec

class Station(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName:str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Station, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 10, 1, -1, -10, 10)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.scaleNote = scaleVec

class Drone(SphereCollideObject):
    droneCount = 0

class ColorDrone(SphereCollideObject):
    droneCount = 0
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName:str, texPath: str, posVec: Vec3, scaleVec: float, r = 0.6, g = 0.6, b = 1.0, a = 1.0):
        super(ColorDrone, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 1)
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.scaleNote = scaleVec
        
        self.modelNode.setColorScale(r, g, b, a)


#CAMERA
def SetCamera(self):
    self.disableMouse()
    self.camera.reparentTo(self.Ship.modelNode)
    self.camera.setFluidPos(0, -10, 0)
