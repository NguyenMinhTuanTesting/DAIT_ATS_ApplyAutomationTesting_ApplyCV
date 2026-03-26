import json
import os
import random
import logging
from datetime import datetime, timedelta
from faker import Faker
from pathlib import Path
from typing import Any
from dto.candidate_dto import CandidateDTO, Page1DTO, Page2DTO, Page3DTO, Page4DTO

logger = logging.getLogger(__name__)


class CandidateGenerator:
    def __init__(self, dropdown_file: str = "data/dropdown_data.json",
                 priority_file: str = "data/priority_candidate.json"):
        self.fake = Faker('vi_VN')
        self.options = self._load_json(dropdown_file)
        self.priority_file = priority_file

        # Bản đồ các trường bắt buộc để kiểm tra tính hợp lệ của file Priority
        self.MANDATORY_MAP = {
            "page_1": [
                "job_opening", "job_apply", "expertise", "rank", "work_location",
                "full_name", "gender", "dob", "nationality", "place_of_birth",
                "ethnicity", "religion", "citizen_id", "issued_date", "issued_place",
                "permanent_address", "permanent_province", "permanent_district",
                "temporary_address", "temporary_province", "temporary_district",
                "phone_1", "email", "emergency_name", "emergency_phone", "emergency_relationship",
                "facebook", "linkedin", "marital_status"
            ],
            "page_2": [
                "father_name", "father_birth_year", "mother_name", "mother_birth_year",
                "edu_from", "edu_to", "school_name", "school_location", "department",
                "degree", "major", "ranking", "achievements",
                "language_name", "lang_listening", "lang_speaking", "lang_reading", "lang_writing"
            ],
            "page_3": [
                "career_from", "career_to", "career_type",
                "career_company", "career_industry", "career_position", "career_salary", "career_duty",
                "career_leaving_reason",
                "ref_name", "ref_position", "ref_company", "ref_relationship", "ref_phone"
            ],
            "page_4": [
                "overtime_intensity", "travel_availability", "passionate", "passionate_description",
                "earliest_start_date", "latest_start_date", "expected_start_date", "source",
                "min_expected_salary", "max_expected_salary",
                "bank_number", "bank_name", "bank_branch", "bank_owner_name"
            ]
        }

    def _load_json(self, file_path: str) -> Any:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def _get_random_files(self, folder_env_var: str, count: int = 1) -> list:
        folder_path = os.getenv(folder_env_var)
        if not folder_path:
            logger.error(f"Biến môi trường {folder_env_var} chưa được cấu hình!")
            return []

        # Chuẩn hóa đường dẫn tuyệt đối để tránh lỗi ký tự đặc biệt như \a
        folder = Path(os.path.normpath(folder_path.strip('"').strip("'")))

        if not folder.exists():
            logger.error(f"Thư mục không tồn tại: {folder.absolute()}")
            return []

        files = [str(f.absolute()) for f in folder.iterdir() if f.is_file()]

        if not files:
            logger.warning(f"Thư mục rỗng: {folder.absolute()}")
            return []

        selected = random.sample(files, min(len(files), count))
        logger.info(f"Đã bốc file cho {folder_env_var}: {[os.path.basename(f) for f in selected]}")
        return selected

    def is_priority_valid(self, data: dict) -> bool:
        if not data:
            return False
        missing_fields = []
        try:
            for page, fields in self.MANDATORY_MAP.items():
                if page not in data:
                    missing_fields.append(f"Mất trang {page}")
                    continue
                for field in fields:
                    val = data[page].get(field)
                    if val is None or str(val).strip() == "":
                        missing_fields.append(f"{page}.{field}")

            if missing_fields:
                print(f"\n[DEBUG] Priority THIẾU các trường sau: {missing_fields}")
                return False
            return True
        except Exception as e:
            logger.error(f"Lỗi validate priority: {e}")
            return False

    def generate_random_candidate(self) -> CandidateDTO:
        logger.info("--- Khởi tạo dữ liệu ngẫu nhiên (Random Mode) ---")

        # Bốc file thực tế từ ổ cứng
        avt_list = self._get_random_files("AVT_FOLDER", 1)
        cv_list = self._get_random_files("CV_FOLDER", 1)
        doc_list = self._get_random_files("DOC_FOLDER", 3)

        # Tạo Timeline giả lập hợp lý
        birth_date = self.fake.date_of_birth(minimum_age=23, maximum_age=35)
        dob_str = birth_date.strftime("%Y-%m-%d")
        issued_date = self.fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")

        edu_start_year = birth_date.year + 18
        edu_from, edu_to = f"{edu_start_year}-09", f"{edu_start_year + 4}-06"
        career_from = f"{edu_start_year + 5}-01"
        career_to = datetime.now().strftime("%Y-%m")

        full_name = self.fake.name().upper()
        p_province = random.choice(list(self.options["page_1"]["location_map"].keys()))
        p_district = random.choice(self.options["page_1"]["location_map"][p_province])

        data = {
            "page_1": {
                "job_opening": random.choice(self.options["page_1"]["job_opening"]),
                "job_apply": random.choice(self.options["page_1"]["job_apply"]),
                "expertise": random.choice(self.options["page_1"]["expertise"]),
                "rank": random.choice(self.options["page_1"]["rank"]),
                "work_location": "20 Trương Định,phường Xuân Hòa,TP Hồ Chí Minh",
                "avatar_path": avt_list[0] if avt_list else "",
                "full_name": full_name,
                "gender": random.choice(["Nam", "Nữ"]),
                "dob": dob_str,
                "height": str(random.randint(155, 185)),
                "weight": str(random.randint(45, 85)),
                "nationality": "Việt Nam",
                "place_of_birth": random.choice(self.options["page_1"]["personal_info"]["place_of_birth"]),
                "ethnicity": random.choice(self.options["page_1"]["personal_info"]["ethnicity"]),
                "religion": random.choice(self.options["page_1"]["personal_info"]["religion"]),
                "citizen_id": "0" + "".join([str(random.randint(0, 9)) for _ in range(11)]),
                "issued_date": issued_date,
                "issued_place": random.choice(self.options["page_1"]["personal_info"]["issued_place"]),
                "permanent_address": self.fake.street_address(),
                "permanent_province": p_province,
                "permanent_district": p_district,
                "temporary_address": self.fake.street_address(),
                "temporary_province": p_province,
                "temporary_district": p_district,
                "phone_1": f"09{random.randint(10000000, 99999999)}",
                "phone_2": f"03{random.randint(10000000, 99999999)}",
                "email": self.fake.free_email(),
                "emergency_name": self.fake.name(),
                "emergency_phone": f"08{random.randint(10000000, 99999999)}",
                "emergency_relationship": random.choice(["Bố", "Mẹ", "Anh", "Chị", "Bạn"]),
                "facebook": f"fb.com/{self.fake.user_name()}",
                "linkedin": f"linkedin.com/in/{self.fake.user_name()}",
                "marital_status": random.choice(self.options["page_1"]["marital_status"])
            },
            "page_2": {
                "father_name": self.fake.name_male(),
                "father_birth_year": str(birth_date.year - random.randint(25, 35)),
                "mother_name": self.fake.name_female(),
                "mother_birth_year": str(birth_date.year - random.randint(22, 30)),
                "edu_from": edu_from,
                "edu_to": edu_to,
                "school_name": f"Đại học {self.fake.city()}",
                "school_location": self.fake.city(),
                "department": "Khoa " + random.choice(["CNTT", "Kinh tế", "Kỹ thuật", "Ngoại ngữ"]),
                "degree": random.choice(self.options["page_2"]["degree"]),
                "major": random.choice(self.options["page_1"]["expertise"]),
                "ranking": random.choice(self.options["page_2"]["grade"]),
                "achievements": self.fake.sentence(nb_words=6),
                "language_name": random.choice(self.options["page_2"]["language"]),
                "lang_listening": random.choice(self.options["page_2"]["skill_options"]),
                "lang_speaking": random.choice(self.options["page_2"]["skill_options"]),
                "lang_reading": random.choice(self.options["page_2"]["skill_options"]),
                "lang_writing": random.choice(self.options["page_2"]["skill_options"])
            },
            "page_3": {
                "career_from": career_from,
                "career_to": career_to,
                "career_type": "Đi làm",
                "career_company": self.fake.company(),
                "career_industry": self.fake.bs(),
                "career_position": random.choice(self.options["page_1"]["job_opening"]),
                "career_salary": str(random.randint(15, 50) * 1000000),
                "career_duty": self.fake.catch_phrase(),
                "career_leaving_reason": "Thay đổi môi trường làm việc",
                "ref_name": self.fake.name(),
                "ref_position": "Quản lý trực tiếp",
                "ref_company": self.fake.company(),
                "ref_relationship": "Cấp trên",
                "ref_phone": f"07{random.randint(10000000, 99999999)}"
            },
            "page_4": {
                "overtime_intensity": random.choice(["Có", "Không", "Thỉnh thoảng"]),
                "travel_availability": random.choice(["Có", "Không", "Thỉnh thoảng"]),
                "passionate": self.fake.job(),
                "passionate_description": self.fake.paragraph(nb_sentences=2),
                "earliest_start_date": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
                "latest_start_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
                "expected_start_date": (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d"),
                "source": random.choice(["Facebook", "LinkedIn", "Website công ty"]),
                "min_expected_salary": str(random.randint(20, 30) * 1000000),
                "max_expected_salary": str(random.randint(35, 60) * 1000000),
                "bank_number": "".join([str(random.randint(0, 9)) for _ in range(12)]),
                "bank_name": "Vietcombank",
                "bank_branch": self.fake.city(),
                "bank_owner_name": full_name,
                "cv_file_path": cv_list[0] if cv_list else "",
                "document_paths": doc_list
            },
            "others_paths": doc_list  # Cấp dữ liệu cho thuộc tính mới của CandidateDTO
        }
        return CandidateDTO(**data)

    def get_candidate(self) -> CandidateDTO:
        priority_data = self._load_json(self.priority_file)

        # 1. Nếu Priority hợp lệ -> Sử dụng và gán thêm files Others để Verify
        if self.is_priority_valid(priority_data):
            logger.info("--- Sử dụng dữ liệu từ priority_candidate.json ---")

            # Đảm bảo vẫn có 3 file Others để thực hiện bước Verify trên ATS
            if "others_paths" not in priority_data:
                priority_data["others_paths"] = self._get_random_files("DOC_FOLDER", 3)

            return CandidateDTO(**priority_data)

        # 2. Nếu không hợp lệ -> Chuyển sang Random Mode
        print("\n[WARNING] file priority_candidate bị thiếu thông tin quan trọng. Kích hoạt Random Mode.")
        return self.generate_random_candidate()