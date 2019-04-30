#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <2/15/19>
#######################################################
import os      # List of  module  import  statements
import os.path
import re
from uuid import UUID
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('/home/ecegridfs/a/ee364/DataFolder/Prelab06')

def getUrlParts(url):
    tup = re.search(r'http://([^/]+)/([^/]+)/([^?]+)',url)
    return tup.groups()

def getQueryParameters(url):
    newurl = (re.findall(r'(?<=\?)[^\]]+',url))
    final= "".join(newurl)
    return re.findall(r'([^=]+)=([^&]+)[&]*', final)

def getSpecial(sentence, letter):
    list1 = []
    list_of_words = re.findall(r'(\w+\s+)',sentence)
    #list_of_words = sentence.split()
    #print(list_of_words)
    for each in list_of_words:
        list1.extend(re.findall(r'\b[{}{}]\w*[^{}{}]\b'.format(letter.upper(), letter.lower(), letter.upper(), letter.lower()), each))
        list1.extend(re.findall(r'\b[^{}{}]\w*[{}{}]\b'.format(letter.upper(), letter.lower(), letter.upper(), letter.lower()), each))
    return list1

def getRealMAC(sentence):
    pattern1 = r'(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)'
    pattern2 = r'(\w\w-\w\w-\w\w-\w\w-\w\w-\w\w)'
    match1 = re.findall(pattern1,sentence)
    match2 = re.findall(pattern2,sentence)
    if len(match1) == 0 and len(match2) == 0:
        return None
    return "".join(match1 or match2)

def getRejectedEntries():
    employee_file = os.path.join(DataPath + "/Employees.txt")
    list1 = []
    with open(employee_file) as my_employee_file:
        for j, lines in enumerate(my_employee_file):
            pattern = r'(;+)'
            match = re.findall(pattern,lines)
            if len(match) == 8:
                pattern2 = r'(\w+)'
                match2 = re.findall(pattern2,lines)
                if len(match2) == 2:
                    list1.append(" ".join(match2))
    return sorted(list1)

def getEmployeesWithIDs():
    employee_file = os.path.join(DataPath + "/Employees.txt")
    dict1 = {}
    with open(employee_file) as my_employee_file:
        for j, lines in enumerate(my_employee_file):
            pattern = r'([^a-zA-Z{}0-9-\s])'
            cleaned = re.sub(pattern,"",lines)
            cleaned = cleaned.split()
            #cleaned = re.findall(r'(.*?)(?:[,;\s])',cleaned)
            if len(cleaned) > 2:
                if len(cleaned[2])==32 or len(cleaned[2]) == 36 or len(cleaned[2]) == 38:
                    id = UUID(cleaned[2])
                    name = cleaned[0] + " "+ cleaned[1]
                    dict1[name] = id.__str__()
    return (dict1)

def getEmployeesWithoutIDs():
    employee_file = os.path.join(DataPath + "/Employees.txt")
    list1 = []
    with open(employee_file) as my_employee_file:
        for j, lines in enumerate(my_employee_file):
            pattern = r'([^a-zA-Z{}0-9-\s])'
            cleaned = re.sub(pattern, "", lines)
            cleaned = cleaned.split()
            #cleaned = re.findall(r'(.*?)(?:[,;\s])', cleaned)
            if len(cleaned) > 2:
                if len(cleaned[2]) != 32 and len(cleaned[2]) != 36 and len(cleaned[2]) != 38:
                    name = cleaned[0] + " "+ cleaned[1]
                    list1.append(name)
    return sorted(list1)

def help_number(orig):
    if len(orig) == 10:
        return "("+orig[0]+orig[1]+orig[2]+")"+ " "+orig[3]+orig[4]+orig[5]+"-"+ orig[6]+orig[7]+orig[8]+orig[9]

def getEmployeesWithPhones():
    employee_file = os.path.join(DataPath + "/Employees.txt")
    dict1 = {}
    with open(employee_file) as my_employee_file:
        for j, lines in enumerate(my_employee_file):
            cleaned = re.sub(r'([^a-zA-Z{}0-9-\s])', "", lines).split()
            if len(cleaned) > 2 and len(cleaned) <= 3:
                if len(cleaned[2]) == 12 or len(cleaned[2]) == 10 or len(cleaned[2]) == 14:
                    cleaned[2] = re.sub(r'-',"",cleaned[2])
                    cleaned[2] = re.sub(r'\(', "", cleaned[2])
                    cleaned[2] = re.sub(r'\)', "", cleaned[2])
                    if re.match(r'^[0-9]*$', cleaned[2]):
                        number = help_number(cleaned[2])
                        name = cleaned[0] + " " + cleaned[1]
                        dict1[name] = number.__str__()
                if len(cleaned[2]) == 3:
                    if re.match(r'[0-9]*$',cleaned[2]):
                        orig = cleaned[2] + cleaned[3]
                        orig = re.sub(r'-',"",orig)
                        number = help_number(orig)
                        name = cleaned[0] + " " + cleaned[1]
                        dict1[name] = number.__str__()
            if len(cleaned) > 3:
                for i, each in enumerate(cleaned):
                    if len(cleaned[i]) == 12 or len(cleaned[i]) == 10 or len(cleaned[i]) == 14:
                        cleaned[i] = re.sub(r'-', "", cleaned[i])
                        cleaned[i] = re.sub(r'\(', "", cleaned[i])
                        cleaned[i] = re.sub(r'\)', "", cleaned[i])
                        if re.match(r'^[0-9]*$', cleaned[i]):
                            number = help_number(cleaned[i])
                            name = cleaned[0] + " " + cleaned[1]
                            dict1[name] = number.__str__()
                    if len(cleaned[i]) == 3:
                        if re.match(r'^[0-9]*$', cleaned[i]):
                            orig = cleaned[i] + cleaned[i+1]
                            orig = re.sub(r'-', "", orig)
                            number = help_number(orig)
                            name = cleaned[0] + " " + cleaned[1]
                            dict1[name] = number.__str__()
    return (dict1)
def getEmployeesWithStates():
    employee_file = os.path.join(DataPath + "/Employees.txt")
    dict1 = {}
    with open(employee_file) as my_employee_file:
        for j, lines in enumerate(my_employee_file):
            cleaned = re.sub(r'([^a-zA-Z{}0-9-\s])', "", lines).split()
            if len(cleaned) == 3:
                if re.match(r'^[a-zA-Z]*$', cleaned[2]):
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = cleaned[2]
            if len(cleaned) == 4:
                if re.match(r'^[a-zA-Z]*$', cleaned[2]) and re.match(r'^[a-zA-Z]*$', cleaned[3]):
                    state = cleaned[2] + " " + cleaned[3]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
                elif re.match(r'^[a-zA-Z]*$', cleaned[3]):
                    state = cleaned[3]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
            if len(cleaned) == 5:
                if re.match(r'^[a-zA-Z]*$', cleaned[3]) and re.match(r'^[a-zA-Z]*$', cleaned[4]):
                    state = cleaned[3] + " " + cleaned[4]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
                elif re.match(r'^[a-zA-Z]*$', cleaned[4]):
                    state = cleaned[4]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
            if len(cleaned) == 6:
                if re.match(r'^[a-zA-Z]*$', cleaned[4]) and re.match(r'^[a-zA-Z]*$', cleaned[5]):
                    state = cleaned[4] + " " + cleaned[5]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
                elif re.match(r'^[a-zA-Z]*$', cleaned[5]):
                    state = cleaned[5]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
            if len(cleaned) == 7:
                if re.match(r'^[a-zA-Z]*$', cleaned[5]) and re.match(r'^[a-zA-Z]*$', cleaned[6]):
                    state = cleaned[5] + " " + cleaned[6]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
                elif re.match(r'^[a-zA-Z]*$', cleaned[6]):
                    state = cleaned[6]
                    name = cleaned[0] + " " + cleaned[1]
                    dict1[name] = state
    return (dict1)

def getCompleteEntries():
    dict1 = getEmployeesWithIDs()
    dict2 = getEmployeesWithPhones()
    dict3 = getEmployeesWithStates()
    dict4 = {}
    list1 = []
    for key in dict1:
        if key not in dict2:
            continue
        elif key not in dict3:
            continue
        else:
            list1 = []
            list1.append(str(dict1[key]))
            list1.append(str(dict2[key]))
            list1.append(str(dict3[key]))
            tup = tuple(list1)
            dict4[key] = tup
    return dict4

def test1(string):
    return re.search(r'(?:[http://])([^/]+)/([^/]+)/([^?]+)',string).groups()

def test2(string):
    return re.findall(r'[^?]+[^=]+',string)



if __name__ == "__main__":
    print(getUrlParts("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    print(getQueryParameters("http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"))
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    print(getSpecial(s,"t"))
    print(getRealMAC("Tuesdays and 000-38-38-29-10-A699tj hi"))
    print(getRejectedEntries())
    print(getEmployeesWithIDs())
    print(getEmployeesWithoutIDs())
    print(getEmployeesWithPhones())
    print(getEmployeesWithStates())
    print(getCompleteEntries())
    print(test1("http://www.purdue.edu/Home/Calendar?Year=2016&Month=September&Semester=Fall"))
    print(test2("http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"))