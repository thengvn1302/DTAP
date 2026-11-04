# Đối chiếu bản nộp và bản sửa (DTAP)

| File | Nội dung |
|---|---|
| `DTAP_changes_marked.pdf` | Bản đối chiếu: **nền vàng** = thêm, **chữ đỏ gạch ngang** = xóa, bảng/hình mới trong khung vàng, bảng/hình cũ trong khung viền đỏ. Mỗi thay đổi có mã `[Cn]` ở lề phải kèm ý kiến phản biện liên quan. Đầu file có **Bảng A** (danh sách mọi thay đổi) và **Bảng B** (ý kiến phản biện → các thay đổi). |
| `DTAP_OMS_revised_changes_marked.pdf` | **Bản nộp cho tạp chí** (tiếng Anh): cùng cách đánh dấu nhưng không có bảng kê tiếng Việt và mã `[Cn]`; có một khung chú giải ngắn dưới tiêu đề. Nộp file này cùng bản sạch `DTAP_OMS.pdf` và file nguồn LaTeX, vì Editor yêu cầu đánh dấu thay đổi. |
| `reviewer1_comments.txt` | Nguyên văn ý kiến của Reviewer 1 (nằm trong email của Editor). `referee_report.pdf` là của Reviewer 2. |
| `response_letter_draft.pdf` | Bản nháp response letter (tiếng Anh), trả lời từng ý kiến M1–M4, m1–m20 và liệt kê các thay đổi do tác giả tự làm. Số mục/bảng/trang lấy tự động từ bản Finally. Chữ xám `[Cn]` là mã nội bộ; chữ đỏ `[CẦN XÁC NHẬN: …]` là chỗ cần tác giả kiểm tra. Cả hai phải xóa trước khi gửi (xem đầu file `.tex`). |
| `change_notes.json` | Mô tả tiếng Việt và ý kiến phản biện cho từng mã `Cn`. Sửa file này rồi build lại để cập nhật Bảng A/B. |
| `review_comments.json` | Tóm tắt các ý kiến trong `referee_report.pdf`. |
| `build_diff.py`, `assemble.py` | Script tạo bản đối chiếu. |

## Cách đọc nhanh

1. Mở `DTAP_changes_marked.pdf`, đọc trang "Cách đọc tài liệu này".
2. Bảng B cho biết mỗi ý kiến phản biện đã được xử lý ở những mã nào (kèm số trang).
3. Bấm/tra mã `Cn` để xem chi tiết trong Bảng A, rồi lật tới trang tương ứng.

## Dựng lại

Cần TeX Live (pdflatex, lualatex, gói `lua-ul`, `luacolor`, `changebar`, `marginnote`), `latexdiff` và Python 3.

```bash
python3 build_diff.py          # tạo DTAP_changes_marked.pdf (bản nội bộ, tiếng Việt)
python3 build_diff.py --journal   # tạo DTAP_OMS_revised_changes_marked.pdf (bản cho tạp chí)
python3 build_diff.py --list   # chỉ in danh sách thay đổi
./build_response.sh            # tạo response_letter_draft.pdf
```

Script tự kiểm tra rằng mọi khối văn bản của cả hai bản đều xuất hiện đúng một lần trong file đối chiếu (dòng `coverage: …`) và báo các mã chưa có mô tả (`changes without a note`). Nếu sửa `main_document.tex`, số mã có thể thay đổi; khi đó cần xem lại `change_notes.json`.

Bản cũ được so sánh: `DTAP_submission/main_document_old.tex` (khớp `DTAP_OMS_submission.pdf`). Bản mới: `DTAP Finally/main_document.tex` (khớp `DTAP_OMS.pdf`).
