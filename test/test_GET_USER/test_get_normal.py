import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user


@pytest.mark.QaseIO(10)
def test():
    head = {
        "Accept" : "aplication/json",
        "Content_Type": "aplication/json",
        "Authorization": "Bearer 9d2570065436c9f331a08dab53fdff4d8bf8208f6b8a2a468e88c04f7b4943a2"
    }
    req = requests.get(api_user, headers=head)
    print(req.json())


    # VALIDATION
    statuscode = req.status_code
    resp_id = req.json()[0]["id"]
    resp_name = req.json()[0]["name"]
    resp_email = req.json()[0]["email"]
    resp_gender = req.json()[0]["gender"]
    resp_status = req.json()[0]["status"]

    #ASSERT
    assert_that(statuscode).is_equal_to(200)
    assert_that(resp_id).is_not_none()
    assert_that(resp_name).is_not_none()
    assert_that(resp_email).is_not_none()
    assert_that(resp_gender).is_not_none()
    assert_that(resp_status).is_not_none()
    assert_that(resp_id).is_type_of(int)
    assert_that(resp_email).contains("@")
    assert_that(resp_gender).is_in("male", "female")
    assert_that(resp_status).is_in("active", "inactive")
