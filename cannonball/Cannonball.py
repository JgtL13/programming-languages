import math
import matplotlib.pyplot as plt

sec = 0
up = True
count = 0

class Cannonball:
    def __init__(self):
        self.xPosition = 0.0
        self.yPosition = 0.0
        self.xVelocity = 0.0
        self.yVelocity = 0.0
        self.pointsX = []
        self.pointsY = []
        self.pointsX.append(0)
        self.pointsY.append(0)
    
    def getX(self):
        return self.xPosition
    
    def getY(self):
        return self.yPosition
    
    def move(self):
        global up
        global count
        self.xPosition = self.xPosition + self.xVelocity
        if (self.yVelocity - 0.981 <= 0):
            up = False
        if up:
            self.yVelocity -= 0.981
            self.yPosition += self.yVelocity
            count += 1
        elif not up:
            self.yVelocity += 0.981
            self.yPosition -= self.yVelocity
            count -= 1
        
    def shoot(self, degrees, velocity):
        global count
        global sec
        angle = degrees * 3.14159 / 180
        self.yVelocity = velocity * math.sin(angle)
        self.xVelocity = velocity * math.cos(angle)
        while True:
            self.move()
            sec += 0.1
            if count == 0:
                break
            if self.yPosition <= 0:
                print("ball touched ground before 0.1 second, please throw harder or higher.")
                break
            print ("Position after " + str(round(sec, 1)) + " second(s)") 
            print ("x : ", self.getX())
            print ("y : ", self.getY())
            self.pointsX.append(self.getX())
            self.pointsY.append(self.getY())
            plt.plot(self.pointsX, self.pointsY)
        plt.xlabel("distance(m)")
        plt.ylabel("height(m)")
        plt.title("Trajectory of the cannonball")
        plt.show()
        
        