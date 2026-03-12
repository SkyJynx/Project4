import math, sys, random
from direct.showbase.ShowBase import ShowBase
from direct.task import Task

from panda3d.core import CollisionTraverser, CollisionHandlerPusher

import classes as classes
import defensepaths as defensePath
import Player as player

#I'm curious what the difference is between "from import *" and "import as"? I had initially typed it as "from import *" before we actually did so following the lecture slides and changed it, but while I can tell there's a funcitonal difference, I'm having a hard time mentally defining it, if that makes sense.


class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.accept('escape', self.quit) # hit 'escape' to exit game window

        self.rootAssetFolder = "./Assets"
        self.setScene()

        self.cTrav = CollisionTraverser()
        self.cTrav.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        self.pusher.addCollider(self.Ship.collisionNode, self.Ship.modelNode)
        self.cTrav.addCollider(self.Ship.collisionNode, self.pusher)
        self.cTrav.showCollisions(self.render)

    def setScene(self):
        #LOAD UNIVERSE/SKYBOX
        self.Universe = classes.Universe(self.loader, self.rootAssetFolder + "/Universe/Universe.x", self.render, "Universe", self.rootAssetFolder + "/Universe/universe_tex.jpg", (0,0,0), 12000) #note to self to continue trying to get tiling to work in spare time
        #LOAD IN PLANETS
        self.Planet1 = classes.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, "Universe", self.rootAssetFolder + "/Planets/planet1_tex.jpg", (5000, 600, -5000), 350) #blue
        self.Planet2 = classes.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, "Universe", self.rootAssetFolder + "/Planets/planet2_tex.jpg", (900, -900, 900), 650) #red
        self.Planet3 = classes.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, "Universe", self.rootAssetFolder + "/Planets/planet3_tex.jpg", (1200, -6700, 900), 250) #pink
        self.Planet4 = classes.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, "Universe", self.rootAssetFolder + "/Planets/planet4_tex.jpg", (4000, 1000, 7000), 500) #purple
        self.Planet5 = classes.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, "Universe", self.rootAssetFolder + "/Planets/planet5_tex.jpg", (200, -700, 200), 250) #gold
        self.Planet6 = classes.Planet(self.loader, self.rootAssetFolder + "/Planets/protoPlanet.x", self.render, "Universe", self.rootAssetFolder + "/Planets/planet6_tex.jpg", (-4000, -400, -7000), 980) #green

        #LOAD IN SPACE STATION
        self.Station = classes.Station(self.loader, self.rootAssetFolder + "/SpaceStation1B/spaceStation.x", self.render, "Universe", self.rootAssetFolder + "/SpaceStation1B/SpaceStation1_Dif2.png", (0, 0, 0), 5)

        #LOAD IN SPACE SHIP
        self.Ship = player.Ship(self.loader, self.taskMgr, self.accept, self.rootAssetFolder + "/Spacejet/spacejet.x", self.render, "Ship", self.rootAssetFolder + "/Spacejet/spacejet_C.png", (5, -80, -2), 5)
        
        



        fullCycle = 60
        increment = 10
        p = 0
        theta = p
        for j in range(fullCycle):
            classes.Drone.droneCount += 1
            nickName = "Drone" + str(classes.Drone.droneCount)
            defensePath.DrawCloudDefense(self, self.Planet2, nickName) #planet 1 is off in narnia right now, so I switched it to planet 2 for easier testing.
            defensePath.DrawBaseballSeams(self, self.Station, nickName, j, fullCycle, 2)
        #I'm really not sure what's going on with the baseball seams. Given the complicated nature of the math, I am not in a position to go messing around with it right now, but I'm guessing I just mis-typed something when copying from the powerpoint slides that I need a second pair of eyes to identify.
            defensePath.DrawCircleX(self, self.Planet3, nickName, increment, p, theta)
            defensePath.DrawCircleY(self, self.Planet1, nickName, increment, p, theta)
            defensePath.DrawCircleZ(self, self.Planet4, nickName, increment, p, theta)
        #I could not get the circles working, although I'm fairly certain I'm once again missing something relatively small and stupid. For now, I've opted to submit this as-is and lose the points rather than fall even FURTHER behind.


        classes.SetCamera(self)

    def quit(self):
        sys.exit()
    #quit
        self.accept('escape', self.quit)
app = SpaceJam()
app.run()

