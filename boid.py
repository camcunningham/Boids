from tkinter import *
from random import randint
import math

class Boid:
    # A boid has a position, velocity, and unique identifier
    def __init__(self, position, velocity, identifier, canvas):
        self.position = position
        self.velocity = velocity
        self.id = identifier

        self.shape = canvas.create_oval(position[0], position[1], position[0] + 25, position[1]+25, fill="blue", outline="black")

    # Function that updates the velocity of a boid
    def addVelocity(self, vel):
        self.velocity = (self.velocity[0] + vel[0], self.velocity[1] + vel[1])

    # Function that applied movement from velocity to the position of the boid
    def move(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
