import tkinter as tk
from boid import *
import random
import cmath, math

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
# Function that moves the boids based on their velocity: Runs once then repeats every 25ms
def moveBoids():
    # Update boid position based on rules
    updateBoidPositions()
    for boid in boids:
        # Move on screen
        canvas.move(boid.shape, boid.velocity[0], boid.velocity[1])
    # Run this function again
    root.after(25,moveBoids)

def updateBoidPositions():
    for boid in boids:
        v1 = rule1(boid)
        v2 = rule2(boid)
        v3 = rule3(boid)
        v4 = edgeRule(boid)

        # Apply new changes to boids velocity
        boid.velocity = (boid.velocity[0] + v1[0] + v2[0] + v3[0] + v4[0], boid.velocity[1] + v1[1] + v2[1] + v3[1] + v4[1])

# Temp return values for these right now

# Rule 1: Boids try to fly towards the center of mass of neighbouring boids
def rule1(b):
    changeInVel = (0,0)
    for boid in boids:
        if boid is not b:
            changeInVel = (changeInVel[0] + boid.position[0], changeInVel[1] + boid.position[1])
    changeInVel = (changeInVel[0] / len(boids) - 1, changeInVel[1] / len(boids) - 1)
    # Making the change smaller: Dividing it by 100 makes it move 1% of the way towards center
    return ( (changeInVel[0] - b.position[0]) / 100 , (changeInVel[0] - b.position[0]) / 100 )

# Rule 2: Boids keep a small distance between them and other boids
def rule2(b):
    return (0.25, 0.25)

def rule3(b):
    return (0.25,0.25)

def edgeRule(b):
    return (0.25,0.25)





root = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(root, height=500, width=500)

boids = []
# Create 10 boids with random velocities at random locations
for i in range(10):
    boids.append(Boid((random.randint(1,500), random.randint(1,500)),(random.randint(-4,4),random.randint(-4,4)), i, canvas))


canvas.pack()
moveBoids()
root.mainloop()
