# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:46:45 2019

@author: Nicolas
"""

from pyDatalog import pyDatalog

pyDatalog.clear()
symptom = 'shakiness, hunger, sweating, headach, diabetic_parents, pale, urination, thirst, blurred_vision, dry_mouth, smelling_breath, shortness_of_breath'
conditions = 'glycemie, concerned, not_concerned, hyperglycemic_risk, hypoglycemic_risk, has_signs_low_sugar, signs_low_sugar_symptom, has_signs_high_sugar, signs_high_sugar_symptom, has_diabetic_parents, diabetic_parents, high_risk_diabete, could_have_diabete, age'
pyDatalog.create_terms('X, Y, Z')
pyDatalog.create_terms(symptom, conditions)

not_concerned(X) <= age(X, Z) & (Z>5)
concerned(X) <= age(X, Z) & (Z<=5)
hyperglycemic_risk(X) <= concerned(X) & glycemie(X, Z) & (Z>10)
hypoglycemic_risk(X) <= concerned(X) & glycemie(X, Z) & (Z<4)
has_diabetic_parents(X) <= concerned(X) & diabetic_parents(X, Z) & (Z==1)

signs_low_sugar_symptom(X) <= shakiness(X) & hunger(X) & sweating(X) & headach(X) & pale(X)
signs_high_sugar_symptom(X) <= urination(X) & thirst(X) & blurred_vision(X) & headach(X) & dry_mouth(X) & smelling_breath(X) & shortness_of_breath(X)

has_signs_low_sugar(X) <= concerned(X) & signs_low_sugar_symptom(X)
has_signs_high_sugar(X) <= concerned(X) & signs_high_sugar_symptom(X)

high_risk_diabete(X) <= concerned(X) & (hypoglycemic_risk(X) & has_signs_low_sugar(X)) or (hyperglycemic_risk(X) & has_signs_high_sugar(X))
could_have_diabete(X) <= concerned(X) & has_diabetic_parents(X) & has_signs_high_sugar(X)




+shakiness('default')
+hunger('default')
+sweating('default')
+headach('default')
+pale('default')
+urination('default')
+thirst('default')
+blurred_vision('default')
+dry_mouth('default')
+smelling_breath('default')
+shortness_of_breath('default')


+age('kid1', 10)


+age('kid2', 3)
+glycemie('kid2', 2)
'''Problème je n'arrive pas à valider la condition si plus de deux symptomes sont vérifiés, je les mets alors tous pour valider la condition'''
+shakiness('kid2')
+hunger('kid2')
+sweating('kid2')
+headach('kid2')
+pale('kid2')



print(pyDatalog.ask('not_concerned(X)'))
print(pyDatalog.ask('has_signs_low_sugar(X)'))
print(pyDatalog.ask('high_risk_diabete(X)'))

'''
Je n'arrive pas à valider la condition s'il y a plus de deux symptomes (shakiness, hunger, etc..)
'''

