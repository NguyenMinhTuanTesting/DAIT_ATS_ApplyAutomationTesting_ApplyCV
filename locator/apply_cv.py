from dataclasses import dataclass


@dataclass
class ApplyCVLocators_Base:
    TIEP_THEO = "//button[text()='Tiếp theo']"
    QUAY_LAI = "//button[text()='Quay lại']"
    LEN_DAU_TRANG = "//button[@id='go-to-top-btn']"
    THANH_TIM_KIEM = "//input[@type='search']"


@dataclass
class ApplyCVLocators_Page1:
    # tải CV
    TAI_CV = "//input[@id='cv_upload']"

    # ngành nghề ứng tuyển
    VI_TRI_UNG_TUYEN = "//span[@id='select2-job_opening_id-container']"
    NGANH_NGHE_UNG_TUYEN = "//span[@id='select2-job_apply-container']//span"
    LINH_VUC = "//span[@id='select2-expertise-container']//span"
    CAP_BAC = "//span[@id='select2-rank-container']//span"
    DIA_DIEM_LAM_VIEC = "//input[@id='work_location']"

    # avatar
    AVATAR = "//input[@id='avatar_file']"
    XOA_ANH = "//button[normalize-space()='Xóa ảnh']"

    # cá nhân
    HO_TEN_CA_NHAN = "//input[@id='family_name']"
    GIOI_TINH = "//div[@id='gender']//input"
    NGAY_SINH = "//input[@id='dob']"
    CHIEU_CAO = "//input[@id='height']"
    CAN_NANG = "//input[@id='weight']"
    QUOC_TICH = "//span[@id='select2-nationality-container']//span"
    NOI_SINH = "//span[@id='select2-place_of_birth-container']//span"
    DAN_TOC = "//span[@id='select2-ethnicity-container']//span"
    TON_GIAO = "//span[@id='select2-religion-container']//span"
    CCCD = "//input[@id='citizen_id']"
    NGAY_CAP_CCCD = "//input[@id='issued_date']"
    NOI_CAP_CCCD = "//span[@id='select2-issued_place-container']//span"

    # địa chỉ
    DIA_CHI_THUONG_TRU = "//input[@id='permanent_address']"
    THUONG_TRU_TINH = "//span[@id='select2-permanent_province-container']"
    THUONG_TRU_PHUONG = "//span[@id='select2-permanent_district-container']"
    DIA_CHI_TAM_TRU = "//input[@id='temporary_address']"
    TAM_TRU_TINH = "//span[@id='select2-temporary_province-container']"
    TAM_TRU_PHUONG = "//span[@id='select2-temporary_district-container']"

    # liên hệ
    SDT_1 = "//input[@id='mobile_phone_1']"
    SDT_2 = "//input[@id='mobile_phone_2']"
    EMAIL = "//input[@id='email']"
    TEN_NGUOI_LIEN_HE_KHAN = "//input[@id='emergency_name']"
    SDT_LIEN_HE_KHAN = "//input[@id='emergency_phone']"
    MOI_QUAN_HE_KHAN = "//input[@id='emergency_relationship']"

    # mạng xã hội
    FACEBOOK = "//input[@id='facebook']"
    LINKEDIN = "//input[@id='linkedin']"
    YOUTUBE = "//input[@id='youtube']"
    MANG_XA_HOI_KHAC = "//span[@id='select2-other_social_type-container']"
    THONG_TIN_MXH_KHAC = "//input[@id='other_social']"
    NUT_THEM_MXH_VN = "//div[text()='Thêm mạng xã hội khác']/.."
    NUT_THEM_MXH_EN = "//div[text()='Add other social']/.."

    # hôn nhân
    TINH_TRANG_HON_NHAN = "//span[@id='select2-marital_status-container']"
    SO_LUONG_CON = "//input[@id='children_status']"
    TUOI_CON = "//input[@id='children_age']"


@dataclass
class ApplyCVLocators_Page2:
    # option
    THUE_CO = "//div[@id='is_tax']//input"
    MA_SO_THUE = "//input[@id='tax_id']"
    THUE_KHONG = "//input[@name='is_tax' and @value='false']"

    BHXH_CO = "//div[@id='is_social_insurance_no']//input[@value='true']"
    MA_SO_BHXH = "//input[@id='social_insurance_no']"
    BHXH_KHONG = "//input[@name='is_social_insurance_no' and @value='true' ]"

    # gia đình
    TEN_CHA = "//input[@id='father_name']"
    NAM_SINH_CHA = "//input[@id='father_birth_year']"
    DIA_CHI_CHA = "//input[@id='father_permanent_address']"
    TEN_ME = "//input[@id='mother_name']"
    NAM_SINH_ME = "//input[@id='mother_birth_year']"
    DIA_CHI_ME = "//input[@id='mother_permanent_address']"
    QUAN_HE_THAN_NHAN_KHAC = "//span[@id='select2-family_relationship-container']"
    TEN_THAN_NHAN_KHAC = "//input[@id='member_family_name']"
    NAM_SINH_THAN_NHAN_KHAC = "//input[@id='family_birth_year']"
    DIA_CHI_THAN_NHAN_KHAC = "//input[@id='family_permanent_address']"
    NUT_THEM_THAN_NHAN_VN = "//div[text()='Thêm mối quan hệ khác']/.."
    NUT_THEM_THAN_NHAN_EN = "//div[text()='Add other relationships']/.."

    # trình độ học vấn
    HOC_BAT_DAU = "//input[@id='edu_from']"
    HOC_KET_THUC = "//input[@id='edu_from']"
    TEN_TRUONG = "//input[@id='edu_school_name']"
    DIA_CHI_TRUONG = "//input[@id='edu_location']"
    KHOA_TRUONG = "//input[@id='edu_department']"
    TRINH_DO_HOC_VAN = "//input[@id='select2-edu_degree-container']"
    NGANH_HOC = "//input[@id='edu_major']"
    DIEM_SO = "//input[@id='edu_grade']"
    XEP_LOAI_HOC_VAN = "//input[@name='edu_graduation_ranking']"
    HOC_CHUC_VU_BAT_DAU = "//input[@id='edu_role_from']"
    HOC_CHUC_VU_KET_THUC = "//input[@id='edu_role_to']"
    TEN_CHUC_VU_TRUONG = "//input[@id='edu_role_name']"
    NUT_THEM_CHUC_VU_VN = "//div[text()='Thêm chức vụ']/.."
    NUT_THEM_CHUC_VU_EN = "//div[text()='Adding position']/.."
    GIAI_THUONG_HOC_VAN = "//textarea[@id='edu_award']"
    NGOAI_KHOA_HOC_VAN = "//input[@id='edu_activity']"
    DOI_MOI_SANG_TAO_CO = "//input[@name='is_innovation_competition' and @value='true']"
    DOI_MOI_SANG_TAO_KHONG = "//input[@name='is_innovation_competition' and @value='false']"
    TEN_CUOC_THI="//input[@name='innovation_competition_name']"
    NUT_THEM_HOC_VAN_VN = "//div[text()='Thêm trình độ học vấn ']/.."
    NUT_THEM_HOC_VAN_EN = "//div[text()='Add education ']/.."

    # trình độ ngoại ngữ
    NGOAI_NGU_TUY_CHON = "//span[@id='select2-language_name-container']"
    NGOAI_NGU_BANG_CAP = "//input[@id='language_degree_name']"
    NGOAI_NGU_THOI_HAN = "//input[@id='language_exp_date']"
    NGOAI_NGU_TANG_NAM = "//span[@class='arrowUp']"
    NGOAI_NGU_GIAM_NAM = "//span[@class='arrowDown']"
    NGOAI_NGU_TANG_NAM_ALT = "//input[@id='edu_role_from']"
    NGOAI_NGU_CHON_THANG = "//div[@class='flatpickr-monthSelect-months']//span"
    NGOAI_NGU_NGHE = "//div[@id='listening_level']//input"
    NGOAI_NGU_NOI = "//div[@id='speaking_level']//input"
    NGOAI_NGU_DOC = "//div[@id='reading_level']//input"
    NGOAI_NGU_VIET = "//div[@id='writing_level']//input"
    NUT_THEM_NGOAI_NGU_VN = "//div[text()='Thêm ngoại ngữ']/.."
    NUT_THEM_NGOAI_NGU_EN = "//div[text()='Add foreign languages']/.."

    # công cụ AI
    CONG_CU_AI_TEN = "//input[@id='ai_tool_name']"
    CONG_CU_AI_THANH_THAO = "//div[@id='ai_tool_level']//input"
    NUT_THEM_CONG_CU_AI_VN = "//div[text()='Thêm công cụ']/.."
    NUT_THEM_CONG_CU_AI_EN = "//div[text()='Add tool']/.."

    # tin học văn phòng
    TIN_HOC_VAN_PHONG_TEN = "//input[@id='office_tech_name']"
    TIN_HOC_VAN_PHONG_THANH_THAO = "//div[@id='office_tech_level']//input"
    NUT_THEM_TIN_HOC_VN = "//div[text()='Thêm công cụ tin học']/.."
    NUT_THEM_TIN_HOC_EN = "//div[text()='Add informatics tools']/.."

    # chứng chỉ chuyên môn
    CHUNG_CHI_BAT_DAU = "//input[@id='professional_cert_from']"
    CHUNG_CHI_KET_THUC = "//input[@id='professional_cert_to']"
    CHUNG_CHI_TEN_TRUONG = "//input[@id='professional_cert_institute']"
    CHUNG_CHI_CHUYEN_NGANH = "//input[@id='professional_cert_major']"
    CHUNG_CHI_THOI_HAN = "//input[@id='professional_cert_date']"
    CHUNG_CHI_THANH_THAO = "//span[@id='select2-professional_cert_proficiency_level-container']"
    CHUNG_CHI_XEP_LOAI = "//div[@id='professional_cert_grade']//input"
    NUT_THEM_CHUNG_CHI_VN = "//div[text()='Thêm chứng chỉ chuyên môn']/.."
    NUT_THEM_CHUNG_CHI_EN = "//div[text()='Add professional certificates']/.."


@dataclass
class ApplyCVLocators_Page3:
    # quá trình làm việc
    QUA_TRINH_O_NHA = "//input[@value='Ở nhà']"
    QUA_TRINH_DI_LAM = "//input[@value='Đi làm']"
    QUA_TRINH_FREELANCE = "//input[@value='Freelancer']"
    QUA_TRINH_BAT_DAU = "//input[@id='career_from']"
    QUA_TRINH_KET_THUC = "//input[@id='career_to']"
    NUT_THEM_QUA_TRINH_VN = "//div[text()='Thêm quá trình']/.."
    NUT_THEM_QUA_TRINH_EN = "//div[text()='Add career']/.."

    # ở nhà
    LY_DO_O_NHA = "//textarea[@id='career_home_reason']"

    # đi làm
    QUA_TRINH_CONG_TY = "//input[@id='career_company_name']"
    QUA_TRINH_NGANH = "//input[@id='career_industry']"
    QUA_TRINH_QUY_MO = "//input[@id='career_company_size']"
    QUA_TRINH_DIA_CHI = "//input[@id='career_company_address']"
    QUA_TRINH_SDT_CONG_TY = "//input[@id='career_company_phone_number']"
    QUA_TRINH_CHUC_VU = "//input[@id='career_position']"
    QUA_TRINH_LUONG = "//input[@id='career_salary']"
    QUA_TRINH_NHIEM_VU = "//textarea[@id='career_duty']"
    QUA_TRINH_THANH_TICH = "//textarea[@id='career_achievement']"
    QUA_TRINH_LY_DO_NGHI_VIEC = "//textarea[@id='career_leaving_reason']"

    # freelance
    QUA_TRINH_MO_TA_FREELANCE = "//textarea[@id='career_freelance_description']"

    # người tham khảo
    THAM_KHAO_TEN = "//input[@id='reference_name']"
    THAM_KHAO_CHUC_VU = "//input[@id='reference_position']"
    THAM_KHAO_DON_VI = "//input[@id='reference_company_name']"
    THAM_KHAO_MOI_QUAN_HE = "//input[@id='reference_relationship']"
    THAM_KHAO_SDT = "//input[@id='reference_phone_number']"
    NUT_THEM_THAM_KHAO_VN = "//div[text()='Thêm người tham khảo']/.."
    NUT_THEM_THAM_KHAO_EN = "//div[text()='Add reference']/.."


@dataclass
class ApplyCVLocators_Page4:
    # thông tin khác
    KHAC_TANG_CA_CO = "//div[@id='overtime_intensity']//input[@value='Có']"
    KHAC_TANG_CA_KHONG = "//div[@id='overtime_intensity']//input[@value='Không']"
    KHAC_TANG_CA_THINHTHOANG = "//div[@id='overtime_intensity']//input[@value='Thỉnh thoảng']"
    KHAC_CONG_TAC_CO = "//div[@id='travel_availability']//input[@value='Có']"
    KHAC_CONG_TAC_KHONG = "//div[@id='travel_availability']//input[@value='Không']"
    KHAC_CONG_TAC_THINHTHOANG = "//div[@id='travel_availability']//input[@value='Thỉnh Thoảng']"
    KHAC_DAM_ME = "//input[@id='passionate']"
    KHAC_THE_HIEN_DAM_ME = "//input[@id='passionate_description']"
    #Người thân CT Group
    NGUOI_THAN_CTGROUP_CO = "//div[@id='has_acquaintance_in_company']//input[@value='Có']"
    NGUOI_THAN_CTGROUP_KHONG = "//div[@id='has_acquaintance_in_company']//input[@value='Không']"
    NGUOI_THAN_CTGROUP_TEN ="//input[@id='earliest_start_date']"
    NGUOI_THAN_CTGROUP_CONGTY = "//input[@id='acquaintance_company']"
    NGUOI_THAN_CTGROUP_CONGTAC = "//input[@id='acquaintance_position']"
    NGUOI_THAN_CTGROUP_MQH = "//input[@id='acquaintance_relationship']"

    THAM_GIA_TRUOC_CO = "//div[@id='applied_before']//input[@value='Có']"
    THAM_GIA_TRUOC_KHONG = "//div[@id='applied_before']//input[@value='Không']"
    THAM_GIA_TRUOC_NGAY ="//input[@id='applied_date']"
    THAM_GIA_TRUOC_CONGTY = "//input[@id='applied_company']"
    THAM_GIA_TRUOC_VITRI = "//input[@id='applied_position']"

    # thông tin nhận việc
    NHAN_VIEC_SOM_NHAT = "//input[@id='earliest_start_date']"
    NHAN_VIEC_MUON_NHAT = "//input[@id='latest_start_date']"
    NHAN_VIEC_MONG_MUON = "//input[@id='expected_start_date']"
    NGUON_UNG_VIEN_FACEBOOK = "//input[@id='facebook_source']"
    NGUON_UNG_VIEN_LINKEDIN = "//input[@id='linkedin_source']"
    NGUON_UNG_VIEN_WEBSITECTY = "//input[@id='website_source']"
    NGUON_UNG_VIEN_BANBE = "//input[@id='friends_source']"
    NGUON_UNG_VIEN_ANPHAM = "//input[@id='traditional_publication_source']"
    NGUON_UNG_VIEN_CONGTHONGTIN = "//input[@id='job_portal_source']"
    NGUON_UNG_VIEN_THAYCO = "//input[@id='lecturer_source']"
    NGUON_UNG_VIEN_KHAC ="//input[@id='other_source']"
    NGUON_UNG_VIEN_KHAC_NOIDUNG = "//input[@id='other_source_text']"
    NGUON_UNG_VIEN_TEN_THAYCO = "//input[@id='lecturer_name']"
    GOP_VON_CO = "//div[@id='has_invested']//input[@value='Có']"
    GOP_VON_KHONG = "//div[@id='has_invested']//input[@value='Không']"
    GOP_VON_CTY= "//input[@id='invested_company_name']"

    # thu nhập
    THU_NHAP_THAP_NHAT = "//input[@id='min_expected_salary']"
    THU_NHAP_CAO_NHAT = "//input[@id='max_expected_salary']"

    # số tài khoản
    TK_NGAN_HANG_SO = "//input[@id='bank_number']"
    TK_NGAN_HANG_TEN = "//input[@id='bank_name']"
    TK_NGAN_HANG_CHI_NHANH = "//input[@id='bank_branch']"
    TK_NGAN_HANG_CHU_TK = "//input[@id='bank_owner_name']"

    # upload tài liệu
    NHAP_TAI_LIEU = "//input[@accept='.jpg,.jpeg,.png,.pdf']"

    #confirm
    XAC_NHAN ="//input[@id='agree_terms']"