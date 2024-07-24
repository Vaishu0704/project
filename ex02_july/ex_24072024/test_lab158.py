import pytest
import allure
import requests

@allure.title("Test GET Request(Positive)-restful booker project #1")
@allure.description("TC1->Positive-Verify that GET Request with id working")
@allure.tag("regression","p0","smoke")
@allure.label("Owner","Vaishnavi")
@allure.testcase("TC#1")
@pytest.mark.smoke

def test_get_single_request_by_id():
    url="https://restful-booker.herokuapp.com/booking/1"
    responseData=requests.get(url)
    print(responseData.json())
    assert responseData.status_code==200

@allure.title("Test GET Request(Negative)-restful booker project #1")
@allure.description("TC2->Negative-Verify that GET Request with id working")
@allure.tag("regression","p0","smoke")
@allure.label("Owner","Vaishnavi")
@allure.testcase("TC#2")
@pytest.mark.smoke

def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404