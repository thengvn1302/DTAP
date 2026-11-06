# Rà soát từng câu — `DTAP Finally v2/main_document.tex`

Mục tiêu: bài dễ đọc, văn phong phù hợp một bài báo toán tối ưu, mỗi câu chặt chẽ, tường minh, ngắn gọn. **Chưa sửa gì trong bài**; bảng này chỉ ghi kết quả rà soát.

## Tiêu chí

Một câu đạt yêu cầu khi người đọc chỉ hiểu được **một nghĩa**, hiểu được **mà không phải đoán**, nội dung **đúng như toán học đã chứng minh**, câu **nối được** với câu trước và sau, và **không có chữ thừa**. Mỗi lỗi được gán một hoặc nhiều mã:

| Mã | Loại | Dấu hiệu |
|---|---|---|
| **A** | Mơ hồ (đọc ra hai nghĩa) | Đại từ hay chủ ngữ không rõ; phạm vi lượng từ không rõ; bổ ngữ treo; câu dễ đọc nhầm cấu trúc. |
| **B** | Tối nghĩa (một nghĩa nhưng phải đoán) | Thuật ngữ, ký hiệu dùng trước khi định nghĩa; biệt ngữ, ẩn dụ; chồng danh từ; nhắc tới quy trình hay tên gọi chưa giới thiệu. |
| **C** | Thiếu chặt chẽ | Khẳng định rộng hơn điều đã chứng minh; thiếu giả thiết hay lượng từ; một ký hiệu hai nghĩa; một khái niệm nhiều tên. |
| **D** | Liên kết | Câu hoặc đoạn không nối với phần trước; từ nối sai logic; một ý lặp ở nhiều nơi; nội dung đặt sai chỗ. |
| **E** | Câu dài hoặc nặng | Trên 30 từ, hoặc từ 3 mệnh đề trở lên, hoặc nhiều phủ định chồng nhau; hoặc chuỗi câu quá ngắn rời rạc. |
| **F** | Thừa / lan man | Phép thử xóa: bỏ câu mà không mất thông tin thì câu thừa; câu lệch mục đích của đoạn, lặp điều đã nói, hoặc rào đón. |

**Súc tích** nghĩa là mỗi câu nói một ý cần thiết, chính xác, bằng ít chữ nhất mà người đọc vẫn không phải đoán. Nén quá mức thành biệt ngữ là lỗi B, không phải súc tích.

Mức độ: **[1] phải sửa** (sai hoặc có thể làm phản biện nghi ngờ kết quả), **[2] nên sửa** (gây khó hiểu), **[3] tùy chọn** (văn phong).

## Kết quả tổng quát

- Đã rà **503 câu/đơn vị** (gồm tiêu đề, chú thích bảng, các bước của Thuật toán 1; không gồm phần thân bảng số liệu và danh mục tài liệu tham khảo).
- **452 câu không cần sửa.**
- **51 câu có vướng lỗi:** 1 câu mức [1], 22 câu mức [2], 28 câu mức [3].
- Theo loại (một câu có thể có nhiều mã): A mơ hồ: 5, B tối nghĩa: 13, C thiếu chặt chẽ: 6, D liên kết: 3, E câu dài/nặng: 21, F thừa/lan man: 3.
- Câu trên 30 từ: 31; trong đó 11 câu được đề nghị tách (mức [2]). Các câu dài còn lại là danh sách tham số hoặc chứa công thức, có thể giữ.
- Phần chứng minh (Mục 3.6–3.9) đạt yêu cầu: các bước đều có lý do, lượng từ rõ, không có câu thừa.
- Hai câu cần lưu ý nhất: câu về công thức (8) "whose maximizers…" (mức [1], đọc ra nghĩa sai) và câu Introduction "the proof uses this weight only to…" (mức [2], chưa chính xác; câu này đang được letter R1.1 trích nguyên văn).

## Vấn đề xuyên suốt cả bài

| Mã | Mức | Vấn đề và cách sửa |
|---|---|---|
| C | [2] | Tên của J không thống nhất: violation measure, merit function, error function, feasibility residual, full residual. Chọn một tên (ví dụ "residual function") cho J; dành "violation" cho v_i. |
| C | [3] | Tên của bước trên track lồi không thống nhất: Polyak step, Polyak-type step, residual-scaled step. Dùng "residual-scaled Polyak-type step". |
| C | [3] | Ký hiệu trùng nghĩa ở Mục 4: η (tốc độ học AFRSFCV và độ dài bước DTAP), T (số bước AFRSFCV, thời điểm cuối PNN, và T_k), t (chỉ số lớp, thời gian, và t = ρᵀw trong chứng minh Mệnh đề 4.1). |
| B | [2] | Hai tên không được định nghĩa: "Tchebyshev scalarization" (tiêu đề Mục 3.1, từ khóa) và "solver diagnostic" (Mục 4 mở đầu, chú thích Bảng 1). |
| D | [3] | Tính lồi của Ω được nói ba lần (Introduction, Mục 2, Mục 3.3); thông tin quy tắc chọn ngưỡng nói hai lần (Mục 4.1.3 và 4.2.2). |
| E | [2] | Nhiều câu dài trên 30 từ, tập trung ở Mục 4.4 và Mục 4.2 (xem số liệu ở Kết quả tổng quát). Các câu nên tách được đánh dấu E [2] trong bảng; các câu dài còn lại là danh sách tham số hoặc chứa công thức, có thể giữ. |

## Bảng rà soát từng câu

Cột 1 là câu nguyên văn (số trong ngoặc vuông là thứ tự câu; [công thức (n)] là công thức hiển thị). Cột 2 ghi có lỗi hay không, kèm mã và mức. Cột 3 ghi "Giữ nguyên" hoặc cách sửa cụ thể.


### Abstract và từ khóa

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [1] We study a nonlinear split feasibility problem whose output set is a normal box and whose component functions are differentiable and each convex or pseudoconvex. | Không | Giữ nguyên |
| [2] We propose the Dual-Track Adaptive Projection (DTAP) algorithm, which splits the constraints into a convex and a pseudoconvex track and works on the nearly most violated constraints of each. | **Có** — B [3] (tối nghĩa, tùy chọn) | Cụm "works on" không nói rõ làm gì với các ràng buộc. Có thể viết: "…and, on each track, uses the gradients of the nearly most violated constraints." |
| [3] DTAP combines a residual-scaled Polyak-type step on the convex track with a safeguarded diminishing step on the pseudoconvex track through a residual-responsive proportional weight, and then projects onto the base convex set. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 32 từ nhưng chỉ một ý; có thể giữ. Nếu muốn ngắn: "DTAP combines a residual-scaled Polyak-type step on the convex track with a safeguarded diminishing step on the pseudoconvex track by a residual-responsive proportional weight, and projects onto the base convex set." |
| [4] Its step sizes require no prescribed operator norm, Lipschitz constant, or Hölder modulus; the proof uses local bounds on the bounded iterate region. | Không | Giữ nguyên |
| [5] Under consistency and continuous differentiability, we prove that the whole sequence converges strongly to a feasible point. | Không | Giữ nguyên |
| [6] As an application, we formulate feature selection as such a problem, with constraints built from fractional and fuzzy-rough feature-selection criteria. | Không | Giữ nguyên |
| [7] Experiments on UCI datasets show that the selected features keep the classification accuracy close to that of the full feature set, and test problems with a nonconvex pseudoconvex constraint exercise the pseudoconvex track; we also compare DTAP with subgradient methods and study its sensitivity to the starting point and the step scale. | **Có** — E [2] (câu dài/nặng, nên sửa) | 52 từ, hai mệnh đề nối bằng dấu chấm phẩy. Tách hai câu: "Experiments on UCI datasets show that the selected features keep the classification accuracy close to that of the full feature set. Test problems with a nonconvex pseudoconvex constraint exercise the pseudoconvex track; we also compare DTAP with subgradient methods and study its sensitivity to the starting point and the step scale." |
| [8] Split feasibility problem; Pseudoconvex optimization; Tchebyshev scalarization; Adaptive step size; Strong convergence; Feature selection 47J25; 90C25; 90C26; 65K05; 68T05 | Không | Giữ nguyên |

### Introduction

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [10] The split feasibility problem (SFP) was introduced by Censor and Elfving [4] as a model for constrained inverse problems. | Không | Giữ nguyên |
| [11] Given nonempty closed convex sets $C\subseteq\mathbb{R}^n$ and $Q\subseteq\mathbb{R}^m$ and a matrix $\mathcal A\in\mathbb{R}^{m\times n}$, it asks to [công thức (1)] | Không | Giữ nguyên |
| [12] Byrne's $CQ$ algorithm [3] iterates [công thức (2)] | Không | Giữ nguyên |
| [13] Here $\\vert \mathcal A\\vert $ is the spectral norm of $\mathcal A$. | Không | Giữ nguyên |
| [14] Relaxed variants project onto supporting half-spaces [17]; self-adaptive steps avoid estimating $\\vert \mathcal A\\vert $ [20, 22, 10]; operator splitting [21] and alternating direction methods [18] decompose the problem. | Không | Giữ nguyên |
| [15] These ideas are standard; DTAP adapts them to the nonlinear case. | **Có** — A [2] (mơ hồ, nên sửa) | "them" gồm cả biến thể chiếu lên nửa không gian tựa, mà DTAP không dùng. Viết rõ: "These ideas are standard; DTAP adapts the self-adaptive step and the decomposition to the nonlinear case." |
| [16] Replacing $\mathcal A$ by a nonlinear map $F$ gives the nonlinear SFP [9, 19] [công thức (3)] where $K\subseteq\mathbb{R}^n$ is nonempty, closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$ is a normal box, and each $F_i$ is differentiable and convex or pseudoconvex on $K$. | Không | Giữ nguyên |
| [17] Since pseudoconvex functions have convex sublevel sets, the feasible set $\Omega=\{x\in K:F(x)\in Q\}$ is convex. | Không | Giữ nguyên |
| [18] We seek a point of $\Omega$, not a minimizer of any $F_i$. | Không | Giữ nguyên |
| [19] Because $Q$ is a box, the $\ell_\infty$-distance from $F(x)$ to $Q$ has the closed form [công thức] | Không | Giữ nguyên |
| [20] Li et al. [9] assume a convex aggregate proximity function, which componentwise pseudoconvexity does not ensure. | Không | Giữ nguyên |
| [21] Yen et al. [19] use the same max-type violation measure and active-set device, but require quasilinear components, a class incomparable with ours. | **Có** — B [3] (tối nghĩa, tùy chọn) | "active-set device" là biệt ngữ. Có thể viết: "…use the same max-type violation measure and an active set of nearly most violated constraints, but require…" |
| [22] Hu et al. [7] treat quasiconvex inequalities, which contain our class, without using the gradient inequality of convex components. | **Có** — A [3] (mơ hồ, tùy chọn) | "our class" chưa được gọi tên. Viết: "…treat quasiconvex inequalities, a class that contains convex and pseudoconvex functions, without using…" |
| [23] Convex and pseudoconvex constraints call for different steps. | Không | Giữ nguyên |
| [24] For a convex constraint, the gradient inequality bounds $\langle \nabla F_i(x),x-x^\star\rangle$, for every $x^\star\in\Omega$, from below by the violation, which justifies a residual-scaled Polyak-type step [14, 10]; for a pseudoconvex constraint, only the sign of this inner product is known, so a safeguarded diminishing step is used. | **Có** — E [2] (câu dài/nặng, nên sửa) | 45 từ. Tách tại dấu chấm phẩy thành hai câu: "For a convex constraint, the gradient inequality bounds ⟨∇F_i(x),x−x*⟩, for every x*∈Ω, from below by the violation, which justifies a residual-scaled Polyak-type step [14, 10]. For a pseudoconvex constraint, only the sign of this inner product is known, so a safeguarded diminishing step is used." |
| [25] DTAP takes the two steps on separate tracks and combines them by a proportional weight; the proof uses this weight only to keep a persistently violated track active (Remark 1). | **Có** — C [2] (thiếu chặt chẽ, nên sửa) | "uses this weight only to keep a persistently violated track active" chưa chính xác: Nhận xét 1 dùng hai tính chất, (27) là cận dưới μ_k ≥ J^cvx_k/(2V) cho track lồi, và Khẳng định 2 cho 1−μ_k ≥ 1/2 khi track giả lồi bị vi phạm kéo dài. Viết: "…the proof uses only two properties of this weight (Remark 1): it is bounded below by a multiple of the convex-track violation, and it gives a persistently violated pseudoconvex track a weight of at least 1/2." LƯU Ý: câu này đang được letter (R1.1) trích nguyên văn; nếu sửa phải sửa letter theo. |
| [26] The contributions are as follows. | Không | Giữ nguyên |
| [27] A dual-track method that uses the gradient inequality on the convex constraints and only sign information on the pseudoconvex ones, without assuming a convex proximity function, unlike [9], or a Hölder modulus, unlike the dynamic step of [7]. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 38 từ, hai cụm "unlike […]" chen giữa làm khó đọc. Có thể viết: "A dual-track method that uses the gradient inequality on the convex constraints and only sign information on the pseudoconvex ones; unlike [9], it assumes no convex proximity function, and unlike the dynamic step of [7], it needs no Hölder modulus." |
| [28] Convergence of the whole sequence to a feasible point under Assumption 1 (Theorem 3.12). | Không | Giữ nguyên |
| [29] A feature-selection application built from fractional and fuzzy-rough criteria, whose constraints are convex (Proposition 4.1), and test problems with a nonconvex pseudoconvex constraint; the experiments report constraint activity, compare DTAP with tuned subgradient methods, and measure its sensitivity to the starting point and the step scale. | **Có** — E [2] (câu dài/nặng, nên sửa) | 46 từ. Tách: "A feature-selection application built from fractional and fuzzy-rough criteria, whose constraints are convex (Proposition 4.1), and test problems with a nonconvex pseudoconvex constraint. On both, the experiments report constraint activity, compare DTAP with tuned subgradient methods, and measure its sensitivity to the starting point and the step scale." |
| [30] Section 2 gives preliminaries. | **Có** — D [3] (liên kết, tùy chọn) | Ba câu rất ngắn liền nhau (mục lục). Có thể gộp: "Section 2 gives preliminaries, Section 3 presents DTAP and its convergence analysis, Section 4 reports experiments, and Section 5 concludes." |
| [31] Section 3 presents DTAP and its convergence analysis. | Không | Giữ nguyên |
| [32] Section 4 reports experiments, and Section 5 concludes. | Không | Giữ nguyên |

### Preliminaries

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [34] Throughout, $H=\mathbb{R}^n$ is the Euclidean space with inner product $\langle \cdot,\cdot\rangle$ and induced norm $\\vert \cdot\\vert $. | Không | Giữ nguyên |
| [35] All convergence statements concern the norm topology. | **Có** — F [3] (thừa/lan man, tùy chọn) | Trong ℝⁿ mọi tô-pô chuẩn trùng nhau nên câu này hiển nhiên. Vì bài giữ cụm "strong convergence", nên dùng câu này để giải thích cụm đó: "In ℝⁿ, strong and weak convergence coincide; we keep the term strong convergence for consistency with the SFP literature." |
| [36] Bounded sequences have convergent subsequences. | **Có** — F [3] (thừa/lan man, tùy chọn) | Điều hiển nhiên (Bolzano–Weierstrass). Có thể bỏ, hoặc ghi "(Bolzano–Weierstrass)" ở chỗ dùng trong chứng minh Định lý 3.12. |
| [37] The standard projection and generalized convexity facts below can be found in [1, 12]. | Không | Giữ nguyên |
| [38] For a nonempty closed convex set $K\subseteq H$, the metric projection $P_K(x)$ is the unique minimizer of $\\vert y-x\\vert $ over $y\in K$. | Không | Giữ nguyên |
| [39] For $x\in H$ and $p\in K$, $p=P_K(x)$ if and only if [công thức (4)] | Không | Giữ nguyên |
| [40] This characterization yields Lemma 3.2 below. | Không | Giữ nguyên |
| [41] A function $f:K\to\mathbb{R}$ is convex if $f((1-t)x+ty)\le(1-t)f(x)+tf(y)$ for $x,y\in K$ and $t\in[0,1]$. | **Có** — C [3] (thiếu chặt chẽ, tùy chọn) | Lượng từ chưa rõ: "for x,y∈K" → "for all x,y∈K and all t∈[0,1]". |
| [42] The following weaker derivative condition was introduced by Mangasarian [11]. | Không | Giữ nguyên |
| [43] A function $f$ that is differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for all $x,y\in K$, [công thức (5)] | Không | Giữ nguyên |
| [44] Every differentiable convex function is pseudoconvex. | Không | Giữ nguyên |
| [45] Pseudoconvex functions have convex sublevel sets, although the functions themselves need not be convex. | **Có** — D [3] (liên kết, tùy chọn) | Tính lồi của Ω được nói ba lần (Introduction, câu này, và sau Giả thiết 1). Có thể bỏ vế này ở đây và giữ lập luận đầy đủ ở Mục 3.3. |

### The DTAP algorithm and its convergence analysis

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [47] We formulate the normal-box NSFP, state DTAP, and prove convergence of the whole sequence to a feasible point. | Không | Giữ nguyên |

### Problem statement and Tchebyshev scalarization

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [48] **(tiêu đề)** Problem statement and Tchebyshev scalarization | **Có** — B [2] | Thuật ngữ "Tchebyshev scalarization" xuất hiện ở tiêu đề (và từ khóa) nhưng không câu nào trong mục giải thích. Thêm vào câu về công thức (8): "…(8) is the Tchebyshev (max-type) scalarization of the residuals (F_i(x)−b_i)^+." |
| [49] Let $K\subseteq H$ be nonempty closed convex, and let $U\subseteq H$ be an open neighbourhood of $K$. | Không | Giữ nguyên |
| [50] Fix an integer $m\ge1$, let $F=(F_1,\dots,F_m):U\to\mathbb{R}^m$, let $b=(b_1,\dots,b_m)\in\mathbb{R}^m$, and set the normal box $Q:=(-\infty,b_1]\times\cdots\times(-\infty,b_m]$. | Không | Giữ nguyên |
| [51] We study the instance of (3) [công thức (6)] and call $\Omega$ the feasible set. | Không | Giữ nguyên |
| [52] To turn $F(x)\in Q$ into a tractable merit function, we measure the residual in the sup-norm. | Không | Giữ nguyên |
| [53] For $z=F(x)$, $d_\infty(z,Q)=\inf_{q\le b}\max_{1\le i\le m}\vert z_i-q_i\vert $. | Không | Giữ nguyên |
| [54] By the box structure the infimum separates over coordinates: if $z_i\le b_i$ then $\inf_{q_i\le b_i}\vert z_i-q_i\vert =0$ (at $q_i=z_i$), and if $z_i>b_i$ then it equals $z_i-b_i$ (at $q_i=b_i$). | **Có** — C [3] (thiếu chặt chẽ, tùy chọn) | "separates over coordinates" chưa nói rõ vì sao inf của max bằng max của các inf. Viết: "Since Q is a product of intervals, the infimum of the maximum equals the maximum of the coordinatewise infima: if z_i ≤ b_i … " |
| [55] Hence $\inf_{q_i\le b_i}\vert z_i-q_i\vert =(z_i-b_i)^+$ with $(t)^+:=\max\{t,0\}$, so [công thức (7)] | Không | Giữ nguyên |
| [56] Define the error function [công thức (8)] | **Có** — C [2] (thiếu chặt chẽ, nên sửa) | Một đại lượng J nhưng có nhiều tên trong bài: "violation measure" (Intro), "merit function" (câu trước), "error function" (đây), "feasibility residual" (câu sau), "full residual" (Nhận xét 5, Kết luận). Chọn một tên, ví dụ "residual function", và dùng thống nhất; "violation" để dành cho v_i. |
| [57] Then $x\in K$ is feasible if and only if $J(x)=0$; when $\Omega\ne\emptyset$, the feasible points are the minimizers of $J$ over $K$. | Không | Giữ nguyên |
| [58] Formula (8) gives a closed-form feasibility residual whose maximizers identify the most violated constraints. | **Có** — A [1] (mơ hồ, phải sửa) | "whose maximizers" đọc như các điểm cực đại của J (là điểm x), trong khi ý là các chỉ số i đạt max trong (8). Viết: "In (8), the indices attaining the maximum are the most violated constraints." (có thể gộp với câu về Tchebyshev ở trên). |
| [59] Section 3.2 introduces an approximate active set to handle the nonsmooth maximum. | Không | Giữ nguyên |

### Decomposition into two tracks

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [61] We split $I:=\{1,\dots,m\}$ into a convex track $I^{\mathrm{cvx}}$ and a pseudoconvex track $I^{\mathrm{ps}}$, each with its own step rule. | Không | Giữ nguyên |
| [62] The convex track uses a Polyak step [14]; the pseudoconvex track uses a safeguarded diminishing step. | **Có** — C [3] (thiếu chặt chẽ, tùy chọn) | Cùng một bước nhưng có ba tên: "Polyak step" (đây), "Polyak-type step" (Abstract, Intro), "residual-scaled step". Dùng thống nhất "residual-scaled Polyak-type step". |
| [63] A proportional weight combines the two updates. | Không | Giữ nguyên |
| [64] Fix a parameter $\delta>0$. | **Có** — D [3] (liên kết, tùy chọn) | δ được cố định trước khi cần tới (dùng ở (12)–(13)). Có thể chuyển câu này xuống ngay trước câu định nghĩa tập hoạt động xấp xỉ. |
| [65] For $x\in U$ define the componentwise violations [công thức (9)] so that $J(x)=\max_i v_i(x)$ by (8). | Không | Giữ nguyên |
| [66] Assumption 1 makes the partition precise. | Không | Giữ nguyên |
| [67] The per-track maximal violations are [công thức (10, 11)] so $J(x)=\max\{J^{\mathrm{cvx}}(x),J^{\mathrm{ps}}(x)\}$. | Không | Giữ nguyên |
| [68] To cope with the nonsmoothness of the maximum, we replace the set of indices at which the maximum is attained by a $\delta$-enlarged approximate active set on each track (`active' meaning within $\delta$ of the largest violation): [công thức (12, 13)] | **Có** — E [2] (câu dài/nặng, nên sửa) | 41 từ, có ngoặc giải thích chen giữa. Viết: "To handle the nonsmooth maximum, we replace the set of maximizing indices by a δ-enlarged approximate active set on each track, which contains the indices whose violation is within δ of the largest one:" |
| [69] On these sets we form the per-track local functions and directions [công thức (14, 15)] | **Có** — B [3] (tối nghĩa, tùy chọn) | "local" không có nghĩa rõ (Φ và g không phải hàm địa phương). Viết: "On these sets we form the per-track functions and search directions". |
| [70] The vectors $g^{\mathrm{cvx}}(x),g^{\mathrm{ps}}(x)$ are the two search directions, and $\Phi^{\mathrm{cvx}}(x)$ supplies the Polyak numerator on the convex track. | Không | Giữ nguyên |
| [71] Along the iterates we abbreviate $J^{\mathrm{cvx}}_k:=J^{\mathrm{cvx}}(x^k)$, $g^{\mathrm{cvx}}_k:=g^{\mathrm{cvx}}(x^k)$, $\Phi^{\mathrm{cvx}}_k:=\Phi^{\mathrm{cvx}}(x^k)$, and likewise on the pseudoconvex track. | Không | Giữ nguyên |

### Assumptions

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [73] We assume (A1)--(A3): | Không | Giữ nguyên |
| [74] (a) $\Omega\ne\emptyset$ (consistency). | Không | Giữ nguyên |
| [75] (b) $I=\{1,\dots,m\}$ is partitioned as $I=I^{\mathrm{cvx}}\cup I^{\mathrm{ps}}$; each $F_i:U\to\mathbb{R}$ is convex on $K$ if $i\in I^{\mathrm{cvx}}$ and pseudoconvex on $K$ if $i\in I^{\mathrm{ps}}$. | Không | Giữ nguyên |
| [76] Each $F_i:U\to\mathbb{R}$ is continuously differentiable on $U$. | Không | Giữ nguyên |
| [77] (i) $\delta>0$ fixed. | Không | Giữ nguyên |
| [78] (ii) $\rho_{\mathrm{cvx}}\in(0,2)$. | Không | Giữ nguyên |
| [79] (iii) $\{\gamma_k\}\subset(0,\infty)$ with $\sum_{k=0}^\infty\gamma_k^2<\infty$ and $\sum_{k=0}^\infty\gamma_k=\infty$. | Không | Giữ nguyên |
| [80] The open-neighbourhood formulation permits fractional functions whose denominators are positive on $K$; the algorithm evaluates the functions and gradients only at points of $K$. | Không | Giữ nguyên |
| [81] Although some component functions may be nonconvex, $\Omega$ is convex: differentiable pseudoconvex functions are quasiconvex on $K$, so all constraint sublevel sets in $K$ are convex. | Không | Giữ nguyên |
| [82] The sequence $\gamma_k:=1/(k+1)$ satisfies (A3)(iii), since $\sum_{k\ge0}(k+1)^{-2}<\infty$ while $\sum_{k\ge0}(k+1)^{-1}=\infty$. | Không | Giữ nguyên |
| [83] More generally $\gamma_k=(k+c)^{-s}$ with $c>0$ and $s\in(1/2,1]$ qualifies; the experiments use $s=0.55$. | Không | Giữ nguyên |

### The DTAP algorithm

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [85] The Dual-Track Adaptive Projection algorithm combines the two track-specific step sizes through the proportional weight $\mu_k$ and projects the combined update onto the base convex set $K$. | **Có** — F [3] (thừa/lan man, tùy chọn) | Lặp lại ý đã nói ở Mục 3.2 và Abstract. Có thể gộp với câu sau: "Algorithm 1 states DTAP; the proportional weight μ_k combines the two track-specific step sizes." |
| [86] It is stated as Algorithm 1. | Không | Giữ nguyên |
| [87] Dual-Track Adaptive Projection (DTAP) for the normal-box NSFP (6). | Không | Giữ nguyên |
| [88] Input: map $F=(F_1,\dots,F_m)$, thresholds $b$, base set $K$, index split $I^{\mathrm{cvx}}\cup I^{\mathrm{ps}}$. | Không | Giữ nguyên |
| [89] Parameters: $\delta>0$, tolerance $\varepsilon>0$, $\rho_{\mathrm{cvx}}\in(0,2)$, sequence $\{\gamma_k\}$ satisfying (A3)(iii). | Không | Giữ nguyên |
| [90] Initialization: choose $x^0\in K$; set $k\leftarrow 0$. | Không | Giữ nguyên |
| [91] Step 1 (per-track quantities). | Không | Giữ nguyên |
| [92] If $J(x^k)\le\varepsilon$, stop and return $x^k$; otherwise: | Không | Giữ nguyên |
| [93] Compute $v_i(x^k)$ for all $i$, and $J^{\mathrm{cvx}}_k=\max_{i\in I^{\mathrm{cvx}}}v_i(x^k)$, $J^{\mathrm{ps}}_k=\max_{j\in I^{\mathrm{ps}}}v_j(x^k)$ (each $0$ if its track is empty). | Không | Giữ nguyên |
| [94] Form the approximate active sets $K^{\mathrm{cvx}}_k,K^{\mathrm{ps}}_k$ via (12)--(13). | Không | Giữ nguyên |
| [95] Form $\Phi^{\mathrm{cvx}}_k$, $g^{\mathrm{cvx}}_k$, $g^{\mathrm{ps}}_k$ via (14)--(15). | Không | Giữ nguyên |
| [96] Per-track step sizes (Polyak on the convex track, safeguarded on the pseudoconvex track): [công thức] | Không | Giữ nguyên |
| [97] Proportional weight: $\displaystyle \mu_k=\frac{J^{\mathrm{cvx}}_k}{J^{\mathrm{cvx}}_k+J^{\mathrm{ps}}_k}$ if $J^{\mathrm{cvx}}_k+J^{\mathrm{ps}}_k>0$, and $\mu_k=1/2$ otherwise. | Không | Giữ nguyên |
| [98] Combine the two directions: $\displaystyle y^k=x^k-\bigl[\mu_k\eta^{\mathrm{cvx}}_k g^{\mathrm{cvx}}_k+(1-\mu_k)\eta^{\mathrm{ps}}_k g^{\mathrm{ps}}_k\bigr].$ | Không | Giữ nguyên |
| [99] Step 2 (projection). | Không | Giữ nguyên |
| [100] \quad $x^{k+1}=P_K(y^k)$; set $k\leftarrow k+1$ and go to Step 1. | Không | Giữ nguyên |
| [101] The proportional weight is an adaptive allocation based on the two maximal violations; we do not claim that it is the only choice for which DTAP converges, or that it is optimal. | Không | Giữ nguyên |
| [102] Its specific form is used in (27) to control the convex-track residual and in Claim 2 of Stage 2 of Theorem 3.12 to ensure that a persistently violated pseudoconvex track retains positive weight. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 33 từ, chuỗi "in Claim 2 of Stage 2 of Theorem 3.12" nặng. Có thể viết: "Its specific form enters the proof twice: in (27), to bound the convex-track residual, and in Claim 2 of Theorem 3.12, to keep a persistently violated pseudoconvex track at positive weight." |
| [103] Although the one-step inequality of Lemma 3.8 holds for every $\mu_k\in[0,1]$, it does not by itself imply convergence for every weight sequence. | Không | Giữ nguyên |
| [104] The iteration does not require prescribed operator norms, Lipschitz constants, or Hölder moduli. | Không | Giữ nguyên |
| [105] The proof nevertheless uses finite bounds on function values and gradients on a compact set containing the iterates, after boundedness has been proved. | Không | Giữ nguyên |
| [106] Bounded gradients imply Lipschitz continuity of the functions on that convex compact set, but these bounds are not algorithm inputs. | Không | Giữ nguyên |
| [107] Assumption (A2) does not imply Lipschitz continuity of the gradients, and the theorem does not require it. | Không | Giữ nguyên |
| [108] The user still chooses $\rho_{\mathrm{cvx}}$, $\delta$, and $\{\gamma_k\}$; these parameters do not depend on any constant of the problem. | Không | Giữ nguyên |
| [109] For the analysis we write the combined increment as [công thức (16)] so $y^k=x^k-d_k$ and $x^{k+1}=P_K(x^k-d_k)$. | Không | Giữ nguyên |

### Per-iteration cost

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [111] Each DTAP iteration evaluates the componentwise violations $v_i(x^k)$ and the active-set gradients $\{\nabla F_i(x^k):i\in K^{\mathrm{cvx}}_k\cup K^{\mathrm{ps}}_k\}$, forms the two search directions $g^{\mathrm{cvx}}_k,g^{\mathrm{ps}}_k$ as weighted sums of these gradients, computes the step sizes, and performs one projection onto $K$. | Không | Giữ nguyên |
| [112] It uses neither an operator-norm estimate nor a line search. | Không | Giữ nguyên |
| [113] The cost is dominated by the constraint evaluations and the projection. | Không | Giữ nguyên |
| [114] The cost for the feature-selection instance is given in Section 4.1 (Remark 6). | Không | Giữ nguyên |

### Auxiliary lemmas

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [116] The two tracks need different arguments. | Không | Giữ nguyên |
| [117] On the convex track, Lemma 3.4 bounds $\langle \nabla F_i(x),x-x^\star\rangle$ from below by the violation $v_i(x)$; this gives a decrease of $\\vert x^k-x^\star\\vert ^2$ of order $\mu_kT_k$. | **Có** — B [2] (tối nghĩa, nên sửa) | Dùng T_k và x* trước khi định nghĩa (T_k ở (19), Mục 3.7). Viết: "On the convex track, Lemma 3.4 bounds ⟨∇F_i(x),x−x*⟩, for x*∈Ω, from below by the violation v_i(x); this yields a guaranteed decrease of ‖x^k−x*‖² (Lemma 3.8)." |
| [118] On the pseudoconvex track, definition (5) gives only the sign of this inner product. | Không | Giữ nguyên |
| [119] Lemma 3.8 combines both tracks in one quasi-Fejér inequality; the choice of the parameter $\zeta$ in Young's inequality keeps the convex-track term negative. | Không | Giữ nguyên |
| [120] Stage 2 of Theorem 3.12 then shows, by contradiction, that at least one cluster point is feasible, and Stage 3 shows that the whole sequence converges strongly to it. | Không | Giữ nguyên |
| [121] The two degenerate cases follow as corollaries. | Không | Giữ nguyên |
| [122] Throughout, $\{x^k\}$ is the infinite sequence generated by Algorithm 1 with the stopping test removed. | Không | Giữ nguyên |
| [123] As shown below (Lemma 3.10 and Theorem 3.12), $J(x^k)\to 0$; hence for any $\varepsilon>0$ there is a finite $k$ with $J(x^k)\le\varepsilon$, so the finite-stopping version terminates after finitely many steps with an $\varepsilon$-feasible point. | **Có** — B [3] (tối nghĩa, tùy chọn) | 33 từ; "finite-stopping version" là cách gọi tự đặt. Viết: "…so Algorithm 1 with its stopping test terminates after finitely many steps with an ε-feasible point." |
| [124] We begin with two preparatory results used repeatedly below. | Không | Giữ nguyên |
| [125] Let $K\subseteq H$ be nonempty closed convex. | Không | Giữ nguyên |
| [126] For every $y\in H$ and $z\in K$, [công thức (17)] | Không | Giữ nguyên |
| [127] Put $p:=P_K(y)$. | Không | Giữ nguyên |
| [128] By Proposition 2.1, $\langle y-p,z-p\rangle\le0$, so expanding $\\vert y-z\\vert ^2=\\vert y-p\\vert ^2+2\langle y-p,p-z\rangle+\\vert p-z\\vert ^2$ and using $\langle y-p,p-z\rangle\ge0$ gives $\\vert y-z\\vert ^2\ge\\vert y-p\\vert ^2+\\vert p-z\\vert ^2$, which is (17). | Không | Giữ nguyên |
| [129] Let $\{a_k\}\subset[0,\infty)$ and $\{\varepsilon_k\}\subset[0,\infty)$ satisfy $a_{k+1}\le a_k+\varepsilon_k$ for all $k$ and $\sum_{k=0}^\infty\varepsilon_k<\infty$. | Không | Giữ nguyên |
| [130] Then $\{a_k\}$ converges to a finite limit. | Không | Giữ nguyên |
| [131] $b_k:=a_k-\sum_{l<k}\varepsilon_l$ is nonincreasing (from $a_{k+1}\le a_k+\varepsilon_k$) and bounded below by $-\sum_l\varepsilon_l>-\infty$, hence converges; since $\sum_{l<k}\varepsilon_l\to S<\infty$, $a_k=b_k+\sum_{l<k}\varepsilon_l$ converges. | Không | Giữ nguyên |
| [132] On the convex track, convexity gives a quantitative link between the gradient and the violation. | Không | Giữ nguyên |
| [133] For $x^\star\in\Omega$, $i\in I^{\mathrm{cvx}}$, and $x\in K$, [công thức] | Không | Giữ nguyên |
| [134] If $v_i(x)=0$ both sides vanish. | Không | Giữ nguyên |
| [135] Let $v_i(x)>0$, i.e. $F_i(x)>b_i$. | Không | Giữ nguyên |
| [136] Define $\varphi:[0,1]\to\mathbb{R}$ by $\varphi(t):=F_i((1-t)x+tx^\star)$; since $K$ is convex, $[x,x^\star]\subset K$, so $\varphi$ is well defined, and by (A1)(b) it is convex, while by (A2) it is differentiable with $\varphi'(0^+)=\langle \nabla F_i(x),x^\star-x\rangle$. | Không | Giữ nguyên |
| [137] The one-dimensional gradient inequality gives $\varphi(1)\ge\varphi(0)+\varphi'(0^+)$, i.e. $F_i(x^\star)\ge F_i(x)+\langle \nabla F_i(x),x^\star-x\rangle$. | Không | Giữ nguyên |
| [138] As $x^\star\in\Omega$ we have $F_i(x^\star)\le b_i<F_i(x)$, whence $\langle \nabla F_i(x),x-x^\star\rangle\ge F_i(x)-b_i=v_i(x)$. | Không | Giữ nguyên |
| [139] Multiplying by $v_i(x)>0$ gives the claim. | Không | Giữ nguyên |
| [140] Summing Lemma 3.4 over the approximate active set $K^{\mathrm{cvx}}_k$ yields $\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}\ge\sum_{i\in K^{\mathrm{cvx}}_k}v_i(x^k)^2=2\Phi^{\mathrm{cvx}}_k$, a bound used in the proofs of Lemmas 3.8 and 3.10. | Không | Giữ nguyên |
| [141] On the pseudoconvex track, only a sign is available. | Không | Giữ nguyên |
| [142] For $x^\star\in\Omega$, $j\in I^{\mathrm{ps}}$, and $x\in K$, $v_j(x)\,\langle \nabla F_j(x),x-x^\star\rangle\ge 0$, with strict inequality when $v_j(x)>0$. | Không | Giữ nguyên |
| [143] If $v_j(x)=0$ both sides vanish. | Không | Giữ nguyên |
| [144] If $v_j(x)>0$ then $F_j(x)>b_j\ge F_j(x^\star)$. | Không | Giữ nguyên |
| [145] By (A1)(b), $F_j\vert _K$ is pseudoconvex; applying (5) with $y=x^\star$ gives $\langle \nabla F_j(x),x^\star-x\rangle<0$, i.e. $\langle \nabla F_j(x),x-x^\star\rangle>0$. | Không | Giữ nguyên |
| [146] Multiplying by $v_j(x)>0$ yields the strict inequality. | Không | Giữ nguyên |
| [147] Finally, two compactness-based norm bounds on the search directions. | **Có** — E [3] (câu dài/nặng, tùy chọn) | Câu không có động từ. Viết: "Finally, we bound the norms of the two search directions on compact sets." |
| [148] Assume $I^{\mathrm{cvx}}\ne\emptyset$ and let $B\subset U$ be compact. | Không | Giữ nguyên |
| [149] With $L_B:=\max_{i\in I^{\mathrm{cvx}}}\sup_{x\in B}\\vert \nabla F_i(x)\\vert $ (finite by (A2)), for every $x\in B$, [công thức] | Không | Giữ nguyên |
| [150] Put $K'=K^{\mathrm{cvx}}(x)$, $m'=\vert K'\vert \le\abs{I^{\mathrm{cvx}}}$. | Không | Giữ nguyên |
| [151] By the triangle and Cauchy--Schwarz inequalities, [công thức] | Không | Giữ nguyên |
| [152] Since $\sum_{i\in K'}v_i(x)^2=2\Phi^{\mathrm{cvx}}(x)$ and $\sum_{i\in K'}\\vert \nabla F_i(x)\\vert ^2\le m'L_B^2\le\abs{I^{\mathrm{cvx}}}L_B^2$, squaring gives the claim. | Không | Giữ nguyên |
| [153] Assume $I^{\mathrm{ps}}\ne\emptyset$ and let $B\subset U$ be compact. | Không | Giữ nguyên |
| [154] With $L'_B:=\max_{j\in I^{\mathrm{ps}}}\sup_{x\in B}\\vert \nabla F_j(x)\\vert $ and $V_B:=\max_{j\in I^{\mathrm{ps}}}\sup_{x\in B}v_j(x)$ (both finite by (A2)), for every $x\in B$, [công thức] | Không | Giữ nguyên |
| [155] By the triangle inequality, $\norm{g^{\mathrm{ps}}(x)}=\bigl\\vert \sum_{j\in K^{\mathrm{ps}}(x)}v_j(x)\nabla F_j(x)\bigr\\vert  \le\sum_{j\in K^{\mathrm{ps}}(x)}v_j(x)\\vert \nabla F_j(x)\\vert \le\abs{K^{\mathrm{ps}}(x)}V_BL'_B \le\abs{I^{\mathrm{ps}}}V_BL'_B$. | Không | Giữ nguyên |

### Boundedness and decay of the iteration error

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [157] The following inequality is of quasi-Fejér type in the sense of Combettes [5]. | Không | Giữ nguyên |
| [158] It yields boundedness of $\{x^k\}$ and decay of the convex-track violation. | Không | Giữ nguyên |
| [159] Set [công thức (18)] and [công thức (19)] | Không | Giữ nguyên |
| [160] For fixed $x^\star\in\Omega$ write $R^{x^\star}_k:=\inner{g^{\mathrm{ps}}_k}{x^k-x^\star}$. | Không | Giữ nguyên |
| [161] For every $x^\star\in\Omega$ and $k\ge 0$, [công thức (20)] | Không | Giữ nguyên |
| [162] Apply Lemma 3.2 with $y=y^k$ and $z=x^\star\in K$ and use $y^k=x^k-d_k$ from (16): [công thức (21)] | Không | Giữ nguyên |
| [163] Cross term. | Không | Giữ nguyên |
| [164] Expanding $d_k$, [công thức (22)] | Không | Giữ nguyên |
| [165] If $\norm{g^{\mathrm{cvx}}_k}=0$ then $\eta^{\mathrm{cvx}}_k=0$ and the first term vanishes. | Không | Giữ nguyên |
| [166] If $\norm{g^{\mathrm{cvx}}_k}>0$, Remark 3 gives $\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}\ge 2\Phi^{\mathrm{cvx}}_k$; multiplying by $\mu_k\eta^{\mathrm{cvx}}_k\ge 0$ and substituting $\eta^{\mathrm{cvx}}_k=2\rho_{\mathrm{cvx}}\Phi^{\mathrm{cvx}}_k/\norm{g^{\mathrm{cvx}}_k}^2$, [công thức (23)] | Không | Giữ nguyên |
| [167] Quadratic term. | Không | Giữ nguyên |
| [168] By Young's inequality $\\vert u+v\\vert ^2\le(1+\zeta)\\vert u\\vert ^2+(1+\zeta^{-1})\\vert v\\vert ^2$ with $u=\mu_k\eta^{\mathrm{cvx}}_k g^{\mathrm{cvx}}_k$, $v=(1-\mu_k)\eta^{\mathrm{ps}}_k g^{\mathrm{ps}}_k$, [công thức] | Không | Giữ nguyên |
| [169] By definition $\eta^{\mathrm{ps}}_k=\gamma_k/\max\{1,\norm{g^{\mathrm{ps}}_k}\}$, so $\eta^{\mathrm{ps}}_k\norm{g^{\mathrm{ps}}_k}\le\gamma_k$ and hence $(\eta^{\mathrm{ps}}_k)^2\norm{g^{\mathrm{ps}}_k}^2\le\gamma_k^2$; with $(1-\mu_k)^2\le 1$, [công thức (24)] | Không | Giữ nguyên |
| [170] Choose $\zeta:=(2-\rho_{\mathrm{cvx}})/(2\rho_{\mathrm{cvx}})>0$. | Không | Giữ nguyên |
| [171] Then $(1+\zeta)\rho_{\mathrm{cvx}}=(2+\rho_{\mathrm{cvx}})/2$, so $(1+\zeta)\rho_{\mathrm{cvx}}^2=\rho_{\mathrm{cvx}}(2+\rho_{\mathrm{cvx}})/2$, and $1+\zeta^{-1}=(2+\rho_{\mathrm{cvx}})/(2-\rho_{\mathrm{cvx}})=C_0$. | Không | Giữ nguyên |
| [172] Combining (21), (22), (23) and (24), [công thức] | Không | Giữ nguyên |
| [173] The bracket equals $\mu_k\rho_{\mathrm{cvx}}\bigl(-2+\tfrac{2+\rho_{\mathrm{cvx}}}{2}\mu_k\bigr)$. | Không | Giữ nguyên |
| [174] Since $\rho_{\mathrm{cvx}}<2$, for all $\mu_k\in[0,1]$ the factor $-2+\tfrac{2+\rho_{\mathrm{cvx}}}{2}\mu_k$ is at most $-(2-\rho_{\mathrm{cvx}})/2<0$ (its maximum over $[0,1]$ is at $\mu_k=1$); multiplying by $\mu_k\rho_{\mathrm{cvx}}\ge0$ gives the bracket $\le -c_0\mu_k$. | Không | Giữ nguyên |
| [175] This yields (20). | Không | Giữ nguyên |
| [176] The sequence $\{x^k\}$ is bounded. | Không | Giữ nguyên |
| [177] Moreover, for each fixed $x^\star\in\Omega$: (i) $\{\\vert x^k-x^\star\\vert ^2\}$ converges in $[0,\infty)$; (ii) $\sum_{k=0}^\infty\mu_k T_k<\infty$; (iii) $\sum_{k=0}^\infty(1-\mu_k)\eta^{\mathrm{ps}}_k R^{x^\star}_k<\infty$. | Không | Giữ nguyên |
| [178] Fix $x^\star\in\Omega$ and set $a_k:=\\vert x^k-x^\star\\vert ^2$. | Không | Giữ nguyên |
| [179] By Lemma 3.5, $R^{x^\star}_k\ge0$, and $\mu_k,T_k,(1-\mu_k)\eta^{\mathrm{ps}}_k\ge0$, so (20) gives $a_{k+1}\le a_k+C_0\gamma_k^2$. | Không | Giữ nguyên |
| [180] Since $\sum_k C_0\gamma_k^2<\infty$ by (A3)(iii), Lemma 3.3 yields (i), and boundedness of $\{x^k\}$ follows. | Không | Giữ nguyên |
| [181] Summing (20) from $0$ to $N-1$, [công thức] | Không | Giữ nguyên |
| [182] The right side is bounded uniformly in $N$; letting $N\to\infty$ and using $c_0>0$ with nonnegative terms gives (ii) and (iii). | Không | Giữ nguyên |
| [183] $\displaystyle\lim_{k\to\infty}J^{\mathrm{cvx}}_k=0$. | Không | Giữ nguyên |
| [184] If $I^{\mathrm{cvx}}=\emptyset$ then $J^{\mathrm{cvx}}_k=0$ for all $k$. | Không | Giữ nguyên |
| [185] Assume $I^{\mathrm{cvx}}\ne\emptyset$, fix $x^\star\in\Omega$, and put $B:=\overline{\conv}\{x^k:k\ge0\}$, compact by Lemma 3.9 and contained in $K\subset U$. | Không | Giữ nguyên |
| [186] By (A2) and compactness, [công thức] | Không | Giữ nguyên |
| [187] If $V=0$ then all $v_i(x^k)=0$ and $J^{\mathrm{cvx}}_k=0$; assume $V>0$. | Không | Giữ nguyên |
| [188] If $L=0$ then each $F_i$, $i\in I^{\mathrm{cvx}}$, is constant on $B$, so $g^{\mathrm{cvx}}_k=0$ and, by Remark 3, $0=\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}\ge 2\Phi^{\mathrm{cvx}}_k\ge(J^{\mathrm{cvx}}_k)^2$, giving $J^{\mathrm{cvx}}_k=0$; assume $L>0$. | Không | Giữ nguyên |
| [189] Set $m^{\mathrm{cvx}}:=\abs{I^{\mathrm{cvx}}}\ge1$. | Không | Giữ nguyên |
| [190] Consider a step with $J^{\mathrm{cvx}}_k>0$ and pick $i^\star\in I^{\mathrm{cvx}}$ with $v_{i^\star}(x^k)=J^{\mathrm{cvx}}_k$. | Không | Giữ nguyên |
| [191] Since $v_{i^\star}(x^k)\ge J^{\mathrm{cvx}}_k-\delta$, we have $i^\star\in K^{\mathrm{cvx}}_k$, whence [công thức (25)] | Không | Giữ nguyên |
| [192] Remark 3 gives $\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}\ge2\Phi^{\mathrm{cvx}}_k>0$, so $g^{\mathrm{cvx}}_k\ne0$; with Lemma 3.6, $\norm{g^{\mathrm{cvx}}_k}^2\le2m^{\mathrm{cvx}}L^2\Phi^{\mathrm{cvx}}_k$, and with (25), [công thức (26)] | Không | Giữ nguyên |
| [193] For a lower bound on $\mu_k$: for all $i\in I$ and $x^k\in B$, $v_i(x^k)\le\vert F_i(x^k)-b_i\vert \le V$, so $J^{\mathrm{cvx}}_k\le V$ and $J^{\mathrm{ps}}_k\le V$; when $J^{\mathrm{cvx}}_k>0$, [công thức (27)] | Không | Giữ nguyên |
| [194] Combining (26) and (27), for $J^{\mathrm{cvx}}_k>0$, $\mu_k T_k\ge(J^{\mathrm{cvx}}_k)^3/(2Vm^{\mathrm{cvx}}L^2)$; this also holds (as $0\ge0$) when $J^{\mathrm{cvx}}_k=0$. | Không | Giữ nguyên |
| [195] By Lemma 3.9(ii), [công thức (28)] so $(J^{\mathrm{cvx}}_k)^3\to0$ and thus $J^{\mathrm{cvx}}_k\to0$. | Không | Giữ nguyên |
| [196] [công thức] in particular, $\norm{x^{k+1}-x^k}\to0$. | Không | Giữ nguyên |
| [197] Since $x^k\in K$ and $x^{k+1}=P_K(y^k)$, Lemma 3.2 with $y=y^k$, $z=x^k$ gives $\norm{x^{k+1}-x^k}\le\\vert y^k-x^k\\vert =\\vert d_k\\vert $. | Không | Giữ nguyên |
| [198] By (24) and $\mu_k^2\le\mu_k$, $\\vert d_k\\vert ^2\le(1+\zeta)\rho_{\mathrm{cvx}}^2\mu_k T_k+C_0\gamma_k^2$. | Không | Giữ nguyên |
| [199] Summing and using Lemma 3.9(ii) and (A3)(iii), both series are finite. | **Có** — A [3] (mơ hồ, tùy chọn) | "both series" chưa nói là chuỗi nào. Viết: "Summing, the series Σ_k μ_kT_k and Σ_k γ_k² are finite by Lemma 3.9(ii) and (A3)(iii), and the claim follows." |

### Strong convergence to a feasible point

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [201] We now prove that the whole sequence converges strongly to a feasible point. | Không | Giữ nguyên |
| [202] The proof has three stages. | Không | Giữ nguyên |
| [203] Stage 1 uses Lemma 3.10 to show that every cluster point satisfies the convex constraints. | Không | Giữ nguyên |
| [204] Stage 2 shows, by contradiction and pseudoconvexity, that at least one cluster point is feasible. | Không | Giữ nguyên |
| [205] Stage 3 uses the convergence of $\\vert x^k-\bar x\\vert $ to show that the whole sequence converges to that point. | Không | Giữ nguyên |
| [206] Under Assumption 1, the sequence $\{x^k\}$ generated by Algorithm 1 converges strongly to a point $x^\infty\in\Omega$. | Không | Giữ nguyên |
| [207] By Lemma 3.9, $\{x^k\}$ is bounded; let $C:=\{\bar x\in H:\exists\,k_l\to\infty,\ x^{k_l}\to\bar x\}$ be its (nonempty, compact) cluster set. | Không | Giữ nguyên |
| [208] Since $K$ is closed and $x^k\in K$, $C\subseteq K$. | Không | Giữ nguyên |
| [209] Stage 1 (convex constraints). | Không | Giữ nguyên |
| [210] Fix $\bar x\in C$ and $x^{k_l}\to\bar x$. | Không | Giữ nguyên |
| [211] By (A2) each $F_i$ is continuous, so $v_i(x^{k_l})\to v_i(\bar x)$; for $i\in I^{\mathrm{cvx}}$, $v_i(x^{k_l})\le J^{\mathrm{cvx}}_{k_l}\to0$ by Lemma 3.10, so by squeezing $v_i(\bar x)=0$, i.e. $F_i(\bar x)\le b_i$. | Không | Giữ nguyên |
| [212] Hence [công thức (29)] | Không | Giữ nguyên |
| [213] If $I^{\mathrm{ps}}=\emptyset$, then (29) gives $C\subseteq\Omega$, so $C\cap\Omega=C\ne\emptyset$. | Không | Giữ nguyên |
| [214] Assume henceforth $I^{\mathrm{ps}}\ne\emptyset$. | Không | Giữ nguyên |
| [215] Stage 2 (a feasible cluster point). | Không | Giữ nguyên |
| [216] Suppose, for contradiction, that $C\cap\Omega=\emptyset$. | Không | Giữ nguyên |
| [217] By (29) and the partition $I=I^{\mathrm{cvx}}\cup I^{\mathrm{ps}}$, for each $\bar x\in C$ there is $j\in I^{\mathrm{ps}}$ with $F_j(\bar x)>b_j$, i.e. $J^{\mathrm{ps}}(\bar x)>0$. | Không | Giữ nguyên |
| [218] As a maximum of finitely many continuous functions, $J^{\mathrm{ps}}$ is continuous and positive on the compact set $C$, so $\alpha:=\min_{x\in C}J^{\mathrm{ps}}(x)>0$. | Không | Giữ nguyên |
| [219] Claim 1 (uniform lower bound for $J^{\mathrm{ps}}_k$). | Không | Giữ nguyên |
| [220] There exist $\tau_0>0$ and $k_0$ with $J^{\mathrm{ps}}_k\ge\tau_0$ for all $k\ge k_0$. | Không | Giữ nguyên |
| [221] Indeed, put $\tau_0:=\alpha/2$. | Không | Giữ nguyên |
| [222] If the claim failed there would be $k_l\to\infty$ with $J^{\mathrm{ps}}_{k_l}<\tau_0$; extracting (same notation) $x^{k_l}\to\tilde x\in C$, continuity gives $J^{\mathrm{ps}}(\tilde x)\le\tau_0<\alpha$, contradicting the definition of $\alpha$. | Không | Giữ nguyên |
| [223] Claim 2 ($\mu_k\to0$). | Không | Giữ nguyên |
| [224] For $k\ge k_0$, $\mu_k=J^{\mathrm{cvx}}_k/(J^{\mathrm{cvx}}_k+J^{\mathrm{ps}}_k)\le J^{\mathrm{cvx}}_k/\tau_0\to0$ by Lemma 3.10. | Không | Giữ nguyên |
| [225] Hence there is $k_1\ge k_0$ with $1-\mu_k\ge1/2$ for $k\ge k_1$. | Không | Giữ nguyên |
| [226] Claim 3 (uniform lower bound for $R^{x^\star}_k$). | Không | Giữ nguyên |
| [227] Fix $x^\star\in\Omega$. | Không | Giữ nguyên |
| [228] There exist $\xi_0>0$ and $k_2\ge k_1$ with $R^{x^\star}_k\ge\xi_0$ for all $k\ge k_2$. | Không | Giữ nguyên |
| [229] Suppose not: there is $k_l\to\infty$ with $R^{x^\star}_{k_l}\to0$. | Không | Giữ nguyên |
| [230] As $\{x^{k_l}\}$ is bounded, extract $x^{k_l}\to\bar x\in C$; since $I^{\mathrm{ps}}$ has finitely many subsets, extract further so that $K^{\mathrm{ps}}_{k_l}\equiv K^\star$ is constant. | Không | Giữ nguyên |
| [231] By assumption $J^{\mathrm{ps}}(\bar x)>0$; choose $j^\star\in\argmax_{j\in I^{\mathrm{ps}}}v_j(\bar x)$, so $v_{j^\star}(\bar x)=J^{\mathrm{ps}}(\bar x)>0$. | Không | Giữ nguyên |
| [232] By continuity $v_{j^\star}(x^{k_l})\to v_{j^\star}(\bar x)$ and $J^{\mathrm{ps}}_{k_l}\to J^{\mathrm{ps}}(\bar x)$, so $J^{\mathrm{ps}}_{k_l}-v_{j^\star}(x^{k_l})\to0$; with $\delta>0$ from (A3)(i), for large $l$ we get $v_{j^\star}(x^{k_l})\ge J^{\mathrm{ps}}_{k_l}-\delta$, hence $j^\star\in K^{\mathrm{ps}}_{k_l}=K^\star$. | Không | Giữ nguyên |
| [233] Each summand of $R^{x^\star}_{k_l}=\sum_{j\in K^\star}v_j(x^{k_l})\inner{\nabla F_j(x^{k_l})}{x^{k_l}-x^\star}$ is nonnegative by Lemma 3.5, so keeping only $j^\star$, [công thức] | Không | Giữ nguyên |
| [234] Letting $l\to\infty$ and using continuity of $v_{j^\star}$ and $\nabla F_{j^\star}$, [công thức] | Không | Giữ nguyên |
| [235] Since $j^\star\in I^{\mathrm{ps}}$ and $x^\star\in\Omega$, $F_{j^\star}(x^\star)\le b_{j^\star}<F_{j^\star}(\bar x)$; definition (5) with $x=\bar x$, $y=x^\star$ gives $\inner{\nabla F_{j^\star}(\bar x)}{\bar x-x^\star}>0$, and with $v_{j^\star}(\bar x)>0$ we get $\Lambda>0$, contradicting $R^{x^\star}_{k_l}\to0$. | Không | Giữ nguyên |
| [236] This proves Claim 3. | Không | Giữ nguyên |
| [237] Reaching the contradiction. | Không | Giữ nguyên |
| [238] By Lemma 3.7 on $B:=\overline{\conv}\{x^k\}$, $\norm{g^{\mathrm{ps}}_k}\le\abs{I^{\mathrm{ps}}}V_B L'_B$ with $L'_B:=\max_{j\in I^{\mathrm{ps}}}\sup_B\\vert \nabla F_j\\vert <\infty$. | Không | Giữ nguyên |
| [239] Put $G':=\max\{1,\abs{I^{\mathrm{ps}}}V_B L'_B\}$; then $\max\{1,\norm{g^{\mathrm{ps}}_k}\}\le G'$ for all $k$, so $\eta^{\mathrm{ps}}_k=\gamma_k/\max\{1,\norm{g^{\mathrm{ps}}_k}\}\ge\gamma_k/G'$. | Không | Giữ nguyên |
| [240] For $k\ge k_2$, combining with $1-\mu_k\ge1/2$ and $R^{x^\star}_k\ge\xi_0$, [công thức] by (A3)(iii), contradicting Lemma 3.9(iii). | Không | Giữ nguyên |
| [241] Hence $C\cap\Omega\ne\emptyset$. | Không | Giữ nguyên |
| [242] Stage 3 (whole-sequence convergence). | Không | Giữ nguyên |
| [243] Fix $\bar x\in C\cap\Omega$. | Không | Giữ nguyên |
| [244] Lemma 3.9(i), applied to $x^\star=\bar x$, ensures that $\lim_{k\to\infty}\\vert x^k-\bar x\\vert ^2$ exists. | Không | Giữ nguyên |
| [245] Since $\bar x\in C$, a subsequence $x^{k_l}$ converges to $\bar x$. | Không | Giữ nguyên |
| [246] Therefore [công thức] | Không | Giữ nguyên |
| [247] Hence the whole sequence converges to $\bar x$, and we set $x^\infty:=\bar x\in\Omega$. | Không | Giữ nguyên |
| [248] The argument does not require $\Omega$ to be a singleton: one feasible cluster point and the convergence of its distance suffice. | Không | Giữ nguyên |
| [249] The parameter $\delta>0$ is not necessary for convergence. | Không | Giữ nguyên |
| [250] When $\delta=0$ one argues by subsequence: along $x^{k_l}\to\bar x\in C$, choose $j_l\in\argmax_{j\in I^{\mathrm{ps}}}v_j(x^{k_l})$; since $I^{\mathrm{ps}}$ is finite, extract $j_l\equiv j^\star$, and $v_{j^\star}(x^{k_l})=J^{\mathrm{ps}}(x^{k_l})\to J^{\mathrm{ps}}(\bar x)>0$, so $j^\star$ attains the maximal violation at $\bar x$ and the pseudoconvexity argument goes through. | Không | Giữ nguyên |
| [251] The role of $\delta>0$ is to simplify: a maximizer at $\bar x$ automatically lies in $K^{\mathrm{ps}}_{k_l}$ for large $l$, avoiding a `finitely many indices' extraction. | Không | Giữ nguyên |
| [252] Larger $\delta$ enlarges $K^{\mathrm{cvx}}_k$ and $K^{\mathrm{ps}}_k$, which may improve numerical stability when several $v_i(x^k)$ are nearly equal. | Không | Giữ nguyên |
| [253] From (28), $\sum_k(J^{\mathrm{cvx}}_k)^3<\infty$, whence $\min_{0\le k<N}J^{\mathrm{cvx}}_k=O(N^{-1/3})$. | Không | Giữ nguyên |
| [254] This bounds the best convex-track violation over the first $N$ iterates. | Không | Giữ nguyên |
| [255] It is not a last-iterate bound, a rate for the full residual $J(x^k)$, or a rate for the distance to a feasible point. | Không | Giữ nguyên |
| [256] For these latter quantities, under (A1)--(A3) alone we assert only qualitative convergence. | Không | Giữ nguyên |

### Degenerate constraint structures

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [258] When the constraint structure degenerates (only a convex track or only a pseudoconvex track), DTAP and its analysis simplify, yielding two corollaries of Theorem 3.12. | Không | Giữ nguyên |
| [259] If $I^{\mathrm{ps}}=\emptyset$, then $J^{\mathrm{ps}}_k\equiv0$, $g^{\mathrm{ps}}_k\equiv0$, and $\mu_k\equiv1$ whenever $J^{\mathrm{cvx}}_k>0$, so Algorithm 1 reduces to $x^{k+1}=P_K(x^k-\eta^{\mathrm{cvx}}_k g^{\mathrm{cvx}}_k)$. | Không | Giữ nguyên |
| [260] The sequence converges strongly to a point $x^\infty\in\Omega=\{x\in K:F_i(x)\le b_i\text{ for all }i\in I^{\mathrm{cvx}}\}$. | Không | Giữ nguyên |
| [261] Here $d_k=\eta^{\mathrm{cvx}}_k g^{\mathrm{cvx}}_k$, and (21) directly gives $\norm{x^{k+1}-x^\star}^2\le\\vert x^k-x^\star\\vert ^2-2\eta^{\mathrm{cvx}}_k\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}+(\eta^{\mathrm{cvx}}_k)^2\norm{g^{\mathrm{cvx}}_k}^2$. | Không | Giữ nguyên |
| [262] If $\norm{g^{\mathrm{cvx}}_k}=0$ then $\eta^{\mathrm{cvx}}_k=0$, $T_k=0$, and the bound is $\norm{x^{k+1}-x^\star}^2\le\\vert x^k-x^\star\\vert ^2$. | Không | Giữ nguyên |
| [263] Otherwise Lemma 3.4 gives $\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}\ge2\Phi^{\mathrm{cvx}}_k$, and substituting $\eta^{\mathrm{cvx}}_k=2\rho_{\mathrm{cvx}}\Phi^{\mathrm{cvx}}_k/\norm{g^{\mathrm{cvx}}_k}^2$ together with $(\eta^{\mathrm{cvx}}_k)^2\norm{g^{\mathrm{cvx}}_k}^2=\eta^{\mathrm{cvx}}_k\cdot2\rho_{\mathrm{cvx}}\Phi^{\mathrm{cvx}}_k$ yields, after simplification, $2\eta^{\mathrm{cvx}}_k\inner{g^{\mathrm{cvx}}_k}{x^k-x^\star}-(\eta^{\mathrm{cvx}}_k)^2\norm{g^{\mathrm{cvx}}_k}^2\ge\rho_{\mathrm{cvx}}(2-\rho_{\mathrm{cvx}})(2\Phi^{\mathrm{cvx}}_k)^2/\norm{g^{\mathrm{cvx}}_k}^2=2c_0T_k$. | Không | Giữ nguyên |
| [264] Hence [công thức (30)] valid for all $k$. | Không | Giữ nguyên |
| [265] Thus $\{\\vert x^k-x^\star\\vert ^2\}$ is nonincreasing and convergent, and summing gives $\sum_k T_k<\infty$. | Không | Giữ nguyên |
| [266] As in Lemma 3.10, when $J^{\mathrm{cvx}}_k>0$ one has $T_k\ge(J^{\mathrm{cvx}}_k)^2/(m^{\mathrm{cvx}}L^2)$ (note the exponent $2$ here, versus $3$ in (28), since no $\mu_k$ factor is present), so $\sum_k(J^{\mathrm{cvx}}_k)^2<\infty$ and $J^{\mathrm{cvx}}_k\to0$. | Không | Giữ nguyên |
| [267] Finally, $I^{\mathrm{ps}}=\emptyset$ makes Stage 2 of Theorem 3.12 vacuous (indeed $C\subseteq\Omega$ already from (29)), and Stage 3 gives $x^k\to x^\infty\in\Omega$. | Không | Giữ nguyên |
| [268] If $I^{\mathrm{cvx}}=\emptyset$, then $J^{\mathrm{cvx}}_k\equiv0$, $g^{\mathrm{cvx}}_k\equiv0$, and $\mu_k\equiv0$ whenever $J^{\mathrm{ps}}_k>0$, so Algorithm 1 reduces to $x^{k+1}=P_K(x^k-\eta^{\mathrm{ps}}_k g^{\mathrm{ps}}_k)$ with $\eta^{\mathrm{ps}}_k=\gamma_k/\max\{1,\norm{g^{\mathrm{ps}}_k}\}$. | Không | Giữ nguyên |
| [269] The sequence converges strongly to a point $x^\infty\in\Omega$. | Không | Giữ nguyên |
| [270] Now $d_k=\eta^{\mathrm{ps}}_k g^{\mathrm{ps}}_k$ with $\\vert d_k\\vert ^2\le\gamma_k^2$, so (21) gives $\norm{x^{k+1}-x^\star}^2\le\\vert x^k-x^\star\\vert ^2-2\eta^{\mathrm{ps}}_k R^{x^\star}_k+\gamma_k^2$, which is (20) in this degenerate case ($T_k=0$, $1-\mu_k=1$). | Không | Giữ nguyên |
| [271] Since $R^{x^\star}_k\ge0$ (Lemma 3.5), $a_{k+1}\le a_k+\gamma_k^2$, and Lemma 3.3 gives convergence of $\{\\vert x^k-x^\star\\vert ^2\}$ and boundedness; summation gives $\sum_k\eta^{\mathrm{ps}}_k R^{x^\star}_k<\infty$. | Không | Giữ nguyên |
| [272] Stage 1 of Theorem 3.12 gives $C\subseteq K$ (the convex part being vacuous); Stage 2 with $\mu_k=0$ (so $1-\mu_k=1$) produces the same contradiction $\sum\eta^{\mathrm{ps}}_k R^{x^\star}_k=+\infty$, so $C\cap\Omega\ne\emptyset$; Stage 3 gives $x^k\to x^\infty\in\Omega$. | Không | Giữ nguyên |

### Numerical experiments

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [274] We separate predictive performance from the numerical solution of the feasibility system. | **Có** — B [2] (tối nghĩa, nên sửa) | "separate" không rõ là tách theo nghĩa nào. Viết: "We report predictive performance (Sections 4.1–4.3) separately from the numerical solution of the feasibility problems (Section 4.4)." |
| [275] The classification comparison uses eight datasets. | Không | Giữ nguyên |
| [276] The solver diagnostic additionally includes Movement Libras and controlled nonconvex pseudoconvex instances. | **Có** — B [2] (tối nghĩa, nên sửa) | "solver diagnostic" là tên không xuất hiện ở tiêu đề mục nào (Mục 4.4 tên là "Constraint activity and a tuned subgradient comparison"). Viết: "Section 4.4 additionally uses Movement Libras and controlled nonconvex pseudoconvex instances." |

### Feature-selection model

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [278] We apply the normal-box NSFP to feature selection by combining criteria from the fractional-programming model of Wang et al. [15] and the fuzzy-rough model AFRSFCV [16]. | Không | Giữ nguyên |
| [279] Let $\mathcal{X}=\{x_1,\ldots,x_n\}$ be the training samples, $A=\{a_1,\ldots,a_p\}$ the features, $X\in\mathbb{R}^{n\times p}$ the data matrix, and $y\in\{1,\ldots,r\}^n$ the class labels. | Không | Giữ nguyên |
| [280] Here $n$ is the number of samples; subscripts index features and superscripts index iterations. | Không | Giữ nguyên |
| [281] The feature weights belong to the compact convex simplex $K=\Delta_{p-1}=\{w\in\mathbb{R}^p:w\ge0,\ \mathbf1_p^{\top}w=1\}$. | Không | Giữ nguyên |
| [282] All supervised quantities below are estimated from the training data. | Không | Giữ nguyên |

### Fractional criterion and N-Fscore

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [284] The supervised similarity matrix $S\in\mathbb{R}^{p\times p}$ has entries [công thức (31)] where $Z_i$ is the discretized feature $a_i$, $C$ is the class variable, and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$ is their interaction information. | Không | Giữ nguyên |
| [285] Entropy and mutual information are estimated from equal-width histograms with ten bins per feature [2]. | Không | Giữ nguyên |
| [286] We set $s_{ij}=0$ if the denominator is zero. | Không | Giữ nguyên |
| [287] The redundancy matrix is [công thức (32)] so $Q_R\succeq0$. | Không | Giữ nguyên |
| [288] The implementation uses $\delta_Q=\max\{0,-\lambda_{\min}(S)\}+10^{-10}$. | Không | Giữ nguyên |
| [289] Let $n_t$, $\bar a_{kt}$, and $\sigma_{kt}^2$ be the class size, mean, and population variance of feature $a_k$ in class $t$, and let $\bar a_k$ be its overall mean. | Không | Giữ nguyên |
| [290] The Fisher scores are [công thức (33)] | Không | Giữ nguyên |
| [291] These scores are nonnegative. | Không | Giữ nguyên |
| [292] The denominator regularization prevents division by zero but does not ensure $\rho_k>0$, since the numerator can vanish. | Không | Giữ nguyên |
| [293] The fractional program underlying N-Fscore is [công thức (34)] assuming the denominator is positive on $K$. | Không | Giữ nguyên |
| [294] The numerator measures redundancy and the denominator relevance. | Không | Giữ nguyên |
| [295] Our N-Fscore baseline uses the projection-neural-network stage of [15], with the Fisher scores in (33). | Không | Giữ nguyên |
| [296] It then applies the common selection rule (44), instead of the source method's $k$-winners-take-all stage. | Không | Giữ nguyên |
| [297] Its dynamics and explicit-Euler implementation are given in Section 4.2.1. | Không | Giữ nguyên |

### Fuzzy-rough criterion and AFRSFCV

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [299] For each class, write $D_t=\{x_i:y_i=t\}$ and $D_t(x_j)=\mathbf1_{\{y_j=t\}}$. | Không | Giữ nguyên |
| [300] AFRSFCV incorporates class variance into a fuzzy relation. | Không | Giữ nguyên |
| [301] With $a_k(x_i)=X_{ik}$, the implemented relation is [công thức (35)] | Không | Giữ nguyên |
| [302] The variance floor makes the formula defined when a feature is constant within a class. | Không | Giữ nguyên |
| [303] The fuzzy lower approximation is [công thức (36)] | Không | Giữ nguyên |
| [304] Its values form the matrix $\underline{R_k}(D)\in[0,1]^{n\times r}$. | Không | Giữ nguyên |
| [305] Let $Y_{it}=\mathbf1_{\{y_i=t\}}$ be the label matrix and define the decision matrix by [công thức (37)] | Không | Giữ nguyên |
| [306] Ties are resolved by the smallest class index. | Không | Giữ nguyên |
| [307] Thus $P_{ik}=1$ precisely when feature $a_k$ predicts sample $x_i$ correctly under this rule. | Không | Giữ nguyên |
| [308] The AFRSFCV baseline [16] minimizes [công thức (38)] where $w_k(\tau)=e^{\tau_k}/\sum_{l=1}^{p}e^{\tau_l}$ ensures $w(\tau)\in K$. | Không | Giữ nguyên |
| [309] The three terms are the label-approximation error, the weight of misclassifying features per sample, and a Tikhonov term. | **Có** — B [3] (tối nghĩa, tùy chọn) | "the weight of misclassifying features per sample" hơi nén. Viết rõ: "…the squared total weight, per sample, of the features that misclassify it, and a Tikhonov term." |
| [310] The baseline uses gradient descent for a fixed iteration budget, followed by (44). | Không | Giữ nguyên |
| [311] The gradient and update are given in Section 4.2.1. | Không | Giữ nguyên |

### Feasibility and feature selection

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [313] We impose separate bounds on three criteria, [công thức (39, 40, 41)] | Không | Giữ nguyên |
| [314] Here $F_1,F_2$ are the first two terms of (38), without their coefficients, and $F_3$ is the objective in (34). | Không | Giữ nguyên |
| [315] For thresholds $b_i>0$, the resulting problem is [công thức (42)] | Không | Giữ nguyên |
| [316] This formulation asks for simultaneous acceptability of the three criteria. | **Có** — B [3] (tối nghĩa, tùy chọn) | "acceptability" mơ hồ. Viết: "A feasible w satisfies the three bounds simultaneously." |
| [317] It omits the Tikhonov term and does not preserve either source optimization problem or its minimizers. | Không | Giữ nguyên |
| [318] If $Q_R\succeq0$ and $\min_k\rho_k>0$, all three functions in (39)--(41) are smooth and convex on an open convex neighbourhood of $K$. | Không | Giữ nguyên |
| [319] Consequently, (42) is an all-convex normal-box NSFP. | Không | Giữ nguyên |
| [320] Hence (42) satisfies (A1) and (A2) of Assumption 1, with $U=U_\rho$, whenever $\Omega\ne\varnothing$. | Không | Giữ nguyên |
| [321] The first two functions are squared norms of affine maps. | Không | Giữ nguyên |
| [322] For $w\in U_\rho$ and any direction $h$, put $t=\rho^{\top}w$ and $a=\rho^{\top}h$. | Không | Giữ nguyên |
| [323] Direct differentiation gives [công thức (43)] | Không | Giữ nguyên |
| [324] Thus $F_3$ is convex and smooth on the open half-space $U_\rho$. | Không | Giữ nguyên |
| [325] Since $\rho^{\top}w\ge\min_k\rho_k>0$ for $w\in K$, this half-space contains $K$. | Không | Giữ nguyên |
| [326] The experiments use $I^{\mathrm{cvx}}=\{1,2\}$, $I^{\mathrm{ps}}=\{3\}$, which is admissible since convex functions are pseudoconvex; DTAP then uses only sign information for $F_3$, so no genuinely nonconvex constraint is tested. | Không | Giữ nguyên |
| [327] The all-convex assignment $I^{\mathrm{cvx}}=\{1,2,3\}$ is also admissible, and Theorem 3.12 applies to both. | Không | Giữ nguyên |
| [328] Proposition 4.1 needs $\min_k\rho_k>0$; on all instances used here the smallest score is $4.77\times10^{-5}$. | Không | Giữ nguyên |
| [329] Hence the safeguard $\max\{\rho^\top w,10^{-15}\}$ in the implementation is never active, and the implemented $F_3$ is (41). | Không | Giữ nguyên |
| [330] The thresholds are calibrated on the training data: $b_i$ is the $q_i$-th percentile of $F_i$ over $3\,000$ Dirichlet points (seed $42$) and the $p$ vertices of $K$, where a fixed rule chooses $q_i$ from the sample size, the number of features and classes, and the class imbalance (supplementary metadata). | **Có** — E [2] (câu dài/nặng, nên sửa) | 49 từ. Tách: "The thresholds are calibrated on the training data. Each b_i is the q_i-th percentile of F_i over 3 000 Dirichlet points (seed 42) and the p vertices of K; a fixed rule chooses q_i from the sample size, the numbers of features and classes, and the class imbalance (supplementary metadata)." |
| [331] All solvers share these thresholds. | Không | Giữ nguyên |
| [332] Calibrating each $b_i$ separately does not guarantee $\Omega\ne\varnothing$; Section 4.4 checks feasibility numerically. | Không | Giữ nguyên |
| [333] Prescribed thresholds would be used as given. | Không | Giữ nguyên |
| [334] For every method, sort the computed weights as $w^\star_{(1)}\ge\cdots\ge w^\star_{(p)}$ and retain the first $s$ features, where [công thức (44)] | Không | Giữ nguyên |
| [335] This cumulative-weight rule does not enforce a prescribed feature budget. | Không | Giữ nguyên |
| [336] Truncating the weights does not preserve the feasibility guarantee for the full vector. | Không | Giữ nguyên |
| [337] With the precomputed matrices, evaluating $F_1,\nabla F_1$ costs $O(nrp)$, evaluating $F_2,\nabla F_2$ costs $O(np)$, and evaluating $F_3,\nabla F_3$ costs $O(p^2)$. | Không | Giữ nguyên |
| [338] Projection onto $K=\Delta_{p-1}$ by sorting costs $O(p\log p)$ operations [6]. | Không | Giữ nguyên |
| [339] A dense iteration therefore costs $O(nrp+p^2)$ operations and requires $O(nrp+p^2)$ storage, including $Q_R$. | Không | Giữ nguyên |
| [340] Preprocessing and classifier training are separate costs. | Không | Giữ nguyên |

### Experimental setup

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [342] The main classification study uses the eight UCI datasets [8] in Table 1. | Không | Giữ nguyên |
| [343] The DTAP runs reported here start at the uniform weight vector and use $\rho_{\mathrm{cvx}}=1.98$, $\delta=10^{-3}$, $\gamma_k=(k+0.5)^{-0.55}$, tolerance $10^{-6}$, and a budget of $1000$ iterations. | Không | Giữ nguyên |
| [344] SG-const uses the step $\nu_k=10^{-3}$ and SG-dyn the sampled modulus $\widehat L$ (Section 4.2.1); tuned moduli are considered only in Section 4.4. | Không | Giữ nguyên |
| [345] N-Fscore uses $\varepsilon_{\mathrm{PNN}}=10^{-3}$ and $1000$ Euler grid points on $[0,0.2]$. | Không | Giữ nguyên |
| [346] AFRSFCV uses learning rate $10^{-3}$, $\lambda_1=1$, $\lambda_2=0.5$, and $1000$ steps. | Không | Giữ nguyên |
| [347] The shared cumulative threshold is $\theta=0.9$. | Không | Giữ nguyên |
| [348] [Chú thích bảng] Datasets used for the main classification comparison. | **Có** — B [2] (tối nghĩa, nên sửa) | Câu thứ hai của chú thích dùng "solver diagnostic" (xem trên). Viết: "The additional Movement Libras instance is used only in Section 4.4." |
| [349] The additional Movement Libras instance is used only in the solver diagnostic. | **Có** — B [2] (tối nghĩa, nên sửa) | Như trên: thay "in the solver diagnostic" bằng "in Section 4.4". |

### Baseline solvers

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [351] The following paragraphs specify the baseline solvers: N-Fscore and AFRSFCV for the models of Sections 4.1.1 and 4.1.2, and the subgradient methods SG-const and SG-dyn. | Không | Giữ nguyên |
| [352] N-Fscore: the projection neural network | Không | Giữ nguyên |
| [353] To solve the fractional program (34), Wang et al. [15] proposed a neurodynamic method coupling a projection neural network (PNN) with a $k$-winners-take-all network. | Không | Giữ nguyên |
| [354] The PNN is the differential system [công thức (45)] with output $w=g(u)$, where $g(u)=\max\{0,u\}$ is the componentwise ReLU, $\Pi=\tfrac1p\mathbf{1}_p\mathbf{1}_p^{\top}$, $\nabla f$ is the gradient of the objective in (34), and $\varepsilon_{\mathrm{PNN}}>0$ is a time constant. | Không | Giữ nguyên |
| [355] We integrate (45) by the explicit Euler method on a uniform grid of $N_{\mathrm{grid}}$ points in $[0,T]$, without a stopping rule, using the parameters of Section 4.2. | Không | Giữ nguyên |
| [356] The weight vector is the projection $P_K\bigl(g(u(T))\bigr)$ of the final network output onto $K$. | Không | Giữ nguyên |
| [357] For a uniform comparison we use only the PNN part to obtain $w^\star$; the $k$-WTA stage is replaced by the shared cumulative-threshold rule of Section 4.1.3. | Không | Giữ nguyên |
| [358] AFRSFCV: gradient and update | Không | Giữ nguyên |
| [359] The softmax loss (38) is minimized over $\tau\in\mathbb{R}^p$ by gradient descent. | Không | Giữ nguyên |
| [360] Its gradient is [công thức (46)] with $\nabla_w L=-\mathbf{M}^{\top}(\vecop(Y)-\mathbf{M}w)+\lambda_1(P^{\top}Pw-P^{\top}\mathbf{1}_n)+\lambda_2 w$, where $\mathbf{M}\in\mathbb{R}^{nr\times p}$ has $k$-th column $\vecop(\underline{R_k}(D))$. | Không | Giữ nguyên |
| [361] The update $\tau^{t+1}=\tau^t-\eta\,\nabla_\tau L(\tau^t)$ runs for a fixed budget of $T$ steps; the final weight $w^\star=w(\tau^T)\in K$ feeds the shared selection rule of Section 4.1.3. | **Có** — C [3] (thiếu chặt chẽ, tùy chọn) | Ký hiệu trùng: η là tốc độ học của AFRSFCV nhưng η_k^cvx, η_k^ps là độ dài bước của DTAP; T là số bước ở đây, thời điểm cuối của PNN ở (45), và T_k ở (19). Có thể đổi tốc độ học thành α và số bước thành N_AF. |
| [362] SG-const and SG-dyn | Không | Giữ nguyên |
| [363] These subgradient methods for quasiconvex feasibility [7] follow its most-violated-constraint strategy: with $\mathcal I_k=\argmax_i v_i(w^k)$, [công thức] | Không | Giữ nguyên |
| [364] SG-const uses $\nu_k=10^{-3}$; SG-dyn uses the dynamic step $\nu_k=J(w^k)/L$ (Hölder exponent $1$), with $L=\widehat L$, the largest gradient norm at $500$ points sampled in $K$. | Không | Giữ nguyên |

### Evaluation protocol

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [366] Each dataset uses a single stratified $80/20$ training-pool/test split (seed $42$). | Không | Giữ nguyên |
| [367] Min--max scaling is fitted once on the full training pool, not separately within its selection folds, and is then applied to the test data. | Không | Giữ nguyên |
| [368] Stratified folds (seed $42$) within the pool use $N_f=10$, reduced to $7$ on Glass and $4$ on Yeast. | Không | Giữ nguyên |
| [369] The fold masks use $\theta=0.9$ in (44); the fixed strict-majority rule retains features selected in at least $\lfloor N_f/2\rfloor+1$ folds. | Không | Giữ nguyên |
| [370] We denote the voted feature set by $A^\star$. | Không | Giữ nguyên |
| [371] The final classifiers use the full pool with these voted features: RBF-SVM ($C=1$, gamma=scale) and $5$-NN, with the full feature set as a reference. | Không | Giữ nguyên |
| [372] Accuracy and macro one-vs-rest AUC are reported. | Không | Giữ nguyên |
| [373] The voted masks are computed once and then reused: the evaluation stage trains only the downstream classifiers on these fixed masks, with SVM probability-calibration seed $42$; identical masks share the same predictions. | Không | Giữ nguyên |
| [374] The test data are not used to select features or to choose any parameter or vote threshold. | Không | Giữ nguyên |
| [375] The training/test split is fixed before the selections are computed, and the rule that chooses the threshold levels uses only the sample size, the number of features, the number of classes and the class sizes of the whole dataset, not any feature values. | **Có** — E [2] (câu dài/nặng, nên sửa) | 43 từ và lặp lại nội dung quy tắc chọn ngưỡng đã nêu ở Mục 4.1.3. Viết: "The training/test split is fixed before the selections are computed, and the threshold rule of Section 4.1.3 uses only dataset sizes, not feature values." |
| [376] Because a single split is used, this is an exploratory evaluation, not an end-to-end or nested-validation study. | Không | Giữ nguyên |
| [377] For the fold-selection matrix $Z\in\{0,1\}^{N_f\times p}$, the Nogueira index [13] is computed as [công thức] | Không | Giữ nguyên |
| [378] Here $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$, and $s_j^2$ is the unbiased variance over the $N_f$ folds. | Không | Giữ nguyên |
| [379] Since the training folds overlap, stability is reported descriptively. | Không | Giữ nguyên |
| [380] For each classifier metric, we use a two-sided signed-rank test across the eight datasets, omitting zero differences, assigning midranks to ties, and enumerating all signs of the nonzero differences; all-zero pairs receive the $p$-value $1$. | Không | Giữ nguyên |
| [381] Holm adjustment covers the four DTAP--baseline comparisons separately for each metric. | Không | Giữ nguyên |
| [382] The Friedman test compares the five selection methods. | Không | Giữ nguyên |

### Classification results

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [384] Tables 2--4 report selected-set size, stability, and predictive performance. | Không | Giữ nguyên |
| [385] DTAP retains $84.2%$ of the features on average, including $33/36$ on Satimage and $49/57$ on Spambase. | Không | Giữ nguyên |
| [386] Its mean stability is $0.786$, compared with N-Fscore's $0.822$. | Không | Giữ nguyên |
| [387] Thus DTAP reduces the number of features moderately; it does not select sparser or more stable sets than the base models. | Không | Giữ nguyên |
| [388] AFRSFCV selects much smaller sets on several datasets, with lower mean accuracy under the fixed configuration. | Không | Giữ nguyên |
| [389] DTAP's mean accuracy is within $0.44$ percentage points of the full-feature reference for both classifiers. | Không | Giữ nguyên |
| [390] It exceeds N-Fscore and AFRSFCV by $3.12$ and $4.83$ points on SVM accuracy, while retaining more features. | Không | Giữ nguyên |
| [391] This is a size--prediction tradeoff, not a matched-budget comparison. | Không | Giữ nguyên |
| [392] Both SG variants have exactly the same voted masks as DTAP on seven datasets; only Spambase differs ($48$ versus $49$ features). | Không | Giữ nguyên |
| [393] SG-dyn used the full 1000-iteration budget in 6/7 selection folds on Glass, 7/10 on Diabetes and 10/10 on Abalone, and SG-const in 1/10 on Abalone (DTAP in none); the voted weights of both SG variants are the best iterates found within the budget. | **Có** — E [2] (câu dài/nặng, nên sửa) | 43 từ, nhiều số liệu trong một câu. Tách: "SG-dyn used the full 1000-iteration budget in 6/7 selection folds on Glass, 7/10 on Diabetes and 10/10 on Abalone; SG-const did so in 1/10 folds on Abalone, and DTAP in none. For both SG variants, the voted weights are the best iterates found within the budget." |
| [394] The SG results on Spambase, the only dataset where they differ from DTAP, are given below Table 3; Table 4 includes all five methods. | Không | Giữ nguyên |
| [395] Fold-wise stability can differ even when the final voted mask is identical. | Không | Giữ nguyên |
| [396] Table 5 reports the signed-rank tests. | Không | Giữ nguyên |
| [397] None of the pairwise comparisons rejects at $0.05$ after Holm adjustment; the SVM comparisons with the two base models have adjusted $p$-values between $0.0625$ and $0.0938$. | Không | Giữ nguyên |
| [398] The asymptotic Friedman tests reject equality globally, but this does not establish a particular pairwise superiority. | Không | Giữ nguyên |
| [399] All DTAP--SG pairwise $p$-values equal $1$; this reflects ties and limited evidence, not a statistical equivalence claim. | Không | Giữ nguyên |
| [400] These small-sample comparisons concern eight heterogeneous datasets and do not measure variation under repeated train/test splits. | Không | Giữ nguyên |
| [401] [Chú thích bảng] Selected count $\vert A^\star\vert $ / Nogueira stability $\Psi$; $p$ is the original dimension. | Không | Giữ nguyên |
| [402] All five selection methods are shown. | Không | Giữ nguyên |
| [403] [Chú thích bảng] Per-dataset accuracy (%) / macro one-vs-rest AUC on the single holdout. | Không | Giữ nguyên |
| [404] Equal voted masks reuse the same predictions; the SG exceptions are stated below. | Không | Giữ nguyên |
| [405] [Chú thích bảng] Unweighted mean classification performance over the eight classification datasets. | Không | Giữ nguyên |
| [406] All five selection methods and the full-feature reference are included. | Không | Giữ nguyên |
| [407] [Chú thích bảng] DTAP versus each baseline: raw / Holm-adjusted signed-rank $p$-values. | Không | Giữ nguyên |
| [408] Each metric has four comparisons over eight datasets. | Không | Giữ nguyên |
| [409] The last column gives the tie-corrected Friedman asymptotic $p$-value for all five methods. | Không | Giữ nguyên |

### Constraint activity and a tuned subgradient comparison

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [411] As noted in Section 4.1.3, the calibrated thresholds need not yield $\Omega\ne\varnothing$. | Không | Giữ nguyên |
| [412] For each full-data instance below, we keep the evaluated point with the largest slack $\min_i(b_i-F_i(w))$ over all runs. | Không | Giữ nguyên |
| [413] Re-evaluated on matrices rebuilt from the data, each of these points satisfies all three inequalities strictly; the smallest slack is $4.33\times10^{-4}$. | Không | Giữ nguyên |
| [414] This is a numerical check, not an exact certificate of feasibility. | Không | Giữ nguyên |
| [415] We count the iterates of a run, including the last (its evaluated points), at which $F_3(w^k)-b_3>10^{-6}$. | **Có** — B [2] (tối nghĩa, nên sửa) | Ngoặc "(its evaluated points)" khó hiểu, trong khi "evaluated points" được dùng suốt Mục 4.4. Viết: "We call the iterates of a run, including the last one, its evaluated points, and count those at which F_3(w^k)−b_3 > 10⁻⁶." |
| [416] This measures violation along the trajectory, rather than whether the constraint is binding at its limit. | Không | Giữ nguyên |
| [417] Table 6 shows that, from the standard start, $F_3$ is violated at no evaluated point on seven of the eight classification datasets, and at one of the $48$ evaluated points on Abalone. | Không | Giữ nguyên |
| [418] Since $F_3$ is convex (Proposition 4.1), these feature-selection instances test a convex subclass and do not demonstrate a need for the nonconvex extension. | Không | Giữ nguyên |
| [419] We also report the all-convex comparator (AC), which assigns all three constraints to the convex track. | Không | Giữ nguyên |
| [420] Protocol and tuning cost. | Không | Giữ nguyên |
| [421] These are optimization-only tests on full-data feasibility instances. | Không | Giữ nguyên |
| [422] They use $J\le10^{-6}$, at most $1\,000$ evaluated points, and identical starting points across methods. | Không | Giữ nguyên |
| [423] SG-const and SG-dyn are defined in Section 4.2.1. | Không | Giữ nguyên |
| [424] Besides SG-dyn with the sampled modulus $\widehat L$, a tuned variant selects $L=c\widehat L$ from the manually specified grid $c\in\{10^{-3},10^{-2.5},\ldots,10^1\}$ using three random starting points (seeds $1101$--$1103$). | Không | Giữ nguyên |
| [425] Selection first maximizes the number of successful runs, then minimizes total evaluations, then total best residual. | Không | Giữ nguyên |
| [426] Evaluation uses the standard start and three different random starts (seeds $2101$--$2103$). | Không | Giữ nguyên |
| [427] The feature starts are Dirichlet samples. | Không | Giữ nguyên |
| [428] Only starting points are held out: tuning and evaluation use the same full-data instance, and no classification score is used. | Không | Giữ nguyên |
| [429] Neither $\widehat L$ nor the tuned value is a certified global Hölder modulus. | Không | Giữ nguyên |
| [430] [Chú thích bảng] Optimization evaluations from the uniform simplex start. | Không | Giữ nguyên |
| [431] AC denotes the all-convex comparator; sampled and tuned refer to SG-dyn. | Không | Giữ nguyên |
| [432] $\dagger$ means the tolerance was not reached within the budget. | Không | Giữ nguyên |
| [433] The last column gives the DTAP third-constraint violation count divided by its number of evaluated points. | Không | Giữ nguyên |
| [434] Whenever $F_3(w^k)\le b_3$ along a run, the pseudoconvex track is empty, $\mu_k=1$ and DTAP coincides step by step with the all-convex comparator; on the eight instances with zero $F_3$ activity, the identical DTAP and AC columns reflect this identity. | **Có** — E [2] (câu dài/nặng, nên sửa) | 38 từ. Tách: "Whenever F_3(w^k) ≤ b_3 along a run, the pseudoconvex track is empty, μ_k = 1, and DTAP coincides step by step with AC. This explains the identical DTAP and AC columns on the eight instances with zero F_3 activity." |
| [435] On Abalone, $F_3$ is violated only at the uniform start ($1/48$), where $J^{\mathrm{ps}}_0\approx1.56\times10^{-3}$ is negligible against $J^{\mathrm{cvx}}_0\approx366.3$, so $1-\mu_0\approx4.27\times10^{-6}$; the values of $J$ along the two trajectories satisfy $\vert J_{\rm DTAP}-J_{\rm AC}\vert \le3.18\times10^{-5}\,J_{\rm AC}$ at every evaluated point, and both runs stop after $48$ evaluated points. | **Có** — E [2] (câu dài/nặng, nên sửa) | 41 từ. Tách ba câu: "On Abalone, F_3 is violated only at the uniform start (1/48), where J^ps_0 ≈ 1.56×10⁻³ is negligible against J^cvx_0 ≈ 366.3, so 1−μ_0 ≈ 4.27×10⁻⁶. Along the two trajectories, \vert J_DTAP − J_AC\vert  ≤ 3.18×10⁻⁵ J_AC at every evaluated point. Both runs stop after 48 evaluated points." |
| [436] The columns are therefore not a comparison of the two assignments, whose success counts differ only on the random starts ($26/36$ versus $36/36$). | Không | Giữ nguyên |
| [437] Tuning raises SG-dyn's standard-start success count from $5/9$ to $9/9$. | Không | Giữ nguyên |
| [438] It can outperform DTAP, for example on Abalone, and SG-const is faster on Movement Libras. | **Có** — A [2] (mơ hồ, nên sửa) | "It" không rõ là SG-dyn đã tinh chỉnh hay việc tinh chỉnh; "faster" chưa nói theo thước đo nào. Viết: "Tuned SG-dyn can outperform DTAP, for example on Abalone, and SG-const needs fewer evaluations on Movement Libras." |
| [439] Across all four starts on all nine feature instances, the success counts are $26/36$ for DTAP, $36/36$ for the all-convex comparator, $33/36$ for SG-const, $15/36$ for sampled SG-dyn, and $28/36$ for tuned SG-dyn. | Không | Giữ nguyên |
| [440] A balanced DTAP variant also obtains $26/36$; it assigns equal weights when both tracks are violated and full weight to the only violated track otherwise. | Không | Giữ nguyên |
| [441] Thus these tests do not establish a uniform advantage of the proportional weight or robustness to initialization. | Không | Giữ nguyên |
| [442] The nine feature-instance searches required $179\,744$ optimization evaluations and $10.80$ seconds of tuning solver time in total. | Không | Giữ nguyên |
| [443] These costs are additional to Table 6; DTAP was not tuned. | Không | Giữ nguyên |
| [444] Initial modulus sampling, preprocessing and search overhead are excluded from this solver-time total. | Không | Giữ nguyên |
| [445] The supplementary records give the cost of each search separately. | Không | Giữ nguyên |
| [446] A genuinely nonconvex pseudoconvex constraint. | Không | Giữ nguyên |
| [447] To exercise the pseudoconvex track directly, consider $K=[-2,2]^d$ and [công thức (47)] | Không | Giữ nguyên |
| [448] Here $d\in\{2,10,50\}$ and $\kappa\in\{0.3,1,3\}$ give nine configurations. | Không | Giữ nguyên |
| [449] The third function is pseudoconvex: it is an increasing differentiable transform, with positive derivative, of a convex quadratic. | Không | Giữ nguyên |
| [450] It is not convex, since its radial Hessian eigenvalue is $2\kappa(1-r^2)/(1+r^2)^2<0$ for $r=\\vert x-e_1\\vert >1$. | Không | Giữ nguyên |
| [451] The exact witness $x=-e_1/10$ has positive slacks $19/100$, $31/25$, and $\kappa\log(300/221)$. | Không | Giữ nguyên |
| [452] The standard start is $1.5\mathbf1$; the three evaluation starts and three tuning starts are drawn uniformly from $[0.8,1.8]^d$ with the seeds above (NumPy default\_rng). | Không | Giữ nguyên |
| [453] For modulus sampling we use $500$ uniform points in $K$ (seed $42$). | Không | Giữ nguyên |
| [454] SG-const uses the same step $\nu_k=10^{-3}$ as on the feature instances. | Không | Giữ nguyên |
| [455] Tuned SG-const uses a constant step $\nu$ selected from the grid $\{10^{-3},10^{-2.5},\ldots,10^1\}$ with the tuning starts and selection rule of tuned SG-dyn; it selects $\nu=10^{-0.5}$ in all nine configurations. | Không | Giữ nguyên |
| [456] The balanced variant is the one described above. | Không | Giữ nguyên |
| [457] [Chú thích bảng] Nonconvex pseudoconvex tests, grouped by $\kappa$. | Không | Giữ nguyên |
| [458] Each entry is successes out of $12$ runs, followed by the median number of evaluated points in parentheses, including capped runs. | Không | Giữ nguyên |
| [459] Each group contains all three dimensions and four starts. | Không | Giữ nguyên |
| [460] Tuned SG-const uses the step selected as described in the text. | Không | Giữ nguyên |
| [461] DTAP encounters a third-constraint violation in every one of these $36$ runs. | Không | Giữ nguyên |
| [462] Its pooled activity is $12\,835/12\,877$ evaluated points. | Không | Giữ nguyên |
| [463] Nevertheless, it reaches the tolerance in only $24/36$ runs, compared with $32/36$ for sampled SG-dyn, $36/36$ for tuned SG-dyn and $36/36$ for tuned SG-const (Table 7). | Không | Giữ nguyên |
| [464] Tuned SG-const reaches the tolerance in every run with a median of $15$--$16$ evaluated points, fewer than any other method at $\kappa=0.3$ and $\kappa=1$; at $\kappa=3$, DTAP and the balanced variant need a median of $4$. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 36 từ. Tách tại dấu chấm phẩy thành hai câu. |
| [465] These counts exclude the $147\,331$ evaluations of its tuning search. | Không | Giữ nguyên |
| [466] With $\nu_k=10^{-3}$, SG-const moves at most $999\times10^{-3}=0.999$ from its start within the budget, whereas every start lies at distance at least $1.11$ from $\Omega$; its zero counts are therefore fixed by the step size and the budget. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 37 từ; có thể tách tại dấu chấm phẩy: "…from Ω. Its zero counts are therefore fixed by the step size and the budget." |
| [467] For $\kappa\le1$ the convex track is satisfied from the second evaluated point on, so DTAP then follows the single-track iteration of Corollary 3.14; both tracks are violated simultaneously at only $32$ of these $12\,877$ evaluated points. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 36 từ. Tách tại dấu chấm phẩy thành hai câu. |
| [468] All DTAP failures occur at $\kappa=0.3$. | Không | Giữ nguyên |
| [469] Changing $\kappa$ leaves the feasible set unchanged, but $v_3$ and $\nabla F_3$ both scale with $\kappa$, so when $\\vert g^{\mathrm{ps}}_k\\vert \le1$ the pseudoconvex step $(1-\mu_k)\gamma_k g^{\mathrm{ps}}_k$ scales with $\gamma_k\kappa^2$. | Không | Giữ nguyên |
| [470] Table 8 changes one DTAP parameter at a time for $\kappa\in\{0.3,1\}$. | Không | Giữ nguyên |
| [471] With $\gamma_k=a(k+0.5)^{-0.55}$, $a=10$ and $a=100$ give $12/12$ successes at $\kappa=0.3$; $\rho_{\mathrm{cvx}}=1$ gives $4/12$, all with $d=2$; $\delta=10^{-1}$ reproduces the baseline iterates exactly (Remark 4); the faster-decaying steps $s=0.75$ and $s=1$ give no success at $\kappa=0.3$, and $s=1$ also fails in all $12$ runs at $\kappa=1$. | **Có** — E [2] (câu dài/nặng, nên sửa) | 45 từ, bốn kết quả nối bằng dấu chấm phẩy. Tách mỗi kết quả thành một câu, ví dụ: "With γ_k = a(k+0.5)^{-0.55}, a = 10 and a = 100 give 12/12 successes at κ = 0.3. The setting ρ_cvx = 1 gives 4/12, all with d = 2. The setting δ = 10⁻¹ reproduces the baseline iterates exactly (Remark 4). The faster-decaying steps s = 0.75 and s = 1 give no success at κ = 0.3, and s = 1 also fails in all 12 runs at κ = 1." |
| [472] The failures at $\kappa=0.3$ are therefore consistent with a diminishing step that is too small for this constraint scale, rather than with a change in feasibility. | Không | Giữ nguyên |
| [473] These tests vary one parameter at a time on one problem family and do not identify a setting that is best in general. | Không | Giữ nguyên |
| [474] On (47), $\delta=10^{-1}$ and $\delta=10^{-3}$ give identical iterates because the pseudoconvex track has a single index, at every start either only $F_1$ is violated or $v_1-v_2\ge4.79$, and the convex track is satisfied from the second evaluated point on; the $\delta$ row of Table 8 is therefore a consistency check, not evidence about the role of $\delta$. | **Có** — E [2] (câu dài/nặng, nên sửa) | 56 từ, câu dài nhất bài. Tách: "On (47), δ = 10⁻¹ and δ = 10⁻³ give identical iterates. The pseudoconvex track has a single index; at every start, either only F_1 is violated or v_1 − v_2 ≥ 4.79; and the convex track is satisfied from the second evaluated point on. The δ row of Table 8 is therefore a consistency check, not evidence about the role of δ." |
| [475] The synthetic tuning searches consumed $188\,295$ optimization evaluations and $10.98$ seconds of solver time for SG-dyn, and $147\,331$ evaluations and $8.27$ seconds for SG-const, with the same exclusions as above, in the environment stated below. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 35 từ; có thể tách thành hai câu (SG-dyn; SG-const). |
| [476] [Chú thích bảng] DTAP on (47) with one parameter changed at a time, $\gamma_k=a(k+0.5)^{-s}$. | Không | Giữ nguyên |
| [477] The baseline $\rho_{\mathrm{cvx}}=1.98$, $\delta=10^{-3}$, $a=1$, $s=0.55$ is the DTAP column of Table 7. | Không | Giữ nguyên |
| [478] Each entry is successes out of $12$ runs (three dimensions, four starts), followed by the median number of evaluated points in parentheses, including capped runs. | Không | Giữ nguyên |
| [479] Reproducibility. | Không | Giữ nguyên |
| [480] The feature-selection results were saved with Python 3.11.7 and NumPy 1.26.4 on Windows, with one BLAS/OpenMP thread requested. | Không | Giữ nguyên |
| [481] The feature oracles use algebraically compressed quadratic forms; checked differences from the original values and gradients are at most $1.82\times10^{-12}$ and $1.10\times10^{-11}$, respectively. | Không | Giữ nguyên |
| [482] The solver times reported for the feature instances refer to this compressed implementation. | Không | Giữ nguyên |
| [483] The accompanying package contains only the uncompressed oracles; it reproduces the evaluation counts, while the reported solver times are those of the original compressed implementation. | Không | Giữ nguyên |
| [484] Tables 7 and 8 and the synthetic tuning costs were produced with Python 3.13.4 and NumPy 2.1.3 on Windows with the default number of BLAS threads; their counts are deterministic, and their solver times are single measurements on that machine. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 40 từ; có thể tách tại dấu chấm phẩy. |
| [485] With Python 3.13.4 and NumPy 2.1.3, the package also reproduces exactly every numerical entry of Tables 1--5 (Tables 4 and 5 from unrounded scores) and of Table 6, and the counts quoted in Sections 4.3 and 4.4. | **Có** — E [3] (câu dài/nặng, tùy chọn) | 37 từ; chấp nhận được trong đoạn tái lập, có thể giữ. |
| [486] The supplementary scripts, raw trajectories, tuning records, witnesses, source hashes and validation instructions accompany the results. | Không | Giữ nguyên |

### Conclusion

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [488] DTAP solves normal-box nonlinear split feasibility problems with convex and pseudoconvex components by combining a residual-scaled convex step with a safeguarded pseudoconvex step. | Không | Giữ nguyên |
| [489] Under consistency and continuous differentiability, the whole sequence converges to a feasible point; no regularity modulus is an input, although the analysis uses bounds on a compact set containing the iterates. | Không | Giữ nguyên |
| [490] In the feature-selection application all constraints are convex, and test problems with a nonconvex pseudoconvex constraint exercise the pseudoconvex track. | Không | Giữ nguyên |
| [491] In the experiments, tuned subgradient methods can match or outperform DTAP, whose finite-budget performance depends on the starting point and the step scale. | Không | Giữ nguyên |
| [492] Rates for the full residual $J(x^k)$, beyond the convex-track bound of Remark 5, and guarantees under error-bound conditions remain open. | Không | Giữ nguyên |

### Declaration of competing interest

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [494] The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. | Không | Giữ nguyên |

### Funding

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [496] The authors received no specific funding for this work. | Không | Giữ nguyên |

### Declaration of generative AI use

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [498] OpenAI Codex was used during revision for language editing. | Không | Giữ nguyên |

### Data availability

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [500] The datasets are available from the UCI Machine Learning Repository [8]. | Không | Giữ nguyên |
| [501] The accompanying reproducibility package contains the scripts, recorded numerical outputs, and instructions for regenerating the reported tables. | Không | Giữ nguyên |

### ORCID

| Câu | Có lỗi không? | Không cần sửa / Cách sửa |
|---|---|---|
| [503] Nguyen Van The \raisebox{-0.1ex}{\textit{https://orcid.org/0009-0004-6548-420X}}  Tran Ngoc Thang \raisebox{-0.1ex}{\textit{https://orcid.org/0009-0000-9549-5736}}  Nguyen Hong Son \raisebox{-0.1ex}{\textit{https://orcid.org/0009-0006-3106-8296}} | Không | Giữ nguyên |
