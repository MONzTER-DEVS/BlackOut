import pygame
from pygame.math import Vector2 as vec

color = pygame.Color

import math, os, sys, random

GRAVITY = 0.5

def raise_user_error(msg):
    print(f"USER ERROR: {msg}")

def raise_user_warning(msg):
    print(f"USER warning: {msg}")
