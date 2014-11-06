# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pp

"""
Parameter der Ellipse
"""

global a 
a = 2.0

global b
b = 1.0
"""
In this example the center of the ellipse is always the origin
"""
def isOnEllipse(x):
	checkDimension(x,2);
	global a
	global b
	if ( (x[0]/a)**2 + (x[1]/b)**2 == 1):
		return True;
	else:
		return False;

"""
Checks if the given point x is in the interior or the boundary of the ellipse 
"""
def isInEllipse(x):
	global a
	global b	
	checkDimension(x,2)

	if ( (x[0]/a)**2 + (x[1]/b)**2 <= 1):
		return True;
	else :
		return False;


def checkDimension(x,expectedDim):
	if (np.size(x) != expectedDim):
                raise Error('The dimension should be: '+ str(expectedDim));


def plotEllipse():
	global a
	global b
	h = 0.01*(a+b)/2;
	x = -a;
 	y = -b;
	res = np.zeros((2,0));
	while (x <= a):
		y = -b;
		while (y <= b):
			if isInEllipse([x,y]):
				res = np.append(res, [[x],[y]],1);
			y+= h;
		x += h;	

	fig = pp.figure();
	im = fig.add_subplot(111);
	im.plot(res[0,:], res[1,:], '+');
	fig.show();

""" Allgemeiner Plan
if(isOnEllipse(a, b, s)):
	def Billiard(s, steigung, a,b):
		s_new = neuerPunktBerechnen(s, steigung)
		normale = normaleBerechnen(s_new)
		steigung = sberechnen(normale, steigung)
	for():
	=> Array mit Punkten
Array sortieren (über winkel)
neues Arry mit winkeln 
benachbarte punkte bleiben benachbart a b y ( immer a neben b)
... siehe blatt
"""

"""
s ist Vektor, steigung ist zahl
"""
def neuerPunkt(s, steigung):
	global a
	global b	
	'Berechne t'
	t = s[1] - steigung * s[0]
	print(t)
	'Berechne x'
	sol1 = solveMitternacht((-b/a) - steigung**2, -2 * steigung * t, b- t**2)
	sol = solveMitternacht((1/a**2)+ (steigung**2/ b**2), 2 * steigung * t/(b**2) , ((t/b)**2) - 1 )

	sol = sol1
	if (s[0] == sol[0]):
		if (s[0] == sol[1]):
			raise Error("Beide Lösungen fallen zusammen")
		else :
			x_neu = sol[1]
	else :
		x_neu = sol[0]
	
	'Berechne y'
	
	y_neu = (steigung * x_neu) + t

	return (x_neu, y_neu)

"""
Löst die Mitternachtsformel korrekt
"""
def solveMitternacht(a,b,c):
	print(a,b,c)
	x1 =  (-b + np.sqrt(b**2 - (4 * a *c)))/(2 * a)
	x2 =  (-b - np.sqrt(b**2 - (4 * a *c)))/(2 * a)
	return (x1 , x2)
	
