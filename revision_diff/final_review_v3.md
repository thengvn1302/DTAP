# Rà soát lần cuối bản v3 (bài + response letter)

Bài mẫu dùng làm chuẩn văn phong và bố cục: Boţ, Csetnek, Meier, *Optimization Methods & Software* 34(3):489–514, 2019 (cùng tạp chí; cùng mảng thuật toán chiếu/tách, hội tụ mạnh, thí nghiệm trên bài toán chấp nhận tách; **không** cùng lớp bài toán NSFP giả lồi).

File được rà: `DTAP Finally v3/main_document.tex` (commit `930f266`, trùng `revision/revision_clean.tex` trên repo đồng nghiệp) và `DTAP Finally v3/response_letter.tex`. Số dòng dưới đây là số dòng trong `main_document.tex`.

Mức độ: **A = lỗi, phải sửa**; **B = bố cục**; **C = lặp nội dung**; **D = văn phong câu**; **E = letter**; **F = hình thức/khác**.

---

## A. Lỗi phải sửa (sai nghĩa, tham chiếu hỏng, đại từ mơ hồ, dấu câu)

| # | Dòng | Hiện tại | Vấn đề | Hướng sửa |
|---|---|---|---|---|
| A1 | 815 | "…for SG-const, with the same exclusions as above, **in the environment stated below**." | Đoạn Reproducibility (nơi nêu môi trường chạy) đã bị xoá, nên "stated below" trỏ vào chỗ không còn tồn tại. | Bỏ cụm "in the environment stated below". |
| A2 | 811 | "At κ=3, DTAP and the balanced variant need a median of 4. These counts exclude the 147 331 evaluations of **its** tuning search." | Sau khi tách câu, "its" đứng ngay sau câu về DTAP/biến thể cân bằng, nên đọc thành tuning của DTAP (DTAP không được tinh chỉnh). | Ghi rõ "of the tuned SG-const search" và đặt ngay sau câu về tuned SG-const. |
| A3 | 776 | "Tuning raises SG-dyn's standard-start success count from 5/9 to 9/9. **It** can outperform DTAP, for example on Abalone…" | "It" có thể hiểu là "Tuning". | "Tuned SG-dyn can outperform DTAP, for example on Abalone (3 versus 48 evaluated points)…" |
| A4 | 643–645 | Công thức Nogueira kết thúc bằng dấu chấm, rồi đoạn mới mở đầu bằng "where $\bar Z_j=…$" | Sai dấu câu: "where" không thể bắt đầu một câu mới. | Bỏ dấu chấm cuối công thức (hoặc đổi "where" thành "Here"). |
| A5 | 150 | "Formula (Jdef) gives a closed-form feasibility residual **whose maximizers** identify the most violated constraints." | Sai nghĩa: "maximizers" của $J$ là các điểm $x$; ý đúng là **các chỉ số** đạt max. | "…whose maximizing indices identify the most violated constraints." |
| A6 | 228 / 591 | Remark 6 (chi phí mỗi vòng lặp cho bài chọn đặc trưng) không được dẫn ở đâu; dòng 228 lại trỏ chung "Section 3.1". | Remark bị "mồ côi"; câu dẫn không chính xác. | Dòng 228: "…is given in Remark 6." |
| A7 | 72, 136 | "Tchebyshev scalarization" có trong keywords và tiêu đề Mục 2.1 nhưng không được giải thích ở đâu trong văn bản. | Thuật ngữ treo. | Thêm cụm "(a Tchebyshev scalarization of the constraint residuals)" vào câu đo residual bằng chuẩn sup ở 2.1. |

## B. Bố cục

| # | Vị trí | Vấn đề | Hướng sửa |
|---|---|---|---|
| B1 | Mục 3.4 | Bài thử phi lồi (công thức (45), Bảng 7–8, khoảng 600 từ) nằm dưới một tiêu đề đoạn bên trong Mục 3.4 "Constraint activity and a tuned subgradient comparison"; tiêu đề mục không bao quát phần này, trong khi đây là thí nghiệm trả lời trực tiếp R1.4. Mục 3.4 hiện dài khoảng 1 200 từ với 3 bảng, Mục 3.3 chỉ khoảng 300 từ. | Tách thành **Mục 3.5 "A nonconvex pseudoconvex test problem"**; đổi tiêu đề đoạn "Protocol and tuning cost" thành đoạn văn thường. Letter phải đổi các chỗ dẫn "Sec. 3.4" cho (45), Bảng 7–8 thành "Sec. 3.5" (R1.1, R1.4, R1.5, gạch đầu dòng tóm tắt). |
| B2 | Mục 3.1 / 3.2 | Hai tên mục gần trùng: "Problem setup" và "Experimental setup"; "Problem setup" không cho biết nội dung. | Đổi 3.1 thành "Feature selection as a normal-box NSFP". |
| B3 | Mục 2 / 2.3 | Tên Mục 2 "The DTAP algorithm and its convergence analysis" trùng một phần tên Mục 2.3 "The DTAP algorithm". | Đổi tên Mục 2 thành "Algorithm and convergence analysis". |
| B4 | Phần sau Kết luận | Tên mục theo kiểu Elsevier: "Declaration of competing interest", "Data availability". Bài mẫu Taylor & Francis dùng "Disclosure statement", "Funding", "ORCID". | Đổi thành "Disclosure statement" và "Data availability statement". |

Đã kiểm tra, **không** còn mục nào chỉ là một đoạn ngắn: Mục 2.1, 2.4, 2.5, 2.6 đều có định lý/bổ đề và chứng minh; 3.2 mở đầu bằng phần dữ liệu; kết luận một đoạn là đúng như letter M1 cam kết.

## C. Lặp nội dung

| # | Vị trí | Nội dung lặp | Hướng sửa |
|---|---|---|---|
| C1 | 103, 153, 237, 260, 276 | Ý "nhánh lồi có bất đẳng thức gradient, nhánh giả lồi chỉ có dấu" xuất hiện 5 lần (Intro ¶4, đầu 2.2, đoạn mở 2.4, câu dẫn Lemma 2.6 và 2.7). Đoạn mở 2.4 còn lặp lộ trình Stage 2–3 của đoạn mở 2.6. | Rút đoạn mở 2.4 còn một câu dẫn ("The following lemmas are used repeatedly below."), giữ các câu dẫn ngắn trước Lemma 2.6/2.7. |
| C2 | 95, 134, 185 | "Ω là tập lồi" nêu 3 lần (Intro, cuối phần chuẩn bị, sau Assumption 1). | Bỏ câu ở Intro (95); giữ lập luận đầy đủ sau Assumption 1. |
| C3 | 96–99 | Công thức $J(x)$ được hiển thị ở Intro rồi định nghĩa lại, kèm chứng minh, ở Mục 2.1. | Bỏ công thức hiển thị ở Intro; giữ một câu "the max-type violation $J$ of Section 2.1". |
| C4 | 496, 499 | Mở đầu Mục 3 và câu đầu Mục 3.1 cùng nói "cast feature selection as a normal-box NSFP". | Bỏ câu đầu của 3.1. |
| C5 | 499, 526, 555 | Ba lần trỏ "Section 3.2.1" cho phần solver. | Bỏ câu "The solvers are described in Section 3.2.1." ở 499. |
| C6 | 496, 596, 600 | "Movement Libras chỉ dùng cho solver diagnostic" nêu 3 lần. | Bỏ câu này khỏi chú thích Bảng 1. |
| C7 | 619, 635 | $\theta=0.9$ nêu 2 lần (Solvers và Evaluation protocol). | Bỏ ở 619. |
| C8 | 654, 656, 679, 702 | "SG trùng mask với DTAP trên 7 bộ" nêu 4 lần (hai câu ở 3.3, chú thích và ghi chú Bảng 3). | Câu p-value (656) chỉ cần "All DTAP–SG p-values equal 1." |
| C9 | 815 | Trong cùng một đoạn, ý "δ=10⁻¹ cho cùng dãy lặp" nêu 2 lần. | Gộp làm một. |
| C10 | 68, 107, 228, 463 | "Không cần chuẩn toán tử/hằng số" nêu ở Abstract, C1, đoạn chi phí (228), Remark 3. | Tuỳ chọn: bỏ câu "It uses neither an operator-norm estimate nor a line search." ở 228 (Remark 3 được letter trích nên giữ). |

## D. Văn phong từng câu

| # | Dòng | Hiện tại | Hướng sửa |
|---|---|---|---|
| D1 | 117 | "All convergence statements concern the norm topology. Bounded sequences have convergent subsequences." (hai câu hiển nhiên trong $\mathbb R^n$) | "Since $H$ is finite-dimensional, bounded sequences have convergent subsequences." |
| D2 | 188 | "combines the two track-specific **step sizes**" (thực ra kết hợp hai bước cập nhật) | "combines the two track-specific updates". |
| D3 | 228 | "The cost is dominated by … The cost for the feature-selection instance is given …" (lặp "cost") | Gộp cùng A6. |
| D4 | 501 | "Here $n$ is the number of samples and $p$ the number of features." (thừa: $x_1..x_n$, $a_1..a_p$ vừa được định nghĩa) | Bỏ câu. |
| D5 | 554 | "the weight of misclassifying features per sample" (khó hiểu) | "the total weight of the features that misclassify each sample". |
| D6 | 571 | "Consequently, … Hence, …" hai từ nối kết luận liên tiếp trong Proposition 3.1 | Gộp: "Consequently, (nsfp-fs) is an all-convex normal-box NSFP and satisfies (A1)–(A2) with $U=U_\rho$ whenever $\Omega\ne\varnothing$." |
| D7 | 583 | "Prescribed thresholds would be used as given." (lửng, thức giả định) | "Thresholds prescribed by an application are used as given." |
| D8 | 654 | "…while retaining more features. These differences reflect a trade-off …, since the methods select subsets of different sizes." (hai ý trùng nhau) | Gộp: "…while retaining more features, so these differences reflect a trade-off between subset size and predictive accuracy." |
| D9 | 654 | "Fold-wise stability can differ even when the final voted mask is identical." (câu treo cuối đoạn) | Đặt ngay sau câu về mask của SG, kèm ví dụ (Segmentation: 0.800 so với 0.888). |
| D10 | 774 | Số liệu quá chi li: $J^{\rm ps}_0\approx1.56\times10^{-3}$, $J^{\rm cvx}_0\approx366.3$, $|J_{\rm DTAP}-J_{\rm AC}|\le3.18\times10^{-5}J_{\rm AC}$ | Giữ $1-\mu_0\approx4.27\times10^{-6}$ và "both runs stop after 48 evaluated points"; bỏ phần còn lại. |
| D11 | 467 | Remark 4: "…avoiding a 'finitely many indices' extraction." (khẩu ngữ, dấu nháy đơn); câu cuối "may improve numerical stability" (phỏng đoán) | Viết lại câu trích xuất cho chuẩn; bỏ câu phỏng đoán. |
| D12 | Intro | Thiếu một câu động cơ vì sao ràng buộc giả lồi xuất hiện trong thực tế (bài mẫu luôn có đoạn động cơ). | Tuỳ chọn, nội dung do nhóm quyết: thêm 1 câu (ví dụ tỉ số của hàm lồi không âm trên hàm affine dương là giả lồi). |

## E. Response letter

| # | Vị trí | Vấn đề | Hướng sửa |
|---|---|---|---|
| E1 | Mở đầu, kết | "more **honest** evidence", "the clarity, rigor, and **honesty** of the manuscript": tự ngụ ý bản cũ thiếu trung thực. | "more complete evidence"; "the clarity and rigor of the manuscript". |
| E2 | Tóm tắt, R1.4 | "genuinely" 3 lần, "plainly" 2 lần, trong khi bài đã bỏ các trạng từ này. | Bỏ các trạng từ này. |
| E3 | Toàn letter | 26 dấu gạch dài "---", rất dày. | Thay phần lớn bằng dấu phẩy hoặc tách câu. |
| E4 | R1.1 | Letter nói với $\mu_k\equiv\tfrac12$ "the proofs … go through with only minor changes", còn Remark 2 nói "these two steps must be re-established". Letter khẳng định mạnh hơn bài. | "…these two steps would have to be re-established, for instance for the constant weight $\mu_k\equiv\tfrac12$." |
| E5 | Tóm tắt | "a heuristic residual-share allocation", trong khi Remark 2 viết "an adaptive allocation". | Thống nhất "an adaptive allocation". |
| E6 | m6 | "Paragraph removed; reduced to one sentence." (tự mâu thuẫn) | "Paragraph reduced to one sentence (Sec. 1)." |
| E7 | R1.4 | "To engage the mixed setting genuinely…" mâu thuẫn với Mục 3.4 (cả hai nhánh cùng vi phạm chỉ 32/12 877 điểm). Trước đây anh chọn giữ. | Nhắc lại vì đây là điểm dễ bị bắt nhất. |
| E8 | R1.5 | Chưa giải thích vì sao "3 trên 4 độ đo" thành 4/4 (p = 1), và phạm vi của SG-dyn tinh chỉnh. Trước đây anh chọn giữ. | Nhắc lại. |
| E9 | Nếu làm B1 | Các chỗ dẫn "Sec. 3.4" cho (45), Bảng 7–8. | Đổi thành "Sec. 3.5". |

## F. Hình thức, khác

| # | Vấn đề |
|---|---|
| F1 | Tuyên bố dùng AI tạo sinh chỉ ghi "OpenAI Codex". Theo chính sách Taylor & Francis cần nêu đúng và đủ các công cụ đã thực sự dùng khi sửa bài. |
| F2 | Con số 10.80 s (bài và letter R1.5) không còn câu giải thích vì sao gói code cho số khác (anh đã chọn không áp dụng D2). |

---

**Tổng hợp:** 7 lỗi phải sửa (A), 4 điểm bố cục (B), 10 chỗ lặp (C), 12 điểm văn phong (D), 9 điểm ở letter (E), 2 điểm khác (F).
