import pytest
import allure
import requests


@pytest.fixture()
def create_token():
    url = "https://restful-booker.herokuapp.com/auth"  # from restful booker curl(create token)
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture()
def create_booking_id():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    responseData = response.json()
    booking_id = responseData["bookingid"]
    return booking_id
def test_update_req1(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Bookingid ->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Sriram",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Sriram"

def test_update_req2(create_token, create_booking_id):
    print("Token ->", create_token)
    print("Bookingid ->", create_booking_id)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking_id)
    PUT_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    json_payload = {
        "firstname": "Sriram",
        "lastname": "Somasundaram",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["lastname"] == "Somasundaram"

