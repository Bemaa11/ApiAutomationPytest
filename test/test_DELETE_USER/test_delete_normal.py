import pytest
import requests
from assertpy import assert_that
from setting.endpoint import api_user
from faker import Faker
fake = Faker()

@pytest.mark.QaseIO(8)
def test():
    #============================= CREATE NEW USER ==============================
    random_name = fake.name()
    random_email = fake.email()
    head = {
        "Accept" : "aplication/json",
        "Content_Type": "aplication/json",
        "Authorization": "Bearer 9d2570065436c9f331a08dab53fdff4d8bf8208f6b8a2a468e88c04f7b4943a2"
    }
    payload = {
        "name": random_name,
        "gender": "male",
        "email": random_email,
        "status": "active"
    }
    req = requests.post(api_user, headers=head, json=payload)
    id_new_user = req.json().get("id")

    # ============================= DELETE NEW USER ==============================

    head = {
        "Accept": "aplication/json",
        "Content_Type": "aplication/json",
        "Authorization": "Bearer 9d2570065436c9f331a08dab53fdff4d8bf8208f6b8a2a468e88c04f7b4943a2"
    }
    req = requests.delete(f"{api_user}/{id_new_user}", headers=head)

    # VALIDATION
    status_code = req.status_code


    # ASSERT
    assert_that(status_code).is_equal_to(204)

