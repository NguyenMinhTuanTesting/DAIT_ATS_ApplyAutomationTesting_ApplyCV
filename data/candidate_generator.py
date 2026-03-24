import json
import os
import random
from datetime import datetime, timedelta
from faker import Faker
from dto.candidate_dto import CandidateDTO


class CandidateGenerator:
    def __init__(self, dropdown_file: str = "data/dropdown_data.json",
                 priority_file: str = "data/priority_candidate.json"):
        self.fake = Faker('vi_VN')
        self.options = self._load_json(dropdown_file)
        self.priority_file = priority_file

        # Danh sách trường bắt buộc để check fallback
        self.mandatory_fields = [
            "full_name", "email", "phone_1", "citizen_id",
            "job_apply", "expertise", "rank", "job_opening",
            "permanent_province", "permanent_district"
        ]

    def _load_json(self, file_path: str):
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}

    # --- HELPER: Tạo ngày ngẫu nhiên định dạng ISO YYYY-MM-DD ---
    def _get_random_date(self, start_year: int, end_year: int) -> str:
        date = self.fake.date_between(start_date=f'-{2026-start_year}y', end_date=f'-{2026-end_year}y')
        return date.strftime("%Y-%m-%d")

    def is_priority_valid(self, priority_data: dict) -> bool:
        if not priority_data or "page_1" not in priority_data:
            return False
        p1 = priority_data["page_1"]
        return all(str(p1.get(f, "")).strip() != "" for f in self.mandatory_fields)

    def generate_random_candidate(self) -> CandidateDTO:
        # --- Page 1 Random Logic ---
        p_province = random.choice(list(self.options["page_1"]["location_map"].keys()))
        p_ward = random.choice(self.options["page_1"]["location_map"][p_province])
        full_name = self.fake.name().upper()
        cccd = "0" + "".join([str(random.randint(0, 9)) for _ in range(11)])

        # --- Page 4 Date Logic ---
        today = datetime.now()
        earliest = today + timedelta(days=random.randint(2, 5))
        expected = earliest + timedelta(days=random.randint(2, 5))
        latest = expected + timedelta(days=random.randint(5, 10))

        # --- Salary Logic ---
        min_salary = random.randint(15, 25) * 1000000
        max_salary = min_salary + (random.randint(5, 15) * 1000000)

        data = {
            "page_1": {
                "full_name": full_name,
                "email": self.fake.email(),
                "phone_1": f"09{random.randint(10000000, 99999999)}",
                "phone_2": random.choice([f"028{random.randint(10000000, 99999999)}", ""]),
                "citizen_id": cccd,
                "job_apply": random.choice(self.options["page_1"]["job_apply"]),
                "expertise": random.choice(self.options["page_1"]["expertise"]),
                "rank": random.choice(self.options["page_1"]["rank"]),
                "job_opening": random.choice(self.options["page_1"]["job_opening"]),
                "dob": self.fake.date_of_birth(minimum_age=22, maximum_age=40).strftime("%Y-%m-%d"),
                "gender": random.choice(["Nam", "Nữ"]),
                "nationality": "Việt Nam",
                "place_of_birth": random.choice(self.options["page_1"]["personal_info"]["place_of_birth"]),
                "ethnicity": random.choice(self.options["page_1"]["personal_info"]["ethnicity"]),
                "religion": random.choice(self.options["page_1"]["personal_info"]["religion"]),
                "issued_date": self._get_random_date(2015, 2023), # Đã dùng helper
                "issued_place": random.choice(self.options["page_1"]["personal_info"]["issued_place"]),
                "permanent_address": self.fake.street_address(),
                "permanent_province": p_province,
                "permanent_district": p_ward,
                "temporary_address": self.fake.street_address(),
                "temporary_province": p_province,
                "temporary_district": p_ward,
                "emergency_name": self.fake.name(),
                "emergency_phone": f"03{random.randint(10000000, 99999999)}",
                "emergency_relationship": random.choice(["Bố", "Mẹ", "Anh", "Chị", "Bạn"]),
                "marital_status": random.choice(self.options["page_1"]["marital_status"]),
                "work_location": "Văn phòng Tập đoàn CT",
                "facebook": f"https://fb.com/{self.fake.user_name()}",
                "linkedin": f"https://linkedin.com/in/{self.fake.user_name()}"
            },
            "page_2": {
                "edu_from": "2016-09", "edu_to": "2020-06", # Chuyển sang YYYY-MM
                "school_name": f"Đại học {self.fake.city()}",
                "school_location": self.fake.city(),
                "department": "Kỹ thuật",
                "degree": random.choice(self.options["page_2"]["degree"]),
                "major": random.choice(self.options["page_1"]["expertise"]),
                "ranking": random.choice(self.options["page_2"]["grade"]),
                "language_name": random.choice(self.options["page_2"]["language"]),
                "lang_listening": random.choice(self.options["page_2"]["skill_options"]),
                "lang_speaking": random.choice(self.options["page_2"]["skill_options"]),
                "lang_reading": random.choice(self.options["page_2"]["skill_options"]),
                "lang_writing": random.choice(self.options["page_2"]["skill_options"]),
                "is_tax": random.choice([True, False]),
                "is_social_insurance": random.choice([True, False])
            },
            "page_3": {
                "career_from": "2021-01", "career_to": "2024-01", # Chuyển sang YYYY-MM
                "career_type": random.choice(["Đi làm", "Ở nhà", "Freelancer"]),
                "career_company": self.fake.company(),
                "career_position": random.choice(self.options["page_1"]["job_opening"]),
                "career_salary": str(random.randint(15, 35) * 1000000),
                "ref_name": self.fake.name(),
                "ref_phone": f"09{random.randint(10000000, 99999999)}",
                "ref_position": "Quản lý trực tiếp",
                "ref_company": self.fake.company(),
                "ref_relationship": random.choice(self.options["page_2"]["other_relationship"])
            },
            "page_4": {
                "overtime_intensity": random.choice(["Có", "Không", "Thỉnh thoảng"]),
                "travel_availability": random.choice(["Có", "Không", "Thỉnh thoảng"]),
                "passionate": self.fake.job(),
                "passionate_description": self.fake.sentence(),
                "earliest_start_date": earliest.strftime("%Y-%m-%d"), # ISO format
                "expected_start_date": expected.strftime("%Y-%m-%d"), # ISO format
                "latest_start_date": latest.strftime("%Y-%m-%d"), # ISO format
                "source": random.choice(["Facebook", "LinkedIn", "Website công ty", "Bạn bè đồng nghiệp"]),
                "min_expected_salary": str(min_salary),
                "max_expected_salary": str(max_salary),
                "bank_number": "".join([str(random.randint(0, 9)) for _ in range(10)]),
                "bank_name": random.choice(["Vietcombank", "Techcombank", "MB Bank", "ACB"]),
                "bank_branch": self.fake.city(),
                "bank_owner_name": full_name
            }
        }
        return CandidateDTO(**data)

    def get_candidate(self) -> CandidateDTO:
        priority_data = self._load_json(self.priority_file)
        if self.is_priority_valid(priority_data):
            return CandidateDTO(**priority_data)
        return self.generate_random_candidate()