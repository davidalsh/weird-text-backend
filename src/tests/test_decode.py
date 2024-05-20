from src.tests.client import client
from src.tests.testbase import WeirdWordTestBase


def test_decode_1():
    body = {
        "text": "\n—weird—\nTihs is a lnog loonog tset sntecnee,\nwtih smoe big (biiiiig) wdros!\n—weird—\nThis long "
                "looong sentence some test with words"
    }
    response = client.post("/api/v1/decode", json=body)
    assert response.status_code == 200
    WeirdWordTestBase(body, response.json()).process()


def test_decode_2():
    body = {
        "text": "\n—weird—\nHree we hvae an eentexdd, lgtnehy tset senntece. It catnoins: iinlcdbery mvaisse "
                "(mvaisseee mvaisse) wrods! The puropse of tihs tset, is to orbevse how it daels wtih isaeecrnd "
                "ltgenh. And, to see if it kpees ehrneyivtg: cnhoreet and esay to unadsrentd.\n—weird—\nHere coherent "
                "contains deals easy everything extended have increased incredibly keeps length lengthy massive "
                "massive massiveee observe purpose sentence test test this understand with words"
    }
    response = client.post("/api/v1/decode", json=body)
    assert response.status_code == 200
    WeirdWordTestBase(body, response.json()).process()


def test_decode_3():
    body = {
        "text": "\n—weird—\nTihs is a vrrery lnog, loonoog tset snentcee. It icluedns: smoe qiute hgue (hgueee hgue) "
                "wrods! The aim of tihs eaplmxe, is to tset how it mgaanes lgnteh and cioxelptmy. "
                "Einursng eihevtyrng rnmeias: celar and raldeabe.\n—weird—\nEnsuring This clear complexity everything "
                "example huge huge hugeee includes length long loooong manages quite readable remains sentence some "
                "test test this verrry words"
    }
    response = client.post("/api/v1/decode", json=body)
    assert response.status_code == 200
    WeirdWordTestBase(body, response.json()).process()
