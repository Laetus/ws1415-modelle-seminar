import bpy
import math
import util


def zeichneEllipse(name,anzPunkte, zWert) :
    pkt = ellipsenPunkte(anzPunkte, zWert)
    kanten = []
    for num in range(0,anzPunkte):
        kanten.append( (num , (num+1) % anzPunkte) )
        
    zeichneMesh(name, pkt, kanten,() )
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
     return (punkte, kanten)
    
              
def zeichneMesh(name, punkte, kanten, flaechen):
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)
    
   # object.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(object)
    
    mesh.from_pydata(punkte, kanten, flaechen)
    mesh.update(calc_edges=True)