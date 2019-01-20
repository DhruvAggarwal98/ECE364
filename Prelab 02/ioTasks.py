#######################################################
#    Author:      <Dhruv Aggarwal >
#    email:       <aggarw45@purdue.edu>
#    ID:           <ee364d01 >
#    Date:         <1/15/19>
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser('/home/ecegridfs/a/ee364/DataFolder/Prelab02')

def getMaxDifference(symbol):
    full_name = symbol + ".dat"
    file = os.path.join(DataPath, full_name)
    current = 0
    with open(file) as myfile:
        for i, line in enumerate(myfile):
            if i >= 2:
                date, close, volume, opens, high, low = line.rsplit(",")
                difference = float(high) - float(low)
                if difference > current:
                    current = difference
                    final_date = date
                i += 1
            else:
                i += 1
    return final_date

def getGainPercent(symbol):
    full_name = symbol + ".dat"
    file = os.path.join(DataPath, full_name)
    counter = 0
    with open(file) as myfile:
        for i, line in enumerate(myfile):
            if i >= 2:
                date, close, volume, opens, high, low = line.rsplit(",")
                if float(close) > float(opens):
                    counter += 1
                i += 1
            else:
                i += 1
    final = (counter / (i-2)) * 100
    return round(final,4)

def getVolumeSum(symbol, date1, date2):
    full_name = symbol + ".dat"
    file = os.path.join(DataPath, full_name)
    tran = 0
    if date1 >= date2:
        return
    else:
        with open(file) as myfile:
            for i, line in enumerate(myfile):
                if i >= 2:
                    date, close, volume, opens, high, low = line.rsplit(",")
                    if date1 <= date <= date2:
                        tran += float(volume)
                    i += 1
                else:
                    i += 1
    return int(tran)

def getBestGain(date):
    dirs = os.listdir(DataPath)
    temp = 0
    for file in dirs:
        files = os.path.join(DataPath, file)
        with open(files) as myfile:
            for i, line in enumerate(myfile):
                if i >= 2:
                    check_date, close, volume, opens, high, low = line.rsplit(",")
                    if check_date == date:
                        gain = ((float(close) - float(opens))/float(opens)) * 100
                        if gain > temp:
                            temp = gain
                            final_gain = gain
                    i += 1
                else:
                    i += 1
    return round(final_gain,4)

def getAveragePrice(symbol, year):
    full_name = symbol + ".dat"
    file = os.path.join(DataPath, full_name)
    counter = 0
    year_avg = 0
    with open(file) as myfile:
        for i, line in enumerate(myfile):
            if i >= 2:
                date, close, volume, opens, high, low = line.rsplit(",")
                check_year, month, day = date.split("/")
                if year == int(check_year):
                    day_avg = (float(close) + float(opens)) / 2
                    year_avg += day_avg
                    counter += 1
                i += 1
            else:
                i += 1
        final = round(year_avg/counter,4)
    return final

def getCountOver(symbol, price):
    price = float(price)
    full_name = symbol + ".dat"
    file = os.path.join(DataPath, full_name)
    counter = 0
    with open(file) as myfile:
        for i, line in enumerate(myfile):
            if i >= 2:
                date, close, volume, opens, high, low = line.rsplit(",")
                if float(opens) >= price and float(close) >= price and float(low) >= price and float(high) >= price:
                    counter += 1
                i += 1
            else:
                i += 1
    return counter

if __name__ == "__main__":
    #TEST FUNCTION 1
    print("*******FUNCTION 1 ***********")
    test1 = getMaxDifference("AAPL")
    print(test1)
    print("***************************************\n")
    # TEST FUNCTION 2
    print("*******FUNCTION 2 ***********")
    test1 = getGainPercent("AAPL")
    print(test1)
    print("***************************************\n")
    # TEST FUNCTION 3
    print("*******FUNCTION 3 ***********")
    test1 = getVolumeSum("AAPL", "2016/06/15", "2018/12/26" )
    print(test1)
    print("***************************************\n")
    # TEST FUNCTION 4
    print("*******FUNCTION 4 ***********")
    test1 = getBestGain("2018/07/02")
    print(test1)
    print("***************************************\n")
    # TEST FUNCTION 5
    print("*******FUNCTION 5 ***********")
    test1 = getAveragePrice("AAPL", 2017)
    print(test1)
    print("***************************************\n")
    # TEST FUNCTION 6
    print("*******FUNCTION 6 ***********")
    test1 = getCountOver("AAPL", 173)
    print(test1)
    print("***************************************\n")