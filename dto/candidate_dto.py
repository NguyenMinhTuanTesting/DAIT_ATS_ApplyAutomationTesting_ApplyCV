from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class JobInfoDTO(BaseModel):
    job_apply: str          # Ngành nghề ứng tuyển
    expertise: str         # Lĩnh vực chuyên môn
    rank: str              # Cấp bậc
    work_location: str     # Địa điểm làm việc
    job_opening: str       # Vị trí ứng tuyển (ID hoặc tên)

class PersonalInfoDTO(BaseModel):
    avatar_path: str       # Đường dẫn file ảnh trên máy tính
    full_name: str
    gender: str            # "Nam" hoặc "Nữ"
    dob: str               # Định dạng dd/mm/yyyy
    nationality: str
    place_of_birth: str
    ethnicity: str
    religion: str
    citizen_id: str
    issued_date: str       # Định dạng dd/mm/yyyy
    issued_place: str

class AddressDTO(BaseModel):
    # Thường trú
    perm_address: str
    perm_province: str
    perm_ward: str
    # Tạm trú
    temp_address: str
    temp_province: str
    temp_ward: str

class ContactSocialDTO(BaseModel):
    phone_1: str = Field(..., max_length=11)
    email: EmailStr
    emergency_name: str
    emergency_phone: str
    emergency_relation: str
    facebook: Optional[str] = None
    linkedin: Optional[str] = None
    marital_status: str

class CandidatePage1DTO(BaseModel):
    """Tổng hợp dữ liệu cho toàn bộ Trang 1"""
    job_info: JobInfoDTO
    personal_info: PersonalInfoDTO
    address_info: AddressDTO
    contact_info: ContactSocialDTO