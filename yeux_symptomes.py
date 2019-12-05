# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:51:33 2019

@author: Nicolas
"""

from pyDatalog import pyDatalog

pyDatalog.clear()
pyDatalog.create_terms('X, G001, G002, G003, G004, G005, G006, G007, G008, G009, G010, G011, G012, G013, G014, G015, G016, G017, G018, G019, G020, G021, G022, G023, P01, P02, P03, P04, P05, P06, P07, P08')


'''
P0X : Maladies
G0XX : Symptômes
'''

P01(X) <= G001(X) & G002(X) & G003(X) & G004(X)
P02(X) <= G001(X) & G002(X) & G005(X) & G006(X)
P03(X) <= G007(X) & G008(X)
P04(X) <= G009(X) & G010(X) & G011(X) & G012(X)
P05(X) <= G013(X) & G014(X) & G015(X) & G016(X)
P06(X) <= G010(X) & G015(X) & G016(X) & G017(X) & G018(X) & G019(X)
P07(X) <= G010(X) & G019(X) & G020(X) & G021(X)
P08(X) <= G001(X) & G010(X) & G019(X) & G022(X) & G023(X)


+G001('default')
+G002('default')
+G003('default')
+G004('default')
+G005('default')
+G006('default')
+G007('default')
+G008('default')
+G009('default')
+G010('default')
+G011('default')
+G012('default')
+G013('default')
+G014('default')
+G015('default')
+G016('default')
+G017('default')
+G018('default')
+G019('default')
+G020('default')
+G021('default')
+G022('default')
+G023('default')


+G013('Personne1')
+G014('Personne1')
+G015('Personne1')
+G016('Personne1')

+G010('Personne2')
+G015('Personne2')
+G016('Personne2')
+G017('Personne2')
+G018('Personne2')
+G019('Personne2')

'''
Qui a la maladie de "Conjonctiviste en allergie ?
'''
print(pyDatalog.ask('P05(X)'))

'''
Qui a la maladie de la Blépharite ?
'''
print(pyDatalog.ask('P01(X)'))

'''
Quel patient souffre du symptôme "Yeux qui brillent ?"
'''
print(pyDatalog.ask('G016(X)'))

