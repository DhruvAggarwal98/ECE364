#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <1/22/19>
#######################################################
import os      # List of  module  import  statements
import os.path

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('/home/ecegridfs/a/ee364/DataFolder/Prelab03')

def convert_comp_to_file(componentSymbol):
    if componentSymbol == "R":
        file_name = "resistors.dat"
    elif componentSymbol == "I":
        file_name = "inductors.dat"
    elif componentSymbol == "C":
        file_name = "capacitors.dat"
    elif componentSymbol == "T":
        file_name = "transistors.dat"
    else:
        raise ValueError("Wrong Component Symbol")
    return file_name

def getComponentCountByProject(projectID, componentSymbol):
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    list_of_circuits = []
    check_list = []
    with open(project_file) as my_project_file:
        for i, line1 in enumerate(my_project_file):
            if i >= 2:
                new_line1 = line1.split()
                check_list.append(new_line1[1])
                if projectID not in check_list:
                    raise ValueError("Wrong Project ID, Try again!")
                for j, each in enumerate(new_line1):
                    if each == projectID:
                        list_of_circuits.append(new_line1[0])
                i = i + 1
            else:
                i = i + 1
    counter = 0
    test_list =[]
    file_name = convert_comp_to_file(componentSymbol)
    project_file = os.path.join(DataPath + "/maps", file_name)
    with open(project_file) as my_project_file:
        for i, line1 in enumerate(my_project_file):
            if i >= 3:
                new_line1 = line1.split()
                for a, object in enumerate(list_of_circuits):
                    circuit_file = os.path.join(DataPath + "/circuits","circuit_" + object + ".dat")
                    with open(circuit_file) as my_circuit_file:
                        for j, line2 in enumerate(my_circuit_file):
                            line2 = line2.replace("\n","")
                            line2 = line2.replace("  ", "")
                            if line2 == new_line1[0]:
                                if line2 in test_list:
                                    continue
                                else:
                                    test_list.append(line2)
                                j = j + 1
                            else:
                                j = j + 1
                i = i + 1
            else:
                i = i + 1
    return len(test_list)

def getComponentCountByStudent(studentName, componentSymbol):
    project_file = os.path.join(DataPath + "/maps", "students.dat")
    studentName = studentName.replace(" ", "")
    test_list = []
    check_list = []
    with open(project_file) as my_project_file:
        for i, line1 in enumerate(my_project_file):
            if i >= 2:
                new_line1 = line1.split("|")
                new_line1[0] = new_line1[0].replace(" ", "")
                new_line1[1] = new_line1[1].replace(" ", "")
                new_line1[1] = new_line1[1].replace("\n","")
                check_list.append(new_line1[0])
                if studentName not in check_list:
                    raise ValueError("Wrong Student Name, Try again!")
                if new_line1[0] == studentName:
                    final_id = new_line1[1]
                i = i + 1
            else:
                i = i + 1
    file_name = convert_comp_to_file(componentSymbol)
    circuit_file = os.path.join(DataPath + "/maps", file_name)
    list = os.listdir(DataPath+"/circuits")
    for i,each in enumerate(list):
        project_file = os.path.join(DataPath + "/circuits", each)
        with open(project_file) as my_project_file:
            for j, line1 in enumerate(my_project_file):
                line1 = line1.replace("\n","")
                if line1 != final_id:
                    j = j + 1
                else:
                    my_project_file.seek(0)
                    for k, line2 in enumerate(my_project_file):
                        line2 = line2.replace(" ", "")
                        line2 = line2.replace("\n", "")
                        with open(circuit_file) as my_circuit_file:
                            for l, object in enumerate(my_circuit_file):
                                objects = object.split()
                                objects[0] = objects[0].replace(" ", "")
                                objects[0] = objects[0].replace("\n", "")
                                if line2 == objects[0]:
                                    if line2 in test_list:
                                        continue
                                    else:
                                        test_list.append(line2)
                    j = j + 1
    return len(test_list)

def getParticipationByStudent(studentName):
    project_file = os.path.join(DataPath + "/maps", "students.dat")
    studentName = studentName.replace(" ", "")
    list1 = []
    check_list = []
    test_set = set()
    with open(project_file) as my_project_file:
        for i, line1 in enumerate(my_project_file):
            if i >= 2:
                new_line1 = line1.split("|")
                new_line1[0] = new_line1[0].replace(" ", "")
                new_line1[1] = new_line1[1].replace(" ", "")
                new_line1[1] = new_line1[1].replace("\n", "")
                check_list.append(new_line1[0])
                if studentName not in check_list:
                    raise ValueError("Wrong Student Name, Try again!")
                if new_line1[0] == studentName:
                    final_id = new_line1[1]
                i = i + 1
            else:
                i = i + 1
    list = os.listdir(DataPath + "/circuits") # GO through all the circuit files
    for i, each in enumerate(list):
        project_file = os.path.join(DataPath + "/circuits", each)
        with open(project_file) as my_project_file: #open all circuit files
            for j, line1 in enumerate(my_project_file):
                line1 = line1.replace("\n","")
                if final_id == line1:
                    each = each.split("_")
                    each[1] = each[1].replace(".dat", "")
                    list1.append(each[1])
                    j = j + 1
                else:
                    j = j + 1
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    with open(project_file) as my_project_file:
        for i, each in enumerate(my_project_file):
            new = each.split()
            new[0] = new[0].replace(" ","")
            for j, objects in enumerate(list1):
                if objects == new[0]:
                    test_set.add(new[1])
    return test_set

def getParticipationByProject(projectID):
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    list_of_circuits = []
    test_set = set()
    check_list = []
    with open(project_file) as my_project_file:
        for i, line1 in enumerate(my_project_file):
            if i >= 2:
                new_line1 = line1.split()
                check_list.append(new_line1[1])
                if projectID not in check_list:
                    raise ValueError("Wrong Project ID, Try again!")
                for j, each in enumerate(new_line1):
                    if each == projectID:
                        list_of_circuits.append(new_line1[0])
                i = i + 1
            else:
                i = i + 1
    for a, objects in enumerate(list_of_circuits):
        circuit_file = os.path.join(DataPath + "/circuits", "circuit_" + objects + ".dat")
        student_file = os.path.join(DataPath + "/maps", "students.dat")
        with open(student_file) as my_student_file:
            with open(circuit_file) as my_circuit_file:
                for b, part in enumerate(my_circuit_file):
                    part = part.replace("\n", "")
                    my_student_file.seek(0)
                    for c, value in enumerate(my_student_file):
                        if c >= 2:
                            values = value.split("|")
                            values[0] = values[0].replace(" ", "")
                            values[1] = values[1].replace(" ", "")
                            values[1] = values[1].replace("\n", "")
                            if part == values[1]:
                                values[0] = values[0].replace(",", ", ")
                                test_set.add(values[0])
                            c = c + 1
                        else:
                            c = c + 1
    return test_set

def getCostOfProjects():
    list_files = ["resistors.dat", "capacitors.dat", "inductors.dat", "transistors.dat"]
    dict1 = dict()
    valuelist = []
    list2 = []
    dict2 = dict()
    dict3 = dict()
    for file in list_files:
        each_file = os.path.join(DataPath + "/maps", file)
        with open(each_file) as my_each_file:
            for i, each in enumerate(my_each_file):
                if i >= 3:
                    compName, price = each.split()
                    dict1[compName] = float(price.replace("$", ""))
                else:
                    i += 1
    list = os.listdir(DataPath + "/circuits")
    for j, each in enumerate(list):
        circuit_file = os.path.join(DataPath + "/circuits", each)
        with open(circuit_file) as my_circuit_file:
            my_circuit_file.seek(0)
            for k, values in enumerate(my_circuit_file):
                values = values.strip()
                valuelist.append(values)
            index1 = valuelist.index("Components:")
            my_circuit_file.seek(0)
            cost = 0
            new = each.split("circuit_")
            new[1] = new[1].replace(".dat", "")
            for d, e in enumerate(my_circuit_file):
                if d >= index1:
                    if e.strip() in dict1:
                        cost += dict1[e.strip()]
                else:
                    d = d + 1
            dict2[new[1]] = cost
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    with open(project_file) as my_project_file:
        my_project_file.readline()
        my_project_file.readline()
        for projects in my_project_file:
            circuit, projectId = projects.split()
            if projectId not in dict3:
                dict3[projectId] = 0
            dict3[projectId] += dict2[circuit]
    for key in dict3:
        dict3[key] = round(dict3[key],2)
    return dict3

def getProjectByComponent(componentIDs):
    list = os.listdir(DataPath + "/circuits")
    list1 = []
    test_set = set()
    for j, each in enumerate(list):
        circuit_file = os.path.join(DataPath + "/circuits", each)
        with open(circuit_file) as my_circuit_file:
            my_circuit_file.seek(0)
            for k, values in enumerate(my_circuit_file):
                values = values.replace("\n","")
                values = values.replace(" ", "")
                for l, objects in enumerate(componentIDs):
                    if objects == values:
                        final = each.split("_")
                        final[1] = final[1].replace(".dat", "")
                        list1.append(final[1])
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    with open(project_file) as my_project_file:
        my_project_file.seek(0)
        for i, each in enumerate(my_project_file):
            if i >= 2:
                new = each.split()
                if new[0] in list1:
                    test_set.add(new[1])
                i = i + 1
            else:
                i = i + 1
    return test_set

def getCommonByProject(projectID1, projectID2):
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    valuelist = []
    check_list = []
    with open(project_file) as my_project_file:
        for j, each in enumerate(my_project_file):
            if j >= 2:
                new = each.split()
                check_list.append(new[1])
                if new[1] == projectID1:
                    list1.append(new[0])
                if new[1] == projectID2:
                    list2.append(new[0])
            else:
                j = j + 1
        if projectID1 not in check_list:
            raise ValueError("Wrong Project ID1, Try again!")
        if projectID2 not in check_list:
            raise ValueError("Wrong Project ID2, Try again!")
    for a, objects in enumerate(list1):
        circuit_file = os.path.join(DataPath + "/circuits", "circuit_" + objects + ".dat")
        with open(circuit_file) as my_circuit_file:
            for b, c in enumerate(my_circuit_file):
                c = c.replace("\n","")
                valuelist.append(c)
            index1 = valuelist.index("Components:")
            my_circuit_file.seek(0)
            for d,e in enumerate(my_circuit_file):
                if d >= index1:
                    e = e.replace("\n","")
                    e = e.replace(" ", "")
                    if e not in list3:
                        if e != "-------------" and e!= "Components:":
                            list3.append(e)
                else:
                    d = d + 1
    for a, objects in enumerate(list2):
        circuit_file = os.path.join(DataPath + "/circuits", "circuit_" + objects + ".dat")
        with open(circuit_file) as my_circuit_file:
            for b, c in enumerate(my_circuit_file):
                c = c.replace("\n","")
                valuelist.append(c)
            index1 = valuelist.index("Components:")
            my_circuit_file.seek(0)
            for d,e in enumerate(my_circuit_file):
                if d >= index1:
                    e = e.replace("\n","")
                    e = e.replace(" ", "")
                    if e not in list4:
                        if e!= "-------------" and e!= "Components:" and e != "" :
                            list4.append(e)
                else:
                    d = d + 1
    for i, each in enumerate(list3):
        for j, objects in enumerate(list4):
            if each == objects:
                if each not in list5:
                    list5.append(each)
    return sorted(list5)

def getComponentReport(componentIDs):
    list = os.listdir(DataPath + "/circuits")
    dict1 = dict()
    dict2 = dict()
    counter = 0
    valuelist = []
    list2 = []
    counter = 0
    project_file = os.path.join(DataPath + "/maps", "projects.dat")
    with open(project_file) as my_project_file:
        for i, each in enumerate(my_project_file):
            if i >= 2:
                values, key = each.rstrip('\n').split()
                if (dict1.get(key, 'N/A') == 'N/A'):
                    dict1[key] = []
                dict1[key].append(values)
                i = i + 1
            else:
                i = i + 1
    for key in dict1:
        for i in dict1[key]:
            circuit_name = "circuit_" + i + ".dat"
            circuit_file = os.path.join(DataPath + "/circuits", circuit_name)
            with open(circuit_file) as my_circuit_file:
                for j,each in enumerate(my_circuit_file):
                    each = each.replace("\n", "")
                    valuelist.append(each)
                index1 = valuelist.index("Components:")
                my_circuit_file.seek(0)
                for d, e in enumerate(my_circuit_file):
                    if d >= index1:
                        e = e.replace("\n", "")
                        e = e.replace(" ", "")
                        if e != "-------------":
                            list2.append(e)
                    else:
                        d = d + 1
    for i, comp_id in enumerate(componentIDs):
        counter = 0
        for j, test in enumerate(list2):
            if test == comp_id:
                counter = counter + 1
            dict2[comp_id] = counter
    return dict2

def getCircuitByStudent(studentNames):
    project_file = os.path.join(DataPath + "/maps", "students.dat")
    test_set = set()
    final_id = []
    with open(project_file) as my_project_file:
        for j,each in enumerate(studentNames):
            studentName = each.replace(" ", "")
            my_project_file.seek(0)
            for i, line1 in enumerate(my_project_file):
                if i >= 2:
                    new_line1 = line1.split("|")
                    new_line1[0] = new_line1[0].replace(" ", "")
                    new_line1[1] = new_line1[1].replace(" ", "")
                    new_line1[1] = new_line1[1].replace("\n", "")
                    if new_line1[0] == studentName:
                        final_id.append(new_line1[1])
                        break
                    i = i + 1
                else:
                    i = i + 1
    list = os.listdir(DataPath + "/circuits")
    for j, each in enumerate(list):
        project_file = os.path.join(DataPath + "/circuits", each)
        with open(project_file) as my_project_file:
            my_project_file.seek(0)
            for k, values in enumerate(my_project_file):
                values = values.replace("\n", "")
                values = values.replace(" ", "")
                for i, objects in enumerate(final_id):
                    if objects == values:
                        final = each.split("_")
                        final[1] = final[1].replace(".dat", "")
                        test_set.add(final[1])
    return test_set

def getCircuitByComponent(componentIDs):
    list = os.listdir(DataPath + "/circuits")
    test_set = set()
    for j, each in enumerate(list):
        project_file = os.path.join(DataPath + "/circuits", each)
        with open(project_file) as my_project_file:
            my_project_file.seek(0)
            for k, values in enumerate(my_project_file):
                values = values.replace("\n","")
                values = values.replace(" ", "")
                for i, objects in enumerate(componentIDs):
                    if objects == values:
                        final = each.split("_")
                        final[1] = final[1].replace(".dat", "")
                        test_set.add(final[1])
    return test_set

if __name__ == "__main__":
    # # TEST FUNCTION 1
    print("**************FUNCTION 1**************")
    test1 = getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "R")
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 2
    print("**************FUNCTION 2**************")
    test1 = getComponentCountByStudent("Adams, Keith", "R")
    test2 = getComponentCountByStudent("Adams, Keith", "I")
    test3 = getComponentCountByStudent("Adams, Keith", "T")
    test4 = getComponentCountByStudent("Adams, Keith", "C")
    print(test1)
    print(test2)
    print(test3)
    print(test4)
    print("**************************************\n")
    # TEST FUNCTION 3
    print("**************FUNCTION 3**************")
    test1 = getParticipationByStudent("Adams, Keith")
    print(test1)
    print("**************************************\n")
    # TEST FUNCTION 4
    print("**************FUNCTION 4**************")
    test1 = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    print(test1)
    print("**************************************\n")
    # TEST FUNCTION 5
    print("**************FUNCTION 5**************")
    getCostOfProjects()
    print("**************************************\n")
    # # TEST FUNCTION 6
    print("**************FUNCTION 6**************")
    test1 = getProjectByComponent({"BLL-583","GLZ-901"})
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 7
    print("**************FUNCTION 7**************")
    test1 = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "082D6241-40EE-432E-A635-65EA8AA374B6")
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 8
    print("**************FUNCTION 8**************")
    test1 = getComponentReport({'BKC-326', 'ECI-702', 'YKC-827', 'CIW-539'})
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 9
    print("**************FUNCTION 9**************")
    print(getCircuitByStudent({"Bell, Kathryn", "Scott, Michael"}))
    print("**************************************\n")
    # TEST FUNCTION 10
    print("**************FUNCTION 10*************")
    test1 = getCircuitByComponent({"TCH-815"})
    print(test1)
    print("**************************************\n")

