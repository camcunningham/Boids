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
# Function that moves the boids based on their velocity
def moveBoids():
    for boid in boids:
        canvas.move(boid.shape, boid.velocity[0], boid.velocity[1])

    root.after(25,moveBoids)

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
