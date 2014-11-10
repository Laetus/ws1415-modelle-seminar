# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pp


""" Allgemeiner Plan

Darstellung von Vektoren immer als v =  np.array([x,y]) oder np.array([x,y,z]) im dreidimensionalen. Denn Operationen mit v sind dann besser lesbar. Dies verbessert die Lesbarkeit denn v * 2  ist dann z.B. np.array([2x , 2y]) und nicht (x , y, x,y )

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

"""
s ist Vektor, steigung ist zahl
"""
def neuerPunkt(s, steigung):
	global a
	global b	
	steigung = steigung *1.0
	'Berechne t'
	t = s[1] - steigung * s[0]
	print(t)

	'Berechne x'
	"sol1 = solveMitternacht((-b/a) - steigung**2, -2 * steigung * t, b- t**2)"
	sol = solveMitternacht((1/a**2)+ (steigung**2/ b**2), 2 * steigung * t/(b**2) , ((t/b)**2) - 1 )

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
Löst die Mitternachtsformel
"""
def solveMitternacht(a,b,c):
	
	a = a * 1.0
	b = b * 1.0
	c = c * 1.0

	square = b**2 - (4 * a *c)
	if square < 0 : 
		raise Error("Wurzel ist negativ, es gibt keine reele Lösung")

	if square == 0 :
		print("Es gibt nur eine Lösung!")

	x1 =  (-b + np.sqrt(square))/(2 * a)
	x2 =  (-b - np.sqrt(square))/(2 * a)
	return (x1 , x2)


"""
Berechne die normierte Normale der Gerade
"""
def berechneNormale(x):
	global a
	global b
	normale = np.array( [x[0]/(a**2)] , [x[1]/(b**2)] )	
	return normale / np.linalg.norm(normale)	


"""
Berechne die neue Steigung am Punkt x, sodass Einfallswinkel = Ausfallswinkel ist
"""
def berechneNeueSteigung(x, m_alt):
	'Berechne Normale am Punkt x'
	normale = berechneNormale(x)
	
	'Berechne Einfallswinkel d.h. Winkel zwischen Normale und Geraden'
	gerade_alt = np.array([1 , m_alt])
	'Normieren'
	gerade_alt = gerade_alt / np.linalg.norm(gerade_alt)

	winkel = np.arccos( np.dot(gerade_alt , normale))

	gerade_neu

	'Drehsinn herausfinden'
	if (drehMatrix2D(winkel) * gerade_alt == normale) :
		gerade_neu = drehMatrix2D(2*winkel) * gerade_alt
	elif (drehMatrix2D(-winkel) * gerade_alt == normale) : 
		gerade_neu = drehMatrix2D(-2*winkel) * gerade_alt
	else :
		raise Error('Alte Gerade konnte nicht auf Normale gedreht werden')
	
	'Steigung ist x[1], wenn x[0]== 1'
	if (gerade_neu[0] != 0) :	
		gerade_neu = gerade_neu / gerade_neu[0]
	else :
		raise Errror('Neue Steigung ist unendlich')
	
	return gerade_neu[1]
	 

def drehMatrix2D(winkel):
	sin = np.sin(winkel)
	cos = np.cos(winkel)
	return np.array( ((cos, -sin) , (sin , cos)) )
	


	


