import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Lab12.MorphingGUI import*
import imageio as Image
import numpy as np
import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QPen,QBrush
from scipy.spatial import Delaunay
import Lab12.Morphing
import PyQt5.QtCore as __PyQt5_QtCore
import PyQt5.QtGui as __PyQt5_QtGui

class MorphingApp(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):

        super(MorphingApp, self).__init__(parent)
        self.setupUi(self)
        self.Blend.setEnabled(False)
        self.ShowT.setEnabled(False)
        self.Alpha.setEnabled(False)
        self.Alpha.setText("0.0")
        self.Slider.setEnabled(False)
        self.LoadStart.clicked.connect(self.loadStartData)
        self.LoadEnd.clicked.connect(self.loadEndData)
        self.ShowT.clicked.connect(self.LoadTriangles)
        self.Blend.clicked.connect(self.blend)
        self.Slider.sliderMoved.connect(self.slider)
        self.Alpha.textChanged.connect(self.alphavalue)
        self.leftcheck = True
        self.rightcheck = True
        self.graphicsStart.mousePressEvent = self.LeftMouseMovement

    def LeftMouseMovement(self,event):
        if self.leftcheck == True:
            pen = QtGui.QPen(QtCore.Qt.green,3)
            x = event.pos().x()
            y = event.pos().y()
            self.lpoint = Lab12.Morphing.Points(x,y,QtCore.Qt.green)
            self.leftpoint = self.graphicsStart.scene().addEllipse(self.lpoint.x, self.lpoint.y, 1, 1, pen)
            self.leftcheck = False
        self.graphicsStart.keyPressEvent = self.LeftKeyMovement
        self.graphicsEnd.mousePressEvent = self.RightMouseMovement

    def LeftKeyMovement(self,event):
        key = event.key()
        if key == QtCore.Qt.Key_Backspace:
            self.graphicsStart.scene().removeItem(self.leftpoint)
            self.leftcheck = True

    def RightMouseMovement(self, event):
        if self.rightcheck == True:
            pen = QtGui.QPen(QtCore.Qt.green, 3)
            x = event.pos().x()
            y = event.pos().y()
            self.rpoint = Lab12.Morphing.Points(x, y, QtCore.Qt.green)
            self.rightpoint = self.graphicsEnd.scene().addEllipse(self.rpoint.x, self.rpoint.y, 1, 1, pen)
            self.rightcheck = False
        self.graphicsEnd.keyPressEvent = self.RightKeyMovement
        if self.leftcheck == False and self.rightcheck == False:
            self.mousePressEvent = self.TurnBlueMovement
            self.graphicsStart.mousePressEvent = self.TurnBlueMovement
    def RightKeyMovement(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Backspace:
            self.graphicsEnd.scene().removeItem(self.rightpoint)
            self.rightcheck = True

    def TurnBlueMovement(self,event):
        pen2 = QtGui.QPen(QtCore.Qt.blue, 3)
        self.graphicsEnd.scene().removeItem(self.leftpoint)
        self.graphicsEnd.scene().removeItem(self.rightpoint)
        self.finalLpoint = self.graphicsStart.scene().addEllipse(self.lpoint.x, self.lpoint.y, 1, 1, pen2)
        self.finalRpoint = self.graphicsEnd.scene().addEllipse(self.rpoint.x, self.rpoint.y, 1, 1, pen2)
        self.leftcheck = True
        self.rightcheck = True
        self.graphicsStart.mousePressEvent = self.LeftMouseMovement
        self.file()

    def file(self):
        xlvalue = str(int(self.lpoint.x/self.rwidth_final))
        ylvalue = str(int(self.lpoint.y/self.rheight_final))
        xlvalue = xlvalue.rjust(8)
        ylvalue = ylvalue.rjust(8)
        xrvalue = str(int(self.rpoint.x/self.rwidth_final))
        yrvalue = str(int(self.rpoint.y/self.rheight_final))
        xrvalue = xrvalue.rjust(8)
        yrvalue = yrvalue.rjust(8)
        self.leftPointsPath = self.LfilePath + ".txt"
        self.rightPointsPath = self.RfilePath + ".txt"
        with open(self.LfilePath + ".txt",'a+') as file:
            file.write(xlvalue + ylvalue + "\n")
        with open(self.RfilePath + ".txt", 'a+') as file2:
            file2.write(xrvalue + yrvalue + "\n")

    def loadStartData(self):
        self.LfilePath, _ = QFileDialog.getOpenFileName(self, caption='Open All ...')
        if not self.LfilePath:
            return
        self.loadStartDataFromFile(self.LfilePath)

    def loadStartDataFromFile(self,filePath):
        self.filePath2 = self.LfilePath + ".txt"
        im = Image.imread(filePath)
        self.graphicsStart.setScene(QtWidgets.QGraphicsScene())
        self.Limage = QtGui.QPixmap(filePath)
        draw = QtGui.QPen(QtCore.Qt.red,3)
        self.lwidth = self.Limage.width()
        self.lheight = self.Limage.height()
        self.Limage = self.Limage.scaled(255,180,QtCore.Qt.KeepAspectRatio)
        self.graphicsStart.scene().addItem(QtWidgets.QGraphicsPixmapItem(self.Limage))
        self.lwidth_2 = self.Limage.width()
        self.lheight_2 = self.Limage.height()
        self.lwidth_final = self.lwidth_2/self.lwidth
        self.lheight_final = self.lheight_2/self.lheight
        if os.path.exists(self.filePath2):
            self.leftPoints = np.loadtxt(self.filePath2)
            self.leftPointsPath = self.filePath2
            for each in self.leftPoints:
                x = each[0]
                y = each[1]
                self.lpoints = Lab12.Morphing.Points(x,y,QtCore.Qt.red)
                self.graphicsStart.scene().addEllipse(self.lpoints.x*self.lwidth_final,self.lpoints.y*self.lheight_final,1,1,draw)
        self.graphicsStart.setScene(self.graphicsStart.scene())
        self.graphicsStart.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsStart.show()

    def loadEndData(self):
        self.RfilePath, _ = QFileDialog.getOpenFileName(self, caption='Open All ...')
        if not self.RfilePath:
            return
        self.loadEndDataFromFile(self.RfilePath)

    def loadEndDataFromFile(self,filePath):
        self.rfilePath2 = self.RfilePath + ".txt"
        im = Image.imread(filePath)
        self.graphicsEnd.setScene(QtWidgets.QGraphicsScene())
        self.Rimage = QtGui.QPixmap(filePath)
        draw = QtGui.QPen(QtCore.Qt.red, 3)
        self.rwidth = self.Rimage.width()
        self.rheight = self.Rimage.height()
        self.Rimage = self.Rimage.scaled(255,180,QtCore.Qt.KeepAspectRatio)
        self.graphicsEnd.scene().addItem(QtWidgets.QGraphicsPixmapItem(self.Rimage))
        self.rwidth_2 = self.Rimage.width()
        self.rheight_2 = self.Rimage.height()
        self.rwidth_final = self.rwidth_2 / self.rwidth
        self.rheight_final = self.rheight_2 / self.rheight
        if os.path.exists(self.rfilePath2) == True:
            self.rightPoints = np.loadtxt(self.rfilePath2)
            self.rightPointsPath = self.rfilePath2
            for each in self.rightPoints:
                x = each[0]
                y = each[1]
                self.rpoints = Lab12.Morphing.Points(x, y, QtCore.Qt.red)
                self.graphicsEnd.scene().addEllipse(self.rpoints.x * self.rwidth_final,
                                                      self.rpoints.y * self.rheight_final, 1, 1, draw)
        self.graphicsEnd.setScene(self.graphicsEnd.scene())
        self.graphicsEnd.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsEnd.show()
        self.Enable()
    def Enable(self):
        self.ShowT.setEnabled(True)
        self.Blend.setEnabled(True)
        self.Alpha.setEnabled(True)
        self.Slider.setEnabled(True)

    def LoadTriangles(self):
        if os.path.exists(self.leftPointsPath) and os.path.exists(self.rightPointsPath):
            self.left, self.right = Lab12.Morphing.loadTriangles(self.leftPointsPath,self.rightPointsPath)
        draw = QtGui.QPen(QtCore.Qt.red, .2)

        for each in self.left:
            ax = each.vertices[0][0]
            ay = each.vertices[0][1]
            bx = each.vertices[1][0]
            by = each.vertices[1][1]
            cx = each.vertices[2][0]
            cy = each.vertices[2][1]
            self.left1=self.graphicsStart.scene().addLine(ax*self.lwidth_final,ay*self.lheight_final,bx*self.lwidth_final,by*self.lheight_final,draw)
            self.left2=self.graphicsStart.scene().addLine(ax*self.lwidth_final,ay*self.lheight_final,cx*self.lwidth_final,cy*self.lheight_final,draw)
            self.left3=self.graphicsStart.scene().addLine(cx*self.lwidth_final,cy*self.lheight_final,bx*self.lwidth_final,by*self.lheight_final,draw)
        self.graphicsStart.setScene(self.graphicsStart.scene())
        self.graphicsStart.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsStart.show()

        for each in self.right:
            ax = each.vertices[0][0]
            ay = each.vertices[0][1]
            bx = each.vertices[1][0]
            by = each.vertices[1][1]
            cx = each.vertices[2][0]
            cy = each.vertices[2][1]
            self.right1=self.graphicsEnd.scene().addLine(ax * self.rwidth_final, ay * self.rheight_final, bx * self.rwidth_final,
                                               by * self.rheight_final, draw)
            self.right2=self.graphicsEnd.scene().addLine(ax * self.rwidth_final, ay * self.rheight_final, cx * self.rwidth_final,
                                               cy * self.rheight_final, draw)
            self.right3=self.graphicsEnd.scene().addLine(cx * self.rwidth_final, cy * self.rheight_final, bx * self.rwidth_final,
                                               by * self.rheight_final, draw)
        self.graphicsEnd.setScene(self.graphicsEnd.scene())
        self.graphicsEnd.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsEnd.show()
        if self.ShowT.checkState()== 0:
           self.removeTriangle()

    def removeTriangle(self):
        for obj in self.graphicsStart.scene().items():
            if isinstance(obj,QtWidgets.QGraphicsLineItem):
                self.graphicsStart.scene().removeItem(obj)
        for obj2 in self.graphicsEnd.scene().items():
            if isinstance(obj2,QtWidgets.QGraphicsLineItem):
                self.graphicsEnd.scene().removeItem(obj2)

    def slider(self):
        self.alpha = self.Slider.value()/100
        self.Alpha.setText(str(self.alpha))
    def alphavalue(self):
        self.alpha = float(self.Alpha.text()) * 100
        self.Slider.setValue(float(self.alpha))

    def blend(self):
        li, ri = Lab12.Morphing.getImage(self.LfilePath, self.RfilePath)
        left,right = Lab12.Morphing.loadTriangles(self.leftPointsPath,self.rightPointsPath)
        good = Lab12.Morphing.Morpher(li,left,ri,right)
        final_array = good.getImageAtAlpha(self.alpha)
        self.graphicsBlend.setScene(QtWidgets.QGraphicsScene())
        im = QtGui.QImage(final_array,final_array.shape[1],final_array.shape[0],QtGui.QImage.Format_Grayscale8)
        image = QtGui.QPixmap(im)
        image = image.scaled(255,180,QtCore.Qt.KeepAspectRatio)
        self.graphicsBlend.scene().addItem(QtWidgets.QGraphicsPixmapItem(image))
        self.graphicsBlend.setScene(self.graphicsBlend.scene())
        self.graphicsBlend.setRenderHint(QtGui.QPainter.Antialiasing)
        self.graphicsBlend.show()

if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = MorphingApp()
    currentForm.show()
    currentApp.exec_()