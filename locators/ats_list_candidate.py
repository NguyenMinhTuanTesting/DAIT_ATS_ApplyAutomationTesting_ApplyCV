# page CV
from dataclasses import dataclass


@dataclass
class ats_list_candidate:
    SEARCH_BAR ="//input[@role='searchbox']" #Clear trước khi search
    CANDIDATE_NAME ="//td[@name='partner_name']" #
    LIST_MODE="//button[@data-tooltip='Danh sách']"