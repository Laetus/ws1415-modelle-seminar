import bpy
import math
import util
import numpy as np
import plot

    
def zeichneRotTranslation(listX, rotZentrum, winkel,richtung):
    punkte = []
    kanten = []
    i = 0
    winkel = -winkel
       
    anzPunkte = len(listX)
    for element in listX :
        #Anwenden der Transformation
        element = rotationUmPunkt(element, rotZentrum, winkel)
        element = element + richtung
        if element.size == 2 : 
            punkte.append( (element[0] , element[1] , 0) )
            kanten.append( (i, (i+1) % anzPunkte) )
            i += 1
        else :
            raise Error("Die Punkte haben die falsche Dimension!")
    
    for i in range(len(punkte)):
        kanten.append( (len(punkte), i) )
        
        
    
    
    focus = rotationUmPunkt(getPositiveFocusPoint(), rotZentrum, winkel) + richtung
    
    punkte.append( (focus[0], focus[1], 0 ))
    
    zeichneMesh('bmf', punkte, kanten, () )
    

def animiereAusrollen(listX, listA):
    listP = listA[0]
    listPos = listA[1]
    listAWW = listA[2]
    
       
    for i in range(len(listX)):
        phi = doStepI(i,listX,listPos)
        print(phi)
        
        
def getPhi(k,l):
    k = k / np.linalg.norm(k)
    l = l / np.linalg.norm(l)
    
    phi = np.arccos(np.dot(k,l))
    print(phi)
    if (np.sign(l[0]) <= 0 ): 
        if (np.sign(l[1]) >= 0 ) :
            return phi
        else :
            return 2*np.pi -  phi
    else :
        if (np.sign(l[1]) <= 0 ):
            return 2*np.pi  - phi   
        else :
            return 2 * np.pi + phi
    

def doStepI(i , listX, listPos):
    print(i)
    
    phi = getPhi(np.array((1,0)) , listX[(i+1) % len(listX) ] - listX[i])
    
    zeichneRotTranslation(listX, listX[i], phi, listPos[i] - listX[i]  )
    
    
    return phi