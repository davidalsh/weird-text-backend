from src.tests.client import client
from src.tests.testbase import WeirdWordTestBase


def test_encode_1():
    body = {
        "text": "This is a long looong test sentence,\nwith some big (biiiiig) words!"
    }
    response = client.post("/api/v1/encode", json=body)
    assert response.status_code == 200
    WeirdWordTestBase(response.json(), body).process()


def test_encode_2():
    body = {
        "text": "Here we have an extended, lengthy test sentence. It contains: incredibly massive (massiveee massive) "
                "words! The purpose of this test, is to observe how it deals with increased length. And, to see if it "
                "keeps everything: coherent and easy to understand."
    }
    response = client.post("/api/v1/encode", json=body)
    assert response.status_code == 200
    WeirdWordTestBase(response.json(), body).process()


def test_encode_3():
    body = {
        "text": "This is a verrry long, loooong test sentence. It includes: some quite huge (hugeee huge) words! "
                "The aim of this example, is to test how it manages length and complexity. Ensuring everything "
                "remains: clear and readable."
    }
    response = client.post("/api/v1/encode", json=body)
    assert response.status_code == 200
    WeirdWordTestBase(response.json(), body).process()


