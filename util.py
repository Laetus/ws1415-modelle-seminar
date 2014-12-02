# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib.pyplot as pp


""" Allgemeiner Plan

Darstellung von Vektoren immer als v =  np.array([x,y]) oder np.array([x,y,z]) im dreidimensionalen. Denn Operationen mit v sind dann besser lesbar. Dies verbessert die Lesbarkeit denn v * 2  ist dann z.B. np.array((2x , 2y)) und nicht (x , y, x,y )

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


def startBilliard(x0, d0):
    x0 = x0 * 1.0
    d0 = d0 * 1.0
    startpunkt = x0

    listX = [x0]  
    listD = [d0]

    for x in range (0, maxIterationen) :
        'Berechne neuen Punkt'
        x_neu = neuerPunktV(x0,d0)
        'Berechne neue Richtung'
        d_neu = berechneNeueRichtung(x_neu, d0)

        if(np.linalg.norm(startpunkt - x_neu) < eps):
            break

        'Schreibe neune Punkte und Richtungen weg'
        listX.append(x_neu)
        listD.append(d_neu)
        
        'Bereite neue Iteration vor'
        x0 = x_neu
        d0 = d_neu
         
    print("Billiard fertig!", x+1) 
    #return (listX, listD)
    listX.sort(key=berechneEllipsenWinkel)
    #listX = sorted(listX, vergleichsFunktion)
    return listX
"""
Parameter der Ellipse
"""

global maxIterationen
maxIterationen = 25

global a 
a = 2.0

global b
b = 1.0

global f
f = np.array((np.sqrt(a**2-b**2),0))

global eps
eps = 0.0000001
"""
In this example the center of the ellipse is always the origin
"""
def isOnEllipse(x):
    checkDimension(x,2);
    if ( np.abs((x[0]/a)**2 + (x[1]/b)**2 -1) < eps ):
        return True;
    else:
        return False;

"""
Checks if the given point x is in the interior or the boundary of the ellipse 
"""
def isInEllipse(x):
    checkDimension(x,2)

    if ( (x[0]/a)**2 + (x[1]/b)**2 <= 1):
        return True;
    else :
        return False;


def checkDimension(x,expectedDim):
    if (np.size(x) != expectedDim):
       raise Error('The dimension should be: '+ str(expectedDim));


def plotEllipse():
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
alt ist der alte Punkt, d ist Richtungsvektor
"""
def neuerPunktV(alt, d):
    d = d * 1.0
    
    sol = solveMitternacht((d[0] / a)**2 + (d[1]/b)**2 , 2 * ( ((d[0] * alt[0]) / a**2 )+((d[1] * alt[1]) / b**2 )) , (alt[0]/a)**2 + (alt[1]/b)**2 -1 )
    
    if (np.abs(sol[0]) < eps):
        if(np.abs(sol[1]) < eps):
            raise Error("Es gibt nur eine Lösung!")
        else:
            neu = alt + (sol[1] * d)
    elif (np.abs(sol[1]) < eps):
        neu = alt + (sol[0] * d)
    else:
        raise Error("Alter Punkt falsch!")
    return neu

"""
Löst die Mitternachtsformel
"""
def solveMitternacht(a,b,c):
    
    a = a * 1.0
    b = b * 1.0
    c = c * 1.0

    square = b**2 - (4 * a *c)
    if square < 0 : 
        raise Error("Wurzel ist negativ, es gibt keine reelle Lösung")

    if square == 0 :
        print("Es gibt nur eine Lösung!")

    x1 =  (-b + np.sqrt(square))/(2 * a)
    x2 =  (-b - np.sqrt(square))/(2 * a)
    return (x1 , x2)


"""
Berechne die normierte Normale der Gerade
"""
def berechneNormale(x):
    normale = np.array((x[0]/(a**2), x[1]/(b**2)))

    'Normieren' 
    return normale / np.linalg.norm(normale)    



"""
Berechnet die neue Richtung d_neu am Ellipsenpunkt x, sodass der Winkel zwischen d_alt und normale = Winkel zwischen d_neu und normale ist.
"""
def berechneNeueRichtung(x, d_alt) :
    'Berechne Normale am Punkt x'
    normale = berechneNormale(x) #normiert

    'Normieren'
    d_alt = d_alt / np.linalg.norm(d_alt)

    cosphi = np.dot(d_alt, normale)
    winkel = np.arccos( cosphi )

    'Drehsinn herausfinden'
    if np.linalg.norm(np.dot(drehMatrix2D(winkel) , d_alt) - normale) < eps :
        d_neu = np.dot(drehMatrix2D(2*winkel), d_alt)
    elif np.linalg.norm(np.dot(drehMatrix2D(-winkel) , d_alt) - normale) < eps : 
        d_neu = np.dot(drehMatrix2D(-2*winkel), d_alt)
    else :
        raise Error("Drehung schlug fehl")
    

    'Ergebnis konvertieren'
    d_neu = np.array((d_neu[0,0] ,d_neu[0,1]))
    return d_neu / np.linalg.norm(d_neu)


def drehMatrix2D(winkel):
    sin = np.sin(winkel)
    cos = np.cos(winkel)
    return np.matrix(((cos, -sin), (sin, cos)))

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
def vergleichsFunktion(p1, p2) :
    alpha = berechneEllipsenWinkel(p1)
    beta = berechneEllipsenWinkel(p2)
    return alpha - beta


def berechneEllipsenWinkel(p):
    alpha = np.arccos( np.abs( p[0] /a))
    if  (p[0] >= 0) & (p[1] >= 0) :
        return alpha
    elif (p[0] <= 0) & (p[1] >= 0 ):
        return np.pi - alpha
    elif (p[0] <= 0 ) & (p[1] <= 0) :
        return np.pi + alpha
    elif (p[0] >= 0) & (p[1] <= 0) :
        return 2 * np.pi - alpha
    
    
def berechneWinkel(p0, p1):
    p0p1 = np.linalg.norm(p0 - p1)
    p0f = np.linalg.norm(p0 - f)
    p1f = np.linalg.norm(p1 - f)
    w0 = np.arccos((p0f**2+p0p1**2-p1f**2)/(2*p0p1*p0f))
    w1 = np.arccos((p1f**2+p0p1**2-p0f**2)/(2*p0p1*p1f))
    return np.array((p0p1, w0, w1))

def spitzPunkt(aww, pos): #aww: von berechenWinkel (Abstand, Winkel1, Winkel2), pos: Position auf x-Achse
    m0 = np.array((np.cos(aww[1]), np.sin(aww[1])))
    m1 = np.array((-np.cos(aww[2]), np.sin(aww[2])))
    lam = (1/(m0[1]-((m0[0]/m1[0]*m1[1]))))*(-aww[0]/m1[0]*m1[1])   
    return pos+(lam*m0)
    #p1 = pos +(aww[0]*np.array((1,0)))
    #mu = (m1[0]-(m1[1]*m0[0]/m0[1]))/(pos[0]-p1[0])
    #x1 = p1[0]+(mu*m1[0])
    #x2 = mu*m1[1]
    #return np.array((x1, x2))
    
def ausrollen(listX):
    pos = np.array((0,0))
    listP = []
    listP.append(pos)
    #print(listP)
    for i in range(len(listX) - 2):
        aww = berechneWinkel( listX[i], listX[i+1] )
        punkt = spitzPunkt(aww, pos)
        #print(punkt)
        pos = pos + aww[0] * np.array((1,0))
        #np.append(listP, [punkt], axis=0)
        listP.append(punkt) 
    return listP     
        
def ellipsenPunkte(N,zWert):
    res = []
    for x in range (0,N+1):
        phi = x * 2 * np.pi / (N+1)
        p = np.array((a * np.cos(phi)  , b * np.sin(phi), zWert ))
        res.append(p);
    
    return res

              
