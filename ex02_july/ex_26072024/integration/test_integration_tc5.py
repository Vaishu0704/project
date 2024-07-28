#Invalid creation-enter a wrong payload or wrong json
import pytest
import allure
import requests
def test_create_booking_id():
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {  }
    response = requests.post(url=URL, headers=headers, json=json_payload)
        # Assertions
    assert response.status_code == 500
