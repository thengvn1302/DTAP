# Đề xuất sửa câu chữ — `DTAP Finally/main_document.tex`

Tài liệu để **duyệt**: chưa có thay đổi nào được áp vào bài. Các đề xuất đã được viết lại để bài **ngắn đi** chứ không dài thêm (Phần IV), theo các tiêu chí ở đầu Phần I. Mỗi mục gồm câu **gốc**, câu **đề xuất** (tiếng Anh), **bản dịch** tiếng Việt của câu đề xuất và **lý do**. Số thứ tự theo `writing_review.md`; dòng là số dòng hiện tại của `main_document.tex`.

Cách duyệt: đánh dấu ở cuối mỗi mục: `[x] Duyệt`, `[x] Sửa lại` (ghi chú bên dưới), hoặc `[x] Bỏ`.

Các số liệu mới đưa vào câu đề xuất đều đã được kiểm từ code và kết quả trong package:
- min điểm Fisher trên các fold: tính lại trong phiên này bằng hàm `_fisher_score` của package;
- cách tính $b_i$: `thresholds.py`;
- sai khác tương đối DTAP/AC: `results/hu2022/datasets/Abalone.json.gz`;
- số bước Euler: `nfscore.py`;
- bước SG-dyn: `hu2022.py`.

> **Lưu ý cho response letter.** Các mục **A0, 50** sửa những câu mà letter đang trích nguyên văn. Nếu duyệt, cần sửa trích dẫn tương ứng trong letter: R1.1 và R1.2 trích Abstract, R1.3 trích câu ở dòng 663–664.

---

## Tiêu chí: vô nghĩa, lan man, súc tích

| Khái niệm | Định nghĩa | Phép thử |
|---|---|---|
| **Vô nghĩa / thừa** | Câu không mang thông tin người đọc cần để hiểu, kiểm chứng hoặc dùng kết quả: câu đệm, câu lặp điều hiển nhiên hoặc điều đã nói, câu đánh giá chung chung. | **Xóa thử:** bỏ câu đi mà không mất gì thì câu đó thừa. |
| **Lan man** | Nội dung lệch mục đích của đoạn: sai chỗ, sai cấp độ chi tiết, lặp một giới hạn ở nhiều nơi, rào đón. | **Mục đích:** câu có phục vụ mục đích của đoạn không? **Lặp:** đã nói ở chỗ khác chưa? |
| **Súc tích** | Mỗi câu nói một ý cần thiết, chính xác, bằng ít chữ nhất mà vẫn không phải đoán. Nén quá mức thành biệt ngữ là tối nghĩa, không phải súc tích. | **Mật độ:** có cách nói ít chữ hơn mà cùng độ chính xác không? **Giải nén:** người đọc có phải đoán ý không? |

Quy tắc cấp độ chi tiết: Introduction nói *vấn đề gì* và *vì sao*; phần thân nói *làm thế nào*; seed, ngưỡng sàn và môi trường chạy thuộc phần thiết lập hoặc tái lập. Mỗi giới hạn chỉ nói **một lần**, ở chỗ phù hợp.

## Phần I. Quy ước dùng chung cho cả bài

Mỗi quy ước được áp ở mọi vị trí liệt kê.

### G1. Một tên cho trọng số $\mu_k$: "proportional weight"
| Dòng | Gốc | Đề xuất |
|---|---|---|
| 68 | The proportional mixing weight | (viết lại cả Abstract, xem A0) |
| 109 | through an adaptive weight | through a proportional weight |
| 234 | through the soft weight $\mu_k$ | through the proportional weight $\mu_k$ |
| 263 | Soft proportional weight: | Proportional weight: |
| 1117 | of residual-share weighting | of the proportional weight |

*Dịch:* "trọng số tỉ lệ".
*Lý do:* hiện có 6 tên cho cùng một đại lượng (mục 3.1 của bản rà soát). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G2. Bỏ "block", định nghĩa "track" một lần
- Dòng 174, câu đầu §3.2. **Gốc:** "We split the constraint index set into a \emph{convex track} and a \emph{pseudoconvex track}."
  **Đề xuất:** "We split $I$ into a \emph{convex track} $I^{\cvx}$ and a \emph{pseudoconvex track} $I^{\ps}$, each with its own step rule."
  **Dịch:** "Ta chia $I$ thành *track lồi* $I^{\cvx}$ và *track giả lồi* $I^{\ps}$, mỗi track có quy tắc bước riêng."
- Dòng 184–186 ("Partition $I$ … into disjoint groups … The per-track maximal violations are"): câu này lặp lại câu trên, nên rút còn: "Assumption~\ref{ass:standing} makes the partition precise. The per-track maximal violations are". **Dịch:** "Giả thiết 1 phát biểu chính xác phép chia này. Độ vi phạm lớn nhất trên mỗi track là".
- Các chữ "block" ở dòng 68 và 103 được xử lý trong A0 và mục 20.

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G3. "third track" (bài chỉ có hai track)
- Dòng 1037: xem mục 76.
- Dòng 1127. **Gốc:** "To exercise the third track directly, consider". **Đề xuất:** "To exercise the pseudoconvex track directly, consider". **Dịch:** "Để kiểm tra trực tiếp track giả lồi, xét".

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G4. Bỏ "strongly" (trong $\mathbb R^n$ từ này không mang thêm nội dung)
| Dòng | Gốc | Đề xuất |
|---|---|---|
| 72 | Strong convergence (keyword) | Global convergence |
| 316 | strong convergence to a feasible point (Theorem 3.12) | (viết lại cả đoạn, mục 45) |
| 571 | \subsection{Strong convergence to a feasible point} | \subsection{Convergence to a feasible point} |
| 572 | The goal of the analysis is strong convergence of $\{x^k\}$ to a feasible point. | (mục 49) |
| 580 | converges strongly to a point $x^\infty\in\Omega$ | converges to a point $x^\infty\in\Omega$ |
| 698, 728 | The sequence converges strongly to a point | The sequence converges to a point |

*Dịch:* "hội tụ toàn cục"; "Hội tụ tới một điểm khả thi"; "dãy hội tụ tới một điểm".
*Lý do:* bài phát biểu trong $\mathbb R^n$, nơi mọi tô-pô thông dụng trùng nhau. "Strongly" khiến người đọc tưởng bài làm trong không gian Hilbert vô hạn chiều. "Global convergence" đúng nghĩa ở đây vì kết quả đúng với mọi điểm đầu $x^0\in K$.
*Lưu ý:* Reviewer 1 tóm tắt bài bằng cụm "strong convergence guarantees"; đổi tên không ảnh hưởng nội dung trả lời. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G5. Gọi tên "consistency"
- Dòng 213. **Gốc:** "(A1) (a) $\Omega\ne\emptyset$." **Đề xuất:** "(A1) (a) $\Omega\ne\emptyset$ (consistency)." **Dịch:** "(A1)(a) $\Omega\ne\emptyset$ (tính nhất quán)."

*Lý do:* Abstract, C2 và Kết luận đều dùng chữ "consistency". [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G6. Nói rõ nghĩa của "approximate active set"
- Trong câu dẫn của (12)–(13), dòng 192–194: "…a $\delta$-enlarged \emph{approximate active set} on each track:" → "…a $\delta$-enlarged \emph{approximate active set} on each track (`active' meaning within $\delta$ of the largest violation):"
  **Dịch:** "…một *tập active xấp xỉ* nới rộng thêm $\delta$ trên mỗi track ('active' nghĩa là cách vi phạm lớn nhất không quá $\delta$):"

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G7. Ký hiệu trùng nghĩa
| Ký hiệu | Vị trí | Đề xuất |
|---|---|---|
| $n$, $x_i$, chỉ số $k$ | đầu §4.1, dòng 747 | Thêm câu: "Here $n$ is the number of samples; subscripts index features and superscripts index iterations." — *Dịch:* "Ở đây $n$ là số mẫu; chỉ số dưới đánh số đặc trưng, chỉ số trên đánh số vòng lặp." |
| $p$ là $p$-value | dòng 904 | "all-zero pairs have $p=1$" → "all-zero pairs receive the $p$-value $1$" — *Dịch:* "các cặp toàn số 0 nhận giá trị $p$ bằng 1". |
| $Q$ thay vì $Q_R$ | dòng 831 | "including $Q$" → "including $Q_R$". |
| $D_\rho$ | dòng 801, 817 | Đổi $D_\rho$ thành $U_\rho$ (đây chính là lân cận mở $U$ của Giả thiết 1). |
| $D_k$ trong SG | dòng 1053–1057 | Đổi thành $\mathcal I_k$ (xem G8). |
| $\epsilon$ (tham số Young) | dòng 465–480, 567 | Đổi thành $\zeta$, để tránh trùng với ngưỡng dừng $\varepsilon$. |
| $L'$ | dòng 644–647 | Đổi thành $L'_B$, như trong Bổ đề 3.7. |
| $\rho_{\cvx}$ và vector Fisher $\rho$ | — | **Giữ nguyên.** Chỉ số dưới đã phân biệt ($\rho_{\cvx}$ luôn có "cvx"; $\rho_k$ là thành phần Fisher). |
| $H$ và $\mathbb R^n$ | — | **Giữ nguyên.** $\mathbb R^n$ dùng ở Introduction trước khi $H$ được định nghĩa; từ §2 trở đi dùng $H$. |

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G8. Định nghĩa SG-const và SG-dyn trước khi dùng
Chuyển định nghĩa từ §4.4 (dòng 1053–1060) lên cuối §4.2.1 và rút gọn. Ở §4.4 chỉ giữ phần tinh chỉnh (mục 78). Số chữ gần như không đổi, vì đây là chuyển chỗ.

**Đề xuất (đoạn mới ở §4.2.1):**
> \paragraph*{SG-const and SG-dyn}
> These subgradient methods for quasiconvex feasibility~\citep{hu2022quasi} follow its most-violated-constraint strategy: with $\mathcal I_k=\argmax_i v_i(w^k)$,
> \[ w^{k+1}=P_K(w^k-\nu_k\bar h_k),\qquad \bar h_k=\frac1{|\mathcal I_k|}\sum_{i\in\mathcal I_k}\frac{\nabla F_i(w^k)}{\|\nabla F_i(w^k)\|}. \]
> SG-const uses $\nu_k=10^{-3}$; SG-dyn uses the dynamic step $\nu_k=J(w^k)/L$ (H\"older exponent $1$), with $L=\widehat L$, the largest gradient norm at $500$ points sampled in $K$.

**Dịch:**
> **SG-const và SG-dyn.** Hai phương pháp dưới gradient cho bài toán khả thi tựa lồi này [7] theo chiến lược "ràng buộc bị vi phạm nhiều nhất" của [7]: với $\mathcal I_k=\argmax_i v_i(w^k)$, chúng lặp theo công thức trên. SG-const dùng $\nu_k=10^{-3}$; SG-dyn dùng bước động $\nu_k=J(w^k)/L$ (số mũ Hölder bằng 1), với $L=\widehat L$ là chuẩn gradient lớn nhất tại 500 điểm lấy mẫu trong $K$.

*Lý do:* SG-const và SG-dyn được dùng ở §4.2–4.3 nhưng đến §4.4 mới được định nghĩa. Đã kiểm `hu2022.py`: công thức trong code khớp với công thức trên. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G9. Mô tả cách tính ngưỡng $b_i$
**Gốc (dòng 822):**
> Externally specified thresholds remain fixed. Training-based thresholds instead define the benchmark instance and must be shared by all solvers. Separate empirical percentiles do not ensure $\Omega\ne\varnothing$. A common point must satisfy all constraints, and checks to a numerical tolerance establish only the corresponding approximate feasibility. The threshold protocol and constraint-activity diagnostics are reported with the experiments.

**Đề xuất:**
> The thresholds are calibrated on the training data: $b_i$ is the $q_i$-th percentile of $F_i$ over $3\,000$ Dirichlet points (seed $42$) and the $p$ vertices of $K$, where a fixed rule chooses $q_i$ from the sample size, the number of features and classes, and the class imbalance (supplementary metadata). All solvers share these thresholds. Calibrating each $b_i$ separately does not guarantee $\Omega\ne\varnothing$; Section~\ref{ssec:feasibility-audit} checks feasibility numerically. Prescribed thresholds would be used as given.

**Dịch:**
> Các ngưỡng được hiệu chỉnh trên dữ liệu huấn luyện: $b_i$ là phân vị bậc $q_i$ của $F_i$ trên 3 000 điểm Dirichlet (seed 42) và $p$ đỉnh của $K$, trong đó một quy tắc cố định chọn $q_i$ theo cỡ mẫu, số đặc trưng và số lớp, và độ mất cân bằng lớp (metadata bổ sung). Mọi bộ giải dùng chung các ngưỡng này. Hiệu chỉnh riêng từng $b_i$ không bảo đảm $\Omega\ne\varnothing$; Mục 4.4 kiểm tra tính khả thi bằng số. Nếu ứng dụng quy định sẵn ngưỡng thì dùng nguyên các ngưỡng đó.

**Kèm theo**, dòng 1021–1026 (khoảng 60 từ) được thay bằng một câu ngắn hơn: "As noted in Section~\ref{ssec:reduction}, the calibrated thresholds need not yield $\Omega\ne\varnothing$." — **Dịch:** "Như đã nêu ở Mục 4.1.3, các ngưỡng hiệu chỉnh không nhất thiết cho $\Omega\ne\varnothing$."

*Lý do:* bài hiện không có câu nào nói $b_i$ được tính thế nào (Reviewer 1 hỏi ở R1.4). Sau khi gộp hai chỗ, tổng số chữ giảm. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G10. Định nghĩa $A^\star$
- Sau câu về bỏ phiếu đa số ở dòng 881. **Đề xuất (câu mới):** "We denote the voted feature set by $A^\star$." **Dịch:** "Ta ký hiệu tập đặc trưng sau bỏ phiếu là $A^\star$."

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G11. Gọi đúng tên (5): đây là định nghĩa, không còn là "contrapositive"
| Dòng | Gốc | Đề xuất |
|---|---|---|
| 386 | applying the contrapositive~\eqref{eq:contrapositive} with $y=x^\star$ gives | applying~\eqref{eq:contrapositive} with $y=x^\star$ gives |
| 638 | the contrapositive~\eqref{eq:contrapositive} with $x=\bar x$, $y=x^\star$ gives | definition~\eqref{eq:contrapositive} with $x=\bar x$, $y=x^\star$ gives |
| 313 | the contrapositive of pseudoconvexity gives only sign information | (mục 45) |

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G12. Bỏ phần lặp và phần thừa
- (15), dòng 202: bỏ định nghĩa $\Phi^{\ps}$, vì không được dùng ở đâu. Câu dẫn "On these sets we form the per-track local functions and directions" giữ nguyên.
- (9), dòng 182. **Gốc:** "$v_i(x):=\bigl(F_i(x)-b_i\bigr)^+,\qquad J(x)=\max_{1\le i\le m}v_i(x).$" **Đề xuất:** chỉ giữ $v_i(x):=(F_i(x)-b_i)^+$ trong (9), rồi viết tiếp "so that $J(x)=\max_i v_i(x)$ by~\eqref{eq:Jdef}." **Dịch:** "nên $J(x)=\max_i v_i(x)$ theo (8)."

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G13. Chuyển chỗ (không đổi câu chữ, trừ chỗ ghi ở mục khác)
- Đoạn 309–323 ("The convergence analysis … ε-feasible point"): chuyển từ cuối §3.5 lên đầu §3.6. Câu chữ của đoạn 309–317 được viết lại ở mục 45.
- Câu 127 về chi phí chiếu lên đơn hình: chuyển vào Nhận xét 6 (mục 32).
- Phần số liệu của Nhận xét 4: chuyển xuống §4.4 (mục 51).

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

---

## Phần II. Từng câu

### A0. Abstract (dòng 68), viết lại toàn bộ (gộp các mục 1–6)
**Đề xuất:**
> We study a nonlinear split feasibility problem in $\R^n$ whose output set is a normal box and whose components are differentiable and either convex or pseudoconvex. The Dual-Track Adaptive Projection (DTAP) algorithm splits the constraints into a convex and a pseudoconvex track. It takes a residual-scaled Polyak-type step on the nearly most violated convex constraints and a safeguarded diminishing step on the nearly most violated pseudoconvex ones, combines the two steps by a proportional weight, and projects onto the base set. The weight is a residual-responsive choice, without a claim of optimality. Its step sizes require no prescribed operator norm, Lipschitz constant, or H\"older modulus; the proof uses bounds over a bounded set containing the iterates. If the problem is consistent and the components are continuously differentiable, the whole sequence converges to a feasible point. In a feature-selection application all three constraints are convex. Experiments with constraint-activity counts, tuned subgradient methods and nonconvex pseudoconvex test problems show that tuned subgradient methods can match or outperform DTAP, and that DTAP is sensitive to its starting point and step scale.

**Dịch:**
> Ta nghiên cứu một bài toán chấp nhận tách phi tuyến trong $\R^n$, có tập đầu ra là hộp chuẩn và các thành phần khả vi, mỗi thành phần lồi hoặc giả lồi. Thuật toán Chiếu Thích nghi Hai Track (DTAP) chia các ràng buộc thành một track lồi và một track giả lồi. Thuật toán lấy một bước kiểu Polyak co theo phần dư trên các ràng buộc lồi gần bị vi phạm nhiều nhất, và một bước giảm dần có chặn an toàn trên các ràng buộc giả lồi gần bị vi phạm nhiều nhất. Hai bước được kết hợp bằng một trọng số tỉ lệ, rồi chiếu lên tập cơ sở. Trọng số này là một lựa chọn phản ứng theo phần dư, không khẳng định là tối ưu. Độ dài bước không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder; chứng minh dùng các cận trên một tập bị chặn chứa dãy lặp. Nếu bài toán nhất quán và các thành phần khả vi liên tục thì toàn bộ dãy hội tụ tới một điểm khả thi. Trong ứng dụng chọn đặc trưng, cả ba ràng buộc đều lồi. Các thực nghiệm (đếm mức hoạt động của ràng buộc, so với các phương pháp dưới gradient đã tinh chỉnh, và thử trên bài toán có ràng buộc giả lồi không lồi) cho thấy các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, và DTAP nhạy với điểm xuất phát và thang bước.

*Lý do:* định nghĩa "track" ngay trong Abstract; giới thiệu trọng số trước khi dùng; nêu rõ giả thiết; nói rõ "convex subclass" là gì; gom các câu giới hạn về một câu cuối. Các cụm R1.1 và R1.2 của letter trích được giữ nguyên ("a residual-responsive choice, without a claim of optimality"; "require no prescribed operator norm, Lipschitz constant, or Hölder modulus"). Riêng cụm R1.2 "the proof uses local bounds on the bounded iterate region" đổi thành "the proof uses bounds over a bounded set containing the iterates", nên letter cần sửa theo. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 7–8. Introduction, dòng 80
**Gốc:** "The split feasibility problem (SFP) models constrained reconstruction~\citep{censor1994}. For closed convex sets $C\subseteq\R^n$, $Q\subseteq\R^m$, and a matrix $\mathcal A$, it seeks"
**Đề xuất:** "The split feasibility problem (SFP) was introduced by Censor and Elfving~\citep{censor1994} as a model for constrained inverse problems. Given nonempty closed convex sets $C\subseteq\R^n$ and $Q\subseteq\R^m$ and a matrix $\mathcal A\in\R^{m\times n}$, it asks to"
**Dịch:** "Bài toán chấp nhận tách (SFP) được Censor và Elfving [4] đưa ra như một mô hình cho các bài toán ngược có ràng buộc. Cho các tập lồi đóng khác rỗng $C\subseteq\R^n$, $Q\subseteq\R^m$ và một ma trận $\mathcal A\in\R^{m\times n}$, bài toán yêu cầu"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 9. Dòng 84
**Gốc:** "Byrne's $CQ$ algorithm~\citep{byrne2002} uses"
**Đề xuất:** "Byrne's $CQ$ algorithm~\citep{byrne2002} iterates" (và sau (2) thêm: "where $\norm{\mathcal A}$ is the spectral norm of $\mathcal A$.")
**Dịch:** "Thuật toán $CQ$ của Byrne [3] lặp theo … trong đó $\norm{\mathcal A}$ là chuẩn phổ của $\mathcal A$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 10–11. Dòng 89
**Gốc:** "Supporting half-spaces simplify projections~\citep{yang2004}, while self-adaptive steps reduce parameter dependence~\citep{…}. Operator splitting~\citep{…} and modified alternating directions~\citep{…} provide decomposition strategies. Adaptive steps and decomposition are therefore established principles."
**Đề xuất:** "Relaxed variants project onto supporting half-spaces~\citep{yang2004}; self-adaptive steps avoid estimating $\norm{\mathcal A}$~\citep{zhang2009adaptive,zhao2011adaptive,lopez2012}; operator splitting~\citep{zhang2012simultaneous} and alternating direction methods~\citep{yang2014alternating} decompose the problem. These ideas are standard; DTAP adapts them to the nonlinear case."
**Dịch:** "Các biến thể nới lỏng chiếu lên nửa không gian tựa [17]; bước tự thích nghi tránh phải ước lượng $\norm{\mathcal A}$ [20, 22, 10]; tách toán tử [21] và phương pháp hướng luân phiên [18] phân rã bài toán. Các ý tưởng này đã là chuẩn mực; DTAP vận dụng chúng cho trường hợp phi tuyến."
*Lý do:* thay các cụm tối nghĩa ("simplify projections", "parameter dependence") và từ nối sai "therefore". [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 12–15. Dòng 91–95
**Gốc:** "We study the nonlinear SFP (3) where $K\subseteq\R^n$ is closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$, and each differentiable component of $F$ … is convex or pseudoconvex on $K$. Pseudoconvex functions have convex sublevel sets, so the feasible set is convex even when some components are nonconvex. We seek feasibility, rather than minimization of every component."
**Đề xuất:** "Replacing $\mathcal A$ by a nonlinear map $F$ gives the nonlinear SFP~\citep{li2013nsfp,yen2019}. We study (3), where $K\subseteq\R^n$ is nonempty, closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$ is a normal box, and each $F_i$ is differentiable and convex or pseudoconvex on $K$. Since pseudoconvex functions have convex sublevel sets, the feasible set $\Omega=\{x\in K:F(x)\in Q\}$ is convex. We seek a point of $\Omega$, not a minimizer of any $F_i$."
**Dịch:** "Thay $\mathcal A$ bằng một ánh xạ phi tuyến $F$ ta được SFP phi tuyến [9, 19]. Ta nghiên cứu (3), trong đó $K\subseteq\R^n$ khác rỗng, đóng và lồi, $Q=\prod_{i=1}^m(-\infty,b_i]$ là hộp chuẩn, và mỗi $F_i$ khả vi và lồi hoặc giả lồi trên $K$. Vì hàm giả lồi có các tập mức dưới lồi, tập khả thi $\Omega=\{x\in K:F(x)\in Q\}$ là lồi. Ta tìm một điểm thuộc $\Omega$, không tìm điểm cực tiểu của $F_i$ nào."
*Lý do:* thêm câu chuyển ý; thêm "nonempty"; sửa câu đọc ra hai nghĩa "each differentiable component"; đặt tên $\Omega$. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 16–18. Dòng 97
**Gốc:** "Nonlinear SFP and generalized convex feasibility have several relevant antecedents. Li et al. use a convex aggregate proximity function, a property not ensured by componentwise pseudoconvexity. Yen et al. combine equilibrium and nonlinear image constraints. Hu et al. treat quasiconvex inequalities, which include our component class. Our method exploits the additional derivative information of convex components within this established feasibility setting."
**Đề xuất:** "Li et al.~\citep{li2013nsfp} assume a convex aggregate proximity function, which componentwise pseudoconvexity does not ensure. Yen et al.~\citep{yen2019} use the same max-type violation measure and active-set device, but require quasilinear components, a class incomparable with ours. Hu et al.~\citep{hu2022quasi} treat quasiconvex inequalities, which contain our class, without using the gradient inequality of convex components."
**Dịch:** "Li và cộng sự [9] giả thiết hàm lân cận tổng hợp lồi, điều mà tính giả lồi của từng thành phần không bảo đảm. Yen và cộng sự [19] dùng cùng hàm đo vi phạm kiểu max và cùng kỹ thuật tập active, nhưng đòi các thành phần tựa tuyến tính, một lớp không so sánh được với lớp của ta. Hu và cộng sự [7] xét bất đẳng thức tựa lồi, một lớp chứa lớp của ta, nhưng không dùng bất đẳng thức gradient của các thành phần lồi."
*Lý do:* sửa cụm "a property" đọc ra hai nghĩa; nêu rõ vì sao Yen et al. liên quan và khác bài này ở đâu; bỏ câu mở đầu và câu kết rỗng nghĩa. Phản ví dụ $x^2$, $x^3$ không đưa vào Introduction vì là chi tiết; có thể nêu trong letter nếu cần. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 19. Dòng 99
**Gốc:** "The box gives the explicit violation measure"
**Đề xuất:** "Because $Q$ is a box, the $\ell_\infty$-distance from $F(x)$ to $Q$ has the closed form"
**Dịch:** "Vì $Q$ là một hộp, khoảng cách $\ell_\infty$ từ $F(x)$ tới $Q$ có dạng tường minh"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 20–24. Dòng 103, viết lại cả đoạn
**Gốc:** (đoạn 10 câu, bắt đầu "The Dual-Track Adaptive Projection algorithm (\dtap) forms violation-weighted gradient sums…")
**Đề xuất:**
> DTAP splits the constraints into a convex track and a pseudoconvex track. On each track it sums the gradients of the nearly most violated constraints, weighted by their violations. The gradient inequality of convex functions justifies a residual-scaled Polyak-type step on the convex track~\citep{polyak1969,lopez2012}; pseudoconvexity gives only the sign of a directional derivative, so the pseudoconvex track uses a safeguarded diminishing step. A proportional weight combines the two steps, and the result is projected onto $K$; the proof uses this weight only to keep a persistently violated track active (Remark~\ref{rem:weight-scope}). No prescribed operator norm, Lipschitz constant, or H\"older modulus is needed: a quasi-Fej\'er inequality shows that the iterates are bounded, and the proof then uses local bounds, without Lipschitz gradients.

**Dịch:**
> DTAP chia các ràng buộc thành một track lồi và một track giả lồi. Trên mỗi track, nó cộng các gradient của những ràng buộc gần bị vi phạm nhiều nhất, có trọng số theo độ vi phạm. Bất đẳng thức gradient của hàm lồi biện minh cho một bước kiểu Polyak co theo phần dư trên track lồi [14, 10]; tính giả lồi chỉ cho biết dấu của đạo hàm theo hướng, nên track giả lồi dùng một bước giảm dần có chặn an toàn. Một trọng số tỉ lệ kết hợp hai bước, rồi kết quả được chiếu lên $K$; chứng minh chỉ dùng trọng số này để giữ cho một track bị vi phạm kéo dài vẫn có trọng số dương (Nhận xét 1). Không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder: một bất đẳng thức tựa Fejér cho thấy dãy lặp bị chặn, sau đó chứng minh dùng các cận địa phương, không cần gradient Lipschitz.

*Lý do:* nối các câu ngắn rời rạc thành một mạch; thay cụm "preventing neglect" bằng ý cụ thể; câu "one-step bound…" đã có ở Nhận xét 1 nên bỏ. Đoạn mới ngắn hơn đoạn gốc. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 25–27. Dòng 105, viết lại cả đoạn
**Gốc:** (đoạn bắt đầu "Feature-selection criteria from fractional and fuzzy-rough models … define separate threshold constraints.")
**Đề xuất:**
> As an application, upper bounds on three criteria from a fractional model~\citep{wang2021fractional} and a fuzzy-rough model~\citep{wang2026afrsfcv} define the constraints; a feasible weight vector satisfies all three bounds but need not solve either source problem. These constraints are convex (Proposition~\ref{prop:fs-reg}), so we also use test problems with a nonconvex pseudoconvex constraint to exercise the pseudoconvex track.

**Dịch:**
> Làm ứng dụng, các cận trên của ba tiêu chí lấy từ một mô hình phân thức [15] và một mô hình tập thô mờ [16] tạo thành các ràng buộc; một vector trọng số khả thi thỏa cả ba cận nhưng không nhất thiết là nghiệm của bài toán gốc nào. Các ràng buộc này lồi (Mệnh đề 4.1), nên ta còn dùng các bài toán thử có ràng buộc giả lồi không lồi để kiểm tra track giả lồi.

*Lý do:* thay cụm tối nghĩa "simultaneous acceptance"; tách cụm chồng danh từ; bỏ câu 32 từ. Chi tiết về phép chia train/test thuộc về §4.2.2, còn câu "tuned subgradient methods can match…" đã có trong Abstract và Kết luận, nên cả hai đều bỏ khỏi đoạn này. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 28–30. Các đóng góp C1–C3 (dòng 109–111)
**Đề xuất:**
> C1. A dual-track method that uses the gradient inequality on the convex constraints and only sign information on the pseudoconvex ones, without assuming a convex proximity function, unlike~\citep{li2013nsfp}, or a H\"older modulus, unlike the dynamic step of~\citep{hu2022quasi}.
> C2. Convergence of the whole sequence to a feasible point under Assumption~\ref{ass:standing} (Theorem~\ref{thm:strong}).
> C3. Experiments that report constraint activity, compare DTAP with tuned subgradient methods, and measure its sensitivity to the starting point and the step scale.

**Dịch:**
> C1. Một phương pháp hai track dùng bất đẳng thức gradient trên các ràng buộc lồi và chỉ thông tin về dấu trên các ràng buộc giả lồi, không cần giả thiết hàm lân cận lồi như [9], cũng không cần mô-đun Hölder như bước động của [7].
> C2. Sự hội tụ của toàn bộ dãy tới một điểm khả thi dưới Giả thiết 1 (Định lý 3.12).
> C3. Các thực nghiệm báo cáo mức hoạt động của ràng buộc, so sánh DTAP với các phương pháp dưới gradient đã tinh chỉnh, và đo độ nhạy của DTAP với điểm xuất phát và thang bước.

*Lý do:* các cụm "the stated step conditions" và "distinguish prediction from feasibility cost" được thay bằng tham chiếu cụ thể. So sánh với Yen et al. đã có ở đoạn 97 nên không lặp lại. Bỏ các câu giới hạn lặp ("They do not establish uniform superiority", "Convergence of distances… suffice"). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 31. §2, dòng 118
**Gốc:** "Throughout, $H=\R^n$ is Euclidean space with…" → **Đề xuất:** "Throughout, $H=\R^n$ is the Euclidean space with…" — **Dịch:** "Trong toàn bài, $H=\R^n$ là không gian Euclid với…"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 32–33. Dòng 127
**Gốc:** "This characterization gives the projection inequality used in Lemma~\ref{lem:proj-nonexp}. The sort-based projection onto a $p$-dimensional simplex takes $O(p\log p)$ operations~\citep{condat2016simplex}."
**Đề xuất:** "This characterization yields Lemma~\ref{lem:proj-nonexp} below." Câu thứ hai chuyển sang Nhận xét 6, dòng 831: "Projection onto $K=\Delta_{p-1}$ by sorting costs $O(p\log p)$ operations~\citep{condat2016simplex}."
**Dịch:** "Đặc trưng này cho ta Bổ đề 3.2 dưới đây." / "Phép chiếu lên $K=\Delta_{p-1}$ bằng sắp xếp tốn $O(p\log p)$ phép tính [6]."
*Lý do:* đơn hình $\Delta_{p-1}$ có $p-1$ chiều, và $p$ chưa được định nghĩa ở §2. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 34. Định nghĩa 2.2 (dòng 133)
**Gốc:** "A function differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for every $x,y\in K$,"
**Đề xuất:** "A function $f$ that is differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for all $x,y\in K$,"
**Dịch:** "Một hàm $f$ khả vi trên một lân cận mở của $K$ được gọi là giả lồi trên $K$ nếu, với mọi $x,y\in K$,"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 36. Dòng 138
**Gốc:** "…need not be convex. This distinction is relevant to the mixed constraint functions studied below."
**Đề xuất:** bỏ câu thứ hai.
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 37. Tiêu đề §3.2 (dòng 173)
**Gốc:** "Decomposition and dual-track scalarization" → **Đề xuất:** "Decomposition into two tracks" — **Dịch:** "Phân tách thành hai track"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 38. Dòng 168
**Gốc:** "Then $F(x)\in Q$ iff $J(x)=0$, so finding a feasible point amounts to minimizing $J$ over $K$."
**Đề xuất:** "Then $x\in K$ is feasible if and only if $J(x)=0$; when $\Omega\ne\emptyset$, the feasible points are the minimizers of $J$ over $K$."
**Dịch:** "Khi đó $x\in K$ khả thi khi và chỉ khi $J(x)=0$; khi $\Omega\ne\emptyset$, các điểm khả thi chính là các điểm cực tiểu của $J$ trên $K$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 39. Dòng 192
**Gốc:** "we replace the exact maximizers by a $\delta$-enlarged \emph{approximate active set} on each track:"
**Đề xuất:** "we replace the set of indices at which the maximum is attained by a $\delta$-enlarged \emph{approximate active set} on each track:" (kèm câu G6 sau (13))
**Dịch:** "ta thay tập các chỉ số đạt cực đại bằng một *tập active xấp xỉ* nới rộng thêm $\delta$ trên mỗi track:"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 40. Giả thiết (A1)(b) (dòng 214–215)
**Gốc:** "for each $i$, $F_i:U\to\R$, and the restriction $F_i|_K$ is convex if $i\in I^{\cvx}$ and pseudoconvex if $i\in I^{\ps}$."
**Đề xuất:** "each $F_i:U\to\R$ is convex on $K$ if $i\in I^{\cvx}$ and pseudoconvex on $K$ if $i\in I^{\ps}$."
**Dịch:** "mỗi $F_i:U\to\R$ lồi trên $K$ nếu $i\in I^{\cvx}$ và giả lồi trên $K$ nếu $i\in I^{\ps}$."
*Lý do:* Định nghĩa 2.2 áp cho hàm khả vi trên một lân cận của $K$; hạn chế $F_i|_K$ không có lân cận nên không áp được. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 41. Nhãn trong Giả thiết 1 (mức 3)
**Đề xuất:** giữ nguyên. Nếu đổi (A3)(i)–(iii) thành (a)–(c) thì phải sửa khoảng 10 chỗ "(A3)(iii)" trong bài, mà lợi ích không đáng kể.
[ ] Duyệt giữ nguyên [ ] Đổi

### Mục 42. Thuật toán 1, kiểm tra dừng
**Đề xuất:** chuyển Bước 3 thành bước đầu của Bước 1: "(1a) If $J(x^k)\le\varepsilon$, stop and return $x^k$. Otherwise compute $v_i(x^k)$…", và Bước 2 kết thúc bằng "set $k\leftarrow k+1$ and go to Step 1".
**Dịch:** "(1a) Nếu $J(x^k)\le\varepsilon$, dừng và trả về $x^k$. Ngược lại, tính $v_i(x^k)$… ; Bước 2: … đặt $k\leftarrow k+1$ và quay lại Bước 1."
*Lý do:* hiện điểm $x^{k+1}$ được tính rồi mới kiểm tra điều kiện dừng cho $x^k$. Thay đổi này không ảnh hưởng chứng minh, vì chứng minh xét dãy đã bỏ điều kiện dừng. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 43. Nhận xét 1 (dòng 276–281)
**Gốc:** "…we do not claim that it is the only convergent choice or that it is optimal. … Although the one-step inequality holds for any $\mu_k\in[0,1]$, this alone does not establish convergence for every such sequence."
**Đề xuất:** "…we do not claim that it is the only choice for which DTAP converges, or that it is optimal. … Although the one-step inequality of Lemma~\ref{lem:fejer} holds for every $\mu_k\in[0,1]$, it does not by itself imply convergence for every weight sequence."
**Dịch:** "…ta không khẳng định đây là lựa chọn duy nhất giúp DTAP hội tụ, cũng không khẳng định nó tối ưu. … Dù bất đẳng thức một bước của Bổ đề 3.8 đúng với mọi $\mu_k\in[0,1]$, riêng nó không suy ra hội tụ với mọi dãy trọng số."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 44. Nhận xét 2, câu cuối (dòng 291)
**Gốc:** "The parameters $\rho_{\cvx}$, $\delta$, and $\{\gamma_k\}$ remain part of the algorithm."
**Đề xuất:** "The user still chooses $\rho_{\cvx}$, $\delta$, and $\{\gamma_k\}$; these parameters do not depend on any constant of the problem."
**Dịch:** "Người dùng vẫn phải chọn $\rho_{\cvx}$, $\delta$ và $\{\gamma_k\}$; các tham số này không phụ thuộc vào hằng số nào của bài toán."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 45–46. Đoạn 309–317 (chuyển lên đầu §3.6)
**Gốc:** "The convergence analysis of \dtap{} is more involved than for classical $CQ$ schemes because the two constraint tracks are asymmetric: … The two are reconciled in a single one-step quasi-Fej\'er inequality with a carefully chosen Young parameter, and a contradiction argument rules out cluster points outside the feasible set. We then obtain the main result, strong convergence to a feasible point (Theorem 3.12), and deduce the two degenerate structural regimes as corollaries."
**Đề xuất:**
> The two tracks need different arguments. On the convex track, Lemma~\ref{lem:grad-cvx} bounds $\inner{\nabla F_i(x)}{x-x^\star}$ from below by the violation $v_i(x)$; this gives a decrease of $\norm{x^k-x^\star}^2$ of order $\mu_kT_k$. On the pseudoconvex track, definition~\eqref{eq:contrapositive} gives only the sign of this inner product. Lemma~\ref{lem:fejer} combines both tracks in one quasi-Fej\'er inequality; the choice of the parameter $\zeta$ in Young's inequality keeps the convex-track term negative. Stage~2 of Theorem~\ref{thm:strong} then shows, by contradiction, that at least one cluster point is feasible, and Stage~3 shows that the whole sequence converges to it. The two degenerate cases follow as corollaries.

**Dịch:**
> Hai track cần hai lập luận khác nhau. Trên track lồi, Bổ đề 3.4 chặn dưới $\inner{\nabla F_i(x)}{x-x^\star}$ bởi độ vi phạm $v_i(x)$; điều này cho một độ giảm của $\norm{x^k-x^\star}^2$ cỡ $\mu_kT_k$. Trên track giả lồi, định nghĩa (5) chỉ cho biết dấu của tích vô hướng này. Bổ đề 3.8 kết hợp hai track trong một bất đẳng thức tựa Fejér; việc chọn tham số $\zeta$ trong bất đẳng thức Young giữ cho số hạng của track lồi âm. Sau đó, Giai đoạn 2 của Định lý 3.12 chứng minh bằng phản chứng rằng có ít nhất một điểm tụ khả thi, và Giai đoạn 3 chứng minh toàn bộ dãy hội tụ tới điểm đó. Hai trường hợp suy biến là các hệ quả.

*Lý do:* câu gốc dài 51 từ (45); quan trọng hơn, câu "rules out cluster points outside the feasible set" **sai so với chứng minh**: Stage 2 chỉ chỉ ra tồn tại một điểm tụ khả thi, đúng chỗ Reviewer 1 soi ở R1.3 (46). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 47. Dòng 430
**Gốc:** "The following quasi-Fej\'er inequality, within the framework of~\citet{combettes2001quasifejer}, yields boundedness of $\{x^k\}$ and decay of the convex-track violation. Set"
**Đề xuất:** "The following inequality is of quasi-Fej\'er type in the sense of Combettes~\citep{combettes2001quasifejer}. It yields boundedness of $\{x^k\}$ and decay of the convex-track violation. Set"
**Dịch:** "Bất đẳng thức sau thuộc loại tựa Fejér theo nghĩa của Combettes [5]. Nó cho tính bị chặn của $\{x^k\}$ và sự suy giảm độ vi phạm trên track lồi. Đặt"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 48. Chứng minh Bổ đề 3.10 (dòng 515, 535)
**Gốc:** "Assume $I^{\cvx}\ne\emptyset$ and put $B:=…$" … (dòng 535) "Fix $x^\star\in\Omega$. Remark~3 gives"
**Đề xuất:** "Assume $I^{\cvx}\ne\emptyset$, fix $x^\star\in\Omega$, and put $B:=…$" và ở dòng 535 bỏ "Fix $x^\star\in\Omega$.": "Remark~3 gives"
**Dịch:** "Giả sử $I^{\cvx}\ne\emptyset$, cố định $x^\star\in\Omega$ và đặt $B:=…$"
*Lý do:* hiện $x^\star$ được dùng ở trường hợp $L=0$ trước khi được cố định. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 49. Đầu §3.8 (dòng 572–576) và tên các giai đoạn
**Gốc:** "The goal of the analysis is strong convergence of $\{x^k\}$ to a feasible point. The argument has three stages: exploit convex-track feasibility (Lemma 3.10) to confine the cluster set to the convex half; use a contradiction argument with pseudoconvexity to produce a cluster point in $\Omega$; and combine with distance convergence to upgrade to convergence of the whole sequence."
**Đề xuất:** "We now prove that the whole sequence converges to a feasible point. The proof has three stages. Stage~1 uses Lemma~\ref{lem:jcvx0} to show that every cluster point satisfies the convex constraints. Stage~2 shows, by contradiction and pseudoconvexity, that at least one cluster point is feasible. Stage~3 uses the convergence of $\norm{x^k-\bar x}$ to show that the whole sequence converges to that point."
Trong chứng minh: "\emph{Stage 1 (convex half)}" → "\emph{Stage 1 (convex constraints)}"; "\emph{Stage 2 (pseudoconvex half by contradiction)}" → "\emph{Stage 2 (a feasible cluster point)}".
**Dịch:** "Ta chứng minh toàn bộ dãy hội tụ tới một điểm khả thi. Chứng minh gồm ba giai đoạn. Giai đoạn 1 dùng Bổ đề 3.10 để chỉ ra mọi điểm tụ thỏa các ràng buộc lồi. Giai đoạn 2 chứng minh bằng phản chứng và tính giả lồi rằng có ít nhất một điểm tụ khả thi. Giai đoạn 3 dùng sự hội tụ của $\norm{x^k-\bar x}$ để chỉ ra toàn bộ dãy hội tụ tới điểm đó." / "Giai đoạn 1 (các ràng buộc lồi)"; "Giai đoạn 2 (một điểm tụ khả thi)".
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 50. Dòng 663–664
**Gốc:** "This argument requires neither uniqueness of the feasible point nor convexity of the target set: one feasible cluster point and convergence of its distance suffice."
**Đề xuất:** "The argument does not require $\Omega$ to be a singleton: one feasible cluster point and the convergence of its distance suffice."
**Dịch:** "Lập luận không đòi $\Omega$ chỉ có một điểm: chỉ cần một điểm tụ khả thi và sự hội tụ của khoảng cách tới nó."
*Lý do:* dưới Giả thiết 1, $\Omega$ luôn lồi (dòng 224), nên vế "nor convexity of the target set" gây hiểu lầm. *Letter:* R1.3 đang trích nguyên văn câu gốc, cần sửa theo. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 51. Nhận xét 4 (dòng 674–680)
**Gốc:** "Larger $\delta$ enlarges $K^{\cvx}_k,K^{\ps}_k$, which may aid numerical stability when several $v_i(x^k)$ are nearly equal; on the test problem~(47), $\delta=10^{-1}$ and $\delta=10^{-3}$ produce identical iterates (Table 8): … The $\delta$ row of Table 8 is therefore a consistency check, not evidence about $\delta$."
**Đề xuất (Nhận xét 4):** "Larger $\delta$ enlarges $K^{\cvx}_k$ and $K^{\ps}_k$, which may improve numerical stability when several $v_i(x^k)$ are nearly equal."
**Đề xuất (chuyển xuống §4.4, sau câu "$\delta=10^{-1}$ reproduces the baseline iterates exactly", dòng 1193):** "This happens because the pseudoconvex track has a single index, at every start either only $F_1$ is violated or $v_1-v_2\ge4.79$, and the convex track is satisfied from the second evaluated point on. The $\delta$ row of Table~\ref{tab:dtap-sweep} is therefore a consistency check, not evidence about the role of $\delta$."
**Dịch:** "$\delta$ lớn hơn làm $K^{\cvx}_k$ và $K^{\ps}_k$ lớn hơn, điều này có thể cải thiện độ ổn định số khi nhiều $v_i(x^k)$ gần bằng nhau." / "Điều này xảy ra vì track giả lồi chỉ có một chỉ số, tại mọi điểm xuất phát hoặc chỉ $F_1$ bị vi phạm hoặc $v_1-v_2\ge4.79$, và track lồi được thỏa từ điểm thứ hai trở đi. Vì vậy dòng $\delta$ của Bảng 8 chỉ là kiểm tra nhất quán, không phải bằng chứng về vai trò của $\delta$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 52. Dòng 644–647: $L'$ → $L'_B$ (xem G7). [ ] Duyệt [ ] Bỏ

### Mục 53. Đầu §4.1: câu ký hiệu (xem G7). [ ] Duyệt [ ] Bỏ

### Mục 54. Dòng 754
**Gốc:** "…and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$."
**Đề xuất:** "…and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$ is the interaction information of $Z_i$, $Z_j$ and $C$."
**Dịch:** "… là thông tin tương tác của $Z_i$, $Z_j$ và $C$."
*Lý do:* đã kiểm: biểu thức này bằng $I(Z_i;Z_j)-I(Z_i;Z_j\mid C)$, tức đúng là thông tin tương tác theo McGill. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 55. Dòng 794
**Gốc:** "The three terms measure label-approximation error, incorrect-decision confidence, and Tikhonov regularization, respectively."
**Đề xuất:** "The three terms are the label-approximation error, the weight of misclassifying features per sample, and a Tikhonov term."
**Dịch:** "Ba số hạng lần lượt là sai số xấp xỉ nhãn, tổng trọng số các đặc trưng phân loại sai trên mỗi mẫu, và một số hạng Tikhonov."
*Lý do:* cụm "incorrect-decision confidence" tối nghĩa. Đã kiểm: $1-(Pw)_i$ đúng bằng tổng trọng số các đặc trưng phân loại sai mẫu $i$. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 56. Dòng 803: "the first two components of (38)" → "the first two terms of (38)" — *Dịch:* "hai số hạng đầu của (38)". [ ] Duyệt [ ] Bỏ

### Mục 57. Mệnh đề 4.1, câu cuối (dòng 810)
**Gốc:** "It satisfies the function assumptions of Assumption 1 whenever $\Omega\ne\varnothing$."
**Đề xuất:** "Hence~\eqref{eq:nsfp-fs} satisfies (A1) and (A2) of Assumption~\ref{ass:standing}, with $U=U_\rho$, whenever $\Omega\ne\varnothing$."
**Dịch:** "Do đó (42) thỏa (A1) và (A2) của Giả thiết 1, với $U=U_\rho$, mỗi khi $\Omega\ne\varnothing$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 58. Dòng 820, câu 1–4
**Gốc:** "The assignment $I^{\cvx}=\{1,2\}$, $I^{\ps}=\{3\}$ used in the experiments is admissible because convexity implies pseudoconvexity. It treats $F_3$ conservatively and does not test a genuinely nonconvex constraint. The all-convex assignment $I^{\cvx}=\{1,2,3\}$ is also available. Under the assumptions of Theorem 3.12, either assignment converges to a feasible weight."
**Đề xuất:** "The experiments use $I^{\cvx}=\{1,2\}$, $I^{\ps}=\{3\}$, which is admissible since convex functions are pseudoconvex; DTAP then uses only sign information for $F_3$, so no genuinely nonconvex constraint is tested. The all-convex assignment $I^{\cvx}=\{1,2,3\}$ is also admissible, and Theorem~\ref{thm:strong} applies to both."
**Dịch:** "Thực nghiệm dùng $I^{\cvx}=\{1,2\}$, $I^{\ps}=\{3\}$; cách xếp này hợp lệ vì hàm lồi là giả lồi. Khi đó DTAP chỉ dùng thông tin về dấu của $F_3$, nên không có ràng buộc thực sự không lồi nào được kiểm tra. Cách xếp toàn lồi $I^{\cvx}=\{1,2,3\}$ cũng hợp lệ, và Định lý 3.12 áp dụng cho cả hai cách xếp."
*Lý do:* "conservatively" là ẩn dụ; "assignment converges" sai chủ ngữ (thuật toán hội tụ, không phải cách xếp). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 59. Dòng 820, câu 5–9; gộp với dòng 1031–1032
**Gốc:** "Score positivity must be checked on each instance. Replacing a zero score by a positive floor changes the model and must be declared. The implementation also uses $\max\{\rho^\top w,10^{-15}\}$ during evaluation. This agrees with (41) only where the floor is inactive. Applying the theorem to this implementation therefore requires that the floor remain inactive." và (dòng 1031) "All Fisher coordinates are positive on these instances, with minimum $5.99\times10^{-5}$."
**Đề xuất (thay câu 5–9; bỏ câu ở dòng 1031–1032):** "Proposition~\ref{prop:fs-reg} needs $\min_k\rho_k>0$; on all instances used here the smallest score is $4.77\times10^{-5}$. Hence the safeguard $\max\{\rho^\top w,10^{-15}\}$ in the implementation is never active, and the implemented $F_3$ is~\eqref{eq:fsF3}."
**Dịch:** "Mệnh đề 4.1 cần $\min_k\rho_k>0$; trên mọi bài toán dùng ở đây, điểm nhỏ nhất là $4.77\times10^{-5}$. Do đó ngưỡng an toàn $\max\{\rho^\top w,10^{-15}\}$ trong cài đặt không bao giờ có hiệu lực, và $F_3$ được cài đặt chính là (41)."
*Lý do:* thay các câu "phải kiểm tra" bằng kết quả kiểm tra thực tế. Con số $4.77\times10^{-5}$ là giá trị nhỏ nhất trên mọi fold (Spambase), nhỏ hơn giá trị $5.99\times10^{-5}$ của các bài toán dùng toàn bộ dữ liệu; tôi tính lại trong phiên này bằng code của package, nên chạy lại để xác nhận. Cả cụm giảm khoảng 25 từ. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 60. Đoạn ngưỡng (dòng 822): xem G9. [ ] Duyệt [ ] Bỏ

### Mục 61. Nhận xét 6 (dòng 831): "including $Q$" → "including $Q_R$", kèm câu chuyển từ mục 32. [ ] Duyệt [ ] Bỏ

### Mục 62. §4.2, dòng 835
**Gốc:** "SG-const uses step $10^{-3}$. The dynamic subgradient comparison is considered separately with sampled and empirically tuned moduli in the solver diagnostic."
**Đề xuất:** "SG-const uses the step $\nu_k=10^{-3}$ and SG-dyn the sampled modulus $\widehat L$ (Section~\ref{sssec:baselines}); tuned moduli are considered only in Section~\ref{ssec:feasibility-audit}."
**Dịch:** "SG-const dùng bước $\nu_k=10^{-3}$ và SG-dyn dùng mô-đun lấy mẫu $\widehat L$ (Mục 4.2.1); mô-đun tinh chỉnh chỉ được xét ở Mục 4.4."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 63. Số bước Euler
**Gốc (dòng 835):** "1000 Euler grid points on $[0,0.2]$" — đúng, giữ nguyên.
**Gốc (dòng 863):** "by explicit Euler on $[0,T]$ with $N_{\mathrm{step}}$ steps" → **Đề xuất:** xem mục 65.
*Lý do:* code dùng `linspace(0, T, 1000)`, tức 1000 điểm lưới và 999 bước. [ ] Duyệt [ ] Bỏ

### Mục 64. Dòng 856
**Gốc:** "The following updates specify the two baseline solvers for the models in Sections 4.1.1 and 4.1.2."
**Đề xuất:** "The following paragraphs specify the baseline solvers: N-Fscore and AFRSFCV for the models of Sections~\ref{sssec:nfscore} and~\ref{sssec:afrsfcv-model}, and the subgradient methods SG-const and SG-dyn."
**Dịch:** "Các đoạn sau mô tả các bộ giải đối chứng: N-Fscore và AFRSFCV cho các mô hình ở Mục 4.1.1 và 4.1.2, và hai phương pháp dưới gradient SG-const, SG-dyn."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 65. Dòng 863
**Gốc:** "We integrate (45) by explicit Euler on $[0,T]$ with $N_{\rm step}$ steps under a fixed budget (no stopping rule), with the fixed parameters reported in the experimental protocol, and take as weight vector the projection $P_K(g(u(T)))$ of the network output at the final time onto the simplex $K$."
**Đề xuất:** "We integrate~\eqref{eq:pnn} by the explicit Euler method on a uniform grid of $N_{\rm grid}$ points in $[0,T]$, without a stopping rule, using the parameters of Section~\ref{ssec:setup}. The weight vector is the projection $P_K(g(u(T)))$ of the final network output onto $K$."
**Dịch:** "Ta tích phân (45) bằng phương pháp Euler hiện trên một lưới đều gồm $N_{\rm grid}$ điểm trong $[0,T]$, không có quy tắc dừng, với các tham số ở Mục 4.2. Vector trọng số là hình chiếu $P_K(g(u(T)))$ của đầu ra cuối cùng của mạng lên $K$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 66. Dòng 886–891
**Gốc:** "No classifier parameter or vote threshold is chosen from these test outcomes. The same holdouts were used when the selections were computed, and the threshold heuristic uses the whole-dataset sample size, dimensions and class counts before splitting. Hence this is an exploratory evaluation, not an end-to-end or nested-validation study."
**Đề xuất:** "The test data are not used to select features or to choose any parameter or vote threshold. The training/test split is fixed before the selections are computed, and the rule that chooses the threshold levels uses only the sample size, the number of features, the number of classes and the class sizes of the whole dataset, not any feature values. Because a single split is used, this is an exploratory evaluation, not an end-to-end or nested-validation study."
**Dịch:** "Dữ liệu kiểm tra không được dùng để chọn đặc trưng hay để chọn bất kỳ tham số hoặc ngưỡng bỏ phiếu nào. Phép chia huấn luyện/kiểm tra được cố định trước khi tính các lựa chọn, và quy tắc chọn bậc ngưỡng chỉ dùng cỡ mẫu, số đặc trưng, số lớp và kích thước các lớp của toàn bộ dữ liệu, không dùng giá trị đặc trưng nào. Vì chỉ dùng một phép chia, đây là đánh giá thăm dò, không phải nghiên cứu đầu-cuối hay kiểm định lồng nhau."
*Lý do:* câu gốc có thể khiến phản biện nghi rò rỉ dữ liệu kiểm tra. Đã kiểm code: `dataset_adaptive_config(n, m, r, class_counts)` chỉ dùng các đại lượng này. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 67. Dòng 899–900
**Gốc:** "Here $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$; the unbiased variance correction is $N_f/(N_f-1)$, not $p/(p-1)$."
**Đề xuất:** "Here $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$, and $s_j^2$ is the unbiased variance over the $N_f$ folds."
**Dịch:** "Ở đây $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$, và $s_j^2$ là phương sai không chệch trên $N_f$ fold."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 68. Dòng 904: $p$-value (xem G7). [ ] Duyệt [ ] Bỏ

### Mục 69. Dòng 913
**Gốc:** "thus the results support moderate reduction rather than uniform sparsity or stability superiority."
**Đề xuất:** "Thus DTAP reduces the number of features moderately; it does not select sparser or more stable sets than the base models."
**Dịch:** "Như vậy DTAP giảm số đặc trưng ở mức vừa phải; nó không chọn được tập thưa hơn hay ổn định hơn các mô hình gốc."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 70. Dòng 926–927
**Gốc:** "The per-dataset exceptions are included in Table 3, and all five methods appear in the summary."
**Đề xuất:** "The SG results on Spambase, the only dataset where they differ from DTAP, are given below Table~\ref{tab:acc}; Table~\ref{tab:perf-summary} includes all five methods."
**Dịch:** "Kết quả SG trên Spambase, bộ dữ liệu duy nhất mà chúng khác DTAP, được ghi dưới Bảng 3; Bảng 4 gồm cả năm phương pháp."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 71. $A^\star$: xem G10. [ ] Duyệt [ ] Bỏ

### Mục 72. Dòng 1021–1026: xem G9 (phần "kèm theo"). [ ] Duyệt [ ] Bỏ

### Mục 73. Dòng 1027–1031
**Gốc:** "For the full-data instances below, saved numerical witnesses satisfy all three inequalities strictly under an independent evaluation; the smallest slack is $4.33\times10^{-4}$. This numerical check is distinct from an exact feasibility certificate."
**Đề xuất:** "For each full-data instance below, we keep the evaluated point with the largest slack $\min_i(b_i-F_i(w))$ over all runs. Re-evaluated on matrices rebuilt from the data, each of these points satisfies all three inequalities strictly; the smallest slack is $4.33\times10^{-4}$. This is a numerical check, not an exact certificate of feasibility."
**Dịch:** "Với mỗi bài toán dùng toàn bộ dữ liệu dưới đây, ta giữ điểm đã đánh giá có độ dư $\min_i(b_i-F_i(w))$ lớn nhất trên mọi lần chạy. Khi đánh giá lại trên các ma trận dựng lại từ dữ liệu, mỗi điểm này thỏa chặt cả ba bất đẳng thức; độ dư nhỏ nhất là $4.33\times10^{-4}$. Đây là kiểm tra bằng số, không phải chứng nhận khả thi chính xác."
*Lý do:* thay các biệt ngữ "witnesses", "independent evaluation" bằng mô tả cụ thể. Đã đối chiếu mô tả "witness" trong `Readme.md` của package. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 74. Điểm Fisher trên các fold: đã gộp vào mục 59. [ ] Duyệt [ ] Bỏ

### Mục 75. Dòng 1034
**Gốc:** "We measure the frequency of $F_3(w^k)-b_3>10^{-6}$ over all evaluated points, including the terminating point."
**Đề xuất:** "We count the iterates of a run, including the last (its evaluated points), at which $F_3(w^k)-b_3>10^{-6}$."
**Dịch:** "Ta đếm số điểm lặp của một lần chạy, kể cả điểm cuối (gọi là các điểm đã đánh giá), mà tại đó $F_3(w^k)-b_3>10^{-6}$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 76. Dòng 1037–1039
**Gốc:** "Table 6 shows that the third track is inactive on seven of the eight standard-start runs for the classification datasets and active at only one of the 48 evaluated points on Abalone."
**Đề xuất:** "Table~\ref{tab:activation-tuning} shows that, from the standard start, $F_3$ is violated at no evaluated point on seven of the eight classification datasets, and at one of the $48$ evaluated points on Abalone."
**Dịch:** "Bảng 6 cho thấy, từ điểm xuất phát chuẩn, $F_3$ không bị vi phạm tại điểm đã đánh giá nào trên bảy trong tám bộ dữ liệu phân loại, và bị vi phạm tại một trong 48 điểm đã đánh giá trên Abalone."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 77. Dòng 1042–1044
**Gốc:** "We include the valid all-convex comparator, which assigns all three constraints to the convex track."
**Đề xuất:** "We also report the all-convex comparator (AC), which assigns all three constraints to the convex track."
**Dịch:** "Ta cũng báo cáo phương án đối chứng toàn lồi (AC), xếp cả ba ràng buộc vào track lồi."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 78. Đoạn "Protocol and tuning cost" (dòng 1048–1069), sau khi chuyển định nghĩa SG lên §4.2.1
**Đề xuất (thay dòng 1050–1060):** "SG-const and SG-dyn are defined in Section~\ref{sssec:baselines}. Besides SG-dyn with the sampled modulus $\widehat L$, a tuned variant selects $L=c\widehat L$ from the grid…" (phần còn lại giữ nguyên; đổi mọi $x^k$ thành $w^k$).
**Dịch:** "SG-const và SG-dyn được định nghĩa ở Mục 4.2.1. Ngoài SG-dyn với mô-đun lấy mẫu $\widehat L$, một biến thể tinh chỉnh chọn $L=c\widehat L$ từ lưới…"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 79. Dòng 1104–1105
**Gốc:** "the values of $J$ along the two trajectories differ by at most $3.18\times10^{-5}$ relative to AC"
**Đề xuất:** "the values of $J$ along the two trajectories satisfy $|J_{\rm DTAP}-J_{\rm AC}|\le3.18\times10^{-5}\,J_{\rm AC}$ at every evaluated point"
**Dịch:** "các giá trị $J$ dọc hai quỹ đạo thỏa $|J_{\rm DTAP}-J_{\rm AC}|\le3.18\times10^{-5}\,J_{\rm AC}$ tại mọi điểm đã đánh giá"
*Lý do:* đã tính lại từ quỹ đạo đã lưu: sai khác tương đối lớn nhất đúng bằng $3.18\times10^{-5}$ (sai khác tuyệt đối lớn nhất là $1.37\times10^{-3}$). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 80. Dòng 1106–1107
**Gốc:** "whose success counts differ only from the random starts (26/36 versus 36/36)."
**Đề xuất:** "whose success counts differ only on the random starts ($26/36$ versus $36/36$)."
**Dịch:** "mà số lần thành công chỉ khác nhau ở các điểm xuất phát ngẫu nhiên (26/36 so với 36/36)."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 81. Dòng 1115–1116
**Gốc:** "it assigns equal weights when both tracks are nonzero and full weight to the sole nonzero track."
**Đề xuất:** "it assigns equal weights when both tracks are violated and full weight to the only violated track otherwise."
**Dịch:** "nó gán trọng số bằng nhau khi cả hai track bị vi phạm, và ngược lại gán toàn bộ trọng số cho track duy nhất bị vi phạm."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 82. Đoạn 1172–1204: chỉ ngắt đoạn, không đổi câu chữ
**Đề xuất:** ngắt thành 3 đoạn:
1. Từ "DTAP encounters a third-constraint violation…" đến hết "…These counts exclude the 147 331 evaluations of its tuning search." (số lần thành công);
2. Từ "With $\nu_k=10^{-3}$, SG-const moves at most…" đến hết "…at only 32 of these 12 877 evaluated points." (giải thích các kết quả SG-const và cấu trúc track);
3. Từ "All DTAP failures occur at $\kappa=0.3$…" đến hết đoạn (độ nhạy với $\kappa$ và Bảng 8).

[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 83. Dòng 1242–1243
**Gốc:** "In this environment the package also reproduces exactly every numerical entry of Tables 1–5…"
**Đề xuất:** "With Python~3.13.4 and NumPy~2.1.3, the package also reproduces exactly every numerical entry of Tables 1–5…"
**Dịch:** "Với Python 3.13.4 và NumPy 2.1.3, package cũng tái lập chính xác mọi giá trị số trong Bảng 1–5…"
*Lý do:* "this environment" không rõ là môi trường nào. `Readme.md` của package ghi rằng kết quả đã lưu được chạy với Python 3.13.4. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 84. Kết luận (dòng 1251), viết lại
**Đề xuất:**
> DTAP solves normal-box nonlinear split feasibility problems with convex and pseudoconvex components by combining a residual-scaled convex step with a safeguarded pseudoconvex step. Under consistency and continuous differentiability, the whole sequence converges to a feasible point; no regularity modulus is an input, although the analysis uses bounds on a compact set containing the iterates. In the feature-selection application all constraints are convex, and test problems with a nonconvex pseudoconvex constraint exercise the pseudoconvex track. In the experiments, tuned subgradient methods can match or outperform DTAP, whose finite-budget performance depends on the starting point and the step scale. Rates for the full residual $J(x^k)$, beyond the convex-track bound of Remark~\ref{rem:rate}, and guarantees under error-bound conditions remain open.

**Dịch:**
> DTAP giải các bài toán chấp nhận tách phi tuyến với hộp chuẩn và các thành phần lồi hoặc giả lồi, bằng cách kết hợp một bước co theo phần dư cho phần lồi với một bước có chặn an toàn cho phần giả lồi. Với giả thiết nhất quán và khả vi liên tục, toàn bộ dãy hội tụ tới một điểm khả thi; không mô-đun chính quy nào là đầu vào, dù phân tích dùng các cận trên một tập compact chứa dãy lặp. Trong ứng dụng chọn đặc trưng, mọi ràng buộc đều lồi, và các bài toán thử có ràng buộc giả lồi không lồi kiểm tra track giả lồi. Trong thực nghiệm, các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, và hiệu năng của DTAP với ngân sách hữu hạn phụ thuộc vào điểm xuất phát và thang bước. Tốc độ hội tụ cho phần dư đầy đủ $J(x^k)$, ngoài cận cho track lồi ở Nhận xét 5, và các bảo đảm dưới điều kiện cận sai số vẫn còn mở.

*Lý do:* giữ đủ nội dung của bản cũ nhưng mỗi ý chỉ nói một lần. Bỏ các câu lặp lại Abstract ("The proportional weight is an admissible residual-responsive choice…", "The activity measurements and controlled nonconvex tests distinguish these settings"). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

---

---

## Phần III. Câu thừa hoặc lặp nên xóa

Mỗi câu dưới đây không qua được phép thử "xóa thử" (bỏ đi không mất thông tin) hoặc phép thử "lặp" (đã được nói ở chỗ khác).

| Dòng | Câu | Đã nói ở | |
|---|---|---|---|
| 744 | "These two scopes are stated separately below." | — (câu đệm) | [ ] Xóa [ ] Giữ |
| 807 | "A feasible weight need not minimize either baseline objective." | câu ngay trước ("does not preserve either source optimization problem or its minimizers") | [ ] Xóa [ ] Giữ |
| 1039–1040 | "Moreover, the quadratic-over-linear function $F_3$ is convex when $Q_R\succeq0$ and $\rho^\top w>0$." | Mệnh đề 4.1 | [ ] Xóa [ ] Giữ |
| 1044–1045 | "Movement Libras is an additional solver robustness case, separate from the eight-dataset classification study." | đầu §4 và chú thích Bảng 1 | [ ] Xóa [ ] Giữ |
| 1203–1204 | "The experiments support neither universal speed superiority nor a finite-budget robustness claim." | Abstract và Kết luận | [ ] Xóa [ ] Giữ |
| 1251 (trong bản viết lại) | các câu lặp lại Abstract | xem mục 84 | — |

---

## Phần IV. Ngân sách số chữ (đo bằng script trên văn xuôi, không tính công thức)

| | 16 đoạn chính | Thay đổi |
|---|---|---|
| Bản đề xuất đầu tiên (đã thay) | 1 218 → 1 665 từ | **+447** |
| Bản hiện tại | 1 288 → 1 147 từ | **−141** |
| Phần III (xóa câu thừa) | | **−53** |
| G2, G6, G7 (câu định nghĩa, ký hiệu) | | **+27** |
| **Tổng ước tính** | | **khoảng −165 từ** |

G8 là chuyển chỗ nên gần như không đổi. Các mục 7–9, 19, 31–57, 62–83 là sửa vài chữ, mỗi mục thay đổi không quá ±10 từ.

**Không đề xuất sửa:** mục 35 (gộp vào G11), mục 41 (giữ nguyên). Các chứng minh trong §3 giữ nguyên ngoài các chỗ đã nêu.
