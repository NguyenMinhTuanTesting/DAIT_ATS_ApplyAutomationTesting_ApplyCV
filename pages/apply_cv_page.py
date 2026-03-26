import allure
from core.base_page import BasePage
from locators.apply_cv import ApplyCVLocators_Page1, ApplyCVLocators_Page2, \
    ApplyCVLocators_Page3, ApplyCVLocators_Page4, ApplyCVLocators_Base
from dto.candidate_dto import Page1DTO, Page2DTO, Page3DTO, Page4DTO


class ApplyCVPage(BasePage):

    @allure.step("Setup: Chuyển đổi ngôn ngữ sang Tiếng Việt")
    def setup_language_vi(self):
        self.click(ApplyCVLocators_Page1.LANGUAGE_DROPDOWN)
        self.click(ApplyCVLocators_Page1.VIETNAMESE_OPTION)
        self.page.wait_for_load_state("networkidle")

    # =================================================================
    # --- TRANG 1: THÔNG TIN CÁ NHÂN & NGÀNH NGHỀ ---
    # =================================================================
    @allure.step("Trang 1: Hoàn thiện thông tin cá nhân và ngành nghề")
    def fill_page_1(self, data: Page1DTO):
        # 1. Ngành nghề ứng tuyển (Select2)
        self.dropdown_by_search(ApplyCVLocators_Page1.NGANH_NGHE_UNG_TUYEN, data.job_apply)
        self.dropdown_by_search(ApplyCVLocators_Page1.LINH_VUC, data.expertise)
        self.dropdown_by_search(ApplyCVLocators_Page1.CAP_BAC, data.rank)
        self.type_and_verify(ApplyCVLocators_Page1.DIA_DIEM_LAM_VIEC, data.work_location)
        self.dropdown_by_search(ApplyCVLocators_Page1.VI_TRI_UNG_TUYEN, data.job_opening)

        # 2. Thông tin cá nhân
        if data.avatar_path:
            self.upload_file(ApplyCVLocators_Page1.AVATAR, data.avatar_path)

        self.type_and_verify(ApplyCVLocators_Page1.HO_TEN_CA_NHAN, data.full_name)

        gender_locator = ApplyCVLocators_Page1.GIOI_TINH_NAM if data.gender == "Nam" else ApplyCVLocators_Page1.GIOI_TINH_NU
        self.click(gender_locator)

        self.fill_date(ApplyCVLocators_Page1.NGAY_SINH, data.dob)

        if data.height: self.type_and_verify(ApplyCVLocators_Page1.CHIEU_CAO, data.height)
        if data.weight: self.type_and_verify(ApplyCVLocators_Page1.CAN_NANG, data.weight)

        self.dropdown_by_search(ApplyCVLocators_Page1.QUOC_TICH, data.nationality)
        self.dropdown_by_search(ApplyCVLocators_Page1.NOI_SINH, data.place_of_birth)
        self.dropdown_by_search(ApplyCVLocators_Page1.DAN_TOC, data.ethnicity)
        self.dropdown_by_search(ApplyCVLocators_Page1.TON_GIAO, data.religion)

        self.type_and_verify(ApplyCVLocators_Page1.CCCD, data.citizen_id)
        self.fill_date(ApplyCVLocators_Page1.NGAY_CAP_CCCD, data.issued_date)
        self.dropdown_by_search(ApplyCVLocators_Page1.NOI_CAP_CCCD, data.issued_place)

        # 3. Địa chỉ
        self.type_and_verify(ApplyCVLocators_Page1.DIA_CHI_THUONG_TRU, data.permanent_address)
        self.dropdown_by_search(ApplyCVLocators_Page1.THUONG_TRU_TINH, data.permanent_province)
        self.dropdown_by_search(ApplyCVLocators_Page1.THUONG_TRU_PHUONG, data.permanent_district)

        self.type_and_verify(ApplyCVLocators_Page1.DIA_CHI_TAM_TRU, data.temporary_address)
        self.dropdown_by_search(ApplyCVLocators_Page1.TAM_TRU_TINH, data.temporary_province)
        self.dropdown_by_search(ApplyCVLocators_Page1.TAM_TRU_PHUONG, data.temporary_district)

        # 4. Liên hệ & MXH
        self.type_and_verify(ApplyCVLocators_Page1.SDT_1, data.phone_1)
        if data.phone_2: self.type_and_verify(ApplyCVLocators_Page1.SDT_2, data.phone_2)
        self.type_and_verify(ApplyCVLocators_Page1.EMAIL, data.email)
        self.type_and_verify(ApplyCVLocators_Page1.TEN_NGUOI_LIEN_HE_KHAN, data.emergency_name)
        self.type_and_verify(ApplyCVLocators_Page1.SDT_LIEN_HE_KHAN, data.emergency_phone)
        self.type_and_verify(ApplyCVLocators_Page1.MOI_QUAN_HE_KHAN, data.emergency_relationship)

        if data.facebook: self.type_and_verify(ApplyCVLocators_Page1.FACEBOOK, data.facebook)
        if data.linkedin: self.type_and_verify(ApplyCVLocators_Page1.LINKEDIN, data.linkedin)

        self.dropdown_by_search(ApplyCVLocators_Page1.TINH_TRANG_HON_NHAN, data.marital_status)

        # Next to Page 2
        self.click(ApplyCVLocators_Base.TIEP_THEO)
        self.wait_for_visible(ApplyCVLocators_Page2.TEN_CHA)

    # =================================================================
    # --- TRANG 2: THUẾ, GIA ĐÌNH, HỌC VẤN ---
    # =================================================================
    @allure.step("Trang 2: Hoàn thiện thuế, gia đình và học vấn")
    def fill_page_2(self, data: Page2DTO):
        # 1. Thuế & BHXH (Giữ nguyên)
        if data.is_tax:
            self.click(ApplyCVLocators_Page2.THUE_CO)
            self.type_and_verify(ApplyCVLocators_Page2.MA_SO_THUE, data.tax_id)
        if data.is_social_insurance:
            self.click(ApplyCVLocators_Page2.BHXH_CO)
            self.type_and_verify(ApplyCVLocators_Page2.MA_SO_BHXH, data.social_insurance_no)

        # 2. Gia đình (Giữ nguyên)
        self.type_and_verify(ApplyCVLocators_Page2.TEN_CHA, data.father_name)
        self.type_and_verify(ApplyCVLocators_Page2.NAM_SINH_CHA, data.father_birth_year)
        self.type_and_verify(ApplyCVLocators_Page2.TEN_ME, data.mother_name)
        self.type_and_verify(ApplyCVLocators_Page2.NAM_SINH_ME, data.mother_birth_year)

        # 3. Học vấn
        self.fill_date(ApplyCVLocators_Page2.HOC_BAT_DAU, data.edu_from)
        self.fill_date(ApplyCVLocators_Page2.HOC_KET_THUC, data.edu_to)
        self.type_and_verify(ApplyCVLocators_Page2.TEN_TRUONG, data.school_name)
        self.type_and_verify(ApplyCVLocators_Page2.DIA_CHI_TRUONG, data.school_location)
        self.type_and_verify(ApplyCVLocators_Page2.KHOA_TRUONG, data.department)
        self.dropdown_by_search(ApplyCVLocators_Page2.TRINH_DO_HOC_VAN, data.degree)
        self.type_and_verify(ApplyCVLocators_Page2.NGANH_HOC, data.major)

        ranking_xpath = f"{ApplyCVLocators_Page2.XEP_LOAI_HOC_VAN}[@value='{data.ranking}']"
        self.click(ranking_xpath)

        # --- ĐÂY LÀ KHÚC BỊ THIẾU ---
        if data.achievements:
            self.type_and_verify(ApplyCVLocators_Page2.GIAI_THUONG_HOC_VAN, data.achievements)

        # BẮT BUỘC: Phải click "Thêm trình độ học vấn" để hệ thống render list dữ liệu
        self.click(ApplyCVLocators_Page2.NUT_THEM_HOC_VAN_VN)
        # ---------------------------

        # 4. Ngoại ngữ
        self.dropdown_by_search(ApplyCVLocators_Page2.NGOAI_NGU_TUY_CHON, data.language_name)
        self.click(f"{ApplyCVLocators_Page2.NGOAI_NGU_NGHE}[@value='{data.lang_listening}']")
        self.click(f"{ApplyCVLocators_Page2.NGOAI_NGU_NOI}[@value='{data.lang_speaking}']")
        self.click(f"{ApplyCVLocators_Page2.NGOAI_NGU_DOC}[@value='{data.lang_reading}']")
        self.click(f"{ApplyCVLocators_Page2.NGOAI_NGU_VIET}[@value='{data.lang_writing}']")

        # BẮT BUỘC: Phải click "Thêm ngoại ngữ"
        self.click(ApplyCVLocators_Page2.NUT_THEM_NGOAI_NGU_VN)

        # Next to Page 3
        self.click(ApplyCVLocators_Base.TIEP_THEO)
        # Chờ locator Page 3 xuất hiện thực sự
        self.wait_for_visible(ApplyCVLocators_Page3.QUA_TRINH_DI_LAM)

    # =================================================================
    # --- TRANG 3: QUÁ TRÌNH LÀM VIỆC ---
    # =================================================================
    @allure.step("Trang 3: Hoàn thiện quá trình làm việc và tham chiếu")
    def fill_page_3(self, data: Page3DTO):
        # Dùng fill_date thay vì type_and_verify
        self.fill_date(ApplyCVLocators_Page3.QUA_TRINH_BAT_DAU, data.career_from)
        self.fill_date(ApplyCVLocators_Page3.QUA_TRINH_KET_THUC, data.career_to)

        if data.career_type == "Đi làm":
            self.click(ApplyCVLocators_Page3.QUA_TRINH_DI_LAM)
            self.type_and_verify(ApplyCVLocators_Page3.QUA_TRINH_CONG_TY, data.career_company)
            self.type_and_verify(ApplyCVLocators_Page3.QUA_TRINH_NGANH,data.career_position)
            self.type_and_verify(ApplyCVLocators_Page3.QUA_TRINH_CHUC_VU, data.career_position)
            self.type_currency(ApplyCVLocators_Page3.QUA_TRINH_LUONG, data.career_salary)
            self.type_and_verify(ApplyCVLocators_Page3.QUA_TRINH_NHIEM_VU,data.career_duty)
            self.type_and_verify(ApplyCVLocators_Page3.QUA_TRINH_LY_DO_NGHI_VIEC,data.career_leaving_reason)
            self.click(ApplyCVLocators_Page3.NUT_THEM_QUA_TRINH_VN)


        # Người tham khảo
        self.type_and_verify(ApplyCVLocators_Page3.THAM_KHAO_TEN, data.ref_name)
        self.type_and_verify(ApplyCVLocators_Page3.THAM_KHAO_CHUC_VU,data.ref_position)
        self.type_and_verify(ApplyCVLocators_Page3.THAM_KHAO_SDT, data.ref_phone)
        self.type_and_verify(ApplyCVLocators_Page3.THAM_KHAO_DON_VI, data.ref_company)
        self.type_and_verify(ApplyCVLocators_Page3.THAM_KHAO_MOI_QUAN_HE, data.ref_relationship)
        self.click(ApplyCVLocators_Page3.NUT_THEM_THAM_KHAO_VN)

        self.click(ApplyCVLocators_Base.TIEP_THEO)
        self.wait_for_visible(ApplyCVLocators_Page4.NHAN_VIEC_SOM_NHAT)

    # =================================================================
    # --- TRANG 4: THU NHẬP & HOÀN TẤT ---
    # =================================================================
    @allure.step("Trang 4: Hoàn thiện thu nhập và gửi hồ sơ")
    def fill_page_4(self, data: Page4DTO):
        # 1. Thông tin khác
        self.click(ApplyCVLocators_Page4.KHAC_TANG_CA_KHONG)
        self.click(ApplyCVLocators_Page4.KHAC_CONG_TAC_KHONG)
        self.type_and_verify(ApplyCVLocators_Page4.KHAC_DAM_ME, data.passionate)
        self.type_and_verify(ApplyCVLocators_Page4.KHAC_THE_HIEN_DAM_ME, data.passionate_description)

        # 2. Nhận việc & Thu nhập
        self.fill_date(ApplyCVLocators_Page4.NHAN_VIEC_SOM_NHAT, data.earliest_start_date)
        self.fill_date(ApplyCVLocators_Page4.NHAN_VIEC_MUON_NHAT, data.latest_start_date)
        self.fill_date(ApplyCVLocators_Page4.NHAN_VIEC_MONG_MUON, data.expected_start_date)

        self.type_currency(ApplyCVLocators_Page4.THU_NHAP_THAP_NHAT, data.min_expected_salary)
        self.type_currency(ApplyCVLocators_Page4.THU_NHAP_CAO_NHAT, data.max_expected_salary)

        # 3. Ngân hàng
        self.type_and_verify(ApplyCVLocators_Page4.TK_NGAN_HANG_SO, data.bank_number)
        self.dropdown_by_search(ApplyCVLocators_Page4.TK_NGAN_HANG_TEN, data.bank_name)
        self.type_and_verify(ApplyCVLocators_Page4.TK_NGAN_HANG_CHI_NHANH, data.bank_branch)
        self.type_and_verify(ApplyCVLocators_Page4.TK_NGAN_HANG_CHU_TK, data.bank_owner_name)

        # 4. UPLOAD TÀI LIỆU
        # Bước A: Upload CV chính
        if data.cv_file_path:
            self.upload_file(ApplyCVLocators_Page4.NHAP_TAI_LIEU, data.cv_file_path)
            self.logger.info("Đã upload CV, chờ 3 giây trước khi upload documents...")
            self.page.wait_for_timeout(3000)

        # Bước B: Upload 3 file others ngẫu nhiên (mỗi file cách nhau 5s)
        if data.document_paths:
            for i, doc_path in enumerate(data.document_paths):
                self.logger.info(f"Đang import document {i + 1}: {doc_path}")
                # Lưu ý: Hàm này sẽ append file nếu web hỗ trợ, hoặc set lại danh sách file
                self.upload_file(ApplyCVLocators_Page4.NHAP_TAI_LIEU, doc_path)

                # Không đợi ở file cuối cùng để tối ưu
                if i < len(data.document_paths) - 1:
                    self.logger.info("Đợi 5 giây cho file tiếp theo...")
                    self.page.wait_for_timeout(5000)

        # 5. Cam kết & Hoàn thành
        self.set_checked(ApplyCVLocators_Page4.XAC_NHAN, data.agree_terms)
        self.click(ApplyCVLocators_Page4.HOAN_THANH)
        self.page.wait_for_timeout(5000)