import bpy
import math
import util
import numpy as np

def zeichneEllipse(name,anzPunkte, zWert) :
    pkt = ellipsenPunkte(anzPunkte, zWert)
    kanten = []
    flaechen = []
    l = []
    #Jede Ecke hat einen Vorgänger und einen Nachfolger
    for num in range(0,anzPunkte):
        kanten.append( (num , (num+1) % anzPunkte) )
    
    l.extend(range(0,anzPunkte))
    #Es gibt eine Fläche, welche alle Punkte als Ecke hat
    flaechen.append( list(range(0,anzPunkte) ) )
    zeichneMesh(name, pkt, kanten,flaechen )
    
    #Zeichne die Focuspunkte mit ein
    left = (np.sqrt(a**2  - b**2) ,0 , zWert ) 
    right = ( - np.sqrt(a**2  - b**2) ,0 , zWert )
    ellipse = bpy.data.objects.get(name)
    scene = bpy.context.scene
    scene.objects.active = ellipse
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.primitive_circle_add(enter_editmode=True, location=left, radius=0.01)
    bpy.ops.mesh.primitive_circle_add(enter_editmode=True, location=right, radius=0.01)
    bpy.ops.object.mode_set(mode='OBJECT')
    
    
    
def entferneMeshes():
    for item in bpy.context.scene.objects:
        if item.type == 'MESH':
           bpy.context.scene.objects.unlink(item)
    for item in bpy.data.objects:
        if item.type == 'MESH':
            bpy.data.objects.remove(item)
    for item in bpy.data.meshes:
        bpy.data.meshes.remove(item)
    for item in bpy.data.materials:
        bpy.data.materials.remove(item)
        
       
def entferneMesh(name):
    bpy.context.scene.objects.unlink(bpy.data.objects[name])
    bpy.data.objects.remove(bpy.data.objects[name])
    bpy.data.meshes.remove(bpy.data.meshes[name])
     

def zeichne2DPolygon(name, listPunkte, zWert):
     punkte = []
     kanten = []
     i  = 0
     anzPunkte = len(listPunkte)
     for element in listPunkte :
         if element.size == 2 : 
             punkte.append( (element[0] , element[1] , zWert) )
             kanten.append( (i, (i+1) % anzPunkte) )
             i += 1
         else :
             raise Error("Die Punkte haben die falsche Dimension!")
            
     #Print mesh into scene
     zeichneMesh(name, punkte, kanten, () )
    
 
def zeichneRotation(name, polygon, N ):
    punkte = []
    kanten = []
    flaechen = []
    anzPunkte = len(polygon)
    for i in range(0,N):
        stellePunkt = 0
        for punkt in polygon:
            neuerPunkt = (punkt[0], np.cos(i/N * np.pi * 2) * punkt[1] , np.sin(i/N * np.pi * 2) * punkt[1] )
            punkte.append(neuerPunkt)
            
            c = ((anzPunkte) * i) + stellePunkt - 1
            d = ((anzPunkte) * i) + stellePunkt 
            a = c - anzPunkte
            b = d - anzPunkte
           
            #erzeuge Kanten
            if ( i == 0 ) :
                if ( stellePunkt != 0 ):
                    #Kante parallel zur Rotationsachse
                    kanten.append( (c, d) )
                    
            else :
                
                if(stellePunkt != 0) : 
                    #Kante parallel zur Rotationsachse
                    kanten.append( (c,d) )
               
                #Kante orthogonal zur Rotationsachse
                kanten.append( (b,d) ) 
                
                if (i == N -1 ) :
                    #Kante orthogonal zur Rotationsachse
                    kanten.append( (stellePunkt, d) )
                
                #erzeuge Flaechen
                if ( stellePunkt != 0):
                    flaechen.append( (a,b,d) )
                    flaechen.append( (a,d,c) )
                    if ( i == N -1 ):
                        flaechen.append( ( c, d, stellePunkt) )
                        flaechen.append( ( c, stellePunkt, stellePunkt -1) )
                        
            stellePunkt = stellePunkt + 1
    zeichneMesh(name, punkte, kanten, flaechen)        
    #return (punkte, kanten, flaechen)

def zeichneAusgerollt(listA, name) :
    
    listP = []
    listPos = []
    
    for i in range(len(listA[0]) ):
        listP.append( (listA[0][i][0] , listA[0][i][1] , 0 ) )

    for i in range(len(listA[1]) ) :
        listPos.append( (listA[1][i][0] , listA[1][i][1] , 0 )) 
    
    punkte = []
    kanten = []
    flaechen = []
    
    j = 0
    
    punkte.extend(listP)
    punkte.extend(listPos)
    
    for i in range(len(listP) ):
        kanten.append( (len(listPos) + i - 1 , i ) )
        kanten.append( ( i, len(listPos) + i  ) ) 
        
        if i != 0:
            kanten.append( (i -1 , i ))
            
    for i in range(1, len(listPos) ) :
        kanten.append( (i + len(listP) -1 , i + len(listP)  ) )
    
    zeichneMesh(name, punkte, kanten, flaechen)
    
    
def zeichneBilliardmitFocus(name, listPunkte) :
    punkte = []
    kanten = []
    i = 0
    anzPunkte = len(listPunkte)
    for element in listPunkte :
        if element.size == 2 : 
            punkte.append( (element[0] , element[1] , 0) )
            kanten.append( (i, (i+1) % anzPunkte) )
            i += 1
        else :
            raise Error("Die Punkte haben die falsche Dimension!")
    
    for i in range(len(punkte)):
        kanten.append( (len(punkte), i) )
    
    
    punkte.append( (getPositiveFocusPoint()[0] , 0 , 0) )
    
    zeichneMesh(name, punkte, kanten, () )
     
        
def zeichneMesh(name, punkte, kanten, flaechen):
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)
    
   # object.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(object)
    
    mesh.from_pydata(punkte, kanten, flaechen )
    mesh.update(calc_edges=True)

def zeichneDelaunay(name,a1,b1, x0, d0, maxIt, r, N):
        global a
        global b
    #    global maxIterationen
        
        a = a1 * 1.0
        b = b1 * 1.0
     #   maxIterationen = maxIt
        listX = startBilliard(x0,d0)
        listA = ausrollen(listX, N)
        zeichneRotation(name, listA[0], r)
        
        
        
    


    
    
                    
                    
                    
                     
                   
           