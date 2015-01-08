import numpy as np
import bpy
import util

#### Parameter für Animation Billiard


x = np.array((a , 0 ))
d = np.array((1, 4.1414141414))
#d = np.array((1, 0.700700700700700))
listX = startBilliard(x,d)



entferneMeshes()
global counter 
counter = 0

anzFrames = animiereBilliard(listX)

for obj in bpy.data.objects:
    obj.hide = True

"""
def my_handlerBilliardPre(scene) : 
    frame = scene.frame_current
    n = frame % anzFrames
    n = n +1000

    bpy.data.objects[str(n)].hide = False
"""   
def my_handlerBilliard(scene) : 
    frame = scene.frame_current
    n = frame % anzFrames
    
    bpy.data.objects[str( n -1 % anzFrames + 1000)].hide = True
    bpy.data.objects[str( n -1 % anzFrames + 1000)].select = True
    bpy.data.objects[str(n + 1000) ].hide = False
    bpy.data.objects[str(n + 1000) ].select = False
    if n <= 1 :
        bpy.data.objects[str(anzFrames -1 +1000)].hide = True
    
   
   
bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_post.clear()


bpy.app.handlers.frame_change_pre.append(my_handlerBilliard)

zeichneEllipse('Ellipse',1000,0)