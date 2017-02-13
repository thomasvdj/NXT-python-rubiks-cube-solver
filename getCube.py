def rotateCube(axis, rotation, orientation):
    if axis == 1: #x-axis
        if rotation == 1:
            return [orientation[4],orientation[1],orientation[0],orientation[3],orientation[5],orientation[2]]
        elif rotation == 2:
            return [orientation[5],orientation[1],orientation[4],orientation[3],orientation[2],orientation[0]]
        elif rotation == 3:
            return [orientation[2],orientation[1],orientation[5],orientation[3],orientation[0],orientation[4]]
    elif axis == 2: #y-axis
        if rotation == 1:
            return [orientation[1],orientation[5],orientation[2],orientation[0],orientation[4],orientation[3]]
        elif rotation == 2:
            return [orientation[5],orientation[3],orientation[2],orientation[1],orientation[4],orientation[0]]
        elif rotation == 3:
            return [orientation[3],orientation[0],orientation[2],orientation[5],orientation[4],orientation[1]]
    elif axis == 3: #z-axis
        if rotation == 1:
            return [orientation[0],orientation[2],orientation[3],orientation[4],orientation[1],orientation[5]]
        elif rotation == 2:
            return [orientation[0],orientation[3],orientation[4],orientation[1],orientation[2],orientation[5]]
        elif rotation == 3:
            return [orientation[0],orientation[4],orientation[1],orientation[2],orientation[3],orientation[5]]

def rotateListOfFour(someList, rotation):
    # rotates a list of four
    finalList = [0]*4
    if rotation == 0:
        return someList
    elif rotation == 1:
        finalList[0] = someList[1]
        finalList[1] = someList[2]
        finalList[2] = someList[3]
        finalList[3] = someList[0]
    elif rotation == 2:
        finalList[0] = someList[2]
        finalList[1] = someList[3]
        finalList[2] = someList[0]
        finalList[3] = someList[1]
    elif rotation == 3:
        finalList[0] = someList[3]
        finalList[1] = someList[0]
        finalList[2] = someList[1]
        finalList[3] = someList[2]
    return finalList
        

def stitchSides(side1, side2, side3, side4, side5, side6):
    # stitch all the 6 scanned sides together into the chosen coordinate system
    # sides are expected in order: Front, Right, Back, Left, Top, Under
    # orientation depends on how the cube is handled by the robot during scanning
    orientation = [side2[-1],side6[-1],side3[-1],side5[-1],side1[-1],side4[-1]]
    defaultOrientation = range(1,7)
    
    # place the sides in the correct order, using the orientation
    requiredRotations = [[0,0],[0,0]]
    if orientation != defaultOrientation:
        if orientation[0] == defaultOrientation[0]:
            #print "option 1"
            for rotation in range(1,4):
                if defaultOrientation == rotateCube(3,rotation, orientation):
                    requiredRotations[0] = [3,rotation]
                    orientation = rotateCube(3,rotation, orientation)
        else:
            for rotation in range(1,4):
                compare = rotateCube(2,rotation, orientation)
                if defaultOrientation[0] == compare[0]:
                    #print "option 2"
                    requiredRotations[0] = [2,rotation]
                    orientation = rotateCube(2,rotation, orientation)
            if requiredRotations[0] == [0,0]:
                #print "option 3"
                for rotation in range(1,4):
                    compare = rotateCube(1,rotation, orientation)
                    if defaultOrientation[0] == compare[0]:
                        print "option 4"
                        requiredRotations[0] = [1,rotation]
                        orientation = rotateCube(1,rotation, orientation)
                        print rotation
    if orientation != defaultOrientation:
        #print "option 6"
        for rotation in range(1,4):
            if defaultOrientation == rotateCube(3,rotation, orientation):
                requiredRotations[1] = [3,rotation]
                orientation = rotateCube(3,rotation, orientation)
                print rotation
    #if defaultOrientation == orientation:
        #print "succes!"
    
    newSide3 = [rotateListOfFour(side3[0],1),rotateListOfFour(side3[1],1), side3[-1]]
    newSide1 = [rotateListOfFour(side1[0],3),rotateListOfFour(side1[1],3),side1[-1]]
    newCorners4 = [side4[0][3], side4[0][2], side4[0][1], side4[0][0]]
    newEdges4 = [side4[1][2], side4[1][1], side4[1][0], side4[1][3]]
    newSide4 = [newCorners4, newEdges4, side4[-1]]
    newSide4 = [rotateListOfFour(newCorners4,2),rotateListOfFour(newEdges4,2), side4[-1]]
    listOfSides = [side2, side6, newSide3, side5, newSide1, newSide4]
    
    if requiredRotations[0] != [0,0]:
        #print "check 1"
        listOfSides = rotateCube(requiredRotations[0][0],requiredRotations[0][1],listOfSides)
    else:
        #print "check 2"
        pass
   
    # determine the orientation of the corners and the edges
    listOfCorners = [0]*6
    listOfEdges = [0]*6
    for i in range(6):
        listOfCorners[i] = listOfSides[i][0]
        listOfEdges[i] = listOfSides[i][1] 
    if requiredRotations == [[0,0],[0,0]]:
        pass
    elif requiredRotations[0][0] == 3:
        listOfCorners[0] = rotateListOfFour(listOfCorners[0],(-1+requiredRotations[0][1])%4)
        listOfEdges[0] = rotateListOfFour(listOfEdges[0],(-1+requiredRotations[0][1])%4)
        listOfCorners[5] = rotateListOfFour(listOfCorners[5],(-1+requiredRotations[0][1])%4)
        listOfEdges[5] = rotateListOfFour(listOfEdges[5],(-1+requiredRotations[0][1])%4)
    elif requiredRotations[0][0] == 2:
        if requiredRotations[0][1] == 1:
            listOfCorners[2] = rotateListOfFour(listOfCorners[2],1)
            listOfEdges[2] = rotateListOfFour(listOfEdges[2],1)
            listOfCorners[4] = rotateListOfFour(listOfCorners[4],3)
            listOfEdges[4] = rotateListOfFour(listOfEdges[4],3)
            listOfCorners[1] = rotateListOfFour(listOfCorners[1],3)
            listOfEdges[1] = rotateListOfFour(listOfEdges[1],3)
            listOfCorners[3] = rotateListOfFour(listOfCorners[2],1)
            listOfEdges[3] = rotateListOfFour(listOfEdges[2],1)
        elif requiredRotations[0][1] == 2:
            listOfCorners[2] = rotateListOfFour(listOfCorners[2],2)
            listOfEdges[2] = rotateListOfFour(listOfEdges[2],2)
            listOfCorners[4] = rotateListOfFour(listOfCorners[4],2)
            listOfEdges[4] = rotateListOfFour(listOfEdges[4],2)
            listOfCorners[1] = rotateListOfFour(listOfCorners[1],2)
            listOfEdges[1] = rotateListOfFour(listOfEdges[1],2)
            listOfCorners[3] = rotateListOfFour(listOfCorners[3],2)
            listOfEdges[3] = rotateListOfFour(listOfEdges[3],2)
            listOfCorners[0] = rotateListOfFour(listOfCorners[0],3)
            listOfEdges[0] = rotateListOfFour(listOfEdges[0],3)
            listOfCorners[5] = rotateListOfFour(listOfCorners[5],3)
            listOfEdges[5] = rotateListOfFour(listOfEdges[5],3)
        elif requiredRotations[0][1] == 3:
            listOfCorners[2] = rotateListOfFour(listOfCorners[2],3)
            listOfEdges[2] = rotateListOfFour(listOfEdges[2],3)
            listOfCorners[4] = rotateListOfFour(listOfCorners[4],1)
            listOfEdges[4] = rotateListOfFour(listOfEdges[4],1)
            listOfCorners[1] = rotateListOfFour(listOfCorners[1],3)
            listOfEdges[1] = rotateListOfFour(listOfEdges[1],3)
            listOfCorners[3] = rotateListOfFour(listOfCorners[3],1)
            listOfEdges[3] = rotateListOfFour(listOfEdges[3],1)
            listOfCorners[0] = rotateListOfFour(listOfCorners[0],2)
            listOfEdges[0] = rotateListOfFour(listOfEdges[0],2)
            listOfCorners[5] = rotateListOfFour(listOfCorners[5],2)
            listOfEdges[5] = rotateListOfFour(listOfEdges[5],2)
    elif requiredRotations[0][0] == 1:
        if requiredRotations[0][1] == 1:
            listOfCorners[2] = rotateListOfFour(listOfCorners[2],2)
            listOfEdges[2] = rotateListOfFour(listOfEdges[2],2)
            listOfCorners[4] = rotateListOfFour(listOfCorners[4],2)
            listOfEdges[4] = rotateListOfFour(listOfEdges[4],2)
            listOfCorners[1] = rotateListOfFour(listOfCorners[1],1)
            listOfEdges[1] = rotateListOfFour(listOfEdges[1],1)
            listOfCorners[3] = rotateListOfFour(listOfCorners[3],3)
            listOfEdges[3] = rotateListOfFour(listOfEdges[3],3)
            listOfCorners[0] = rotateListOfFour(listOfCorners[0],3)
            listOfEdges[0] = rotateListOfFour(listOfEdges[0],3)
            listOfCorners[5] = rotateListOfFour(listOfCorners[5],3)
            listOfEdges[5] = rotateListOfFour(listOfEdges[5],3)
        elif requiredRotations[0][1] == 2:
            listOfCorners[2] = rotateListOfFour(listOfCorners[2],2)
            listOfEdges[2] = rotateListOfFour(listOfEdges[2],2)
            listOfCorners[4] = rotateListOfFour(listOfCorners[4],2)
            listOfEdges[4] = rotateListOfFour(listOfEdges[4],2)
            listOfCorners[1] = rotateListOfFour(listOfCorners[1],2)
            listOfEdges[1] = rotateListOfFour(listOfEdges[1],2)
            listOfCorners[3] = rotateListOfFour(listOfCorners[3],2)
            listOfEdges[3] = rotateListOfFour(listOfEdges[3],2)
            listOfCorners[0] = rotateListOfFour(listOfCorners[0],1)
            listOfEdges[0] = rotateListOfFour(listOfEdges[0],1)
            listOfCorners[5] = rotateListOfFour(listOfCorners[5],1)
            listOfEdges[5] = rotateListOfFour(listOfEdges[5],1)
        elif requiredRotations[0][1] == 3:
            listOfCorners[1] = rotateListOfFour(listOfCorners[1],3)
            listOfEdges[1] = rotateListOfFour(listOfEdges[1],3)
            listOfCorners[3] = rotateListOfFour(listOfCorners[3],1)
            listOfEdges[3] = rotateListOfFour(listOfEdges[3],1)
            listOfCorners[0] = rotateListOfFour(listOfCorners[0],1)
            listOfEdges[0] = rotateListOfFour(listOfEdges[0],1)
            listOfCorners[5] = rotateListOfFour(listOfCorners[5],1)
            listOfEdges[5] = rotateListOfFour(listOfEdges[5],1)
    if requiredRotations[1] != [0,0]:
        #print "check 3"
        listOfSides = rotateCube(requiredRotations[1][0],requiredRotations[1][1],listOfSides)
        for i in range(6):
            listOfCorners[i] = listOfSides[i][0]
            listOfEdges[i] = listOfSides[i][1] 
        listOfCorners[0] = rotateListOfFour(listOfCorners[0],requiredRotations[1][1])
        listOfEdges[0] = rotateListOfFour(listOfEdges[0],requiredRotations[1][1])
        listOfCorners[5] = rotateListOfFour(listOfCorners[5],requiredRotations[1][1])
        listOfEdges[5] = rotateListOfFour(listOfEdges[5],requiredRotations[1][1])

    #place the lists of corners and edges in the coordinate system
    edges = [[listOfEdges[0][0],listOfEdges[1][2]],[listOfEdges[0][1],listOfEdges[2][2]],
             [listOfEdges[0][2],listOfEdges[3][2]],[listOfEdges[0][3],listOfEdges[4][2]],
             [listOfEdges[5][0],listOfEdges[1][0]],[listOfEdges[5][1],listOfEdges[2][0]],
             [listOfEdges[5][2],listOfEdges[3][0]],[listOfEdges[5][3],listOfEdges[4][0]],
             [listOfEdges[1][3],listOfEdges[4][1]],[listOfEdges[1][1],listOfEdges[2][3]],
             [listOfEdges[3][3],listOfEdges[2][1]],[listOfEdges[3][1],listOfEdges[4][3]]]
    corners = [[listOfCorners[0][0],listOfCorners[1][3],listOfCorners[4][2]],
               [listOfCorners[0][1],listOfCorners[2][3],listOfCorners[1][2]],
               [listOfCorners[0][2],listOfCorners[3][3],listOfCorners[2][2]],
               [listOfCorners[0][3],listOfCorners[4][3],listOfCorners[3][2]],
               [listOfCorners[5][0],listOfCorners[4][1],listOfCorners[1][0]],
               [listOfCorners[5][1],listOfCorners[1][1],listOfCorners[2][0]],
               [listOfCorners[5][2],listOfCorners[2][1],listOfCorners[3][0]],
               [listOfCorners[5][3],listOfCorners[3][1],listOfCorners[4][0]]]
    return [corners, edges, orientation]
