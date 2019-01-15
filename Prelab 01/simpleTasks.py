#######################################################
#    Author:      <Dhruv Aggarwal >
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('/home/ecegridfs/a/ee364/DataFolder/Prelab01')

#function reads the file sequence.txt given and  searches for the provided input pattern string throughout, and returns a list of all number sequences that match the given pattern.
def find(pattern):

    file= os.path.join(DataPath, 'sequence.txt')
    with open(file) as myfile:
        read_data = myfile.read()
    length = len(pattern)
    newlist = []
    count = 0
    new_sequence = [read_data[i:i+length] for i in range(0, len(read_data)-length+1, 1)]
    for j in range(len(new_sequence)):
        count = 0
        for k in range(len(pattern)):
            if pattern[k] == "X":
                continue
            if pattern[k] == new_sequence[j][k]:
                continue
            if pattern[k] != new_sequence[j][k]:
                count = 1
                break
        if count == 0:
            newlist.append(new_sequence[j])
    return newlist

#searches the string sequence for all sub-sequences, whose size is between 2 and maxSize, inclusively, and returns a list of all sequences whose digital product is equal to product.
def getStreakProduct(sequence, maxSize, product):
    newlist = []
    new_sequence = []
    for i in range(len(sequence)):
        for j in range(2,maxSize + 1, 1):
            if i+j <= len(sequence):
                new_sequence.append(sequence[i:i+j])
    result = 1
    for k in range(len(new_sequence)):
        for l in range(len(new_sequence[k])):
            result = result * int(new_sequence[k][l])
            if result == product:
                newlist.append(new_sequence[k])
        result = 1
    return newlist

# saves one or more pyramid-shaped sequence of characters in file, separated by a single space at the base.
def writePyramids(filePath,baseSize, count, char):
    string = ""
    spaces = " "
    j = 1
    a = int(baseSize/2)
    newlist = []
    for counter in range(a + 1):
        j += 2
        for i in range(count):
            if(i == count - 1):
                string += spaces * (a - counter) + (char * (j - 2)) + spaces * (a - counter ) + "\n"
            else:
                string += spaces * (a - counter) + (char * (j - 2)) + spaces * (a - counter + 1)
        x = string.center(baseSize)
        newlist.append(string)
        string = ''
    with open(filePath, 'w') as myfile:
        myfile.writelines(newlist)

#takes in a sequence, and checks to make sure there is a valid letter, and then prints out the streaks in order of their appearance in the sequence
def getStreaks(sequence, letters):
    newlist = []
    string = ""
    previous = ""
    index = 0
    for index in range(len(sequence)):
        for j in range(len(letters)):
            if sequence[index] == letters[j]:
                if string == "":
                    string += str(sequence[index])
                    continue
                elif(sequence[index -1] == sequence[index]):
                    string += str(sequence[index])
                else:
                    newlist.append(string)
                    string = sequence[index]
        if string != "" and index == len(sequence)-1:
            newlist.append(string)
    return newlist

#searches nameList, depending on input and will return matching names
def findNames(nameList, part, name):
    newlist = []
    for i in nameList:
        first, last= i.split()
        if part == "F":
            if first.lower() == name.lower():
                 newlist.append(i)
        elif part == "L":
            if last.lower() == name.lower():
                newlist.append(i)
        elif part == "FL":
            if first.lower() == name.lower() or last.lower() == name.lower():
                newlist.append(i)
        else:
            return newlist
    return newlist

#converts decimal number into boolean ("True or Falses") depending on binary representation
def convertToBoolean(num, size):
    newlist = []
    if isinstance(num,int) == False:
        return newlist
    if isinstance(size, int) == False:
        return newlist
    else:
        newnumber = bin(num)[2:]
        length = len(newnumber)
        final = size - length
        if length < size:
            for i in range(final):
                newlist.append(False)
        for i in newnumber:
            i = int(i)
            if i == 1:
                newlist.append(True)
            else:
                newlist.append(False)
        return newlist

#converts a list of booleans ("True or Falses") to a decimal value
def convertToInteger(boolList):
    if isinstance(boolList, list) == False:
        return None
    if all(isinstance(i, bool) for i in boolList) == False:
        return None
    if len(boolList) == 0:
        return None
    else:
        decimal = 0
        for i in boolList:
            i = bool(i)
            i = int(i == True)
            decimal = decimal * 2 + int(i)
        return decimal

# This  block  is  optional
if __name__  == "__main__":
    
#    Test for Function 1
     print("FUNCTION 1 ********************TEST****\n")
     test1 = find('1XXX9')
     print(test1)
     print("***************************************\n")

#    Test for Function 2
     print("FUNCTION 2 ********************TEST****\n")
     sequence = "54789654321687984"
     test1 = getStreakProduct(sequence,5,288)
     test2 = getStreakProduct(sequence,3,140)
     test3 = getStreakProduct(sequence,9,10)
     print(test1)
     print(test2)
     print(test3)
     print("***************************************\n")

#    Test for Function 3
     print("FUNCTION 3 ********************TEST****\n")
     writePyramids('test1.txt',13, 6,'X')
     print("***************************************\n")
     
#    Test for Function 4
     print("FUNCTION 4 ********************TEST****\n")
     sequence = "AAASSSSSSAPPPSSPPBBCCCSSS"
     test1 = getStreaks(sequence,"SAQT")
     test2 = getStreaks(sequence,"PAZ")
     test3 = getStreaks(sequence,"GL@")
     test4 = getStreaks(sequence,"X")
     print(test1)
     print(test2)
     print(test3)
     print(test4)
     print("***************************************\n")
     
#    Test for Function 5
     print("FUNCTION 5 ********************TEST****\n")
     names = ["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield", "Johnson Cadence"]
     test1 = findNames(names,"F","Johnson")
     test2 = findNames(names, "L", "Johnson")
     test3 = findNames(names, "FL", "Johnson")
     test4 = findNames(names, "FL", "SMITh")
     print(format(test1))
     print(format(test2))
     print(format(test3))
     print(format(test4))
     print("***************************************\n")
     
#    Test for Function 6
     print("FUNCTION 6 ********************TEST****\n")
     test1 = convertToBoolean(135, 12)
     print(test1)
     test2 = convertToBoolean(9,3)
     print(test2)
     print("***************************************\n")
     
#    Test for Function 7
     print("FUNCTION 7 ********************TEST****\n")
     test1 = [True,False, False, False, False, True, True, True]
     test2 = [False, False, True, False, False, True]
     answer1 = convertToInteger(test1)
     answer2 = convertToInteger(test2)
     print(answer1)
     print(answer2)
     print("***************************************\n")
