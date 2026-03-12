from panda3d.core import PandaNode, Loader, NodePath, CollisionNode, CollisionSphere, CollisionInvSphere, CollisionCapsule, Vec3


class PlacedObject(PandaNode):
    #just a generic object in the scene at this poitn. No relation to collisions.
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        self.modelNode: NodePath = loader.loadModel(modelPath)
        
        #we want to make sure we are having the right type passed to this parameter, or else throw an error.
        if not isinstance(self.modelNode, NodePath):
            raise AssertionError("PlacedObject loader.loadModel(" +modelPath + ")did not return a proper PandaNode!")
        
        self.modelNode.reparentTo(parentNode)
        self.modelNode.setName(nodeName)

class CollidableObject(PlacedObject): #relate our PlacedObject to collisions by using it as a helper class for this function to create collisions
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str):
        super(CollidableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        #Every single type of collider will get the "_cNode" tag behind it to signifiy that it's a collidable object.
        self.collisionNode = self.modelNode.attachNewNode(CollisionNode(nodeName + '_cNode'))

class InverseSphereCollideObject(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super(InverseSphereCollideObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionInvSphere(colPositionVec, colRadius))
        self.collisionNode.show() #makes colliders visible for debugging

class CapsuleCollidableObject(CollidableObject):
    # a and b are respectively the furthest point on a capsule collider on either side
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, ax: float, ay: float, az: float, bx: float, by: float, bz: float, r: float):
        super(CapsuleCollidableObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionCapsule(ax, ay, az, bx, by, bz, r))
        self.collisionNode.show() #makes colliders visible for debugging


class SphereCollideObject(CollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, colPositionVec: Vec3, colRadius: float):
        super(SphereCollideObject, self).__init__(loader, modelPath, parentNode, nodeName)
        self.collisionNode.node().addSolid(CollisionSphere(colPositionVec, colRadius))
        self.collisionNode.show() #makes colliders visible for debugging
