﻿ws1415-modelle-seminar
======================


Projekt Visualisierung Delaunay Flächen
filename = "C:/Users/..."
exec(compile(open(filename).read(), filename, 'exec'))

Gute Werte bei a = 1.5 b =1 & a = 1.25 b=1


x = (1.5,0) d=  (1, 0.700700700701) 
x = (1.5,0) d=  (1, 4.1414141414) <- aktuell das beste

x = (1.5,0) d=(1.5, 0.2)
x = (1.5,0) d = (1, 0.5005005005)

path = '/home/laetus/Desktop/Seminar/ws1415-modelle-seminar/'
plo = path + 'plot.py'
ut = path + 'util.py'
anim = path + 'animation.py'

exec(compile(open(ut).read(), ut, 'exec')) , exec(compile(open(plo).read(), plo, 'exec')) , exec(compile(open(anim).read(), anim, 'exec'))

#Zum  Ausführen der Billiard Animation

anBi = path + "animBilliard.py"
exec(compile(open(anBi).read(), anBi, 'exec'))

#Zum Ausführen der Ausrollen Animation
anAu = path + "animAusrollen.py"
exec(compile(open(anAu).read(), anAu, 'exec'))


