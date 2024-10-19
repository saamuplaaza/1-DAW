p1 = float(input("Introduce la nota de la práctica 1: "))
p2 = float(input("Introduce la nota de la práctica 2: "))
p3 = float(input("Introduce la nota de la práctica 3: "))
ep = float(input("Introduce la nota del examen parcial: "))
ef = float(input("Introduce la nota del examen final: "))
pp = (p1+p2+p3)/3
prom = (pp+2*ep+3*ef)/6
prom= prom.__round__(2)
print(prom)
