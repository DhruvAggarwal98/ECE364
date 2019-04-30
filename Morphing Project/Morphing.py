#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <4/5/19>
#######################################################
import os      # List of  module  import  statements
import os.path
import numpy as np
from scipy.spatial import Delaunay
import scipy.interpolate
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import imageio
import matplotlib.pyplot as plt
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class Triangle:
    vertices = np.array
    def __init__(self, vertices):
        if vertices.dtype == "float64":
            self.vertices = vertices
        else:
            raise ValueError("not of type float64")

    def getPoints(self):
        max_x = max([self.vertices[0][0], self.vertices[1][0], self.vertices[2][0]])
        max_y = max([self.vertices[0][1], self.vertices[1][1], self.vertices[2][1]])
        image = Image.new("L", (int(max_x),int(max_y)),color = 0)
        draw = ImageDraw.Draw(image)
        draw.polygon([(self.vertices[0][0], self.vertices[0][1]),(self.vertices[1][0], self.vertices[1][1]),(self.vertices[2][0], self.vertices[2][1])], fill=255)
        imageArray = np.array(image)
        nonzero = np.nonzero(imageArray)
        length = len(nonzero[0])
        s = (length,2)
        n_array = np.zeros(s)
        for each,each2,row in zip(nonzero[0],nonzero[1],n_array):
            row[0] = each2
            row[1] = each
        return n_array

    #rachef office hours ^^

def getImage(leftImage,rightImage):
    li = np.array(imageio.imread(leftImage),np.uint8)
    ri = np.array(imageio.imread(rightImage),np.uint8)
    return li,ri

class Morpher:
    leftImage = np.array
    leftTriangles = list()
    rightImage = np.array
    rightTriangles = list()
    def __init__(self,leftImage,leftTriangles,rightImage,rightTriangles):
        #li,ri = getImage(leftImage,rightImage)
        if leftImage.dtype == "uint8":
            self.leftImage = leftImage
        else:
            raise TypeError("Wrong Type")
        if type(leftTriangles) == list:
            self.leftTriangles = leftTriangles
        else:
            raise TypeError("Wrong Type")
        if rightImage.dtype == "uint8":
            self.rightImage = rightImage
        else:
            raise TypeError("Wrong Type")
        if type(rightTriangles) == list:
            self.rightTriangles = rightTriangles
        else:
            raise TypeError("Wrong Type")

    def getImageAtAlpha(self,alpha):
        mid_triangle = list()
        testList = list()
        left = scipy.interpolate.RectBivariateSpline(range(self.leftImage.shape[0]),range(self.leftImage.shape[1]),self.leftImage)
        right = scipy.interpolate.RectBivariateSpline(range(self.rightImage.shape[0]), range(self.rightImage.shape[1]),self.rightImage)
        FinalArray = np.array(Image.new('L', (self.leftImage.shape[1], self.leftImage.shape[0])))
        counter = 0

        for each,each2 in zip(self.leftTriangles,self.rightTriangles):
            leftcoord = self.leftTriangles[counter].vertices
            rightccord = self.rightTriangles[counter].vertices
            mid_triangle.append(Triangle((1-alpha)*leftcoord+(alpha*rightccord)))
            templist_L = np.array([[each.vertices[0][0],each.vertices[0][1],1,0,0,0],
                        [0,0,0,each.vertices[0][0],each.vertices[0][1],1],
                        [each.vertices[1][0], each.vertices[1][1], 1, 0, 0, 0],
                        [0, 0, 0, each.vertices[1][0], each.vertices[1][1], 1],
                        [each.vertices[2][0], each.vertices[2][1], 1, 0, 0, 0],
                        [0, 0, 0, each.vertices[2][0], each.vertices[2][1], 1]])
            templist2 = np.array([[mid_triangle[counter].vertices[0][0]],
                         [mid_triangle[counter].vertices[0][1]],
                         [mid_triangle[counter].vertices[1][0]],
                         [mid_triangle[counter].vertices[1][1]],
                         [mid_triangle[counter].vertices[2][0]],
                         [mid_triangle[counter].vertices[2][1]]])

            final_list_L = np.linalg.solve(templist_L, templist2)

            h_L = np.array([[final_list_L[0][0], final_list_L[1][0], final_list_L[2][0]],
                                [final_list_L[3][0],final_list_L[4][0],final_list_L[5][0]],
                                [0,0,1]
                                ])

            hinverse_L = np.linalg.inv(h_L)

            templist_R = np.array([[each2.vertices[0][0], each2.vertices[0][1], 1, 0, 0, 0],
                                       [0, 0, 0, each2.vertices[0][0], each2.vertices[0][1], 1],
                                       [each2.vertices[1][0], each2.vertices[1][1], 1, 0, 0, 0],
                                       [0, 0, 0, each2.vertices[1][0], each2.vertices[1][1], 1],
                                       [each2.vertices[2][0], each2.vertices[2][1], 1, 0, 0, 0],
                                       [0, 0, 0, each2.vertices[2][0], each2.vertices[2][1], 1]])

            final_list_R = np.linalg.solve(templist_R, templist2)

            h_R = np.array([[final_list_R[0][0], final_list_R[1][0], final_list_R[2][0]],
                                [final_list_R[3][0], final_list_R[4][0], final_list_R[5][0]],
                                [0, 0, 1]
                                ])
            hinverse_R = np.linalg.inv(h_R)

            new = mid_triangle[counter].getPoints()
            new_trans = np.transpose(new)
            for j,each3 in new:
                coord = np.vstack((j,each3,1))
                xy_L = np.matmul(hinverse_L, coord)
                xy_R = np.matmul(hinverse_R,coord)
                a = left.ev(xy_L[1],xy_L[0])
                b = right.ev(xy_R[1],xy_R[0])
                blended = (1-alpha) * a + b*alpha
                FinalArray[int(each3), int(j)] = np.uint8(blended)

            counter += 1

        return FinalArray

def loadTriangles(leftPointFilePath, rightPointFilePath):
    group1 = np.loadtxt(leftPointFilePath)
    group2 = np.loadtxt(rightPointFilePath)
    pointsLeft = Delaunay(group1)
    leftTriangles = [Triangle(vertices) for vertices in group1[pointsLeft.simplices]]
    rightTriangles = [Triangle(vertices) for vertices in group2[pointsLeft.simplices]]
    return (leftTriangles, rightTriangles)

class Points:
    def __init__(self,x,y,color_value):
        self.x = x
        self.y = y
        self.color_value = color_value

if __name__ == "__main__":
    DataPath1 = ('/home/ecegridfs/a/ee364/DataFolder/Lab12/TestData/points.left.txt')
    DataPath2 = ('/home/ecegridfs/a/ee364/DataFolder/Lab12/TestData/points.right.txt')
    DataPath3 = ('/home/ecegridfs/a/ee364/DataFolder/Lab12/TestData/LeftGray.png')
    DataPath4 = ('/home/ecegridfs/a/ee364/DataFolder/Lab12/TestData/RightGray.png')
    left, right =loadTriangles(DataPath1,DataPath2)
    li,ri = getImage(DataPath3,DataPath4)
    hi = Morpher(li,left,ri,right)
    final_array = hi.getImageAtAlpha(0.5)
    imageio.imwrite("test.png", final_array)
    #coords = Triangle(np.array([(0.0,60.0), (10.0,20.0), (50.0,100.0)]))
    #coords.getPoints()
    # for l in left:
    #     print(l.vertices)
