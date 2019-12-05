# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:18:29 2019

@author: Nicolas
"""

from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('X, Y, triangle, nbCote, nbCoteEgaux, angle_droit, triangleRectangle, triangleIsocele, triangleEquilateral')

triangle(X) <= nbCote(X,Y) & (Y==3)
triangleRectangle(X) <= triangle(X) & angle_droit(X)
triangleIsocele(X) <= triangle(X) & nbCoteEgaux(X, Y) & (Y==2)
triangleEquilateral(X) <= triangle(X) & nbCoteEgaux(X, Y) & (Y==3)

'''+triangle(polygone_1, polygone_2, polygone_3)
'''
+nbCote("polygone_1", 3)
+angle_droit("polygone_1")

+nbCote("polygone_2", 3)
+nbCoteEgaux("polygone_2", 2)

+nbCote("polygone_3", 3)
+nbCoteEgaux("polygone_3", 3)

print(pyDatalog.ask('triangleRectangle(X)'))
print(pyDatalog.ask('triangleIsocele(X)'))
print(pyDatalog.ask('triangleEquilateral(X)'))