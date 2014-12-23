import bpy
import math
import util
import numpy as np
import plot
import time
import random

    
def zeichneRotTranslation(listX, rotZentrum, winkel,richtung):
    punkte = []
    kanten = []
    flaechen = []
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
            flaechen.append( ( i, (i+1) % anzPunkte , anzPunkte) )
            i += 1
        else :
            raise Error("Die Punkte haben die falsche Dimension!")
    
    for i in range(len(punkte)):
        kanten.append( (len(punkte), i) )
        
        
    
    
    focus = rotationUmPunkt(getPositiveFocusPoint(), rotZentrum, winkel) + richtung
    
    punkte.append( (focus[0], focus[1], 0 ))
    
    
    name = str(random.randint(0,1000000))
    #entferneMesh(name)
    zeichneMesh(name, punkte, kanten, flaechen )
    bpy.data.objects[name].modifiers.new('Wireframe', type='WIREFRAME')
    bpy.ops.object.convert(target='MESH', keep_original=False)


def animiereAusrollen(listX, listA):
    listP = listA[0]
    listPos = listA[1]
    listAWW = listA[2]
    
    phi_alt = 0
    for i in range(len(listX)):
        phi_alt = doStepI(i,listX,listPos, phi_alt)
        #delay anlegen
        #time.sleep(2)
        

def doStepI(i , listX, listPos, phi_alt):
    l = len(listX)
    #Berechne Drehwinkel
    phi_neu = getPhi(np.array((1,0)) , listX[(i+1) % l ] - listX[i % l])
    if(phi_alt != 0):
        for phi in np.linspace(phi_alt, phi_neu, num=10):
            zeichneRotTranslation(listX, listX[i % l], phi, listPos[i] - listX[i %l]  )
    else :
        zeichneRotTranslation(listX, listX[i % l], phi_neu, listPos[i] - listX[i %l]  )
    return phi_neu
    

def getPhi(k,l):
    k = k / np.linalg.norm(k)
    l = l / np.linalg.norm(l)
    
    phi = np.arccos(np.dot(k,l))
   
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
        
        
        
def mySleep(t):
    startingTime = time.time()
    while(True):
        if(startingTime + t < time.time() ) :
            break
        