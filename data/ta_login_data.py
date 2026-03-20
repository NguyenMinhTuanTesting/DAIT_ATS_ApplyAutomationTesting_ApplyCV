import os
from dotenv import load_dotenv
from dto.ta_login_dto import TALoginDTO

load_dotenv()

VALID_TA_LOGIN = TALoginDTO(
    email=os.getenv("ATS_EMAIL"),
    password=os.getenv("ATS_PASSWORD")
)

INVALID_TA_LOGIN = TALoginDTO(
    email="wrong@email.com",
    password="wrongpassword"
)