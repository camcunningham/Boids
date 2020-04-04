import tkinter as tk
from boid import *
import random
import cmath, math
from utility import *

'''
Structure:

init positions

Loop:
    draw_boids()
        Draws all boids at their current position
    updateBoidPositions()
        Will change their velocities based on the three rules for each boid
        Then will apply that to their position
        Structure:
            Vector v1,v2,v3
            for boid in boids:
                v1 = rule1(boid)
                v2 = rule2(boid)
                v3 = rule3(boid)

                boid.velocity += (v1 + v2 + v3)
                boid.position = boid.position + boid.velocity
EndLoop

The rules:

Rule 1: Boids try to fly towards the center of mass of neighbouring boids (Cohesion)

Rule 2: Boids keep a small distance between them and other boids (Separation)

Rule 3: Boids try to match their velocity with other boids (Alignment)

For a soft bound:
PROCEDURE bound_position(Boid b)
	Integer Xmin, Xmax, Ymin, Ymax, Zmin, Zmax
	Vector v

	IF b.position.x < Xmin THEN
		v.x = 10
	ELSE IF b.position.x > Xmax THEN
		v.x = -10
	END IF
	IF b.position.y < Ymin THEN
		v.y = 10
	ELSE IF b.position.y > Ymax THEN
		v.y = -10
	END IF
	IF b.position.z < Zmin THEN
		v.z = 10
	ELSE IF b.position.z > Zmax THEN
		v.z = -10
	END IF

	RETURN v
END PROCEDURE
'''
MAXSPEED = 2
# Function that moves the boids based on their velocity: Runs once then repeats every 25ms
def moveBoids():
    # Update boid position based on rules
    updateBoidVelocities()
    for boid in boids:
        # Move on screen
        canvas.move(boid.shape, boid.velocity[0], boid.velocity[1])
        boid.position = tadd(boid.position, boid.velocity)
    # Run this function again
    root.after(10,moveBoids)

def updateBoidVelocities():
    for boid in boids:
        # Normalizing speed so it doesnt go out of control
        if boid.velocity[0] > MAXSPEED:
            boid.velocity = (MAXSPEED, boid.velocity[1])
        elif boid.velocity[0] < (-MAXSPEED):
            boid.velocity = (-MAXSPEED, boid.velocity[1])

        if boid.velocity[1] > MAXSPEED:
            boid.velocity = (boid.velocity[0], MAXSPEED)
        elif boid.velocity[1] < (-MAXSPEED):
            boid.velocity = (boid.velocity[0], -MAXSPEED)


        v1 = rule1(boid)
        v2 = rule2(boid)
        v3 = rule3(boid)
        v4 = edgeRule(boid)

        boid.velocity = tadd(boid.velocity, v1)
        boid.velocity = tadd(boid.velocity, v2)
        # boid.velocity = tadd(boid.velocity, v3)
        boid.velocity = tadd(boid.velocity, v4)

        # print("VELOCITY FOR BOID CURRENTLY:" + str(boid.velocity[0]) + "," + str(boid.velocity[1]))
        # print("VELOCITY FOR EDGE RULE CURRENTLY:" + str(v4[0]) + "," + str(v4[1]))
        # Apply new changes to boids velocity
        # boid.velocity = (boid.velocity[0] + v1[0] + v2[0] + v3[0] + v4[0], boid.velocity[1] + v1[1] + v2[1] + v3[1] + v4[0])

# Temp return values for these right now

# Rule 1: Boids try to fly towards the center of mass of neighbouring boids
def rule1(b):
    changeInVel = (0,0)
    for boid in boids:
        if boid is not b:
            changeInVel = tadd(changeInVel, boid.position)
    changeInVel = (changeInVel[0] / len(boids) - 1, changeInVel[1] / len(boids) - 1)
    # Making the change smaller: Dividing it by 100 makes it move 1% of the way towards center
    return ( (changeInVel[0] - b.position[0]) / 2000 , (changeInVel[0] - b.position[0]) / 2000 )

# Rule 2: Boids keep a small distance between them and other boids
def rule2(b):
    changeInVel = (0,0)
    for boid in boids:
        if boid is not b:
            if abs(boid.position[0] - b.position[0]) < 10 and abs(boid.position[1] - b.position[1]) < 50:
                changeInVel = tdiv(tsub(changeInVel, (tsub(boid.position, b.position))), 5)
    return changeInVel

# Rule 3: Boids try to match velocity with near boids
def rule3(b):
    changeInVel = (0,0)
    for boid in boids:
        if boid is not b:
            changeInVel = tadd(changeInVel, boid.velocity)
    changeInVel = tdiv(changeInVel, len(boids) - 1)
    return tdiv(tsub(changeInVel, b.velocity), 8)

def edgeRule(b):
    XMIN = 100
    YMIN = 100
    XMAX = 600
    YMAX = 600
    changeInVel = (0,0)

    if b.position[0] < XMIN:
        print(" XMIN Conditiion met")
        changeInVel = (1, changeInVel[1])
    elif b.position[0] > XMAX:
        print("XMAX Conditiion met")
        changeInVel = (-1, changeInVel[1])

    if b.position[1] < YMIN:
        print("YMIN Conditiion met")
        changeInVel = (changeInVel[0], 1)
    elif b.position[1] > YMAX:
        print("YMAX Conditiion met")
        changeInVel = (changeInVel[0], -1)

    return changeInVel







root = Tk()

WIDTH = 1000
HEIGHT = 1000

canvas = Canvas(root, height=1000, width=1000)

boids = []
# Create 10 boids with random velocities at random locations
for i in range(10):
    boids.append(Boid((random.randint(1,500), random.randint(1,500)), (1,1), i, canvas))


canvas.pack()
moveBoids()
root.mainloop()
