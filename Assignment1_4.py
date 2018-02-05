# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 20:33:51 2018

@author: krishna.i
 
Assignment 1.4: Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r3

"""

Sphere_diameter = int(input("Enter Diameter of the Sphere to find Volume: "))

Sphere_radius = Sphere_diameter / 2  # Calculating the radius value

Sphere_volume = (4/3) * (3.1416) * (Sphere_radius**3) # Calculation as per Volume of Sphere formula

print("Volume of the Sphere with the given diameter is: ", Sphere_volume) # printing of output - Sphere volume value

# End of the code