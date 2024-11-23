from graphics import *
from random import *

def GateKeyPers():
    keys = ["Square", "Circle", "Triangle", "Hexagon", "Diamond"]
    doors = []
    for i in range(3):
        gate = {
                "locked": True,
            "key" : ""
        }
        while gate.key == "":
            k = keys[randrange(0, 5)]
            taken = False
            for j in range(i):
                if doors[j].key == k:
                    taken = True
            if not taken:
                gate.key = k
        doors.append(gate)
    