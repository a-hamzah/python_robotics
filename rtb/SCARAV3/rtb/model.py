import roboticstoolbox as rtb
import math
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3

#! Creating model

# Link lengths in mm

a1 = float(input("a1: "))
a2 = float(input("a2: "))
a3 = float(input("a3: "))
a4 = float(input("a4: "))

# Converting from mm to m


def milimeters_to_meters(input):
    output = input/1000
    return output


a1 = milimeters_to_meters(a1)
a2 = milimeters_to_meters(a2)
a3 = milimeters_to_meters(a3)
a4 = milimeters_to_meters(a4)

# TODO: Watch the video and add next
