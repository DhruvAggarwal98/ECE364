#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <1/31/19>
#######################################################
import os      # List of  module  import  statements
import os.path

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('/home/ecegridfs/a/ee364/DataFolder/Prelab04')

def createDict(ReportName):
    report_file = os.path.join(DataPath + "/reports", ReportName)
    dict1 = dict()
    with open(report_file) as my_report_file:
        for j,lines in enumerate(my_report_file):
            if j >= 4:
                trial, virus, units = lines.split()
                if virus not in dict1:
                    dict1[virus] = int(units)
                elif virus in dict1:
                    dict1[virus] += int(units)
    return dict1
def createNameDict():
    virus_file = os.path.join(DataPath + "/maps", "viruses.dat")
    dict1 = dict()
    with open(virus_file) as my_virus_file:
        for j, lines in enumerate(my_virus_file):
            if j >= 2:
                name, id, cost = [x.strip() for x in lines.split("|")]
                dict1[id] = name
    return dict1

def createvirus_cost_Dict():
    virus_file = os.path.join(DataPath + "/maps", "viruses.dat")
    dict1 = dict()
    with open(virus_file) as my_virus_file:
        for j, lines in enumerate(my_virus_file):
            if j >= 2:
                name, id,cost = [x.strip() for x in lines.split("|")]
                cost = cost.replace("$","")
                dict1[id] = cost
    return dict1

def createTechDict():
    tech_file = os.path.join(DataPath + "/maps", "technicians.dat")
    dict1 = dict()
    with open(tech_file) as my_tech_file:
        for j, lines in enumerate(my_tech_file):
            if j >= 2:
                name, id = [x.strip() for x in lines.split("|")]
                dict1[id] = name
    return dict1

def getTechWork(techName):
    tech_file = os.path.join(DataPath + "/maps", "technicians.dat")
    virusDict = createNameDict()
    list1 = []
    dict2 = dict()
    dict3 = dict()
    list3 = []
    with open(tech_file) as my_tech_file:
        for i, line in enumerate(my_tech_file):
            if i >= 2:
                Name,Id = line.split("|")
                Id = Id.replace(" ", "")
                if techName.replace(" ","") == Name.replace(" ", ""):
                    Id = Id.replace("\n", "")
                    final_id = Id
    list = os.listdir(DataPath + "/reports")
    for i, each_file in enumerate(list):
        report_file = os.path.join(DataPath + "/reports",each_file)
        with open(report_file) as my_report_file:
            for j,lines in enumerate(my_report_file):
                if j == 0:
                    User, number = lines.split(":")
                    number = number.replace(" ", "")
                    temp_id = number.replace("\n", "")
                if temp_id != final_id:
                    break
                else:
                    if each_file not in list1:
                        list1.append(each_file)
    for i, each_file in enumerate(list1):
        list3.append(createDict(each_file))
    for x in list3:
        for y in x:
            if y not in dict2:
                dict2[y] = 0
            dict2[y] += x[y]
    for key in dict2:
        dict3[virusDict[key]] = dict2[key]
    return dict3

def getStrainConsumption(virusName):
    tech_dict = createTechDict()
    virus_dict = createNameDict()
    final_dict = {}
    list = os.listdir(DataPath + "/reports")
    for i, each_file in enumerate(list):
        report_file = os.path.join(DataPath + "/reports", each_file)
        with open(report_file) as my_report_file:
            for j, lines in enumerate(my_report_file):
                if j == 0:
                    User, number = [x.strip() for x in lines.split(":")]
                    temp_id = tech_dict[number]
                elif j >= 4:
                    trial,virus,units = [x.strip() for x in lines.split()]
                    if virus_dict[virus] == virusName:
                        if temp_id not in final_dict:
                            final_dict[temp_id] = 0
                        final_dict[temp_id] += int(units)
    return final_dict

def getTechSpending():
    tech_dict = createTechDict()
    new_dict = dict()
    final_dict = dict()
    virus_dict = createNameDict()
    virus_cost_dict = createvirus_cost_Dict()
    list = os.listdir(DataPath + "/reports")
    for i, each_file in enumerate(list):
        report_file = os.path.join(DataPath + "/reports", each_file)
        with open(report_file) as my_report_file:
            for j, lines in enumerate(my_report_file):
                if j == 0:
                    User, number = [x.strip() for x in lines.split(":")]
                    temp_id = tech_dict[number]
                elif j >= 4:
                    trial, virus, units = [x.strip() for x in lines.split()]
                    new_dict[virus] = int(units)
                    if temp_id not in final_dict:
                        final_dict[temp_id] = 0
                    final_dict[temp_id] += int(units) * float(virus_cost_dict[virus])
    for key in final_dict:
        final_dict[key] = round(final_dict[key],2)
    return final_dict

def getStrainCost():
    virus_dict = createNameDict()
    virus_cost_dict = createvirus_cost_Dict()
    new_dict = dict()
    final_dict = dict()
    list = os.listdir(DataPath + "/reports")
    for i, each_file in enumerate(list):
        report_file = os.path.join(DataPath + "/reports", each_file)
        with open(report_file) as my_report_file:
            for j, lines in enumerate(my_report_file):
                if j >= 4:
                    trial, virus, units = [x.strip() for x in lines.split()]
                    virus_id = virus_dict[virus]
                    new_dict[virus_id] = int(units)
                    if virus_id not in final_dict:
                        final_dict[virus_id] = 0
                    final_dict[virus_id] += int(units) * float(virus_cost_dict[virus])
    for key in final_dict:
        final_dict[key] = round(final_dict[key], 2)
    return final_dict

def getAbsentTechs():
    dict1 = createTechDict()
    list = os.listdir(DataPath + "/reports")
    set1 = set()
    for i, each_file in enumerate(list):
        report_file = os.path.join(DataPath + "/reports", each_file)
        with open(report_file) as my_report_file:
            for j, lines in enumerate(my_report_file):
                if j == 0:
                    User, number = lines.split(":")
                    number = number.replace(" ", "")
                    temp_id = number.replace("\n", "")
                    if temp_id in dict1:
                        del dict1[temp_id]
                        break
                    break
    for key in dict1:
        set1.add(dict1[key])
    return set1

def getUnusedStrains():
    dict1 = createNameDict()
    list = os.listdir(DataPath + "/reports")
    set1 = set()
    for i, each_file in enumerate(list):
        report_file = os.path.join(DataPath + "/reports", each_file)
        with open(report_file) as my_report_file:
            for j, lines in enumerate(my_report_file):
                if j >= 4:
                    trial, virus, cost = lines.split()
                    virus = virus.replace(" ", "")
                    if virus in dict1:
                        del dict1[virus]
                        break
                    break
    for key in dict1:
        set1.add(dict1[key])
    return set1

if __name__ == "__main__":
    # # TEST FUNCTION 1
    print("**************FUNCTION 1**************")
    test1 = getTechWork("Morris, Heather")
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 2
    print("**************FUNCTION 2**************")
    test1 = getStrainConsumption("Mupapillomavirus")
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 3
    print("**************FUNCTION 3**************")
    test1 = getTechSpending()
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 4
    print("**************FUNCTION 4**************")
    test1 = getStrainCost()
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 5
    print("**************FUNCTION 5**************")
    test1 = getAbsentTechs()
    print(test1)
    print("**************************************\n")
    # # TEST FUNCTION 6
    print("**************FUNCTION 6**************")
    test1 = getUnusedStrains()
    print(test1)
    print("**************************************\n")