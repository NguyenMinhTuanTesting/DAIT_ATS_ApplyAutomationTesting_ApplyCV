from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

# --- Trang 1: Thông tin cá nhân & Ngành nghề ---
class Page1DTO(BaseModel):
    job_apply: str
    expertise: str
    rank: str
    work_location: str
    job_opening: str
    avatar_path: str = ""
    full_name: str
    gender: str
    dob: str
    height: str = ""
    weight: str = ""
    nationality: str
    place_of_birth: str
    ethnicity: str
    religion: str
    citizen_id: str
    issued_date: str
    issued_place: str
    permanent_address: str
    permanent_province: str
    permanent_district: str
    temporary_address: str
    temporary_province: str
    temporary_district: str
    phone_1: str
    phone_2: str = ""
    email: EmailStr
    emergency_name: str
    emergency_phone: str
    emergency_relationship: str
    facebook: str = ""
    linkedin: str = ""
    youtube: str = ""
    other_social_type: str = ""
    other_social_link: str = ""
    marital_status: str
    children_count: str = "0"
    children_age: str = ""

# --- Trang 2: Thuế, Gia đình, Học vấn, Kỹ năng ---
class Page2DTO(BaseModel):
    is_tax: bool = False
    tax_id: str = ""
    is_social_insurance: bool = False
    social_insurance_no: str = ""
    father_name: str
    father_birth_year: str
    father_address: str = ""
    mother_name: str
    mother_birth_year: str
    mother_address: str = ""
    edu_from: str
    edu_to: str
    school_name: str
    school_location: str
    department: str
    degree: str
    major: str
    grade_score: str = ""
    ranking: str
    achievements: str = ""
    extra_activities: str = ""
    language_name: str
    lang_listening: str
    lang_speaking: str
    lang_reading: str
    lang_writing: str

# --- Trang 3: Kinh nghiệm làm việc & Tham chiếu ---
class Page3DTO(BaseModel):
    career_from: str
    career_to: str
    career_type: str
    career_company: str = ""
    career_industry: str = ""
    career_position: str = ""
    career_salary: str = ""
    career_duty: str = ""
    career_leaving_reason: str = ""
    ref_name: str
    ref_position: str
    ref_company: str
    ref_relationship: str
    ref_phone: str

# --- Trang 4: Thông tin khác, Thu nhập, Tài khoản ---
class Page4DTO(BaseModel):
    overtime_intensity: str
    travel_availability: str
    passionate: str
    passionate_description: str
    earliest_start_date: str
    latest_start_date: str
    expected_start_date: str
    source: str
    min_expected_salary: str
    max_expected_salary: str
    bank_number: str
    bank_name: str
    bank_branch: str
    bank_owner_name: str
    cv_file_path: str = ""
    # MỚI: Danh sách 3 file tài liệu bổ sung
    document_paths: List[str] = []
    agree_terms: bool = True

# --- Root DTO ---
class CandidateDTO(BaseModel):
    page_1: Page1DTO
    page_2: Page2DTO
    page_3: Page3DTO
    page_4: Page4DTO
    others_paths: List[str] = []