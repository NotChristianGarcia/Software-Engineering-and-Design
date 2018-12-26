"""
Author: Christian R. Garcia
Creating three functions to load and return data from a file, "sunspots.csv"
Function F returns all data from the inputted file with no arguments.
Function G returns data, but only from a specified start to a specified end year.
Function H returns data, but with a limit on rows of data and with an offset.
Alongside that there is an "interactiveProgram" function that will interactively
guide you through picking which function you want to use.

Run with "python3 hw1.py"
"""
import csv


def csvDataReaderf(inputCSV):
    """
    Used as csvDataReaderf().
    Inputs everything in the .csv into a list of
    dictionaries and then outputs said list.
    """
    with open(inputCSV, mode='r') as csvFile:
        f = []
        i = 0
        fieldNames = ["year", "spots"]
        dataReader = list(csv.DictReader(csvFile, fieldNames))
        for x in dataReader:
            x = (dict(x))
            x["year"] = int(x["year"])
            x["spots"] = int(x["spots"])
            x["id"] = i
            i += 1
            f.append(x)
    print("f()")
    return f


def csvDataReaderg(inputCSV, start=-10000, end=100000000):
    """
    Used as csvDataReaderg(start, end).
    If you only want end then you can input "end = int"
    rather than comma delimited non-defined inputs.
    Start and end are both ints that refer the the year
    of data. You're giving the function a range of years
    to give data from.
    """
    with open(inputCSV, mode='r') as csvFile:
        g = []
        i = 0
        fieldNames = ["year", "spots"]
        dataReader = list(csv.DictReader(csvFile, fieldNames))
        for x in dataReader:
            x = (dict(x))
            x["year"] = int(x["year"])
            x["spots"] = int(x["spots"])
            x["id"] = i
            i += 1
            if int(x["year"]) >= start and int(x["year"]) <= end:
                g.append(x)
    introText = "g("
    if start != -10000:
        introText += "start=" + str(start)
        if end != 100000000:
            introText += ", "
    if end != 100000000:
        introText += "end=" + str(end)
    print(introText + ")")
    return g


def csvDataReaderh(inputCSV, limit=100000000, offset=0):
    """
    Used as csvDataReaderh(limit, offset).
    If you only want offset then you can input "offset = int"
    rather than comma delimited non-defined inputs.
    Limit and offset are both ints. Limit refers to the amount
    of results that you want (ex. Limit = 1 will give one result)
    and offset refers to where you want the list to start.
    """
    with open(inputCSV, mode='r') as csvFile:
        h = []
        i = 0
        fieldNames = ["year", "spots"]
        dataReader = list(csv.DictReader(csvFile, fieldNames))
        limitCounter = 0
        for x in dataReader:
            x = (dict(x))
            x["year"] = int(x["year"])
            x["spots"] = int(x["spots"])
            x["id"] = i
            i += 1
            if limitCounter < limit:
                if int(x["id"]) >= offset:
                    limitCounter += 1
                    h.append(x)
    introText = "h("
    if limit != 100000000:
        introText += "limit=" + str(limit)
        if offset != 0:
            introText += ", "
    if offset != 0:
        introText += "offset=" + str(offset)
    print(introText + ")")
    return h


def interactiveProgram(inputCSV):
    """
    Ask user which query they wanted to use, corresponding to functions
    f, g, and h. In the case of g, or h, the user is prompted to give
    inputs to the functions. Prompts have error handling.
    """
    print("Query Types (input lowercase letter)\n     a: for whole dataset\n\
     b: to search by start and end year\n     c: to search by limit and offset")

    # Insures that input is either "a", "b", or "c", otherwise ask
    # user to try again.
    while True:
        queryType = input("Which query type would you like to use? ")
        queryType = queryType.lower()
        if queryType not in ("a", "b", "c"):
            print("Sorry, input error, try again with a, b, or c as inputs.")
        else:
            break

    # Completes use of csvDataReaderf().
    if queryType == "a":
        f = csvDataReaderf(inputCSV)
        print("[", end="")
        flag = True
        for y in f:
            if flag == True:
                print("{{'id':{},'year':{},'spots':{}}},".format(y["id"], y["year"], y["spots"]))
                flag = False
            else:
                print(" {{'id':{},'year':{},'spots':{}}},".format(y["id"], y["year"], y["spots"]))
        print("]")

    # Checks if inputs are ints or "n" and if not ask for input to be given again.
    # Also checks to see if the end date is after the start, as otherwise that
    # wouldn't make much sense.
    # Completes use of csvDataReaderg() if everything is good.
    elif queryType == "b":
        while True:
            while True:
                start = input("Which start year would you like to use? (n for none) ")
                if start == "n":
                    start = -10000
                    break
                try:
                    isinstance(int(start), int)
                    break
                except ValueError:
                    print("Sorry, please input n or an int")
                    continue

            while True:
                end = input("Which end year would you like to use? (n for none) ")
                if end == "n":
                    end = 100000000
                    break
                try:
                    isinstance(int(end), int)
                    break
                except TypeError:
                    print("Sorry, please input n or an int")
                    continue

            if int(start) > int(end):
                print("Sorry, the end year can not be before the start year")
            else:
                break

        g = csvDataReaderg(inputCSV, int(start), int(end))
        print("[", end="")
        flag = True
        for y in g:
            if flag is True:
                print("{{'id':{},'year':{},'spots':{}}},"\
                        .format(y["id"], y["year"], y["spots"]))
                flag = False
            else:
                print(" {{'id':{},'year':{},'spots':{}}},"\
                        .format(y["id"], y["year"], y["spots"]))
        print("]")

    # Checks to see if inputs are ints or "n" if not, ask to try again.
    # Checks to make sure limit is a positive int, otherwise ask to try again.
    # Completes use of csvDataReaderh() if everything is good.
    elif queryType == "c":
        while True:
            limit = input("Which result limit would you like to use? (n for none) ")
            if limit == "n":
                limit = 100000000
                break
            try:
                isinstance(int(limit), int)
                if int(limit) > 0:
                    break
                else:
                    print("Sorry, limit must be a positive int")
                    continue
            except ValueError:
                print("Sorry, please input n or an int")

        while True:
            offset = input("Which result offset would you like to use? (n for none) ")
            if offset == "n":
                offset = 0
                break
            try:
                isinstance(int(offset), int)
                break
            except TypeError:
                print("Sorry, please input n or an int")

        h = csvDataReaderh(inputCSV, int(limit), int(offset))
        print("[", end="")
        flag = True
        for y in h:
            if flag is True:
                print("{{'id':{},'year':{},'spots':{}}},"\
                        .format(y["id"], y["year"], y["spots"]))
                flag = False
            else:
                print(" {{'id':{},'year':{},'spots':{}}},"\
                        .format(y["id"], y["year"], y["spots"]))
        print("]")


if __name__ == "__main__":
    interactiveProgram("sunspots.csv")
