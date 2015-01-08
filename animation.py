import bpy
import math
import util
import numpy as np
import plot
import time
import random

    
global counter 
counter = 0

global billiard_subdiv
billiard_subdiv = 50

global ausrollen_subdiv
ausrollen_subdiv = 25
    
def zeichneRotTranslation(listX, rotZentrum, winkel,richtung):
    punkte = []
    kanten = []
    flaechen = []
    i = 0
    winkel = -winkel
       
    anzPunkte = len(listX)
    for element in listX :
        #Anwenden der Transformationani
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
    
    global counter 
    name = str(counter)
    counter = counter +1
    #entferneMesh(name)
    zeichneMesh(name, punkte, kanten, flaechen )
    bpy.data.objects[name].modifiers.new('Wireframe', type='WIREFRAME')
    #bpy.ops.object.convert(target='MESH', keep_original=False)


def animiereAusrollen(listX, listA):
    global counter 
    counter =  counter + 1000
    alt = counter
    listP = listA[0]
    listPos = listA[1]
    listAWW = listA[2]
    
    phi_alt = 0
    for i in range(len(listX)):
        phi_alt = doStepI(i,listX,listPos, phi_alt)
    return counter - alt


def doStepI(i , listX, listPos, phi_alt):
    l = len(listX)
    #Berechne Drehwinkel
    phi_neu = getPhi(np.array((1,0)) , listX[(i+1) % l ] - listX[i % l])
    if(phi_alt != 0):
        for phi in np.linspace(phi_alt, phi_neu, num=ausrollen_subdiv):
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
  
        
def animiereBilliard(listX):
    global counter
    counter =  counter + 1000
    alt = counter
    for i in range(1,len(listX)) :
        for lmd in np.linspace(0,1,billiard_subdiv) :
            zeichneSchuss(i,listX, lmd)
    return counter - alt
        
        
def zeichneSchuss(i, listX, lmd):
    punkte = []
    kanten = []
    flaechen = []
    
    for j in range(0,i) :
        punkte.append( (listX[j][0] , listX[j][1] , 0.01) )
        if j != 0 :
            kanten.append( (j-1 , j) )
    
    konvKomb = ((1-lmd) * listX[i-1]) + (lmd * listX[i])
    
    punkte.append(( konvKomb[0] , konvKomb[1] , 0.01 ))
    kanten.append( ( i-1 , i) )
   
    global counter 
    name = str(counter)
    counter = counter +1
    #entferneMesh(name)
    zeichneMesh(name, punkte, kanten, flaechen )
    
    #bpy.data.objects[name].modifiers.new('Wireframe', type='WIREFRAME')
    #bpy.ops.object.convert(target='MESH', keep_original=False)
    
    