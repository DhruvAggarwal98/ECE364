#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <2/15/19>
#######################################################
import os      # List of  module  import  statements
import os.path
import math
import copy
from collections import UserList
from collections import defaultdict
import statistics
from enum import Enum
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class Datum:

    def __init__(self, *args):

        for each in args:
            if type(each) != float:
                raise TypeError("Input not a float")
            else:
                self._storage = args

    def __str__(self):
        list1 = []

        for each in self._storage:
            list1.append(format(each,'.2f'))
        new_list = str(list1)
        new_list = new_list.replace("[","(")
        new_list = new_list.replace("]", ")")
        new_list = new_list.replace("'", "")
        return str(new_list)

    def __repr__(self):
        return repr(self._storage)

    def __hash__(self):
        return hash(self._storage)

    def distanceFrom(self, Datum):
        count1 = len(self._storage)
        count2 = len(Datum)
        count3 = 0
        i = 0
        sub = 0
        list1 = list(self._storage)
        list2 = list(Datum)
        for each in Datum:
            if type(each) != float:
                raise TypeError("Input not a float")
        else:
            if count1 != count2:
                if count1 < count2:
                    count3 = count2 - count1
                    while i < count3:
                        list1.append(0.0)
                        i += 1
                if count2 < count1:
                    count3 = count1 - count2
                    while i < count3:
                        list2.append(0.0)
                        i += 1
            for val1, val2 in zip(list1, list2):
                sub += abs(val1-val2)**2
                final = math.sqrt(sub)
        return final

    def clone(self):
        return copy.deepcopy(self)

    def __contains__(self, item):
        if type(item) != float:
            raise TypeError("Invalid Input")
        else:
            if item not in self._storage:
                return False
            else:
                return True

    def __len__(self):
        return len(self._storage)

    def __iter__(self):
        return iter(self._storage)

    def __neg__(self):
        new = self.clone()
        new_again = list(new)
        list2 = list()
        for each in new_again:
            list2.append(each * -1)
        new._storage = tuple(list2)
        return new

    def __getitem__(self, item):
        return self._storage[item]

    def __add__(self, other):
        if isinstance(other,Datum):
            list1 = list(self)
            list2 = list(other)
            final = self.clone()
            count1 = len(list1)
            count2 = len(list2)
            count3 = 0
            i = 0
            sub = 0
            l = []
            if count1 != count2:
                if count1 < count2:
                    count3 = count2 - count1
                    while i < count3:
                        list1.append(0.0)
                        i += 1
                if count2 < count1:
                    count3 = count1 - count2
                    while i < count3:
                        list2.append(0.0)
                        i += 1
                for val1, val2 in zip(list1, list2):
                    l.append(val1 + val2)
                final._storage = l
            return final
        elif type(other) == float:
            list1 = list(self)
            l = []
            final = self.clone()
            for each in list1:
                l.append(each + other)
                final._storage = l
            return final
        else:
            raise TypeError("Invalid Input")

    def __radd__(self, other):
        return self.__add__(other)


    def __sub__(self, other):
        if isinstance(other,Datum):
            list1 = list(self)
            list2 = list(other)
            final = self.clone()
            count1 = len(list1)
            count2 = len(list2)
            count3 = 0
            i = 0
            sub = 0
            l = []
            if count1 != count2:
                if count1 < count2:
                    count3 = count2 - count1
                    while i < count3:
                        list1.append(0.0)
                        i += 1
                if count2 < count1:
                    count3 = count1 - count2
                    while i < count3:
                        list2.append(0.0)
                        i += 1
                for val1, val2 in zip(list1, list2):
                    l.append(val1 - val2)
                final._storage = l
            return final
        elif type(other) == float:
            list1 = list(self)
            l = []
            final = self.clone()
            for each in list1:
                l.append(each - other)
                final._storage = l
            return final
        else:
            raise TypeError("Invalid Input")

    def __mul__(self, other):
        if isinstance(other,Datum):
            list1 = list(self)
            list2 = list(other)
            final = self.clone()
            count1 = len(list1)
            count2 = len(list2)
            count3 = 0
            i = 0
            sub = 0
            l = []
            if count1 != count2:
                if count1 < count2:
                    count3 = count2 - count1
                    while i < count3:
                        list1.append(0.0)
                        i += 1
                if count2 < count1:
                    count3 = count1 - count2
                    while i < count3:
                        list2.append(0.0)
                        i += 1
                for val1, val2 in zip(list1, list2):
                    l.append(val1 * val2)
                final._storage = l
            return final
        elif type(other) == float:
            list1 = list(self)
            l = []
            final = self.clone()
            for each in list1:
                l.append(each * other)
                final._storage = l
            return final
        else:
            raise TypeError("Invalid Input")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other,Datum):
            list1 = list(self)
            list2 = list(other)
            final = self.clone()
            count1 = len(list1)
            count2 = len(list2)
            count3 = 0
            i = 0
            sub = 0
            l = []
            if count1 != count2:
                if count1 < count2:
                    count3 = count2 - count1
                    while i < count3:
                        list1.append(0.0)
                        i += 1
                if count2 < count1:
                    count3 = count1 - count2
                    while i < count3:
                        list2.append(0.0)
                        i += 1
                for val1, val2 in zip(list1, list2):
                    l.append(val1 / val2)
                final._storage = l
            return final
        elif type(other) == float:
            list1 = list(self)
            l = []
            final = self.clone()
            for each in list1:
                l.append(each / other)
                final._storage = l
            return final
        else:
            raise TypeError("Invalid Input")

    def helper(self,input):
        list1 = []
        dist1 = 0.0
        dist2 = 0.0
        sub = 0.0
        sub2 = 0.0
        if not isinstance(input,Datum):
            raise TypeError("Invalid Input")
        for each in  self:
            sub += each ** 2
        dist1 = math.sqrt(sub)
        for each in  input:
            sub2 += each ** 2
        dist2 = math.sqrt(sub2)
        list1.append(dist1)
        list1.append(dist2)
        return list1

    def __eq__(self, other):
        list1=self.helper(other)
        return list1[0] == list1[1]

    def __ne__(self, other):
        list1=self.helper(other)
        return list1[0] != list1[1]

    def __lt__(self, other):
        list1=self.helper(other)
        return list1[0] < list1[1]

    def __le__(self, other):
        list1=self.helper(other)
        return list1[0] <= list1[1]

    def __gt__(self, other):
        list1=self.helper(other)
        return list1[0] > list1[1]

    def __ge__(self, other):
        list1=self.helper(other)
        return list1[0] >= list1[1]

class Data(UserList):
    def __init__(self,var=None):
        list1 = []
        if var is None:
            super().__init__(list1)
        else:
            for each in var:
                if not isinstance(each,Datum):
                    raise TypeError("Invalid Input")
                else:
                    continue
            super().__init__(var)

    def helper2(self,tup,length):
        i = 0
        list1 = list(tup)
        diff = length - len(tup)
        if len(tup) != length:
            while i < diff:
                list1.append(0.0)
                i += 1
        return tuple(list1)

    def computeBounds(self):
        listx = list(self)
        length = 0
        list1=[]
        dict1 = defaultdict(str)
        for each in listx:
            if len(each) > length:
                length = len(each)
        for each in listx:
            final = self.helper2(each,length)
            list1.append(final)
        for each in list1:
            for counter2,each2 in enumerate(each):
                dict1[str(counter2)] += str(each2) + " "
        floatList = []
        min_list = []
        max_list = []
        for key in dict1:
            floatList = []
            value = dict1[key]
            value = value.split(" ")
            value = value[0:len(value) -1]
            for x in value:
                x = float(x)
                floatList.append(x)
            dict1[key] = floatList
        for each in dict1.values():
            for each2 in each:
                min_list.append(min(each))
                max_list.append(max(each))
                break
        min_tup = Datum(*min_list)
        max_tup = Datum(*max_list)
        final_tup = (min_tup,max_tup)
        return final_tup

    def computeMean(self):
        listx = list(self)
        length = 0
        list1 = []
        dict1 = defaultdict(str)
        for each in listx:
            if len(each) > length:
                length = len(each)
        for each in listx:
            final = self.helper2(each, length)
            list1.append(final)
        for each in list1:
            for counter2, each2 in enumerate(each):
                dict1[str(counter2)] += str(each2) + " "
        floatList = []
        list_final = []
        final_tup = tuple()
        for key in dict1:
            floatList = []
            value = dict1[key]
            value = value.split(" ")
            value = value[0:len(value) -1]
            for x in value:
                x = float(x)
                floatList.append(x)
            dict1[key] = floatList
        for each in dict1.values():
            avg = 0
            for each2 in each:
                avg = statistics.mean(each)
                list_final.append(avg)
                break
        final_tup = Datum(*list_final)
        return final_tup

    def append(self, item):
        if not isinstance(item, Datum):
            raise TypeError("Invalid Input")
        else:
            super().append(item)

    def count(self, item):
        if not isinstance(item, Datum):
            raise TypeError("Invalid Input")
        else:
            return super().count(item)

    def index(self, i: int, item):
        if not isinstance(item, Datum):
            raise TypeError("Invalid Input")
        else:
            return super().index(i,item)

    def insert(self, i: int, item):
        if not isinstance(item, Datum):
            raise TypeError("Invalid Input")
        else:
           return super().insert(i,item)

    def remove(self, item):
        if not isinstance(item, Datum):
            raise TypeError("Invalid Input")
        else:
            super().remove(item)

    def __setitem__(self, key,value):
        if not isinstance(value, Datum):
            raise TypeError("Invalid Input")
        else:
            super().__setitem__(key,value)

    def extend(self, item):
        if not isinstance(item, Datum):
            raise TypeError("Invalid Input")
        else:
            super().extend(item)


class DataClass(Enum):
    Class1 = 1
    Class2 = 2

class DataClassifier:
    def __init__(self,group1,group2):
        if not isinstance(group1,Data):
            raise TypeError("Invalid Input")
        if not isinstance(group2,Data):
            raise TypeError(" Invalid Input")
        if group1 is None and group2 is None:
            raise TypeError("group is empty")
        else:
            self._class1 = group1
            self._class2 = group2

    # def helper2(self, tup1,tup2):
    #     i = 0
    #     list1 = list(tup1)
    #     list2 = list(tup2)
    #     if len(tup1) < len(tup2):
    #         diff = len(tup2-tup1)
    #         while i < diff:
    #             list1.append(0.0)
    #             i += 1
    #         return tuple(list1)
    #     if len(tup2) < len(tup1):
    #         diff = len(tup1-tup2)
    #         while i < diff:
    #             list2.append(0.0)
    #             i += 1
    #         return tuple(list2)
    #
    # def distance(self,tup1,tup2):
    #     sub = 0
    #     list1 = list(tup1)
    #     list2 = list(tup2)
    #     for each,each2 in zip(list1,list2):
    #         sub += (each-each2)**2
    #     return math.sqrt(sub)
    #
    # def classify(self,input):
    #     point1 = self._class1
    #     point2 = self._class2
    #     new_tup = []
    #     final = 0
    #     final2 = 0
    #     for each in point1:
    #         hi= self.helper2(each,input)
    #         final += self.distance(hi,input)
    #     final = final / len(point1)
    #
    #     for each in point2:
    #         hi= self.helper2(each,input)
    #         final2 += self.distance(hi,input)
    #     final2 = final2 / len(point2)
    #
    #     if final < final2:
    #         return DataClass.Class1
    #     else:
    #         return DataClass.Class2


if __name__ == "__main__":
    a = Datum(1.2,12.3,42.12,314.56,67.54)
    print(a)
    # f = Datum(3.4,2.7,2.456,9.78,7.89,98.56)
    # g = (3.4, 2.7, 2.456, 9.78, 7.89, 98.56)
    # h = Datum(2.0,4.0,6.0,8.0)
    # i = Datum(2.0,4.0,6.0,8.0)
    b = a.distanceFrom((3.4,2.7,2.456,9.78,7.89,98.56))
    print(b)
    # #c = Datum.clone(a)
    # #print(c)
    # #d = Datum.__repr__(a)
    # #print(d)
    # print(1.2 in a)
    # #print(a.__len__())
    # #print(a.__iter__())
    # #print(a.__neg__())
    # #print(a.__getitem__(0))
    # print(a.__add__(f))
    # print(a.__sub__(.4))
    # print(a.__mul__(f))
    # print(a.__truediv__(2.0))
    # print(h.__eq__(i))
    # print(a.__ne__(f))
    # print(h.__lt__(i))
    # print(h.__le__(i))
    # print(h.__gt__(i))
    # print(h.__ge__(i))
    #
    # a1 = Datum(1.0,4.0,7.0)
    # b1 = Datum(6.0,3.0,4.0)
    # c1 = Datum(9.0,0.0,2.0)
    #
    # a2 = Datum(2.0, 2.0, 2.0)
    # b2 = Datum(4.0, 7.0, 8.0)
    # c2 = Datum(3.0, 1.0,2.4)
    #
    # list1 = [a1,b1,c1]
    # list2 = [a2, b2, c2]
    # d1 = Data(list1)
    # d5 = Data(list2)
    # #print(d1)
    # d2 = d1.computeBounds()
    # print(d2)
    # d3 = d1.computeMean()
    # print(d3)
    # e1 = Datum(3.5,4.2,2.7)
    # g1 = DataClassifier(d1,d5)
    # #print(g1.classify(e1))









