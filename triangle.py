# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:18:29 2019

@author: Johann
"""

from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('X, triangle, cote_egaux_2, cote_egaux_3, angle_droit, rectangle, isocele, equilateral, quelquonque')

rectangle(X) <= triangle(X) & angle_droit(X)
isocele(X) <= triangle(X) & cote_egaux_2(X)
equilateral(X) <= triangle(X) & cote_egaux_3(X)

'''+triangle(polygone_1, polygone_2, polygone_3)
'''
+triangle(polygone_1)
+angle_droit(polygone_1)

+triangle(polygone_2)
+cote_egaux_2(polygone_2)

+triangle(polygone_3)
+cote_egaux_3(polygone_3)

print(pyDatalog.ask('rectangle(X)'))
print(pyDatalog.ask('isocele(X)'))
print(pyDatalog.ask('equilateral(X)'))