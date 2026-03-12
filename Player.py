from CollideObjectBase import SphereCollideObject

from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task


class Ship(SphereCollideObject):
    def __init__(self, loader: Loader, taskMgr: TaskManager, accept: Callable[[str, Callable], None], modelPath: str, parentNode: NodePath, nodeName:str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Ship, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0, 0, 0), 2)
        
        self.accept = accept
        self.taskManager = taskMgr
        
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.scaleNote = scaleVec

        self.SetKeyBindings()


    #FORWARD
    def GoForward(self, keyDown):
        if keyDown:
            self.taskManager.add(self.MoveForward, 'MoveForward')
        else:
            self.taskManager.remove('MoveForward')

    def MoveForward(self, task):
        rate = 5
        trajectory = self.modelNode.parent.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont

    #LEFT
    def GoLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.TurnLeft, 'TurnLeft')
        else:
            self.taskManager.remove('TurnLeft')
    def TurnLeft(self, task):
        #half a degree every frame.
        rate = 0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont

    #RIGHT
    def GoRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.TurnRight, 'TurnRight')
        else:
            self.taskManager.remove('TurnRight')
    def TurnRight(self, task):
        #half a degree every frame.
        rate = -0.5
        self.modelNode.setH(self.modelNode.getH() + rate)
        return Task.cont

    #UP
    def GoUp(self, keyDown):
        if keyDown:
            self.taskManager.add(self.TurnUp, 'TurnUp')
        else:
            self.taskManager.remove('TurnUp')
    def TurnUp(self, task):
        #half a degree every frame.
        rate = -0.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont

    #DOWN
    def GoDown(self, keyDown):
        if keyDown:
            self.taskManager.add(self.TurnDown, 'TurnDown')
        else:
            self.taskManager.remove('TurnDown')
    def TurnDown(self, task):
        #half a degree every frame.
        rate = 0.5
        self.modelNode.setP(self.modelNode.getP() + rate)
        return Task.cont

    #LEFTROLL
    def RollLeft(self, keyDown):
        if keyDown:
            self.taskManager.add(self.LeftRoll, 'LeftRoll')
        else:
            self.taskManager.remove('LeftRoll')
    def LeftRoll(self, task):
        #half a degree every frame.
        rate = -0.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont

    #RIGHTROLL
    def RollRight(self, keyDown):
        if keyDown:
            self.taskManager.add(self.RightRoll, 'RightRoll')
        else:
            self.taskManager.remove('RightRoll')
    def RightRoll(self, task):
        #half a degree every frame.
        rate = 0.5
        self.modelNode.setR(self.modelNode.getR() + rate)
        return Task.cont
    
    #SPEEDBOOST
    def GoFaster(self, keyDown):
        if keyDown:
            self.taskManager.add(self.MoveFaster, 'MoveFaster')
        else:
            self.taskManager.remove('MoveFaster')

    def MoveFaster(self, task):
        rate = 25
        trajectory = self.modelNode.parent.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return Task.cont
    
    #REVERSE
    def GoBack(self, keyDown):
        if keyDown:
            self.taskManager.add(self.MoveBack, 'MoveBack')
        else:
            self.taskManager.remove('MoveBack')

    def MoveBack(self, task):
        rate = -5
        trajectory = self.modelNode.parent.getRelativeVector(self.modelNode, Vec3.forward())
        trajectory.normalize()
        self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)

        return Task.cont

    
    def SetKeyBindings(self): #all key bindings for spaceship movement
        #forward movement
        self.accept('space', self.GoForward, [1])
        self.accept('space-up', self.GoForward, [0])
        #left turn
        self.accept('a', self.GoLeft, [1])
        self.accept('a-up', self.GoLeft, [0])
        #right turn
        self.accept('d', self.GoRight, [1])
        self.accept('d-up', self.GoRight, [0])
        #down turn
        self.accept('s', self.GoUp, [1])
        self.accept('s-up', self.GoUp, [0])
        #down turn
        self.accept('w', self.GoDown, [1])
        self.accept('w-up', self.GoDown, [0])
        #left roll
        self.accept('q', self.RollLeft, [1])
        self.accept('q-up', self.RollLeft, [0])
        #right roll
        self.accept('e', self.RollRight, [1])
        self.accept('e-up', self.RollRight, [0])
        
        #speed boost - this is to make testing faster for myself.
        self.accept('v', self.GoFaster, [1])
        self.accept('v-up', self.GoFaster, [0])
        #back up - this is to make testing faster for myself.
        self.accept('z', self.GoBack, [1])
        self.accept('z-up', self.GoBack, [0])
