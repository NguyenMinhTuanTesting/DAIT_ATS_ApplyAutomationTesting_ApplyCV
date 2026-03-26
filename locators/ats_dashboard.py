# page CV
from dataclasses import dataclass


@dataclass
class ats_dashboard:
    TUYENDUNG_MODULE ="//a[@data-menu-id='173']"
    TUYENDUNG_CANDIDATE_DROPDOWN ="//button[@data-hotkey='1']"
    NHU_CAU_TUYEN_DUNG_TRANSFER="//a[text()='Nhu cầu tuyển dụng']"
    VI_TRI_CONG_VIEC_TRANSFER="//a[text()='Theo Vị trí công việc']"
    DANH_SACH_UNG_VIEN_TRANSFER = "//a[text()='Tất cả đơn xin việc']"
