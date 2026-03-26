import os
from dotenv import load_dotenv
from dto.ta_login_dto import TALoginDTO

load_dotenv()

VALID_TA_LOGIN = TALoginDTO(
    email=os.getenv("TA_EMAIL") or "",
    password=os.getenv("TA_PASSWORD") or ""
)

INVALID_TA_LOGIN = TALoginDTO(
    email="wrong@gmail.com",
    password="lêu lêu"
)