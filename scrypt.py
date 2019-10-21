#!/usr/bin/env python3

import random;

noms = ['Arthur', 'Bernard', 'Alexis', 'Jason']
surnoms = ['La Vermine', 'L\'Ours', 'L\'Araignée', 'Le Crustacé', 'La belette']

rdmNoms = int(random.random()*len(noms) -1)
rdmSurnoms = int(random.random()*len(surnoms) -1)

print("Resultat: " + noms[rdmNoms] + " " + surnoms[rdmSurnoms])