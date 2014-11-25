import bpy
import math
import util

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




def zeichneEllipse() :
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

    
    print(a)
    pkt = np.transpose(ellipsenPunkte(100))   
    
    mesh = bpy.data.meshes.new("Ellipse")
    object = bpy.data.objects.new("Ellipse", mesh)
    
    object.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(object)
    
    mesh.from_pydata(np.asarray(pkt), [], [])
    mesh.update(calc_edges=True)
    
    
    
def ellipsenPunkte(N):
	res = np.zeros((2,0));
	for x in range (0,N+1):
		phi = x * 2 * np.pi / (N+1)
		p = [[a * np.cos(phi) ] , [b * np.sin(phi) ]]
		res = np.append(res, p,1);
	
	return res