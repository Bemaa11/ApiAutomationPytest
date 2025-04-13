# ========================================== HOST ===================================
import os
from os import environ

host_gorest = "https://gorest.co.in/public/v2"
host_qase_io = "https://api.qase.io/v1"
api_result_qase_io = host_qase_io +"/result"


#=============================== ENDPOINT ====================================
api_user = host_gorest + "/users"
api_user_wrong = host_gorest + "/userssss"

#=============================== CONFIG ====================================
TOKEN_QASE_IO = os.environ.get("TOKEN_QASE_IO")
PROJECT_CODE_QASE_IO = "APP"
TEST_RUN_QASE_IO = "1"

#=============================== SLACK ====================================
WEBHOOK = os.environ.get("WEBHOOK_SLACK")
