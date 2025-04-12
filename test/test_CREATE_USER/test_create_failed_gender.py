import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()

@pytest.mark.QaseIO(6)
def test():
    random_name = fake.name()
    random_email = fake.email()
    head = {
        "Accept" : "aplication/json",
        "Content_Type": "aplication/json",
        "Authorization": "Bearer 9d2570065436c9f331a08dab53fdff4d8bf8208f6b8a2a468e88c04f7b4943a2"
    }
    payload = {
        "name": random_name,
        "gender": "pria",
        "email": random_email,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)

    # VALIDATION
    status_code = req.status_code
    resp_field = req.json()[0]["field"]
    resp_msg = req.json()[0]["message"]

    # ASSERT
    assert_that(status_code).is_equal_to(422)
    assert_that(resp_field).is_equal_to("gender")
    assert_that(resp_msg).is_equal_to("can't be blank, can be male of female")
