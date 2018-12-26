"""
Author: Christian R. Garcia
Tester for HW1's functions to read "sunspots.csv" data and display in different ways.
Function names tell what they're doing well enough.

Run with "py.test-3 hw2.py"
"""
import sys
sys.path.append('../hw1')
from hw1 import csvDataReaderf, csvDataReaderg, csvDataReaderh


csvFile = "../hw1/sunspots.csv"


#Test Set One
def test_funcFListCheck():
    assert isinstance(csvDataReaderf(csvFile), list)

def test_funcFDictTypeCheck():
    for x in csvDataReaderf(csvFile):
        assert isinstance(x, dict)

def test_funcFDictSizeCheck():
    for x in csvDataReaderf(csvFile):
        assert len(x) == 3

def test_funcFKeyTypeCheck():
    for x in csvDataReaderf(csvFile):
        assert isinstance(x["id"], int)
        assert isinstance(x["year"], int)
        assert isinstance(x["spots"], int)

def test_funcFOutputSizeCheck():
    assert len(open(csvFile).readlines()) == len(csvDataReaderf(csvFile))

def test_funcFFirstNLastCheck():
    assert int(open(csvFile).readlines()[0][0:4]) == csvDataReaderf(csvFile)[0]["year"]
    assert int(open(csvFile).readlines()[-1][0:4]) == csvDataReaderf(csvFile)[-1]["year"]


#Test Set Two
def test_funcGListCheck():
    assert isinstance(csvDataReaderg(csvFile), list)

def test_funcGDictTypeCheck():
    for x in csvDataReaderg(csvFile):
        assert isinstance(x, dict)

def test_funcGDictSizeCheck():
    for x in csvDataReaderg(csvFile):
        assert len(x) == 3

def test_funcGKeyTypeCheck():
    for x in csvDataReaderg(csvFile):
        assert isinstance(x["id"], int)
        assert isinstance(x["year"], int)
        assert isinstance(x["spots"], int)

def test_funcGNoInputsCheck():
    assert len(open(csvFile).readlines()) == len(csvDataReaderg(csvFile))

def test_funcGStartNoEndCheck():
    assert int(open(csvFile).readlines()[60][0:4]) == csvDataReaderg(csvFile, 1830)[0]["year"]
    assert int(open(csvFile).readlines()[-1][0:4]) == csvDataReaderg(csvFile, 1830)[-1]["year"]

def test_funcGEndNoStartCheck():
    assert int(open(csvFile).readlines()[0][0:4]) == csvDataReaderg(csvFile, end=1820)[0]["year"]
    assert int(open(csvFile).readlines()[50][0:4]) == csvDataReaderg(csvFile, end=1820)[-1]["year"]

def test_funcGStartAndEndCheck():
    assert int(open(csvFile).readlines()[20][0:4]) == csvDataReaderg(csvFile, 1790, 1840)[0]["year"]
    assert int(open(csvFile).readlines()[70][0:4]) == csvDataReaderg(csvFile, 1790, 1840)[-1]["year"]

def test_funcGPotpourri():
    csvDataReaderg(csvFile, 1792, 1829)
    csvDataReaderg(csvFile, 1772, 1868)
    csvDataReaderg(csvFile, 1200, 1834)
    csvDataReaderg(csvFile, 1820, 2018)
    csvDataReaderg(csvFile, 2018, 1200)
    csvDataReaderg(csvFile, 1200, 2018)
    csvDataReaderg(csvFile, 1772, 1772)


#Test Set Three
def test_funcHListCheck():
    assert isinstance(csvDataReaderh(csvFile), list)

def test_funcHDictTypeCheck():
    for x in csvDataReaderh(csvFile):
        assert isinstance(x, dict)

def test_funcHDictSizeCheck():
    for x in csvDataReaderh(csvFile):
        assert len(x) == 3

def test_funcHKeyTypeCheck():
    for x in csvDataReaderh(csvFile):
        assert isinstance(x["id"], int)
        assert isinstance(x["year"], int)
        assert isinstance(x["spots"], int)

def test_funcHNoInputsCheck():
    assert len(open(csvFile).readlines()) == len(csvDataReaderh(csvFile))

def test_funcHLimitNoOffsetCheck():
    assert int(open(csvFile).readlines()[0][0:4]) == csvDataReaderh(csvFile, 20)[0]["year"]
    assert int(open(csvFile).readlines()[19][0:4]) == csvDataReaderh(csvFile, 20)[-1]["year"]

def test_funcHOffsetNoLimitCheck():
    assert int(open(csvFile).readlines()[15][0:4]) == csvDataReaderh(csvFile, offset=15)[0]["year"]
    assert int(open(csvFile).readlines()[-1][0:4]) == csvDataReaderh(csvFile, offset=15)[-1]["year"]

def test_funcHLimitAndOffsetCheck():
    assert int(open(csvFile).readlines()[15][0:4]) == csvDataReaderh(csvFile, 20, 15)[0]["year"]
    assert int(open(csvFile).readlines()[34][0:4]) == csvDataReaderh(csvFile, 20, 15)[-1]["year"]

def test_funcHPotpourri():
    csvDataReaderh(csvFile, 0, 0)
    csvDataReaderh(csvFile, 10, 10)
    csvDataReaderh(csvFile, 20, 30)
    csvDataReaderh(csvFile, 200, 30)
    csvDataReaderh(csvFile, 30, 200)
