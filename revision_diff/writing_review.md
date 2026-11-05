# Rà soát văn phong và độ chặt chẽ — `DTAP Finally/main_document.tex`

Mục đích: kiểm tra xem bản sửa đã đáp ứng ý kiến M2 và G của Reviewer 2 chưa ("many sentences are ambiguous… describe the problem, algorithms, etc. in short sentences… make the paper concise"). Đây chỉ là bản rà soát; **chưa sửa gì trong bài**. Số dòng là số dòng của `main_document.tex` hiện tại.

## 1. Tiêu chí: thế nào là câu mơ hồ / tối nghĩa

Với một bài toán tối ưu, một câu đạt yêu cầu khi người đọc chỉ hiểu được **một nghĩa**, hiểu được **mà không phải đoán**, và nội dung đó **đúng như toán học đã chứng minh**. Mọi câu vi phạm một trong năm loại dưới đây đều bị ghi lại:

| Mã | Loại | Dấu hiệu nhận biết |
|---|---|---|
| **A** | **Mơ hồ** (đọc ra hai nghĩa) | Đại từ hay chủ ngữ không rõ ("this", "its role", "which" gắn với danh từ nào); phạm vi lượng từ không rõ ("for all"/"some"); bổ ngữ treo ("within the framework of…" không biết bổ nghĩa cho ai); câu dễ đọc nhầm cấu trúc (garden-path). |
| **B** | **Tối nghĩa** (một nghĩa nhưng phải đoán) | Thuật ngữ, ký hiệu dùng trước khi định nghĩa; ẩn dụ hay biệt ngữ ("prevent neglect", "convex half", "third track"); chồng danh từ ("quadratic-over-positive-affine criterion"); nhắc tới một quy trình chưa mô tả. |
| **C** | **Thiếu chặt chẽ** | Khẳng định rộng hơn điều đã chứng minh; thiếu giả thiết; một ký hiệu mang hai nghĩa; một khái niệm có nhiều tên; gọi sai tên kết quả (ví dụ gọi một định nghĩa là "contrapositive"). |
| **D** | **Liên kết** | Câu hoặc đoạn không nối với câu hoặc đoạn trước; từ nối sai logic ("therefore" không có quan hệ nhân quả); một ý lặp lại ở nhiều nơi; nội dung đặt sai mục; tham chiếu tới phần chưa xuất hiện mà không giải thích. |
| **E** | **Câu dài hoặc nặng** | Trên 30 từ, hoặc từ 3 mệnh đề trở lên, hoặc chồng nhiều phủ định; ngược lại, một chuỗi câu quá ngắn rời rạc không có từ nối cũng khó đọc. |

Mức độ: **[1] phải sửa** (sai, thiếu định nghĩa, có thể làm phản biện nghi ngờ kết quả); **[2] nên sửa** (gây khó hiểu); **[3] tùy chọn** (văn phong).

## 2. Kết luận chung

- **Độ dài câu đã đạt.** Bài có khoảng 300 câu văn xuôi, trung bình 15 từ, trung vị 13 từ. Chỉ khoảng 8 câu dài trên 35 từ. Về mặt "câu ngắn", yêu cầu M2 đã được đáp ứng.
- **Độ rõ nghĩa chưa đạt.** Khi rút gọn, nhiều đoạn bị cắt thành chuỗi câu ngắn rời rạc. Thuật ngữ được dùng trước khi định nghĩa, và một khái niệm mang nhiều tên khác nhau. Reviewer 2 sẽ vẫn có cơ sở để nói "many sentences are ambiguous", nhất là ở **Abstract, Introduction, §4.1.3, §4.2 và §4.4**.
- **Phần toán (§3) chặt chẽ hơn hẳn phần văn.** Các chứng minh đọc được và đúng. Vấn đề nằm ở câu dẫn và nhận xét quanh chứng minh: có 3 chỗ khẳng định không khớp với điều đã chứng minh (C1, C2, C3 ở mục 3).
- **Bốn nhóm lỗi xuyên suốt** nên sửa trước, vì mỗi nhóm kéo theo hàng chục câu (mục 3).

## 3. Vấn đề xuyên suốt (sửa một lần cho cả bài)

### 3.1 Một khái niệm, nhiều tên [1, C]
| Khái niệm | Các tên đang dùng (dòng) | Gợi ý |
|---|---|---|
| Trọng số $\mu_k$ | "proportional mixing weight" (68), "proportional weight" (103, 276, 1251), "adaptive weight" (109), "soft weight" (234), "Soft proportional weight" (263), "residual-share weighting" (1117) | Chọn **một** tên, định nghĩa ở (1e), dùng nhất quán. |
| Hai nhóm ràng buộc | "block" (68, 103), "track" (§3 trở đi), "groups" (185) | Định nghĩa "track" một lần ở §3.2 (= tập chỉ số + bước tương ứng); bỏ "block". |
| Ràng buộc thứ ba / track giả lồi | "third track" (1037, 1127) — bài chỉ có **hai** track | "third constraint" hoặc "pseudoconvex track". |
| Kết quả hội tụ | "converges strongly" (Thm 3.12, Cor 3.13–3.14, §3.8, keyword) và "convergence of the whole sequence" (Abstract, C2) | Trong $\mathbb R^n$, chữ "strongly" không mang thêm nội dung và dễ làm người đọc tưởng bài làm trong không gian Hilbert. Nên thống nhất "the whole sequence converges to a feasible point". |
| $\Omega\neq\emptyset$ | "consistency" (68, 110, 1027, 1251) — Giả thiết 1 không gọi tên này | Gọi (A1)(a) là "consistency" ngay trong Giả thiết 1. |
| Tập $K^{\rm cvx}, K^{\rm ps}$ | "approximate active set" | Trong tối ưu, "active" nghĩa là $F_i=b_i$. Ở đây là tập ràng buộc **gần vi phạm nhiều nhất**. Đây cũng là điểm Reviewer 2 hỏi ở m4. Nên đổi tên hoặc nói rõ nghĩa ngay khi định nghĩa. |

### 3.2 Ký hiệu trùng nghĩa [1, C]
| Ký hiệu | Nghĩa 1 | Nghĩa 2 |
|---|---|---|
| $n$ | số chiều, $H=\mathbb R^n$ (§2–3) | số mẫu (§4.1, dòng 747) |
| $x$, $x_i$ | điểm lặp $x^k$ (§3) | mẫu dữ liệu $x_i$ (747); công thức SG ở 1055 lại dùng $x^k$ cho bài toán trọng số $w$ |
| chỉ số $k$ | vòng lặp ($x^k$, $w^k$) | đặc trưng ($w_k$, $\rho_k$, $a_k$, $R_k$) — $w^k$ và $w_k$ cùng xuất hiện ở §4.4 |
| $\rho$ | $\rho_{\rm cvx}$ (tham số Polyak) | vector Fisher $\rho$, $\rho_k$ |
| $p$ | số đặc trưng | $p$-value (904: "all-zero pairs have $p=1$") |
| $Q$ | hộp chuẩn $Q$ | dòng 831 "including $Q$" (ý là $Q_R$) |
| $D$ | $D_t$ (lớp, vừa là tập vừa là hàm chỉ thị) | $D_\rho$ (nửa không gian), $D_k$ (tập argmax trong SG), $\underline{R_k}(D)$ |
| $\varepsilon$, $\epsilon$ | ngưỡng dừng $\varepsilon$ | $\epsilon$ (tham số Young), $\varepsilon_k$ (Bổ đề 3.3), $\varepsilon_\rho$, $\varepsilon_{\rm PNN}$ |
| $L'$ / $L'_B$ | Bổ đề 3.7 viết $L'_B$ | chứng minh Định lý 3.12 (644) viết $L'$ |

### 3.3 Dùng trước khi định nghĩa / thiếu định nghĩa [1, B–D]
- **SG-const, SG-dyn**: dùng ở §4.2 (835) và cả §4.3 (Bảng 2–5) nhưng chỉ được định nghĩa ở §4.4 (1050–1059). Người đọc §4.3 không biết đây là phương pháp gì.
- **Cách chọn ngưỡng $b_i$**: bài **không còn mô tả đầy đủ** cách tính. Dòng 822 nhắc "Separate empirical percentiles", dòng 1021–1026 chỉ nói "The sampling pool contains 3 000 Dirichlet points… The heuristic chooses percentile levels…", không có câu "$b_i$ là phân vị bậc … của $F_i$ trên tập mẫu". Reviewer 1 (R1.4) hỏi đúng vào điểm này.
- **$A^\star$** (chú thích Bảng 2, 941): không còn được định nghĩa từ khi bỏ Định nghĩa 3.5 cũ.
- **$d_\infty$, "normal box"**: Abstract và Introduction (99–101) đã dùng, đến (7) mới định nghĩa.
- **"the proportional weight"** (103): dùng mạo từ xác định khi chưa giới thiệu trọng số nào.
- **"Young parameter"** (314), **"evaluated points"** (1034), **"full-data instances"**, **"witnesses"** (1028–1029): biệt ngữ chưa giải thích.

### 3.4 Lặp ý và đặt sai chỗ [2, D]
- Tính lồi của $\Omega$ được nói **3 lần**: 95, 138, 224–225.
- $J$ được định nghĩa **3 lần**: công thức không đánh số ở 101, (8), và lại trong (9).
- Tính lồi của $F_3$: Mệnh đề 4.1 và lặp lại ở 1039–1040.
- $\Phi^{\rm ps}$ (15): định nghĩa nhưng **không dùng ở đâu** (chỉ xuất hiện ở dòng 202).
- §3.5 "Per-iteration cost" chứa đoạn tổng quan phương pháp chứng minh (309–317) và quy ước "Throughout, $\{x^k\}$ is the infinite sequence…" (319–323). Hai đoạn này thuộc phần mở đầu phân tích hội tụ (đầu §3.6), không thuộc chi phí mỗi vòng lặp.
- Nhận xét 4 (667–680), trong phần lý thuyết, có một câu 60 từ về số liệu thực nghiệm và tham chiếu tới Bảng 8 ở §4.4.
- Câu về độ phức tạp chiếu lên đơn hình (127) đặt ở §2 dùng $p$ khi chưa định nghĩa; câu này thuộc Nhận xét 6.

## 4. Rà theo từng mục

Mỗi dòng gồm: vị trí · câu gốc (rút gọn) · vấn đề · mã · mức độ · hướng sửa.

### Abstract (68)
1. "A max-type violation measure **identifies nearly active constraints in two blocks**." — Hai "blocks" chưa được giới thiệu. Bản thân $J$ không "identify" ràng buộc; việc đó do các tập gần-cực-đại làm. · B, C · [1] · Nói thẳng: các thành phần được chia thành nhóm lồi và nhóm giả lồi; ở mỗi nhóm thuật toán dùng các ràng buộc gần vi phạm nhiều nhất.
2. "**The proportional mixing weight** is a residual-responsive choice, without a claim of optimality." — Câu đầu tiên nhắc tới trọng số đã dùng mạo từ "The"; người đọc chưa biết có trọng số nào. · B · [2]
3. "Under consistency and continuous differentiability…" — "consistency" chưa định nghĩa; thiếu giả thiết lồi/giả lồi và điều kiện bước. · B, C · [2]
4. "…belongs to **the convex subclass**." — Lớp con nào? · B · [2] · "all three constraint functions are convex".
5. "The results also show initialization sensitivity…" — Nhạy với khởi tạo là của DTAP hay của mọi phương pháp? · A · [2]
6. Văn phong: 5/12 câu là câu phủ định hoặc rào đón ("without a claim of optimality", "do not establish…"). Một abstract toán học nên nêu kết quả dương tính trước; các giới hạn để vào phần thân hoặc phần kết luận. · E · [3]

### §1 Introduction
7. (80) "The split feasibility problem (SFP) **models constrained reconstruction**." — Mơ hồ, không nói ai đưa ra và mô hình hóa gì. · B · [2] · "was introduced by Censor and Elfving [4] for inverse problems such as …".
8. (80) "…and a matrix $\mathcal A$" — Thiếu kích thước $\mathcal A\in\mathbb R^{m\times n}$; $\|\mathcal A\|$ trong (2) là chuẩn phổ nhưng không nói rõ. · C · [2]
9. (84) "Byrne's CQ algorithm **uses** (2)" — "uses" mơ hồ; nên là "iterates". · B · [3]
10. (89) "**Supporting half-spaces simplify projections** [17], while self-adaptive steps **reduce parameter dependence**" — Người đọc phải biết trước relaxed CQ mới hiểu; "parameter dependence" thực ra là "removes the need to know $\|\mathcal A\|$". · B · [2]
11. (89) "Adaptive steps and decomposition are **therefore** established principles." — "therefore" sai quan hệ logic: đây là câu tóm tắt, không phải hệ quả. Ý thật là "đây không phải đóng góp của bài". · D · [2]
12. Không có câu chuyển từ SFP tuyến tính (đoạn 1) sang trường hợp phi tuyến (đoạn 2): vì sao cần $F$ phi tuyến? · D · [2]
13. (95) "where $K\subseteq\mathbb R^n$ is closed and convex" — Thiếu "nonempty". · C · [2]
14. (95) "**each differentiable component** of $F$ … is convex or pseudoconvex on $K$" — Đọc ra nghĩa "chỉ thành phần nào khả vi mới cần lồi hoặc giả lồi". · A · [1] · "each component $F_i$ is differentiable and either convex or pseudoconvex on $K$".
15. (95) "…so **the feasible set** is convex…" — Tập khả thi chưa được định nghĩa; dùng tên $\Omega$ ngay tại đây. · B · [3]
16. (97) "Li et al. use a convex aggregate proximity function, **a property** not ensured by componentwise pseudoconvexity." — Về ngữ pháp, cụm đồng vị "a property" bổ nghĩa cho "function"; ý muốn nói là tính lồi. · A · [2] · "Li et al. assume that the aggregate proximity function is convex; componentwise pseudoconvexity does not ensure this."
17. (97) "Yen et al. combine equilibrium and nonlinear image constraints." — Không nói **vì sao** công trình này liên quan, cũng không nói nó khác bài này ở điểm nào. Bản cũ có ý quan trọng: Yen et al. dùng cùng hàm đo vi phạm kiểu max và cùng cơ chế tập active, nhưng yêu cầu các hàm là quasilinear. · B, D · [1] · Nêu rõ điểm giống và điểm khác; đây là công trình gần nhất.
18. (97) "Our method exploits **the additional derivative information** of convex components **within this established feasibility setting**." — Tối nghĩa: "derivative information" thực chất là bất đẳng thức gradient; "this established setting" mơ hồ. · B · [2]
19. (99) "**The box gives** the explicit violation measure" — Ẩn dụ. · B · [2] · "Because $Q$ is a box, the $\ell_\infty$-distance from $F(x)$ to $Q$ has the closed form …".
20. (103) Đoạn gồm 10 câu ngắn rời rạc, không có từ nối (thuật toán → biện minh bước → trọng số → phạm vi của trọng số → hằng số → tính bị chặn → gradient). · D, E · [2]
21. (103) "**Its role in preventing neglect** is used in the convergence proof." — Câu tối nghĩa điển hình: không rõ "neglect" cái gì, không rõ "its" chỉ gì. Ý đúng: trọng số bảo đảm một track bị vi phạm kéo dài vẫn nhận trọng số dương. · A, B · [1]
22. (103) "A one-step bound valid for all weights in $[0,1]$ does not by itself establish convergence for every weight sequence." — Ở phần mở đầu, người đọc chưa biết "one-step bound" là gì; câu rào đón này nên chuyển xuống Nhận xét 1. · B, D · [2]
23. (103) "…local bounds on **the bounded iterate region**" — Nên là "on a bounded set containing the iterates". · B · [3]
24. (103) "Continuous gradients need not be Lipschitz." — Câu treo; ý là giả thiết (A2) không đòi gradient Lipschitz. · A · [2]
25. (105) "This construction expresses **simultaneous acceptance**, not equivalence to the source optimization models." — Tối nghĩa. · B · [2]
26. (105) "The **positive-semidefinite quadratic-over-positive-affine criterion** is convex" — Chồng danh từ. · B, E · [2]
27. (105) "Classification **scores** feature selections that are computed once and then reused, on the same holdout split that was fixed when they were computed, and tuned subgradient methods can match or outperform DTAP." — 32 từ; dễ đọc nhầm ("scores" là động từ hay danh từ?); hai ý không liên quan nối bằng "and"; chi tiết phương pháp luận quá sâu cho phần mở đầu. · A, E, D · [1]
28. (110) C2 "…the stated step conditions…" — Điều kiện nào, nêu ở đâu? "Convergence of distances and one feasible cluster point suffice." là chi tiết chứng minh, không phải đóng góp. · B · [2]
29. (111) C3 "Experiments **distinguish prediction from feasibility cost**" — Tối nghĩa. · B · [2]
30. Ba đóng góp C1–C3 không nêu điểm mới **so với** Li et al. / Yen et al. / Hu et al.; người đọc phải tự suy ra. · D · [2]

### §2 Preliminaries
31. (118) "$H=\mathbb R^n$ is Euclidean space" — Thiếu mạo từ. Bài lúc dùng $\mathbb R^n$ (Introduction, Giả thiết), lúc dùng $H$ (§2–3). Reviewer 2 (m16) đã bắt lỗi lặp $H$; nên chọn một ký hiệu cho cả bài. · C · [2]
32. (127) "projection onto a **$p$-dimensional simplex**" — $\Delta_{p-1}$ có $p-1$ chiều; $p$ chưa được định nghĩa ở §2. · C, D · [1]
33. (127) "This characterization **gives the projection inequality used in** Lemma 3.2" — Bổ đề 3.2 chính là bất đẳng thức đó. · B · [3]
34. (133) Định nghĩa 2.2: "A function differentiable on…" rồi dùng $f$ mà chưa đặt tên. · C · [2] · "A function $f$, differentiable on an open neighbourhood of $K$, is pseudoconvex on $K$ if …".
35. (5) giờ **là định nghĩa**, nhưng chứng minh Bổ đề 3.5 (386) và Định lý 3.12 (638) vẫn gọi nó là "**the contrapositive (5)**". · C · [1]
36. (138) "This distinction is relevant to the mixed constraint functions studied below." — Câu đệm, không thêm thông tin. · E · [3]

### §3 The DTAP algorithm and its convergence analysis
37. Tiêu đề §3.2 "Decomposition and **dual-track scalarization**" — Mục này làm phân tách, không làm vô hướng hóa. · B · [3]
38. (168) "…so finding a feasible point amounts to **minimizing $J$ over $K$**" — Chỉ đúng khi $\Omega\neq\emptyset$ (giá trị nhỏ nhất bằng 0). Chặt chẽ hơn: "finding $x\in K$ with $J(x)=0$". · C · [2]
39. (192) "we replace **the exact maximizers**" — Thứ được thay là tập **chỉ số** đạt cực đại, không phải "maximizers". · C · [2]
40. (214–215) (A1)(b) "the restriction $F_i|_K$ is … pseudoconvex" — Định nghĩa 2.2 đòi hàm khả vi trên một lân cận mở của $K$, mà hạn chế $F_i|_K$ thì không có lân cận. · C · [1] · "$F_i$ is pseudoconvex on $K$".
41. Cách đánh nhãn trong Giả thiết 1 không nhất quán: (A1) dùng (a)(b), (A3) dùng (i)(ii)(iii). · C · [3]
42. Thuật toán 1, Bước 3: kiểm tra dừng $J(x^k)\le\varepsilon$ đặt **sau** khi đã tính $x^{k+1}$ rồi trả về $x^k$. Thứ tự này không sai nhưng khó theo; nên kiểm tra ở đầu Bước 1. · D · [3]
43. (277) Nhận xét 1: "the only **convergent choice**" — Trọng số không "hội tụ"; ý là "the only choice for which convergence holds". "the one-step inequality" cần dẫn chiếu Bổ đề 3.8. · C · [2]
44. (291) Nhận xét 2: "The parameters … **remain part of the algorithm**." — Ý định không rõ. Ý thật: người dùng vẫn phải chọn các tham số này, nhưng chúng không phụ thuộc hằng số của bài toán. · B · [2]
45. (309–312) "The convergence analysis … is more involved … because the two constraint tracks are asymmetric: on the convex track the gradient inequality gives a quantitative lower bound of order $v_i(x)^2$, hence a strict decrease, whereas…" — 51 từ. "Cận dưới" của đại lượng nào? "Giảm" cái gì (khoảng cách tới $x^\star$)? · E, B · [2]
46. (314–315) "a contradiction argument **rules out cluster points outside the feasible set**" — **Sai so với chứng minh.** Stage 2 chỉ ra **tồn tại** một điểm tụ khả thi ($C\cap\Omega\neq\emptyset$), không loại trừ điểm tụ ngoài $\Omega$. Đó là việc của Stage 3. Đây cũng chính là điểm Reviewer 1 (R1.3) soi. · C · [1]
47. (430) "The following quasi-Fejér inequality, **within the framework of** Combettes [5], yields…" — Bổ ngữ treo. · A · [3] · "The following inequality is of quasi-Fejér type in the sense of Combettes [5]; it yields…".
48. (518–527) Chứng minh Bổ đề 3.10: $x^\star$ được dùng trong trường hợp $L=0$ trước câu "Fix $x^\star\in\Omega$" (535). · C · [2]
49. (572–576) "…confine the cluster set to **the convex half**…" — Ẩn dụ; câu 45 từ liệt kê ba bước. · B, E · [2] · "the set on which all convex constraints hold".
50. (663–664) "This argument requires neither uniqueness of the feasible point **nor convexity of the target set**" — Dưới Giả thiết 1, $\Omega$ **luôn lồi** (đã nói ở dòng 224), nên vế này gây hiểu lầm: người đọc tưởng $\Omega$ có thể không lồi. Câu này lại được trích nguyên văn trong response letter ở R1.3. · C · [1] · Hoặc nói "the argument does not use the convexity of $\Omega$", hoặc bỏ vế này.
51. (674–680) Nhận xét 4: câu 60 từ trộn lý thuyết với số liệu ($v_1-v_2\ge4.79$, tham chiếu Bảng 8 ở §4.4). · E, D · [2] · Chuyển phần số liệu xuống §4.4.
52. (644) $L'$ so với $L'_B$ trong Bổ đề 3.7. · C · [3]

### §4.1 Feature-selection model
53. (747) $\mathcal X=\{x_1,\ldots,x_n\}$ — Trùng $x$ và $n$ với §3 (xem 3.2). · C · [1]
54. (752–754) $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$ — Không gọi tên đại lượng này (interaction information) và không nói quy ước dấu. · B · [3]
55. (794) "The three terms measure label-approximation error, **incorrect-decision confidence**, and Tikhonov regularization" — Cụm ở giữa tối nghĩa. · B · [2]
56. (803) "Here $F_1,F_2$ are the first two **components** of (38)" — Nên là "terms". · B · [3]
57. (810) Mệnh đề 4.1 "It satisfies **the function assumptions** of Assumption 1" — Cụ thể là (A1)(b) và (A2). · B · [3]
58. (820) "It treats $F_3$ **conservatively**…"; "either **assignment converges**" — Ẩn dụ; một phép gán không hội tụ, thuật toán mới hội tụ. · B, C · [2]
59. (820) "Replacing a zero score by a positive floor changes the model and **must be declared**. The implementation also uses $\max\{\rho^\top w,10^{-15}\}$…" — Chi tiết cài đặt chen giữa đoạn mô hình; chuỗi 7 câu ngắn rời rạc. · D, E · [2]
60. (822) "**Externally specified thresholds remain fixed.** Training-based thresholds instead define the benchmark instance… **Separate empirical percentiles** do not ensure $\Omega\neq\emptyset$…" — Đoạn tối nghĩa nhất của bài. Nó dựa vào quy trình chọn ngưỡng chưa được mô tả (chỉ xuất hiện ở §4.4, và cũng không đầy đủ). · B, D · [1]
61. (831) Nhận xét 6 "…storage, **including $Q$**" — Đây là $Q_R$, không phải hộp $Q$. · C · [1]

### §4.2 Experimental setup
62. (835) "SG-const uses step $10^{-3}$. **The dynamic subgradient comparison** is considered separately…" — SG-const và SG-dyn chưa được định nghĩa (xem 3.3). · D · [1]
63. (835) "1000 Euler **grid points**" so với 4.2.1 viết "$N_{\rm step}$ **steps**" — 1000 điểm lưới tương ứng 999 bước; không nhất quán. · C · [2]
64. (856) "The following **updates** specify the two baseline solvers" — Dùng từ lạ. · B · [3]
65. (863) "We integrate (45) by explicit Euler on $[0,T]$ with $N_{\rm step}$ steps under a fixed budget (no stopping rule), with the fixed parameters…, and take as weight vector…" — 47 từ. · E · [2]
66. (888–890) "**The same holdouts were used when the selections were computed**, and the threshold heuristic uses the whole-dataset sample size…" — Câu này có thể khiến phản biện **nghi rò rỉ dữ liệu kiểm tra**. Cần nói rõ: tập kiểm tra không dùng để chọn đặc trưng; chỉ phép chia dữ liệu được cố định trước, còn heuristic chỉ dùng kích thước dữ liệu ($n,p,r$), không dùng giá trị. · A · [1]
67. (900) "the unbiased variance correction is $N_f/(N_f-1)$, **not $p/(p-1)$**" — Câu phản bác một điều mà người đọc chưa từng thấy (là dấu vết của bản cũ). · D · [2]
68. (904) "all-zero pairs have **$p=1$**" — Trùng ký hiệu với $p$ là số đặc trưng. · C · [2]

### §4.3 Classification results
69. (913) "…thus the results support moderate reduction rather than **uniform sparsity** or stability superiority." — "uniform sparsity" tối nghĩa. · B · [2]
70. (926–927) "**The per-dataset exceptions** are included in Table 3" — Ngoại lệ gì? (Spambase, nơi SG khác DTAP.) · B · [2]
71. (941) Bảng 2: $A^\star$ chưa định nghĩa. · B · [1]

### §4.4 Constraint activity and a tuned subgradient comparison
72. (1021–1026) "The percentile calibration… **The sampling pool** contains 3 000 Dirichlet points…" — Không có câu nào nói $b_i$ được tính thế nào từ tập mẫu này (xem 3.3, R1.4). · B · [1]
73. (1028–1032) "**saved numerical witnesses** satisfy all three inequalities strictly **under an independent evaluation**" — Biệt ngữ; "independent" so với cái gì? · B · [2]
74. (1031–1032) "All Fisher coordinates are positive **on these instances**" — Chỉ nói cho các bài toán dùng toàn bộ dữ liệu. Với các fold của nghiên cứu phân loại (Bảng 2–5), bài không cho biết điều kiện $\min_k\rho_k>0$ của Mệnh đề 4.1 có thỏa hay không, nên chưa rõ định lý có áp dụng được cho các lần chạy đó. · C · [1]
75. (1034) "**evaluated points**" — Nên định nghĩa một lần: các điểm lặp $w^0,\dots,w^K$ kể cả điểm dừng. · B · [3]
76. (1037) "**third track**" — Bài chỉ có hai track. · C · [1]
77. (1044) "We include **the valid** all-convex comparator" — "valid" theo nghĩa nào? · B · [3]
78. (1051–1059) Công thức SG dùng $x^k$ trong khi biến của bài toán là $w$; $\widehat L$ được dùng (1051) trước khi $L$ xuất hiện (1059); $\nu_k=J(x^k)/L$ ứng với số mũ Hölder 1 nhưng bài không nói ra. · C · [2]
79. (1104–1105) "…differ by at most $3.18\times10^{-5}$ **relative to AC**" — Sai khác tuyệt đối hay tương đối? · A · [2]
80. (1106–1107) "whose success counts **differ only from the random starts**" — Dễ đọc nhầm; ý là "differ only on the random starts". · A · [2]
81. (1116) "nonzero tracks" — Ý là "both track violations are positive". · B · [3]
82. (1172–1204) Một đoạn khoảng 33 dòng trộn 8 kết quả khác nhau. Nên tách thành 2–3 đoạn, mỗi đoạn một ý. · E, D · [2]
83. (1231–1246) Reproducibility: kết quả chọn đặc trưng "saved with Python 3.11.7", Bảng 7–8 "Python 3.13.4". Câu "**In this environment** the package also reproduces exactly every numerical entry of Tables 1–5…" không rõ là môi trường nào. · A · [2]

### §5 Conclusion
84. (1251) Một đoạn 12 câu, phần lớn là rào đón; không có câu nêu rõ đóng góp chính và hướng phát triển cụ thể. · E · [3]

## 5. Đề xuất thứ tự sửa

1. **Nhóm [1] xuyên suốt (mục 3):**
   - thống nhất tên gọi ($\mu_k$, track, "strong convergence", consistency, active set);
   - tách các ký hiệu trùng ($n$, $x$, $k$, $\rho$, $p$, $Q$, $D$, $\varepsilon$);
   - định nghĩa SG-const/SG-dyn, cách tính $b_i$ và $A^\star$ trước khi dùng.
2. **Các khẳng định không khớp với chứng minh:** 35, 40, 46, 50, 32, 74.
3. **Các câu tối nghĩa hoặc mơ hồ mức [1]:** 14, 17, 21, 27, 60, 66, 76.
4. **Liên kết và cấu trúc:**
   - viết lại đoạn 103 và đoạn 105 của Introduction cho liền mạch;
   - chuyển các đoạn 309–323 về đầu §3.6;
   - chuyển phần số liệu của Nhận xét 4 xuống §4.4;
   - bỏ các chỗ lặp (mục 3.4).
5. Các mục [2], [3] còn lại.

Sau khi sửa: cập nhật response letter nếu câu được trích (R1.3 trích nguyên văn câu ở dòng 663–664, xem mục 50), rồi chạy lại `make_colored.py` để bản chữ đỏ phản ánh các thay đổi mới.
