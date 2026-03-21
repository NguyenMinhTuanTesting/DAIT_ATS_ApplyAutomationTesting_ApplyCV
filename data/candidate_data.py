import os
import random
from faker import Faker
from dto.candidate_dto import (
    CandidatePage1DTO, JobInfoDTO, PersonalInfoDTO,
    AddressDTO, ContactSocialDTO
)

fake = Faker('vi_VN')

# --- DANH MỤC DỮ LIỆU THỰC TẾ (CT GROUP) ---
JOB_APPLY_LIST = ["Bán dẫn", "Công nghệ thông tin", "ESG", "Lượng tử", "Máy bay không người lái", "Trí tuệ nhân tạo",
                  "Ô tô Điện - Tàu điện", "Đô thị Xanh thông minh"]
EXPERTISE_LIST = ["An ninh mạng", "Công nghệ phần mềm", "Khoa học dữ liệu", "Kỹ thuật phần mềm", "Marketing",
                  "Quản lý chất lượng", "Thiết kế đồ họa", "AI"]
RANK_LIST = ["E2", "M1", "M2", "D1", "C1", "E1", "Thực tập sinh", "E4"]
OPENING_LIST = ["Kỹ sư UAV", "Chuyên viên cao cấp", "Chuyên viên", "Thực tập sinh", "Trưởng phòng", "Phó Giám đốc"]

NATIONALITY_LIST = ["Việt Nam", "Anh", "Pháp", "Mỹ", "Nhật Bản", "Hàn Quốc"]
ETHNIC_LIST = ["Kinh", "Tày", "Thái", "Mường", "Khmer", "Hoa", "Nùng"]
RELIGION_LIST = ["Không", "Phật giáo", "Thiên chúa giáo", "Hòa Hảo", "Cao Đài"]
MARITAL_LIST = ["Độc thân", "Ly hôn", "Có gia đình", "Góa (vợ/chồng)"]

# Map Tỉnh/Thành với Phường/Xã tương ứng để tránh lệch data
LOCATION_MAP = {
    "Thành Phố Hà Nội (VN)": ["Phường Hoàn Kiếm", "Phường Cửa Nam", "Phường Ba Đình", "Phường Ngọc Hà",
                              "Phường Giảng Võ", "Phường Vĩnh Tuy"],
    "Thành Phố Hồ Chí Minh (VN)": ["Phường Cầu Kiệu", "Phường Phú Nhuận", "Phường Tân Sơn Hòa", "Phường Tân Sơn Nhất",
                                   "Phường Thảo Điền"],
    "Thành Phố Đà Nẵng (VN)": ["Phường Hải Châu", "Phường Hòa Cường", "Phường Thanh Khê", "Phường An Khê",
                               "Phường Sơn Trà"],
    "Tỉnh Nghệ An (VN)": ["Xã Nghi Lộc", "Xã Phúc Lộc", "Xã Đông Lộc", "Xã Quế Phong", "Xã Tiền Phong"],
    "Tỉnh Đắk Lắk (VN)": ["Xã Ea M’Droh", "Xã Quảng Phú", "Xã Cuôr Đăng", "Xã Ea Tul", "Xã Krông Năng"],
    "Tỉnh Ninh Bình (VN)": ["Phường Nam Hoa Lư", "Phường Đông Hoa Lư", "Phường Tam Điệp", "Phường Yên Sơn"],
    "Thành Phố Cần Thơ (VN)": ["Phường Ninh Kiều", "Phường Cái Khế", "Phường Tân An", "Phường Bình Thủy"]
}

ISSUED_PLACE_LIST = ["Cục Cảnh sát quản lý hành chính về trật tự xã hội", "Thành phố Hồ Chí Minh", "Thành phố Hà Nội",
                     "Tỉnh Đắk Lắk", "Tỉnh Thanh Hóa"]


def get_fake_candidate_page1() -> CandidatePage1DTO:
    "random data cho mỗi lần chạy case"

    # Chọn ngẫu nhiên Tỉnh và Phường tương ứng cho Thường trú & Tạm trú
    perm_province = random.choice(list(LOCATION_MAP.keys()))
    perm_ward = random.choice(LOCATION_MAP[perm_province])

    temp_province = random.choice(list(LOCATION_MAP.keys()))
    temp_ward = random.choice(LOCATION_MAP[temp_province])

    # --- 1. Thông tin ngành nghề ---
    job_info = JobInfoDTO(
        job_apply=random.choice(JOB_APPLY_LIST),
        expertise=random.choice(EXPERTISE_LIST),
        rank=random.choice(RANK_LIST),
        work_location="Hồ Chí Minh",
        job_opening=random.choice(OPENING_LIST)
    )

    # --- 2. Thông tin cá nhân ---
    avatar_path = r"D:\Download\Copy.jpg"

    gender = random.choice(["Nam", "Nữ"])
    full_name = fake.name_male() if gender == "Nam" else fake.name_female()

    personal_info = PersonalInfoDTO(
        avatar_path=avatar_path,
        full_name=full_name,
        gender=gender,
        dob=fake.date_of_birth(minimum_age=20, maximum_age=45).strftime("%d/%m/%Y"),
        nationality=random.choice(NATIONALITY_LIST),
        place_of_birth=random.choice(list(LOCATION_MAP.keys())),
        ethnicity=random.choice(ETHNIC_LIST),
        religion=random.choice(RELIGION_LIST),
        citizen_id=fake.numerify("############"),
        issued_date="20/10/2021",
        issued_place=random.choice(ISSUED_PLACE_LIST)
    )

    # --- 3. Thông tin địa chỉ ---
    address_info = AddressDTO(
        perm_address=f"{random.randint(1, 999)} Đường {fake.street_name()}",
        perm_province=perm_province,
        perm_ward=perm_ward,
        temp_address=f"{random.randint(1, 999)} Đường {fake.street_name()}",
        temp_province=temp_province,
        temp_ward=temp_ward
    )

    # --- 4. Thông tin liên hệ & MXH ---
    contact_info = ContactSocialDTO(
        phone_1=fake.numerify("09########"),
        email=fake.free_email(),
        emergency_name=fake.name(),
        emergency_phone=fake.numerify("03########"),
        emergency_relation=random.choice(["Cha", "Mẹ", "Anh/Em", "Vợ/Chồng"]),
        facebook=f"https://facebook.com/{fake.user_name()}",
        linkedin=f"https://linkedin.com/in/{fake.user_name()}",
        marital_status=random.choice(MARITAL_LIST)
    )

    return CandidatePage1DTO(
        job_info=job_info,
        personal_info=personal_info,
        address_info=address_info,
        contact_info=contact_info
    )