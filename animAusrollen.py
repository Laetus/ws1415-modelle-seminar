import numpy as np
import bpy
import util

### Parameter für Animation Ausrollen

x = np.array((a , 0 ))
#d = np.array((1, 0.700700700700700))
d = np.array((1, 4.1414141414))
listX = startBilliard(x,d)
listA = ausrollen(listX,1)



##### 
entferneMeshes()
anzFrames = animiereAusrollen(listX, listA)



global counter 
counter = 0



for obj in bpy.data.objects :
    obj.hide = True
    

def my_handlerAusrollen(scene) : 
    frame = scene.frame_current
    n = frame % anzFrames
    
    bpy.data.objects[str( n -1 % anzFrames + 1000)].hide = True
    bpy.data.objects[str(n + 1000) ].hide = False
    
    if n <= 1 :
        bpy.data.objects[str(anzFrames -1 + 1000)].hide = True
        bpy.data.objects[str(anzFrames -2 + 1000)].hide = True
        
        
bpy.app.handlers.frame_change_pre.clear()
bpy.app.handlers.frame_change_post.clear()


bpy.app.handlers.frame_change_pre.append(my_handlerAusrollen)

zeichneAusgerollt(listA, 'Ausgerollt') 