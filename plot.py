import bpy
import math
import util

'''
# clear mesh and object
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

# mesh arrays
verts = []
faces = []

# mesh variables
numX = 100
numY = 100

# variance and scale variables
variance = .35
scale = 4

# fill verts array
for i in range (0, numX):
    for j in range(0,numY):
        # nomalize range
        u = 2*(i/numX-1/2)
        v = 2*(j/numY-1/2)

        s = variance
        x = scale*u
        y = scale*v
        z = scale*1/math.sqrt(2*math.pi*s*s)*math.exp(-(u*u+v*v)/(2*s*s))

        vert = (x,y,z)
        verts.append(vert)

# fill faces array
count = 0
for i in range (0, numY *(numX-1)):
    if count < numY-1:
        A = i
        B = i+1
        C = (i+numY)+1
        D = (i+numY)
        face = (A,B,C,D)
        faces.append(face)
        count = count + 1
    else:
        count = 0

# create mesh and object
mesh = bpy.data.meshes.new("wave")
object = bpy.data.objects.new("wave",mesh)

# set mesh location
object.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(object)

# create mesh from python data
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)

'''


def zeichneEllipse(name,anzPunkte, zWert) :
    pkt = util.ellipsenPunkte(anzPunkte, zWert)
    zeichneMesh(name, pkt, (),() )


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