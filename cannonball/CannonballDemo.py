import os
from Cannonball import Cannonball

cb = Cannonball()
angle = 0
velocity = 0.0
print ("Enter angle and velocity")
angle = input ("Angle : ")
velocity = input ("Velocity : ")
angle = int(angle)
velocity = int(velocity)
cb.shoot(angle, velocity)

print()
os.system("pause")