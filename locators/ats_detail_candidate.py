# page CV
from dataclasses import dataclass


@dataclass
class ats_detail_candidate:
    CANDIDATE_NAME ="//input[@id='candidate_id_0']"
    CANDIDATE_EMAIL="//input[@id='email_from_0']"
    CANDIDATE_PHONE="//input[@id='partner_phone_0']"
    CANDIDATE_SCHOOL="//input[@id='name_education_0']"
    CANDIDATE_CCCD="//input[@id='identity_id_0']"
    CANDIDATE_ATTACHED_IMAGE="//img[@class='img img-fluid my-0 mx-auto rounded']" #lấy tên file từ thuộc tính alt
    CANDIDATE_ATTACHED_FILE ="//div[@aria-label='Preview']/.." #lấy tên file từ thuộc tính title


