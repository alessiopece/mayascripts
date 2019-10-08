import maya.cmds as cmds
import random

def execute(*args):
    mySel = cmds.ls(sl=True)
    N = cmds.intFieldGrp(Number, q=True, value1=True)
    if N < 1 : N = 1
    clonedItems = []
    for i in range(N):
        clonedItems.append(cmds.duplicate(mySel[0]))
        print clonedItems[i]
    x = 0
    y = 0
    z = 0
    cubeEdge = round(N ** (1. / 3))
    if cubeEdge < 1 : cubeEdge = 1
    for i in clonedItems:
        cmds.scale(1,1,1,i)
        cmds.move(0,0,0,i)
    
    for i in clonedItems:
        cmds.move(0+x,0+y,0+z,i)
        r = random.random()
        cmds.scale(r,r,r,i)
        

        x=x+1
        if x>cubeEdge-1:
            x=0
            y=y+1
            if y>cubeEdge-1:
                y=0
                z=z+1

            
         
    

window = cmds.window("UI7", s=False)
cmds.columnLayout()
Number = cmds.intFieldGrp( numberOfFields=1, label='Number of clones', extraLabel='N', value1=0)

ScriptButton = cmds.button(label ='Go !', c=execute)
cmds.showWindow( window )