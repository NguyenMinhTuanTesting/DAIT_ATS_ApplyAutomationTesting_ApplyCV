# page CV
from dataclasses import dataclass


@dataclass
class ats_login:
    search_bar ="//input[@role='searchbox']"
    candicate_name ="//td[@name='partner_name']"