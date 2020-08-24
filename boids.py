import tkinter as tk
from boid import *
import random
import cmath, math
from utility import *
import numpy as np

# Global setting variables
MAX_SPEED = 5
DRIFT = 0.5
PERCEPTION = 70
MAX_FORCE = 0.05
SIZE = 800

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

# Updates each boids velocity based on the rules
def updateBoidVelocities():
    # Run through each boid and apply the 4 modifiers
    for boid in boids:
        v1 = rule1(boid)
        v2 = rule2(boid)
        v3 = rule3(boid)
        v4 = rule4(boid)
        boid.velocity = tadd(boid.velocity, v1)
        boid.velocity = tadd(boid.velocity, v2)
        boid.velocity = tadd(boid.velocity, v3)
        boid.velocity = tadd(boid.velocity, v4)

        # Ensuring that speed does not go over MAX_SPEED, if it does, reduce speed by 10%
        if math.hypot(boid.velocity[0], boid.velocity[1]) > MAX_SPEED:
            boid.velocity = tmul(boid.velocity, 0.9)

# Cohesion
def rule1(b):
    # Vector that will be added to b's velocity
    steering = (0,0)
    # Total number of boids that impact this one based on perception value
    total = 0
    # Vector that holds center of mass that this boid will fly toward
    centerOfMass = (0,0)
    # Run through each boid
    for boid in boids:
        # Store the subtraction of the boid - this boid
        temp = tsub(boid.position, b.position)
        # If the normalized vector holding the distance between this boid and the one in the loop is less than
        # the perception value, it impacts us, add it to center mass and increase total
        if np.linalg.norm([temp[0], temp[1]]) < PERCEPTION:
            # Add to center of mass
            centerOfMass = tadd(centerOfMass, boid.position)
            # Increase total
            total += 1
    # If total > 0 then at least one other boid impacted this one, need to make a change
    if total > 0:
        # To get the average center of mass, divide the aggregate by total
        centerOfMass = tdiv(centerOfMass, total)
        # Vector to be compared
        vecToCompare = tsub(centerOfMass, b.position)
        # If the normalized vector is greater than 0
        if np.linalg.norm([vecToCompare[0], vecToCompare[1]]) > 0:
            # Scale it to be MAX_SPEED
            vecToCompare = tmul(tdiv(vecToCompare, np.linalg.norm([vecToCompare[0], vecToCompare[1]])), MAX_SPEED)
        # Apply changes to steering vector
        steering = tsub(vecToCompare, b.velocity)
        # If these changes apply more force than legal
        if np.linalg.norm([steering[0], steering[1]]) > MAX_FORCE:
            # Change that value to be the maximum: MAX_FORCE
            steering = tmul(tdiv(steering, np.linalg.norm([steering[0], steering[1]])), MAX_FORCE)
    return steering

# Separation
def rule2(b):
    # Vector that will be applied to b's velocity
    steering = (0,0)
    # For each boid
    for boid in boids:
        # If the boid is not itself
        if boid.id != b.id:
            # No need to check perception, we basically do that here
            # If the distance between b and the boid is less than 25, do not move any closer
            if abs(boid.position[0] - b.position[0]) < 25 and abs(boid.position[1] - b.position[1]) < 25:
                steering = tdiv(tsub(steering, (tsub(boid.position, b.position))), 5)
    return steering

# Alignment
def rule3(b):
    # Steering vector to be returned
    steering = (0,0)
    # Total boids that will affect this one based on perception range
    total = 0
    # Vector that will hold the average position of the perceptable boids
    average = (0,0)
    for boid in boids:
        # Store the subtraction of boid and b in temp variable
        temp = tsub(boid.position, b.position)
        # If the normalized position vector is in perception range, then if will affect us
        if np.linalg.norm([temp[0], temp[1]]) < PERCEPTION:
            # Add this vectors velocity to the average
            average = tadd(average, boid.velocity)
            # Increase total boids affecting b
            total += 1
        # If total > 0 then this boid was impacted by at least one other so we apply the change
        if total > 0:
            # Divite average by total to get the average velocity of the flock
            average = tdiv(average, total)
            # Normalize the average velocity so we can scale it to our MAX_SPEED
            average = tmul(tdiv(average, np.linalg.norm([average[0], average[1]])), MAX_SPEED)
            # To get the direction we want to steer in, subtract b's velocity from the average velocity, and
            # add that vector to b's velocity
            steering = tsub(average, b.velocity)
    return steering

# Soft boundary
def rule4(boid):
    sum = (0.0, 0.0)
    # Magnitude of velocity vector
    mag = math.hypot(boid.velocity[0], boid.velocity[1])
    # Check if the position of the boid is outside of legal bounds, if so add / subtract (based on limit being lowest or highest)
    # a velocity based on drift and magnitude
    if boid.position[0] < 0:
        sum = tadd(sum, (DRIFT * mag, 0.0))
    if boid.position[0] > SIZE:
        sum = tsub(sum, (DRIFT * mag, 0.0))
    if boid.position[1] < 0:
        sum = tadd(sum, (0.0, DRIFT * mag))
    if boid.position[1] > SIZE:
        sum = tsub(sum, (0.0, DRIFT * mag))
    return sum

root = Tk()
canvas = Canvas(root, height=800, width=800)
boids = []
# Create 15 boids with random velocities at random locations
for i in range(15):
    boids.append(Boid((random.randint(1,500), random.randint(1,500)), (random.randint(1,2),random.randint(-2,-1)), i, canvas))

canvas.pack()
moveBoids()
root.mainloop()
