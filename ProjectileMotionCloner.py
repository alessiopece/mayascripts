import maya.cmds as cmds
import math

def execute(*args):
    mySel = cmds.ls(sl=True)
    D = cmds.intFieldGrp(Density, q=True, value1=True)
    angle = cmds.intFieldGrp(Angle, q=True, value1=True)
    if D > 100 : D = 100
    if D < 0   : D = 0
    clonedItems = []

    startingPointItem = mySel[0]
    endingPointItem = mySel[1]
    startingPoint = cmds.objectCenter(mySel[0])
    endingPoint = cmds.objectCenter(mySel[1])

    #This ensure that the starting point is always the highest object selected
    if startingPoint[1] < endingPoint[1] :
        temp = startingPointItem
        startingPointItem = endingPointItem
        endingPointItem = temp
        startingPoint = cmds.objectCenter(startingPointItem)
        endingPoint = cmds.objectCenter(endingPointItem)




    time = 0
    distance = math.sqrt(((endingPoint[0]-startingPoint[0])**2)+(endingPoint[2]-startingPoint[2])**2)
    initialSpeed = (distance/math.cos(math.radians(angle)))*math.sqrt(9.8/(2*distance*math.tan(math.radians(angle))+2*startingPoint[1]))
    flightTime = distance/(initialSpeed*math.cos(math.radians(angle)))
    
    print "START HEIGHT: ", math.sin(math.radians(2*angle))
    
    print "DISTANCE: ", distance
    
    print "SPEED: ", initialSpeed
    print "TIME: ", flightTime
    
    
    
    print distance

    deltaX = endingPoint[0]-startingPoint[0]
    deltaZ = endingPoint[2]-startingPoint[2]
    
    if deltaZ != 0 :
        directionAngle = math.atan(deltaX/deltaZ)
    else:
        if deltaX>0:
            directionAngle=(math.pi)/2
        else:
            directionAngle=(-math.pi)/2
    print "Angle2: ",directionAngle
    if deltaX<0 and deltaZ<0:
        directionAngle = directionAngle + math.pi
    elif deltaX>=0 and deltaZ<0:
        directionAngle = directionAngle + math.pi

        


    while time <= flightTime :

        newClone = cmds.duplicate(startingPointItem)
        x = startingPoint[0] + initialSpeed*math.cos(math.radians(angle))*math.sin(directionAngle)*time
        y = -0.5*9.8*(time**2) + initialSpeed*math.sin(math.radians(angle))*time + startingPoint[1]
        z = startingPoint[2] + initialSpeed*math.cos(math.radians(angle))*math.cos(directionAngle)*time
        print "time: ",time
        print "X: ",x,"Y: ",y,"Z: ",z
        cmds.move(x,y,z,newClone,absolute=True)

        time = time + 0.3
    

         
    

window = cmds.window("UI9", s=False)
cmds.columnLayout()
Density = cmds.intFieldGrp( numberOfFields=1, label='Density of clones', extraLabel='%', value1=50)
Angle = cmds.intFieldGrp( numberOfFields=1, label='Angle', extraLabel='Degrees', value1=30)

ScriptButton = cmds.button(label ='Go !', c=execute)
cmds.showWindow( window )