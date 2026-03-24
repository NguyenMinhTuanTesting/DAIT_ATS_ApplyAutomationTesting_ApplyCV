from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List


# --- Trang 1: Thông tin cá nhân & Ngành nghề ---
class Page1DTO(BaseModel):
    # Thông tin công việc
    job_apply: str
    expertise: str
    rank: str
    work_location: str
    job_opening: str

    # Thông tin cá nhân
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

    # Địa chỉ
    permanent_address: str
    permanent_province: str
    permanent_district: str
    temporary_address: str
    temporary_province: str
    temporary_district: str

    # Liên hệ
    phone_1: str
    phone_2: str = ""
    email: EmailStr
    emergency_name: str
    emergency_phone: str
    emergency_relationship: str

    # Mạng xã hội
    facebook: str = ""
    linkedin: str = ""
    youtube: str = ""
    other_social_type: str = ""
    other_social_link: str = ""

    # Hôn nhân
    marital_status: str
    children_count: str = "0"
    children_age: str = ""


# --- Trang 2: Thuế, Gia đình, Học vấn, Kỹ năng ---
class Page2DTO(BaseModel):
    # Thuế & Bảo hiểm
    is_tax: bool = False
    tax_id: str = ""
    is_social_insurance: bool = False
    social_insurance_no: str = ""

    # Gia đình
    father_name: str
    father_birth_year: str
    father_address: str = ""
    mother_name: str
    mother_birth_year: str
    mother_address: str = ""
    other_rel_type: str = ""
    other_rel_name: str = ""
    other_rel_birth_year: str = ""
    other_rel_address: str = ""

    # Học vấn (Tối thiểu 1)
    edu_from: str
    edu_to: str
    school_name: str
    school_location: str
    department: str
    degree: str
    major: str
    grade_score: str = ""
    ranking: str

    # Chức vụ trong trường (Optional)
    role_from: str = ""
    role_to: str = ""
    role_name: str = ""

    # Thành tích & Ngoại khóa
    achievements: str = ""
    extra_activities: str = ""
    is_innovation: bool = False
    innovation_competition_name: str = ""

    # Ngoại ngữ (Tối thiểu 1)
    language_name: str
    lang_degree: str = ""
    lang_exp_date: str = ""
    lang_listening: str
    lang_speaking: str
    lang_reading: str
    lang_writing: str

    # Công cụ (AI & Tin học)
    ai_tool_name: str = ""
    ai_tool_level: str = ""
    office_tool_name: str = ""
    office_tool_level: str = ""

    # Chứng chỉ chuyên môn
    cert_from: str = ""
    cert_to: str = ""
    cert_school: str = ""
    cert_major: str = ""
    cert_exp_date: str = ""
    cert_proficiency: str = ""
    cert_grade: str = ""


# --- Trang 3: Kinh nghiệm làm việc & Tham chiếu ---
class Page3DTO(BaseModel):
    # Quá trình làm việc
    career_from: str
    career_to: str
    career_type: str  # Đi làm / Ở nhà / Freelancer
    career_company: str = ""
    career_industry: str = ""
    career_size: str = ""
    career_address: str = ""
    career_phone: str = ""
    career_position: str = ""
    career_salary: str = ""
    career_duty: str = ""
    career_achievement: str = ""
    career_leaving_reason: str = ""

    # Freelancer/At home reason
    career_home_reason: str = ""
    career_freelance_desc: str = ""

    # Người tham khảo (Tối thiểu 1)
    ref_name: str
    ref_position: str
    ref_company: str
    ref_relationship: str
    ref_phone: str


# --- Trang 4: Thông tin khác, Thu nhập, Tài khoản ---
class Page4DTO(BaseModel):
    # Thông tin khác
    overtime_intensity: str
    travel_availability: str
    passionate: str
    passionate_description: str
    has_acquaintance: bool = False
    acquaintance_name: str = ""
    acquaintance_company: str = ""
    acquaintance_position: str = ""
    acquaintance_relationship: str = ""

    applied_before: bool = False
    applied_date: str = ""
    applied_company: str = ""
    applied_position: str = ""

    # Nhận việc
    earliest_start_date: str
    latest_start_date: str
    expected_start_date: str
    source: str
    source_other_text: str = ""
    lecturer_name: str = ""

    has_invested: bool = False
    invested_company_name: str = ""

    # Thu nhập & Ngân hàng
    min_expected_salary: str
    max_expected_salary: str
    bank_number: str
    bank_name: str
    bank_branch: str
    bank_owner_name: str

    # Upload & Commit
    cv_file_path: str = ""
    agree_terms: bool = True


# --- Root DTO: Đại diện cho 1 ứng viên hoàn chỉnh ---
class CandidateDTO(BaseModel):
    page_1: Page1DTO
    page_2: Page2DTO
    page_3: Page3DTO
    page_4: Page4DTO