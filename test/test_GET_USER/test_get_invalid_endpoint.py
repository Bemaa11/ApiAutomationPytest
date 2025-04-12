import pytest
import requests
from assertpy import assert_that

from setting.endpoint import api_user_wrong

@pytest.mark.QaseIO(9)
def test():
    head = {
        "Accept" : "aplication/json",
        "Content_Type": "aplication/json",
        "Authorization": "Bearer 9d2570065436c9f331a08dab53fdff4d8bf8208f6b8a2a468e88c04f7b4943a2"
    }
    req = requests.get(api_user_wrong, headers=head)

    # VALIDATION
    statuscode = req.status_code


    #ASSERT
    assert_that(statuscode).is_equal_to(404)
