import pytest
import allure
import requests

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