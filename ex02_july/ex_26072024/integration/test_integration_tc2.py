#Create a booking,delete the booking id and verify using Get  request that it should not exist
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

def test_delete(create_token, create_booking_id):
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking_id
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
#GET request to verify that the booking id does not exist
    response = requests.get(url=DELETE_URL, headers=headers)
    assert response.status_code == 404

