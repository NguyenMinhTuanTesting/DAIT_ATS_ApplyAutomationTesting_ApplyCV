import allure
import os
from core.base_page import BasePage
from locators.ats_detail_candidate import ats_detail_candidate
from playwright.sync_api import expect


class ATSCandidateDetailPage(BasePage):

    def _compare_field(self, field_name, actual, expected):
        with allure.step(f"So sánh {field_name}"):
            # ghi log so sánh
            log_content = f"Dữ liệu kiểm tra: {field_name}\n"
            log_content += f"[-] Giá trị mong đợi (Expected): {expected}\n"
            log_content += f"[+] Giá trị tìm thấy (Actual)  : {actual}"

            allure.attach(log_content, name=f"Log_So_Sanh_{field_name}", attachment_type=allure.attachment_type.TEXT)

            assert actual == expected, f"❌ Lệch {field_name}!\n  + Mong đợi: {expected}\n  + Thực tế: {actual}"
            self.logger.info(f"✅ Khớp {field_name}: {actual}")

    @allure.step("So khớp thông tin ứng viên và 3 file tài liệu")
    def verify_candidate_e2e(self, candidate_dto):
        # 1. Đợi trang Detail hiện ra
        self.page.wait_for_selector(ats_detail_candidate.CANDIDATE_NAME, state="visible", timeout=10000)

        # 2. Trích xuất dữ liệu thực tế
        actual_name = self.page.locator(ats_detail_candidate.CANDIDATE_NAME).input_value()
        actual_email = self.page.locator(ats_detail_candidate.CANDIDATE_EMAIL).input_value()
        actual_school = self.page.locator(ats_detail_candidate.CANDIDATE_SCHOOL).input_value()
        actual_cccd = self.page.locator(ats_detail_candidate.CANDIDATE_CCCD).input_value()

        # 3. Thực hiện so sánh từng trường (Hiển thị chi tiết trên Allure)
        with allure.step("BƯỚC 10.1: Kiểm tra thông tin văn bản"):
            self._compare_field("Họ và Tên", actual_name, candidate_dto.page_1.full_name)
            self._compare_field("Email", actual_email, candidate_dto.page_1.email)
            self._compare_field("Số CCCD/Passport", actual_cccd, candidate_dto.page_1.citizen_id)
            self._compare_field("Trường học", actual_school, candidate_dto.page_2.school_name)

            # 4. Kiểm tra 3 file trong phần Others
            with allure.step("BƯỚC 10.2: Kiểm tra file đính kèm (Ảnh, PDF, Word)"):
                # KIỂM TRA: Nếu danh sách file rỗng (do Priority không chuẩn bị) thì bor qua
                if not candidate_dto.others_paths:
                    allure.attach("Dữ liệu Priority không có file Others. Bỏ qua bước kiểm tra này.",
                                  name="Skip_Notification",
                                  attachment_type=allure.attachment_type.TEXT)
                    self.logger.info("⚠️ Bỏ qua kiểm tra file Others vì dữ liệu trống.")
                    return  # KẾT THÚC BƯỚC CHECK FILE TẠI ĐÂY

                # Nếu có file thì mới chạy vòng lặp này
                for file_path in candidate_dto.others_paths:
                    file_name = os.path.basename(file_path)
                    with allure.step(f"Kiểm tra file: {file_name}"):
                        file_locator = self.page.locator(f"div[title*='{file_name}']")
                        try:
                            expect(file_locator).to_be_visible(timeout=5000)
                        except AssertionError:
                            self.take_screenshot(f"Missing_{file_name}")
                            raise AssertionError(f"❌ Không tìm thấy file {file_name}!")

        self.take_screenshot("Verify_ATS_Final_Success")