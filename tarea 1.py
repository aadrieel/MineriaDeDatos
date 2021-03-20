# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 01:39:34 2021

@author: adrielmac
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df =pd.read_csv('C:/Users/adrie/Documents/FCFM/Enero Junio 2021/Minería de Datos/nbasalaries.csv')

df['2020/21'] = df['2020/21'].str.replace('$', '', ).str.replace(',', '').astype(int)
df['2021/22'] = df['2021/22'].str.replace('$', '', ).str.replace(',', '').astype(int)
df['2022/23'] = df['2022/23'].str.replace('$', '', ).str.replace(',', '').astype(int)
df['2023/24'] = df['2023/24'].str.replace('$', '', ).str.replace(',', '').astype(int)
df.rename(columns = {'Rank':'RANK', 'Team':'TEAM'}, inplace = True)

df.head()
print(df.shape)
print(df.columns)
print(df.info())
print(df)

print("Dato Mínimo 20/21: ", + df["2020/21"].min())
print("Dato Mínimo 21/22: ", + df["2021/22"].min())
print("Dato Mínimo 22/23: ", + df["2022/23"].min())
print("Dato Mínimo 23/24: ", + df["2023/24"].min())

print("Dato Máximo 20/21: ", + df["2020/21"].max())
print("Dato Máximo 21/22: ", + df["2021/22"].max())
print("Dato Máximo 22/23: ", + df["2022/23"].max())
print("Dato Máximo 23/24: ", + df["2023/24"].max())

print("Media Aritmética 20/21: ", + round(df["2020/21"].mean(), 2))
print("Media Aritmética 21/22: ", + round(df["2021/22"].mean(), 2))
print("Media Aritmética 22/23: ", + round(df["2022/23"].mean(), 2))
print("Media Aritmética 23/24: ", + round(df["2023/24"].mean(), 2))

print("Desviación Estándar 20/21: ", + round(df["2020/21"].std(), 2))
print("Desviación Estándar 21/22: ", + round(df["2021/22"].std(), 2))
print("Desviación Estándar 22/23: ", + round(df["2022/23"].std(), 2))
print("Desviación Estándar 23/24: ", + round(df["2023/24"].std(), 2))

print("Número de Datos: ", + df["RANK"].count())

x = df['TEAM']
y = df['2020/21']

plt.plot(x, y, color = "black")
plt.title("Salario Por Equipo Temporada 2020/21")
plt.xlabel("Equipo")
plt.ylabel("Salario")

plt.xticks(rotation = "90")

plt.close()

m1 = round(df["2020/21"].mean(), 2)
m2 = round(df["2021/22"].mean(), 2)
m3 = round(df["2022/23"].mean(), 2)
m4 = round(df["2023/24"].mean(), 2)

prom = [m1, m2, m3, m4]
temp = ["20/21"] + ["21/22"] + ["22/23"] + ["23/24"]

medias = pd.DataFrame({"Temporada":temp, "Salario Promedio":prom})

x1 = medias["Temporada"]
y1 = medias["Salario Promedio"]

plot1 = plt.bar(x1, y1, color = "black", ecolor = "white")

plt.title("Salario Promedio Por Temporada")
plt.xlabel("Temporada")
plt.ylabel("Salario Promedio")

plt.xticks(rotation = "90")


std1 = df["2020/21"].std()
sal = df.pop("2020/21")
team = df.pop("TEAM")
n = df["RANK"].count()
med = (n + 1)/2
print(med)

print("Asimetría/Sesgo 20-21: ", + round((3 * (m1 - med)/std1), 2), "%")

