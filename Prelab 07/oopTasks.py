#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <2/20/19>
#######################################################
import os      # List of  module  import  statements
import os.path
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

from enum import Enum

class Level(Enum):
    Freshman = "Freshman"
    Sophomore = "Sophomore"
    Junior = "Junior"
    Senior = "Senior"

class ComponentType(Enum):
    Resistor = "Resistor"
    Capacitor = "Capacitor"
    Inductor = "Inductor"
    Transistor = "Transistor"

class Student:
    ID = str
    firstName = str
    lastName = str
    level = Level
    def __init__(self,ids,fn,ln,l):
        self.ID = ids
        self.firstName = fn
        self.lastName = ln
        self.level = l
        if type(self.level) is not Level:
            raise TypeError("The level must be an instance of the 'Level'. Enum.")
    def __str__(self):
        return self.ID + "," + " " +self.firstName +" "+ self.lastName + "," + " "+ self.level._value_

class Component:
    ID = str
    ctype = ComponentType
    price = float

    def __init__(self,ids,ct,p):
        self.ID = ids
        self.ctype= ct
        self.price= p

        if type(self.ctype) is not ComponentType:
            raise TypeError("The component type must be an instance of the 'Component'. Enum.")

    def __str__(self):
        return self.ctype._value_ + "," + " " +self.ID +","+" " + "${:.2f}".format(self.price)

    def __hash__(self):
        return hash(self.ID)

class Circuit:
    ID = str
    components = set()
    cost = float
    dict1 = {}
    count = 0

    def __init__(self,ids,comp,ct):
        self.ID = ids
        self.components = comp
        self.cost = ct
    for each in components:
        dict1[each] = count
        count += 1


        # if type(self.components) is not ComponentType:
        #     raise TypeError("The component type must be an instance of the 'Component'. Enum.")

    def __str__(self):
        return str(self.ID) + ":" + " " + str(self.components) + "," + " Cost = $"


 # class Capstone(Project):
    #     def __init__(self, *args, **kwargs):
    #         print(args)
    #         print(kwargs)
    #         args = [v for v in kwargs.values()]
    #         if type(args[0]) is Project:
    #             # self.circuits = args[0].circuits
    #             # self.participants = args[0].participants
    #             # self.ID = args[0].ID
    #             print(args[0])
    #             Project.__init__(self, args[0].ID, args[0].participants, args[0].circuits)
    #             for student in self.participants:
    #                 if student.level.name != 'Senior':
    #                     raise ValueError('not senior')
    #         else:
    #             print(args)
    #             Project.__init__(self, args[0], args[1], args[2])
    #             for student in self.participants:
    #                 if student.level.name != 'Senior':
    #                     raise ValueError('not senior')

if __name__ == "__main__":
    print(Student("0028896590", "Dhruv","Aggarwal", Level.Junior))
    print(Component( "REW-321",ComponentType.Resistor, 1.40))
    print(hash("REW-321"))
    print(Circuit("01",{ComponentType.Resistor,ComponentType.Capacitor},1.3))
    


