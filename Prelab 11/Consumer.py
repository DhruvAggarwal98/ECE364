
#######################################################
#   Author:     <Your Full Name>
#   email:      <Your Email>
#   ID:         <Your course ID, e.g. ee364j20>
#   Date:       <Start Date>
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):


        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.btnSave.setEnabled(False)
        self.list1 = [self.txtComponentName_1, self.txtComponentCount_1,self.txtComponentName_2, self.txtComponentCount_2,
                      self.txtComponentName_3, self.txtComponentCount_3,self.txtComponentName_4, self.txtComponentCount_4,
                      self.txtComponentName_5, self.txtComponentCount_5,self.txtComponentName_6, self.txtComponentCount_6,
                      self.txtComponentName_7, self.txtComponentCount_7,self.txtComponentName_8, self.txtComponentCount_8,
                      self.txtComponentName_9, self.txtComponentCount_9,self.txtComponentName_10, self.txtComponentCount_10,
                      self.txtComponentName_11, self.txtComponentCount_11,self.txtComponentName_12, self.txtComponentCount_12,
                      self.txtComponentName_13, self.txtComponentCount_13,self.txtComponentName_14, self.txtComponentCount_14,
                      self.txtComponentName_15, self.txtComponentCount_15,self.txtComponentName_16, self.txtComponentCount_16,
                      self.txtComponentName_17, self.txtComponentCount_17,self.txtComponentName_18, self.txtComponentCount_18,
                      self.txtComponentName_19, self.txtComponentCount_19,self.txtComponentName_20, self.txtComponentCount_20,]
        self.list2 = [self.txtComponentName_1,self.txtComponentName_2,
                      self.txtComponentName_3,self.txtComponentName_4,
                      self.txtComponentName_5,self.txtComponentName_6,
                      self.txtComponentName_7,self.txtComponentName_8,
                      self.txtComponentName_9,self.txtComponentName_10,
                      self.txtComponentName_11,self.txtComponentName_12,
                      self.txtComponentName_13,self.txtComponentName_14,
                      self.txtComponentName_15,self.txtComponentName_16,
                      self.txtComponentName_17,self.txtComponentName_18,
                      self.txtComponentName_19,self.txtComponentName_20,]
        self.list3 = [self.txtComponentCount_1, self.txtComponentCount_2,
                      self.txtComponentCount_3, self.txtComponentCount_4,
                      self.txtComponentCount_5, self.txtComponentCount_6,
                      self.txtComponentCount_7, self.txtComponentCount_8,
                      self.txtComponentCount_9, self.txtComponentCount_10,
                      self.txtComponentCount_11, self.txtComponentCount_12,
                      self.txtComponentCount_13, self.txtComponentCount_14,
                      self.txtComponentCount_15, self.txtComponentCount_16,
                      self.txtComponentCount_17, self.txtComponentCount_18,
                      self.txtComponentCount_19, self.txtComponentCount_20, ]
        self.btnClear.clicked.connect(self.clearForm)
        for each in self.list1:
            each.textChanged.connect(self.save_load)
            self.txtStudentName.textChanged.connect(self.save_load)
            self.txtStudentID.textChanged.connect(self.save_load)
            self.chkGraduate.stateChanged.connect(self.save_load)
            self.cboCollege.currentIndexChanged.connect(self.save_load)
        self.btnSave.clicked.connect(self.save)
        self.btnLoad.clicked.connect(self.loadData)


    def clearForm(self):
        for each in self.list1:
            each.clear()
        self.txtStudentName.clear()
        self.txtStudentID.clear()
        self.chkGraduate.setCheckState(False)
        self.cboCollege.setCurrentIndex(0)
        self.btnSave.setEnabled(False)
        self.btnLoad.setEnabled(True)

    def save_load(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)

    def save(self):
        with open ("target.xml", 'w') as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<Content>\n')
            if self.chkGraduate.isChecked():
                file.write('    <StudentName graduate="true">{}</StudentName>\n'.format(self.txtStudentName.text()))
            else:
                file.write('    <StudentName graduate ="false">{}</StudentName>\n'.format(self.txtStudentName.text()))
            file.write('    <StudentID>{}</StudentID>\n'.format(self.txtStudentID.text()))
            file.write('    <College>{}</College>\n'.format(self.cboCollege.currentText()))
            file.write('    <Components>\n')
            for each,each2 in zip(self.list2,self.list3):
                if each.text() is not "":
                    file.write('        <Component name="{}" count="{}" />\n'.format(each.text(),each2.text()))
            file.write('    </Components>\n')
            file.write('</Content>')


    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """
        count = 0
        with open(filePath , "r") as file:
            for each in file:
                if re.search(r'<StudentName',each) is not None:
                    grad = (re.findall(r'"(.+)"',each))
                    print(grad)
                    if grad[0] == 'true':
                        self.chkGraduate.setCheckState(True)
                    else:
                        self.chkGraduate.setCheckState(False)
                    name = (re.findall(r'>(.+)<',each))
                    self.txtStudentName.setText(name[0])
                if re.search(r'<StudentID',each) is not None:
                    id = re.findall(r'>(.+)<',each)
                    self.txtStudentID.setText(id[0])
                if re.search(r'<College',each) is not None:
                    college = re.findall(r'>(.+)<',each)
                    self.cboCollege.setCurrentText(college[0])
                if re.search(r'<Component name=',each) is not None:
                    count = count+1
                    if count < 21:
                        comp = re.findall(r'name="(.+)"\scount="(.+)"',each)
                        (component, counts) = comp[0]
                        self.list2[count-1].setText(component)
                        self.list3[count-1].setText(counts)

        pass



if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()
