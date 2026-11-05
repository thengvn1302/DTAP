# Đối chiếu bản nộp và bản sửa (DTAP)

| File | Nội dung |
|---|---|
| `DTAP_changes_marked.pdf` | Bản đối chiếu: **nền vàng** = thêm, **chữ đỏ gạch ngang** = xóa, bảng/hình mới trong khung vàng, bảng/hình cũ trong khung viền đỏ. Mỗi thay đổi có mã `[Cn]` ở lề phải kèm ý kiến phản biện liên quan. Đầu file có **Bảng A** (danh sách mọi thay đổi) và **Bảng B** (ý kiến phản biện → các thay đổi). |
| `../DTAP Finally/main_document_colored.tex`, `../DTAP Finally/DTAP_OMS_colored.pdf` | **Bản sửa có chữ đỏ** theo yêu cầu của Editor. So sánh theo nội dung từng câu: bỏ qua thay đổi chỉ về hình thức (dtap/DTAP, in đậm, cách đánh số tham chiếu, ngắt dòng công thức); câu sửa ít thì chỉ chữ mới đỏ, câu sửa từ một nửa trở lên hoặc câu mới thì đỏ cả câu; ô bảng so với đúng dòng/cột của bảng cũ. References để đen. Bản gốc `main_document.tex` giữ nguyên. Tạo bằng `python3 make_colored.py`. |
| `reviewer1_comments.txt` | Nguyên văn ý kiến của Reviewer 1 (nằm trong email của Editor). `referee_report.pdf` là của Reviewer 2. |
| `../DTAP Finally/main_document_v2.tex`, `../DTAP Finally/DTAP_OMS_v2.pdf` | **Bản sao đã áp dụng toàn bộ đề xuất** trong `proposed_edits.md` (trừ các mục ghi "Giữ nguyên"). Bản `main_document.tex` giữ nguyên. Tạo bằng `python3 apply_proposals.py`. Nếu dùng bản này thì cần cập nhật các câu trích trong response letter (R1.1, R1.2, R1.3, M-mục về Combettes) và dựng lại bản tô đỏ. |
| `../DTAP Finally/response_letter.tex`, `../DTAP Finally/response_letter.pdf` | **Bản response letter cuối để nộp** (bản sao của `response_letter_draft.tex`, biên dịch độc lập bằng `lualatex`). |
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
python3 build_diff.py          # tạo DTAP_changes_marked.pdf
python3 build_diff.py --list   # chỉ in danh sách thay đổi
python3 make_colored.py        # tạo bản sao có chữ đỏ main_document_colored.tex + DTAP_OMS_colored.pdf
python3 apply_proposals.py     # tạo main_document_v2.tex (áp dụng mọi đề xuất); biên dịch bằng pdflatex
./build_response.sh            # tạo response_letter_draft.pdf
```

Script tự kiểm tra rằng mọi khối văn bản của cả hai bản đều xuất hiện đúng một lần trong file đối chiếu (dòng `coverage: …`) và báo các mã chưa có mô tả (`changes without a note`). Nếu sửa `main_document.tex`, số mã có thể thay đổi; khi đó cần xem lại `change_notes.json`.

Bản cũ được so sánh: `DTAP_submission/main_document_old.tex` (khớp `DTAP_OMS_submission.pdf`). Bản mới: `DTAP Finally/main_document.tex` (khớp `DTAP_OMS.pdf`).
