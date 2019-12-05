# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:27:05 2019

@author: Nicolas
"""

from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('X, fritz, croakes, eatsFlies, frog, chirps, sings, canary, green, yellow')

frog(X) <= croakes(X) & eatsFlies(X)
canary(X) <= chirps(X) & sings(X)
green(X) <= frog(X)
yellow(X) <= canary(X)

pyDatalog.assert_fact('croakes','fritz')
pyDatalog.assert_fact('eatsFlies','fritz')

print(pyDatalog.ask('green(X)'))
print(pyDatalog.ask('green(fritz)'))
print(pyDatalog.ask('green(orange)'))