# This is where the code will run, we will define the rules, animations, window, etc.
# here.
from p5 import setup, draw, size, background, run
import numpy as np
from boid import Boid

width = 1000
height = 1000

def setup():
    # Runs once at the start
    size(width,height)

def draw():
    # Runs every frame
    background(30,30,47)

run()
