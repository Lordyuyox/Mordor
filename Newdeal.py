#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Lordyuyox

# Graficador de datos del Survey SHINING

import csv 
import numpy as np
import matplotlib.pyplot as plt

#Functions

# Para esta primera tabla ('resolvedmaps_fluxes-Table6_MRF.csv') lo separare en las columnas que se cuales son, sin embargo
# para las proximas podría hacerlo con un algoritmo, con la finalidad de no tener que estar haciendo un codigo para cada tabla.
# Por lo que a priori, este codigo me servira para la interpretacion de los datos actuales.

#Name, NIII57, NIII57err, OI63, OI63err, OIII88, OIIIerr, NII122, NII122err, OI145, OI145err, CIII158, CII158err, S63, S63err, S122, S122err = np.loadtxt('resolvedmaps_fluxes-Table6_MRF.txt', dtype= 'str, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float', delimiter=',', usecols=None, unpack=True)
Name, NIII57, NIII57err, OI63, OI63err, OIII88, OIIIerr, NII122, NII122err, OI145, OI145err, CIII158, CII158err, S63, S63err, S122, S122err = np.loadtxt('resolvedmaps_fluxes-Table6_MRF.txt', dtype= 'str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str', comments=';', delimiter=',', usecols=None, unpack=False)
#data = np.loadtxt('resolvedmaps_fluxes-Table6_MRF.txt', dtype= 'str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str', delimiter=',', usecols=None)
#data = np.loadtxt('resolvedmaps_fluxes-Table6_MRF.txt', dtype= 'str, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float, float', delimiter=',', unpack=True)


print(Name)