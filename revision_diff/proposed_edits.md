# Đề xuất sửa câu chữ — `DTAP Finally/main_document.tex`

Tài liệu để **duyệt**: chưa có thay đổi nào được áp vào bài. Mỗi mục gồm câu **gốc**, câu **đề xuất** (tiếng Anh), **bản dịch** tiếng Việt của câu đề xuất và **lý do**. Số thứ tự theo `writing_review.md`; dòng là số dòng hiện tại của `main_document.tex`.

Cách duyệt: đánh dấu ở cuối mỗi mục: `[x] Duyệt`, `[x] Sửa lại` (ghi chú bên dưới), hoặc `[x] Bỏ`.

Các số liệu mới đưa vào câu đề xuất đều đã được kiểm từ code và kết quả trong package:
- min điểm Fisher trên các fold: tính lại trong phiên này bằng hàm `_fisher_score` của package;
- cách tính $b_i$: `thresholds.py`;
- sai khác tương đối DTAP/AC: `results/hu2022/datasets/Abalone.json.gz`;
- số bước Euler: `nfscore.py`;
- bước SG-dyn: `hu2022.py`.

> **Lưu ý cho response letter.** Các mục **A0, 50** sửa những câu mà letter đang trích nguyên văn. Nếu duyệt, cần sửa trích dẫn tương ứng trong letter: R1.1 và R1.2 trích Abstract, R1.3 trích câu ở dòng 663–664.

---

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
  **Đề xuất:** "We split the constraint indices into two sets, $I^{\cvx}$ and $I^{\ps}$. Each set, together with the step rule used on it, is called a \emph{track}: the \emph{convex track} and the \emph{pseudoconvex track}."
  **Dịch:** "Ta chia các chỉ số ràng buộc thành hai tập $I^{\cvx}$ và $I^{\ps}$. Mỗi tập, cùng với quy tắc bước dùng trên nó, được gọi là một *track*: track lồi và track giả lồi."
- Dòng 185. **Gốc:** "into disjoint groups". **Đề xuất:** "into two disjoint sets". **Dịch:** "thành hai tập rời nhau".
- Các chỗ dùng "block" ở 68 và 103 được xử lý trong A0 và mục 20.

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
- Thêm sau (13), dòng 198. **Đề xuất (câu mới):** "Here `active' refers to a violation within $\delta$ of the largest violation on the track, not to the equality $F_i(x)=b_i$." **Dịch:** "Ở đây 'active' chỉ các vi phạm cách vi phạm lớn nhất trên track không quá $\delta$, không phải đẳng thức $F_i(x)=b_i$."

*Lý do:* trong tối ưu, "active" thường nghĩa là $F_i=b_i$; Reviewer 2 cũng hỏi về thuật ngữ này ở m4. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G7. Ký hiệu trùng nghĩa
| Ký hiệu | Vị trí | Đề xuất |
|---|---|---|
| $n$, $x_i$, chỉ số $k$ | đầu §4.1, dòng 747 | Thêm câu: "In this section the variable is $w\in\R^p$; $n$ denotes the number of samples and $x_i$ a sample, subscripts index features, and superscripts index iterations." — *Dịch:* "Trong mục này biến là $w\in\R^p$; $n$ là số mẫu, $x_i$ là một mẫu, chỉ số dưới đánh số đặc trưng và chỉ số trên đánh số vòng lặp." |
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
Thêm một đoạn vào cuối §4.2.1 (sau "AFRSFCV: gradient and update", dòng 870). Đồng thời bỏ phần định nghĩa tương ứng ở §4.4 (dòng 1050–1060), chỉ giữ phần tinh chỉnh (xem mục 78).

**Đề xuất (đoạn mới):**
> \paragraph*{SG-const and SG-dyn: subgradient methods}
> We also compare with two subgradient methods for quasiconvex feasibility~\citep{hu2022quasi}. Both follow the most-violated-constraint strategy of~\citep{hu2022quasi}: with $\mathcal I_k=\argmax_i v_i(w^k)$, they iterate
> \[ w^{k+1}=P_K(w^k-\nu_k\bar h_k),\qquad \bar h_k=\frac1{|\mathcal I_k|}\sum_{i\in\mathcal I_k}\frac{\nabla F_i(w^k)}{\|\nabla F_i(w^k)\|}, \]
> where the average over $\mathcal I_k$ handles ties. SG-const uses the constant step $\nu_k=10^{-3}$. SG-dyn uses the dynamic step $\nu_k=J(w^k)/L$ of~\citep{hu2022quasi} with H\"older exponent $1$. By default $L=\widehat L$, the largest gradient norm over $500$ points sampled in $K$.

**Dịch:**
> **SG-const và SG-dyn: các phương pháp dưới gradient.** Ta còn so sánh với hai phương pháp dưới gradient cho bài toán khả thi tựa lồi [7]. Cả hai theo chiến lược "ràng buộc bị vi phạm nhiều nhất" của [7]: với $\mathcal I_k=\argmax_i v_i(w^k)$, chúng lặp theo công thức trên, trong đó việc lấy trung bình trên $\mathcal I_k$ xử lý trường hợp có nhiều chỉ số cùng đạt cực đại. SG-const dùng bước hằng $\nu_k=10^{-3}$. SG-dyn dùng bước động $\nu_k=J(w^k)/L$ của [7] với số mũ Hölder bằng 1. Mặc định $L=\widehat L$, là chuẩn gradient lớn nhất trên 500 điểm lấy mẫu trong $K$.

*Lý do:* SG-const và SG-dyn được dùng ở §4.2–4.3 (Bảng 2–5) nhưng đến §4.4 mới được định nghĩa. Đã kiểm code `hu2022.py`: $\beta=1$, hệ số bước động bằng 1, nên công thức khớp. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### G9. Mô tả cách tính ngưỡng $b_i$
Thay đoạn ở dòng 822 bằng đoạn sau.

**Gốc:**
> Externally specified thresholds remain fixed. Training-based thresholds instead define the benchmark instance and must be shared by all solvers. Separate empirical percentiles do not ensure $\Omega\ne\varnothing$. A common point must satisfy all constraints, and checks to a numerical tolerance establish only the corresponding approximate feasibility. The threshold protocol and constraint-activity diagnostics are reported with the experiments.

**Đề xuất:**
> In the experiments the thresholds are computed from the training data of each instance. We draw $3\,000$ points from the uniform (Dirichlet) distribution on $K$ (seed $42$), add the $p$ vertices of $K$, and set $b_i$ to the $q_i$-th percentile of the values of $F_i$ at these points. The levels $q_1,q_2,q_3$ are chosen by a fixed rule from the sample size, the number of features, the number of classes and the class-imbalance ratio of the dataset; they are listed in the supplementary metadata. All solvers use the same thresholds. Since each $b_i$ is calibrated separately, this procedure does not guarantee $\Omega\ne\varnothing$; Section~\ref{ssec:feasibility-audit} reports numerical feasibility checks. When an application prescribes the thresholds, they are used as given, and consistency remains an assumption.

**Dịch:**
> Trong thực nghiệm, các ngưỡng được tính từ dữ liệu huấn luyện của từng bài toán. Ta lấy 3 000 điểm theo phân phối đều (Dirichlet) trên $K$ (seed 42), thêm $p$ đỉnh của $K$, rồi đặt $b_i$ bằng phân vị bậc $q_i$ của các giá trị $F_i$ tại các điểm này. Các bậc $q_1,q_2,q_3$ được chọn theo một quy tắc cố định, dựa trên cỡ mẫu, số đặc trưng, số lớp và tỉ lệ mất cân bằng lớp của bộ dữ liệu; chúng được liệt kê trong metadata bổ sung. Mọi bộ giải dùng chung các ngưỡng này. Vì mỗi $b_i$ được hiệu chỉnh riêng, quy trình này không bảo đảm $\Omega\ne\varnothing$; Mục 4.4 báo cáo các kiểm tra khả thi bằng số. Khi ứng dụng đã quy định ngưỡng, ngưỡng được dùng nguyên như vậy và tính nhất quán vẫn là một giả thiết.

*Lý do:* hiện bài không có câu nào nói $b_i$ được tính thế nào; Reviewer 1 hỏi đúng điểm này ở R1.4. Đã đối chiếu `thresholds.py`: 3000 mẫu Dirichlet(1) với seed 42, thêm các đỉnh, lấy phân vị. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

**Kèm theo**, dòng 1021–1026 rút gọn thành:
> **Đề xuất:** "As noted in Section~\ref{ssec:reduction}, the calibrated thresholds do not guarantee that the sublevel sets intersect. In an application with prescribed thresholds, consistency remains an assumption."
> **Dịch:** "Như đã nêu ở Mục 4.1.3, các ngưỡng hiệu chỉnh không bảo đảm các tập mức dưới giao nhau. Trong ứng dụng có ngưỡng quy định sẵn, tính nhất quán vẫn là một giả thiết."

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
**Gốc:** (xem dòng 68)

**Đề xuất:**
> We study a nonlinear split feasibility problem in $\R^n$ whose output set is a normal box and whose component functions are differentiable and either convex or pseudoconvex. The constraints are split into a convex track and a pseudoconvex track. On each track, the Dual-Track Adaptive Projection (DTAP) algorithm uses the nearly most violated constraints: it takes a residual-scaled Polyak-type step on the convex track and a safeguarded diminishing step on the pseudoconvex track. It combines the two steps with a proportional weight, a residual-responsive choice for which no optimality is claimed, and projects the result onto the base convex set. Its step sizes require no prescribed operator norm, Lipschitz constant, or H\"older modulus. Assuming that the problem is consistent and the component functions are continuously differentiable, we prove that the whole sequence of iterates converges to a feasible point. The proof uses bounds on the functions and gradients over a bounded set that contains the iterates. In a feature-selection application, three constraints are taken from a fractional model and a fuzzy-rough model; we show that all three are convex. The experiments report how often the pseudoconvex constraint is violated, compare DTAP with subgradient methods whose moduli are tuned, and test DTAP on problems with a nonconvex pseudoconvex constraint. Tuned subgradient methods can match or outperform DTAP, and DTAP is sensitive to its starting point and to the scale of its diminishing step.

**Dịch:**
> Ta nghiên cứu một bài toán chấp nhận tách phi tuyến trong $\R^n$, có tập đầu ra là một hộp chuẩn và các hàm thành phần khả vi, mỗi hàm lồi hoặc giả lồi. Các ràng buộc được chia thành một track lồi và một track giả lồi. Trên mỗi track, thuật toán Chiếu Thích nghi Hai Track (DTAP) dùng các ràng buộc gần bị vi phạm nhiều nhất: nó lấy một bước kiểu Polyak co theo phần dư trên track lồi và một bước giảm dần có chặn an toàn trên track giả lồi. Nó kết hợp hai bước bằng một trọng số tỉ lệ (một lựa chọn phản ứng theo phần dư, không khẳng định là tối ưu) rồi chiếu kết quả lên tập lồi cơ sở. Độ dài bước không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder. Với giả thiết bài toán nhất quán và các hàm thành phần khả vi liên tục, ta chứng minh toàn bộ dãy lặp hội tụ tới một điểm khả thi. Chứng minh dùng các cận của hàm và gradient trên một tập bị chặn chứa dãy lặp. Trong ứng dụng chọn đặc trưng, ba ràng buộc được lấy từ một mô hình phân thức và một mô hình tập thô mờ; ta chứng minh cả ba đều lồi. Thực nghiệm báo cáo tần suất ràng buộc giả lồi bị vi phạm, so sánh DTAP với các phương pháp dưới gradient có mô-đun được tinh chỉnh, và thử DTAP trên các bài toán có ràng buộc giả lồi không lồi. Các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, và DTAP nhạy với điểm xuất phát và với thang của bước giảm dần.

*Lý do:*
- định nghĩa "track" ngay trong Abstract (mục 1);
- giới thiệu trọng số trước khi dùng mạo từ xác định (mục 2);
- nêu rõ các giả thiết (mục 3);
- nói rõ "lớp con lồi" là gì (mục 4);
- nói rõ DTAP là phương pháp nhạy với điểm xuất phát (mục 5);
- đưa các câu phủ định xuống cuối (mục 6).

*Letter:* R1.1 trích "a residual-responsive choice, without a claim of optimality", nay thành "a residual-responsive choice for which no optimality is claimed". R1.2 trích "the proof uses local bounds on the bounded iterate region", nay thành câu mới. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

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
**Đề xuất:** "Relaxed variants replace the projections onto $C$ and $Q$ by projections onto supporting half-spaces, which have closed forms~\citep{yang2004}. Self-adaptive step sizes remove the need to know $\norm{\mathcal A}$~\citep{zhang2009adaptive,zhao2011adaptive,lopez2012}. Operator splitting~\citep{zhang2012simultaneous} and modified alternating direction methods~\citep{yang2014alternating} decompose the problem into simpler subproblems. This paper uses both ideas, adaptive step sizes and decomposition, but does not claim them as new."
**Dịch:** "Các biến thể nới lỏng thay phép chiếu lên $C$ và $Q$ bằng phép chiếu lên các nửa không gian tựa, vốn có công thức tường minh [17]. Bước tự thích nghi giúp không cần biết $\norm{\mathcal A}$ [20, 22, 10]. Phương pháp tách toán tử [21] và phương pháp hướng luân phiên cải biên [18] phân rã bài toán thành các bài toán con đơn giản hơn. Bài báo này dùng cả hai ý tưởng, bước thích nghi và phân rã, nhưng không coi chúng là đóng góp mới."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 12–15. Dòng 91–95
**Gốc:** "We study the nonlinear SFP (3) where $K\subseteq\R^n$ is closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$, and each differentiable component of $F=(F_1,\ldots,F_m)$ is convex or pseudoconvex on $K$. Pseudoconvex functions have convex sublevel sets, so the feasible set is convex even when some components are nonconvex. We seek feasibility, rather than minimization of every component."
**Đề xuất:** "Replacing the matrix $\mathcal A$ by a nonlinear map $F$ gives the nonlinear SFP~\citep{li2013nsfp,yen2019}. We study it in the form (3), where $K\subseteq\R^n$ is nonempty, closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$ is a normal box, and each component $F_i$ of $F=(F_1,\ldots,F_m)$ is differentiable and either convex or pseudoconvex on $K$. Since pseudoconvex functions have convex sublevel sets, the feasible set $\Omega=\{x\in K:F(x)\in Q\}$ is convex even when some components are nonconvex. We seek a point of $\Omega$; we do not minimize any of the components."
**Dịch:** "Thay ma trận $\mathcal A$ bằng một ánh xạ phi tuyến $F$ ta được SFP phi tuyến [9, 19]. Ta nghiên cứu nó dưới dạng (3), trong đó $K\subseteq\R^n$ khác rỗng, đóng và lồi, $Q=\prod_{i=1}^m(-\infty,b_i]$ là một hộp chuẩn, và mỗi thành phần $F_i$ của $F$ khả vi và lồi hoặc giả lồi trên $K$. Vì hàm giả lồi có các tập mức dưới lồi, tập khả thi $\Omega=\{x\in K:F(x)\in Q\}$ lồi ngay cả khi một số thành phần không lồi. Ta tìm một điểm thuộc $\Omega$; ta không cực tiểu hóa thành phần nào."
*Lý do:* thêm câu chuyển ý (mục 12); thêm "nonempty" (13); sửa câu đọc ra hai nghĩa "each differentiable component" (14); đặt tên $\Omega$ ngay khi nói tới tập khả thi (15). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 16–18. Dòng 97
**Gốc:** "Nonlinear SFP and generalized convex feasibility have several relevant antecedents. Li et al. use a convex aggregate proximity function, a property not ensured by componentwise pseudoconvexity. Yen et al. combine equilibrium and nonlinear image constraints. Hu et al. treat quasiconvex inequalities, which include our component class. Our method exploits the additional derivative information of convex components within this established feasibility setting."
**Đề xuất:** "Nonlinear SFPs and feasibility problems with generalized convex functions have been studied before. Li et al.~\citep{li2013nsfp} solve the nonlinear multiple-sets SFP under the assumption that the aggregate proximity function is convex; componentwise pseudoconvexity does not imply this. Yen et al.~\citep{yen2019} use the same max-type violation measure and the same active-set device as we do, but require every component to be quasilinear, that is, both quasiconvex and quasiconcave. This class neither contains nor is contained in ours: $x\mapsto x^2$ is convex but not quasilinear, and $x\mapsto x^3$ is quasilinear but not pseudoconvex. Hu et al.~\citep{hu2022quasi} solve systems of quasiconvex inequalities, a class that contains ours, by subgradient methods. Our method additionally uses the gradient inequality satisfied by the convex components."
**Dịch:** "SFP phi tuyến và các bài toán khả thi với hàm lồi suy rộng đã được nghiên cứu trước đây. Li và cộng sự [9] giải SFP đa tập phi tuyến với giả thiết hàm lân cận tổng hợp là lồi; tính giả lồi của từng thành phần không suy ra được điều này. Yen và cộng sự [19] dùng cùng hàm đo vi phạm kiểu max và cùng kỹ thuật tập active như ta, nhưng đòi mọi thành phần là tựa tuyến tính, tức vừa tựa lồi vừa tựa lõm. Lớp này không chứa và cũng không bị chứa trong lớp của ta: $x\mapsto x^2$ lồi nhưng không tựa tuyến tính, còn $x\mapsto x^3$ tựa tuyến tính nhưng không giả lồi. Hu và cộng sự [7] giải hệ bất đẳng thức tựa lồi, một lớp chứa lớp của ta, bằng phương pháp dưới gradient. Phương pháp của ta dùng thêm bất đẳng thức gradient mà các thành phần lồi thỏa mãn."
*Lý do:* sửa cụm "a property" đọc ra hai nghĩa (16); nêu rõ vì sao Yen et al. liên quan và khác bài này ở đâu, đây là công trình gần nhất (17); bỏ cụm tối nghĩa "this established setting" (18). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 19. Dòng 99
**Gốc:** "The box gives the explicit violation measure"
**Đề xuất:** "Because $Q$ is a box, the $\ell_\infty$-distance from $F(x)$ to $Q$ has the closed form"
**Dịch:** "Vì $Q$ là một hộp, khoảng cách $\ell_\infty$ từ $F(x)$ tới $Q$ có dạng tường minh"
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 20–24. Dòng 103, viết lại cả đoạn
**Gốc:** (đoạn 10 câu, bắt đầu "The Dual-Track Adaptive Projection algorithm (\dtap) forms violation-weighted gradient sums…")
**Đề xuất:**
> DTAP uses the two tracks introduced above. On each track it forms a weighted sum of the gradients of the nearly most violated constraints. On the convex track, the gradient inequality of convex functions justifies a residual-scaled Polyak-type step~\citep{polyak1969,lopez2012}. On the pseudoconvex track, pseudoconvexity gives only the sign of a directional derivative, and DTAP takes a safeguarded diminishing step. The two steps are combined with a proportional weight $\mu_k$, and the result is projected onto $K$. We do not claim that this weight is unique or optimal; the convergence proof uses it to ensure that a track which stays violated keeps a positive weight (Remark~\ref{rem:weight-scope}). The step sizes require no prescribed operator norm, Lipschitz constant, or H\"older modulus. The proof first shows, by a quasi-Fej\'er inequality, that the iterates are bounded, and then uses bounds on the functions and gradients over a compact set that contains them; the gradients need not be Lipschitz continuous.

**Dịch:**
> DTAP dùng hai track nêu trên. Trên mỗi track, nó lập tổng có trọng số các gradient của những ràng buộc gần bị vi phạm nhiều nhất. Trên track lồi, bất đẳng thức gradient của hàm lồi biện minh cho một bước kiểu Polyak co theo phần dư [14, 10]. Trên track giả lồi, tính giả lồi chỉ cho biết dấu của đạo hàm theo hướng, và DTAP lấy một bước giảm dần có chặn an toàn. Hai bước được kết hợp bằng trọng số tỉ lệ $\mu_k$ và kết quả được chiếu lên $K$. Ta không khẳng định trọng số này là duy nhất hay tối ưu; chứng minh hội tụ dùng nó để bảo đảm một track bị vi phạm kéo dài vẫn giữ trọng số dương (Nhận xét 1). Độ dài bước không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder. Chứng minh trước hết dùng một bất đẳng thức tựa Fejér để chỉ ra dãy lặp bị chặn, rồi dùng các cận của hàm và gradient trên một tập compact chứa dãy lặp; gradient không cần liên tục Lipschitz.

*Lý do:* nối các câu ngắn rời rạc thành một mạch (20); thay câu "preventing neglect" bằng ý cụ thể (21); câu "one-step bound…" đã có ở Nhận xét 1 nên bỏ khỏi phần mở đầu (22); sửa hai cụm tối nghĩa (23, 24). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 25–27. Dòng 105, viết lại cả đoạn
**Gốc:** (đoạn bắt đầu "Feature-selection criteria from fractional and fuzzy-rough models … define separate threshold constraints.")
**Đề xuất:**
> As an application, we take three criteria from a fractional feature-selection model~\citep{wang2021fractional} and a fuzzy-rough model~\citep{wang2026afrsfcv} and impose an upper bound on each. A feasible weight vector is then acceptable for all three criteria simultaneously; it need not solve either source optimization problem. The fractional criterion is a positive semidefinite quadratic form divided by a linear form that is positive on $K$. We show that it is convex, so this application has only convex constraints. To exercise the pseudoconvex track, we also use test problems with a pseudoconvex constraint that is not convex. In the classification study, the feature selections are computed once and evaluated on one fixed training/test split (Section~\ref{sssec:protocol}). Subgradient methods with tuned moduli can match or outperform DTAP.

**Dịch:**
> Làm ứng dụng, ta lấy ba tiêu chí từ một mô hình chọn đặc trưng phân thức [15] và một mô hình tập thô mờ [16], rồi áp một cận trên cho mỗi tiêu chí. Khi đó một vector trọng số khả thi chấp nhận được đồng thời theo cả ba tiêu chí; nó không nhất thiết là nghiệm của bài toán tối ưu gốc nào. Tiêu chí phân thức là một dạng toàn phương nửa xác định dương chia cho một dạng tuyến tính dương trên $K$. Ta chứng minh nó lồi, nên ứng dụng này chỉ có ràng buộc lồi. Để kiểm tra track giả lồi, ta còn dùng các bài toán thử có ràng buộc giả lồi nhưng không lồi. Trong nghiên cứu phân loại, các lựa chọn đặc trưng được tính một lần và đánh giá trên một phép chia huấn luyện/kiểm tra cố định (Mục 4.2.2). Các phương pháp dưới gradient có mô-đun được tinh chỉnh có thể bằng hoặc tốt hơn DTAP.

*Lý do:* thay cụm tối nghĩa "simultaneous acceptance" (25); tách cụm chồng danh từ (26); tách câu 32 từ dễ đọc nhầm (27). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 28–30. Các đóng góp C1–C3 (dòng 109–111)
**Đề xuất:**
> C1. A dual-track projection method that uses the gradient inequality on the convex constraints and only sign information on the pseudoconvex constraints, and combines the two steps with a proportional weight. Unlike~\citep{li2013nsfp}, it does not require the aggregate proximity function to be convex; unlike~\citep{yen2019}, it admits convex components that are not quasilinear; unlike the dynamic step of~\citep{hu2022quasi}, its step on the convex track needs no H\"older modulus.
> C2. Under Assumption~\ref{ass:standing} (consistency, continuous differentiability, convexity or pseudoconvexity of each component, and the step-size conditions), the whole sequence of iterates converges to a feasible point (Theorem~\ref{thm:strong}).
> C3. Experiments that separate classification quality from the cost of solving the feasibility problem, report how often the pseudoconvex constraint is violated, compare DTAP with tuned subgradient methods, and measure its sensitivity to the starting point and to the step scale. They do not show that DTAP is uniformly faster.

**Dịch:**
> C1. Một phương pháp chiếu hai track: dùng bất đẳng thức gradient trên các ràng buộc lồi và chỉ thông tin về dấu trên các ràng buộc giả lồi, rồi kết hợp hai bước bằng một trọng số tỉ lệ. Khác với [9], phương pháp không đòi hàm lân cận tổng hợp lồi; khác với [19], nó chấp nhận các thành phần lồi không tựa tuyến tính; khác với bước động của [7], bước trên track lồi không cần mô-đun Hölder.
> C2. Dưới Giả thiết 1 (tính nhất quán, khả vi liên tục, mỗi thành phần lồi hoặc giả lồi, và các điều kiện về bước), toàn bộ dãy lặp hội tụ tới một điểm khả thi (Định lý 3.12).
> C3. Thực nghiệm tách chất lượng phân loại khỏi chi phí giải bài toán khả thi, báo cáo tần suất ràng buộc giả lồi bị vi phạm, so sánh DTAP với các phương pháp dưới gradient đã tinh chỉnh, và đo độ nhạy của DTAP với điểm xuất phát và thang bước. Thực nghiệm không cho thấy DTAP nhanh hơn một cách đồng đều.

*Lý do:* thay cụm "the stated step conditions" không rõ ở đâu (28); thay cụm tối nghĩa "distinguish prediction from feasibility cost" (29); nêu điểm mới so với ba công trình gần nhất (30). [ ] Duyệt [ ] Sửa lại [ ] Bỏ

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
**Đề xuất:** "Then $F(x)\in Q$ if and only if $J(x)=0$. Hence $x\in K$ is feasible if and only if $J(x)=0$, and, when $\Omega\ne\emptyset$, the feasible points are exactly the minimizers of $J$ over $K$."
**Dịch:** "Khi đó $F(x)\in Q$ khi và chỉ khi $J(x)=0$. Do đó $x\in K$ khả thi khi và chỉ khi $J(x)=0$, và khi $\Omega\ne\emptyset$ thì các điểm khả thi chính là các điểm cực tiểu của $J$ trên $K$."
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
**Đề xuất:** "The first term measures how well the weighted lower approximations reproduce the label matrix; the second penalizes, for each sample, the total weight of the features that classify it incorrectly; the third is a Tikhonov regularization."
**Dịch:** "Số hạng thứ nhất đo mức các xấp xỉ dưới có trọng số tái tạo ma trận nhãn; số hạng thứ hai phạt, với mỗi mẫu, tổng trọng số của các đặc trưng phân loại sai mẫu đó; số hạng thứ ba là hiệu chỉnh Tikhonov."
*Lý do:* đã kiểm: $1-(Pw)_i$ đúng bằng tổng trọng số các đặc trưng phân loại sai mẫu $i$. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 56. Dòng 803: "the first two components of (38)" → "the first two terms of (38)" — *Dịch:* "hai số hạng đầu của (38)". [ ] Duyệt [ ] Bỏ

### Mục 57. Mệnh đề 4.1, câu cuối (dòng 810)
**Gốc:** "It satisfies the function assumptions of Assumption 1 whenever $\Omega\ne\varnothing$."
**Đề xuất:** "Hence~\eqref{eq:nsfp-fs} satisfies (A1) and (A2) of Assumption~\ref{ass:standing}, with $U=U_\rho$, whenever $\Omega\ne\varnothing$."
**Dịch:** "Do đó (42) thỏa (A1) và (A2) của Giả thiết 1, với $U=U_\rho$, mỗi khi $\Omega\ne\varnothing$."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 58. Dòng 820, câu 1–4
**Gốc:** "The assignment $I^{\cvx}=\{1,2\}$, $I^{\ps}=\{3\}$ used in the experiments is admissible because convexity implies pseudoconvexity. It treats $F_3$ conservatively and does not test a genuinely nonconvex constraint. The all-convex assignment $I^{\cvx}=\{1,2,3\}$ is also available. Under the assumptions of Theorem 3.12, either assignment converges to a feasible weight."
**Đề xuất:** "The experiments assign $F_3$ to the pseudoconvex track, $I^{\cvx}=\{1,2\}$ and $I^{\ps}=\{3\}$; this is admissible because convex functions are pseudoconvex. With this assignment DTAP uses only sign information for $F_3$, so the instances do not test a genuinely nonconvex constraint. The all-convex assignment $I^{\cvx}=\{1,2,3\}$ is also admissible. Under the assumptions of Theorem~\ref{thm:strong}, DTAP converges to a feasible weight vector with either assignment."
**Dịch:** "Thực nghiệm xếp $F_3$ vào track giả lồi, $I^{\cvx}=\{1,2\}$ và $I^{\ps}=\{3\}$; điều này hợp lệ vì hàm lồi là giả lồi. Với cách xếp này DTAP chỉ dùng thông tin về dấu của $F_3$, nên các bài toán không kiểm tra một ràng buộc thực sự không lồi. Cách xếp toàn lồi $I^{\cvx}=\{1,2,3\}$ cũng hợp lệ. Dưới các giả thiết của Định lý 3.12, DTAP hội tụ tới một vector trọng số khả thi với cả hai cách xếp."
[ ] Duyệt [ ] Sửa lại [ ] Bỏ

### Mục 59. Dòng 820, câu 5–9 (và mục 74)
**Gốc:** "Score positivity must be checked on each instance. Replacing a zero score by a positive floor changes the model and must be declared. The implementation also uses $\max\{\rho^\top w,10^{-15}\}$ during evaluation. This agrees with (41) only where the floor is inactive. Applying the theorem to this implementation therefore requires that the floor remain inactive."
**Đề xuất:** "Proposition~\ref{prop:fs-reg} requires every Fisher score to be positive. This holds on every instance used here: the smallest score is $4.77\times10^{-5}$ over all selection folds of the classification study and $5.99\times10^{-5}$ over the full-data instances of Section~\ref{ssec:feasibility-audit}. For numerical safety, the implementation evaluates the denominator of $F_3$ as $\max\{\rho^\top w,10^{-15}\}$; since $\rho^\top w\ge\min_k\rho_k$ on $K$, this floor is never active on these instances, and the implemented $F_3$ coincides with~\eqref{eq:fsF3}."
**Dịch:** "Mệnh đề 4.1 đòi mọi điểm Fisher dương. Điều này đúng trên mọi bài toán dùng ở đây: điểm nhỏ nhất là $4.77\times10^{-5}$ trên mọi fold chọn đặc trưng của nghiên cứu phân loại, và $5.99\times10^{-5}$ trên các bài toán dùng toàn bộ dữ liệu ở Mục 4.4. Để an toàn số, cài đặt tính mẫu số của $F_3$ là $\max\{\rho^\top w,10^{-15}\}$; vì $\rho^\top w\ge\min_k\rho_k$ trên $K$, ngưỡng sàn này không bao giờ có hiệu lực trên các bài toán này, và $F_3$ được cài đặt trùng với (41)."
*Lý do:* thay các câu "phải kiểm tra" bằng kết quả kiểm tra thực tế. Con số $4.77\times10^{-5}$ (Spambase) tôi tính lại trong phiên này bằng hàm `_fisher_score` của package, cùng phép chia và cùng fold như `comparison.py`; nên chạy lại để xác nhận. Con số $5.99\times10^{-5}$ lấy từ dòng 1032. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

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

### Mục 74. Điểm Fisher trên các fold: đã gộp vào mục 59; câu ở dòng 1031–1032 có thể giữ nguyên. [ ] Duyệt [ ] Bỏ

### Mục 75. Dòng 1034
**Gốc:** "We measure the frequency of $F_3(w^k)-b_3>10^{-6}$ over all evaluated points, including the terminating point."
**Đề xuất:** "We call the iterates $w^0,w^1,\dots$ of a run, including the last one, its evaluated points, and we count the evaluated points at which $F_3(w^k)-b_3>10^{-6}$."
**Dịch:** "Ta gọi các điểm lặp $w^0,w^1,\dots$ của một lần chạy, kể cả điểm cuối, là các điểm đã đánh giá, và đếm số điểm đã đánh giá mà tại đó $F_3(w^k)-b_3>10^{-6}$."
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
> We studied a nonlinear split feasibility problem with a normal-box output set and convex or pseudoconvex component functions. DTAP combines a residual-scaled step on the convex constraints with a safeguarded diminishing step on the pseudoconvex constraints and projects onto the base set. Under consistency and continuous differentiability, the whole sequence of iterates converges to a feasible point; the proof combines a quasi-Fej\'er inequality with the existence of one feasible cluster point. The method needs no prescribed regularity modulus, but the analysis uses bounds on a compact set that contains the iterates. The proportional weight is one admissible choice, not an optimal one. In the feature-selection application all constraints turn out to be convex, and controlled examples with a nonconvex pseudoconvex constraint exercise the pseudoconvex track. In these experiments, tuned subgradient methods can match or outperform DTAP, and within a finite budget the performance of DTAP depends on the starting point and on the scale of its diminishing step. Rates for the full residual $J(x^k)$, beyond the best-iterate bound of Remark~\ref{rem:rate} for the convex track, and guarantees under additional geometric assumptions, such as error bounds, remain open.

**Dịch:**
> Ta đã nghiên cứu một bài toán chấp nhận tách phi tuyến với tập đầu ra là hộp chuẩn và các hàm thành phần lồi hoặc giả lồi. DTAP kết hợp một bước co theo phần dư trên các ràng buộc lồi với một bước giảm dần có chặn an toàn trên các ràng buộc giả lồi, rồi chiếu lên tập cơ sở. Với giả thiết nhất quán và khả vi liên tục, toàn bộ dãy lặp hội tụ tới một điểm khả thi; chứng minh kết hợp một bất đẳng thức tựa Fejér với sự tồn tại của một điểm tụ khả thi. Phương pháp không cần biết trước mô-đun chính quy nào, nhưng phân tích dùng các cận trên một tập compact chứa dãy lặp. Trọng số tỉ lệ là một lựa chọn hợp lệ, không phải lựa chọn tối ưu. Trong ứng dụng chọn đặc trưng, mọi ràng buộc hóa ra đều lồi, còn các ví dụ có kiểm soát với ràng buộc giả lồi không lồi kiểm tra track giả lồi. Trong các thực nghiệm này, các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, và với ngân sách hữu hạn, hiệu năng của DTAP phụ thuộc vào điểm xuất phát và thang của bước giảm dần. Tốc độ hội tụ cho phần dư đầy đủ $J(x^k)$, ngoài cận cho điểm lặp tốt nhất của Nhận xét 5 trên track lồi, và các bảo đảm dưới giả thiết hình học bổ sung như cận sai số, vẫn còn là câu hỏi mở.

*Lý do:* giữ nội dung cũ nhưng sắp lại theo trình tự kết quả → giới hạn → câu hỏi mở. Cụm "such as error bounds" là ví dụ mới thêm, có thể bỏ. [ ] Duyệt [ ] Sửa lại [ ] Bỏ

---

**Không đề xuất sửa:** mục 35 (gộp vào G11), mục 41 (giữ nguyên). Các chứng minh trong §3 giữ nguyên ngoài các chỗ đã nêu.
