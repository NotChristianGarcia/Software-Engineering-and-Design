"""
Author: Christian R. Garcia
Tester for HW3's flask server of HW1's data reading and returning functions
Split into Five sections, each testing function f, g, and h from hw1 and the
id and year functions introduced in HW3.
Function names give a good sense of what's happening throughout this tester.

Insure flask server from HW3 is running then run with "py.test-3 hw4.py"
"""
import requests as r
import pytest


csvFile = "../hw1/sunspots.csv"
BASE_URL = "http://localhost:5000"


def requestFromServer(extraURL):
    req = r.get("{}{}".format(BASE_URL, extraURL))
    return req


# Section One
@pytest.fixture(scope="module")
def sectionOne():
    return requestFromServer("/spots")

def test_a1CheckStatus(sectionOne):
    assert sectionOne.status_code == 200

def test_b1CheckJSON(sectionOne):
    assert sectionOne.json() is not None

def test_c1CheckList(sectionOne):
    assert isinstance(sectionOne.json(), list)

def test_d1CheckDict(sectionOne):
    assert isinstance(sectionOne.json()[1], dict)

def test_e1CheckDictLen(sectionOne):
    assert len(sectionOne.json()[1]) == 3

def test_f1CheckKeyType(sectionOne):
    for i in sectionOne.json():
        assert isinstance(i["id"], int)
        assert isinstance(i["year"], int)
        assert isinstance(i["spots"], int)

def test_g1CheckListLen(sectionOne):
    assert len(sectionOne.json()[:]) == 100

def test_f1CheckFirstNLastDict(sectionOne):
    assert int(open(csvFile).readlines()[0][0:4]) == sectionOne.json()[0]["year"]
    assert int(open(csvFile).readlines()[-1][0:4]) == sectionOne.json()[-1]["year"]


# Section Two
@pytest.fixture(scope="module", params=[["start=1780&end=1819", 40],\
                                        ["start=1780"         , 90],\
                                        ["end=1839"           , 70],\
                                        ["start=1820&end=1780",  0],\
                                        ["limit=10&offset=20" , 10],\
                                        ["limit=20"           , 20],
                                        ["offset=20"          , 80]])
def sectionTwo(request):
    return [requestFromServer("/spots?{}".format(request.param[0])), request.param[1]]

def test_a2CheckStatus(sectionTwo):
    assert sectionTwo[0].status_code == 200

def test_b2CheckJSON(sectionTwo):
    assert sectionTwo[0].json() is not None

def test_c2CheckList(sectionTwo):
    assert isinstance(sectionTwo[0].json(), list)

def test_d2CheckListLen(sectionTwo):
    assert len(sectionTwo[0].json()[:]) == sectionTwo[1]


# Section Three
@pytest.fixture(scope="module", params=["start=abc",\
                                        "end=abc",\
                                        "limit=-1",\
                                        "offset=-1",\
                                        "start=1770&limit=20"])
def sectionThree(request):
    return requestFromServer("/spots?{}".format(request.param))

def test_a3CheckStatus(sectionThree):
    assert sectionThree.status_code == 400

def test_b3CheckString(sectionThree):
    assert isinstance(sectionThree.json(), str)

def test_c3CheckList(sectionThree):
    assert sectionThree.json()[0] is not None


# Section Four
@pytest.fixture(scope="module", params=["1", "30", "99"])
def sectionFour(request):
    return [requestFromServer("/spots/{}".format(request.param)), request.param]

def test_a4CheckStatus(sectionFour):
    assert sectionFour[0].status_code == 200

def test_b4CheckJSON(sectionFour):
    assert sectionFour[0].json() is not None

def test_c4CheckDict(sectionFour):
    assert isinstance(sectionFour[0].json(), dict)

def test_d4CheckDictLen(sectionFour):
    assert len(sectionFour[0].json()) == 3

def test_e4CheckID(sectionFour):
    assert sectionFour[0].json()["id"] == int(sectionFour[1])


# Section Five
@pytest.fixture(scope="module", params=["1771", "1834", "1859"])
def sectionFive(request):
    return [requestFromServer("/spots/years/{}".format(request.param)), request.param]

def test_a5CheckStatus(sectionFive):
    assert sectionFive[0].status_code == 200

def test_b5CheckJSON(sectionFive):
    assert sectionFive[0].json() is not None

def test_c5CheckDict(sectionFive):
    assert isinstance(sectionFive[0].json(), dict)

def test_d5CheckDictLen(sectionFive):
    assert len(sectionFive[0].json()) == 3

def test_e5CheckID(sectionFive):
    assert sectionFive[0].json()["year"] == int(sectionFive[1])
