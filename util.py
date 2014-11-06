# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as pp



"""
In this example the center of the ellipse is always the origin
"""
def isOnEllipse(a,b, x):
	checkDimension(x,2);

	if ( (x[0]/a)**2 + (x[1]/b)**2 == 1):
		return True;
	else:
		return False;

"""
Checks if the given point x is in the interior or the boundary of the ellipse 
"""
def isInEllipse(a,b,x):
	checkDimension(x,2);

	if ( (x[0]/a)**2 + (x[1]/b)**2 <= 1):
		return True;
	else :
		return False;


def checkDimension(x,expectedDim):
	if (np.size(x) != expectedDim):
                raise Error('The dimension should be: '+ str(expectedDim));


def plotEllipse(a,b):
	
	h = 0.01*(a+b)/2;
	x = -a;
 	y = -b;
	res = np.zeros((2,0));
	while (x <= a):
		y = -b;
		while (y <= b):
			if isInEllipse(a,b, [x,y]):
				res = np.append(res, [[x],[y]],1);
			y+= h;
		x += h;	

	fig = pp.figure();
	im = fig.add_subplot(111);
	im.plot(res[0,:], res[1,:], '+');
	fig.show();
