# Đối chiếu trước và sau chỉnh sửa: `DTAP Finally` → `DTAP Finally v2`

- **Trước** = `DTAP Finally/main_document.tex` (bản DTAP_OMS.pdf cũ).
- **Sau** = `DTAP Finally v2/main_document.tex` (bản v2).
- Danh sách lấy tự động từ phép so sánh từng câu giữa hai file; mọi câu khác nhau đều có mặt dưới đây (68 chỗ khác nhau, gom thành 58 mục).
- Không liệt kê chi tiết các thay đổi **chỉ về ký hiệu**; chúng được ghi gọn ở **Phụ lục** cuối file.
- Số mục, số công thức, số tài liệu tham khảo ghi theo bản PDF tương ứng (hai bản có cùng cách đánh số).
- Công thức hiển thị không đổi được ghi tắt là "(số công thức)".
- Mỗi câu tiếng Anh có bản dịch tiếng Việt ngay bên dưới (dòng bắt đầu bằng →).

---

## A. Tóm tắt và từ khóa

### 1. Abstract — viết lại toàn bộ

**Trước**
1. We study a nonlinear split feasibility problem with a normal-box output set and differentiable convex and pseudoconvex component functions.
   → Ta nghiên cứu một bài toán chấp nhận tách phi tuyến có tập đầu ra là hộp chuẩn và các hàm thành phần khả vi, lồi và giả lồi.
2. A max-type violation measure identifies nearly active constraints in two blocks.
   → Một độ đo vi phạm kiểu max xác định các ràng buộc gần hoạt động trong hai khối.
3. The Dual-Track Adaptive Projection (DTAP) algorithm combines a residual-scaled step for the convex block with a safeguarded diminishing step for the pseudoconvex block, followed by projection onto the base convex set.
   → Thuật toán Chiếu Thích nghi Hai Track (DTAP) kết hợp một bước co theo phần dư cho khối lồi với một bước giảm dần có chặn an toàn cho khối giả lồi, rồi chiếu lên tập lồi cơ sở.
4. Its step sizes require no prescribed operator norm, Lipschitz constant, or Hölder modulus.
   → Độ dài bước của nó không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder.
5. Under consistency and continuous differentiability, we prove convergence of the whole sequence to a feasible point in finite-dimensional Euclidean space.
   → Dưới giả thiết nhất quán và khả vi liên tục, ta chứng minh toàn bộ dãy hội tụ tới một điểm khả thi trong không gian Euclid hữu hạn chiều.
6. The proof uses local bounds on the bounded iterate region.
   → Chứng minh dùng các cận địa phương trên miền bị chặn chứa dãy lặp.
7. The proportional mixing weight is a residual-responsive choice, without a claim of optimality.
   → Trọng số pha trộn tỉ lệ là một lựa chọn phản ứng theo phần dư, không khẳng định là tối ưu.
8. A feature-selection formulation combines criteria from fractional and fuzzy-rough models and belongs to the convex subclass.
   → Một mô hình chọn đặc trưng kết hợp các tiêu chí từ mô hình phân thức và mô hình tập thô mờ, và thuộc lớp con lồi.
9. Experiments report constraint activity, classification comparisons, and subgradient comparisons with empirically tuned moduli.
   → Các thực nghiệm báo cáo mức hoạt động của ràng buộc, các so sánh phân loại, và các so sánh với phương pháp dưới gradient có mô-đun được tinh chỉnh thực nghiệm.
10. Controlled examples with a nonconvex pseudoconvex constraint test the pseudoconvex track.
    → Các ví dụ có kiểm soát với một ràng buộc giả lồi không lồi kiểm tra track giả lồi.
11. On these examples, DTAP is sensitive to the scale of its diminishing step.
    → Trên các ví dụ này, DTAP nhạy với thang của bước giảm dần.
12. The results also show initialization sensitivity and do not establish uniform computational superiority.
    → Kết quả cũng cho thấy sự nhạy với điểm khởi đầu và không chứng tỏ được ưu thế tính toán đồng đều.

**Sau**
1. We study a nonlinear split feasibility problem in $\mathbb{R}^n$ whose output set is a normal box and whose components are differentiable and either convex or pseudoconvex.
   → Ta nghiên cứu một bài toán chấp nhận tách phi tuyến trong $\mathbb{R}^n$, có tập đầu ra là hộp chuẩn và các thành phần khả vi, mỗi thành phần lồi hoặc giả lồi.
2. The Dual-Track Adaptive Projection (DTAP) algorithm splits the constraints into a convex and a pseudoconvex track.
   → Thuật toán Chiếu Thích nghi Hai Track (DTAP) chia các ràng buộc thành một track lồi và một track giả lồi.
3. It takes a residual-scaled Polyak-type step on the nearly most violated convex constraints and a safeguarded diminishing step on the nearly most violated pseudoconvex ones, combines the two steps by a proportional weight, and projects onto the base set.
   → Thuật toán lấy một bước kiểu Polyak co theo phần dư trên các ràng buộc lồi gần bị vi phạm nhiều nhất và một bước giảm dần có chặn an toàn trên các ràng buộc giả lồi gần bị vi phạm nhiều nhất, kết hợp hai bước bằng một trọng số tỉ lệ, rồi chiếu lên tập cơ sở.
4. The weight is a residual-responsive choice, without a claim of optimality.
   → Trọng số này là một lựa chọn phản ứng theo phần dư, không khẳng định là tối ưu.
5. The step sizes require no prescribed operator norm, Lipschitz constant, or Hölder modulus; the proof uses bounds over a bounded set containing the iterates.
   → Độ dài bước không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder; chứng minh dùng các cận trên một tập bị chặn chứa dãy lặp.
6. If the problem is consistent and the components are continuously differentiable, the whole sequence converges to a feasible point.
   → Nếu bài toán nhất quán và các thành phần khả vi liên tục thì toàn bộ dãy hội tụ tới một điểm khả thi.
7. In a feature-selection application all three constraints are convex.
   → Trong một ứng dụng chọn đặc trưng, cả ba ràng buộc đều lồi.
8. Experiments with constraint-activity counts, tuned subgradient methods and nonconvex pseudoconvex test problems show that tuned subgradient methods can match or outperform DTAP, and that DTAP is sensitive to its starting point and step scale.
   → Các thực nghiệm (đếm mức hoạt động của ràng buộc, so với các phương pháp dưới gradient đã tinh chỉnh, và thử trên bài toán có ràng buộc giả lồi không lồi) cho thấy các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, và DTAP nhạy với điểm xuất phát và thang bước.

### 2. Từ khóa

- **Trước:** Strong convergence → *Hội tụ mạnh*
- **Sau:** Global convergence → *Hội tụ toàn cục*

---

## B. Mục 1. Introduction

### 3. Đoạn mở đầu (SFP, thuật toán CQ, các hướng mở rộng)

**Trước**
1. The split feasibility problem (SFP) models constrained reconstruction [4].
   → Bài toán chấp nhận tách (SFP) mô hình hóa bài toán tái tạo có ràng buộc [4].
2. For closed convex sets $C\subseteq\mathbb{R}^n$, $Q\subseteq\mathbb{R}^m$, and a matrix $\mathcal A$, it seeks (1).
   → Với các tập lồi đóng $C\subseteq\mathbb{R}^n$, $Q\subseteq\mathbb{R}^m$ và một ma trận $\mathcal A$, bài toán tìm (1).
3. Byrne's $CQ$ algorithm [3] uses (2).
   → Thuật toán $CQ$ của Byrne [3] dùng (2).
4. Supporting half-spaces simplify projections [17], while self-adaptive steps reduce parameter dependence [20, 22, 10].
   → Nửa không gian tựa làm đơn giản phép chiếu [17], còn bước tự thích nghi làm giảm sự phụ thuộc vào tham số [20, 22, 10].
5. Operator splitting [21] and modified alternating directions [18] provide decomposition strategies.
   → Tách toán tử [21] và hướng luân phiên cải biên [18] cung cấp các chiến lược phân rã.
6. Adaptive steps and decomposition are therefore established principles.
   → Do đó, bước thích nghi và phân rã là những nguyên lý đã được xác lập.

**Sau**
1. The split feasibility problem (SFP) was introduced by Censor and Elfving [4] as a model for constrained inverse problems.
   → Bài toán chấp nhận tách (SFP) được Censor và Elfving [4] đưa ra như một mô hình cho các bài toán ngược có ràng buộc.
2. Given nonempty closed convex sets $C\subseteq\mathbb{R}^n$ and $Q\subseteq\mathbb{R}^m$ and a matrix $\mathcal A\in\mathbb{R}^{m\times n}$, it asks to (1).
   → Cho các tập lồi đóng khác rỗng $C\subseteq\mathbb{R}^n$, $Q\subseteq\mathbb{R}^m$ và một ma trận $\mathcal A\in\mathbb{R}^{m\times n}$, bài toán yêu cầu (1).
3. Byrne's $CQ$ algorithm [3] iterates (2).
   → Thuật toán $CQ$ của Byrne [3] lặp theo (2).
4. Here $\|\mathcal A\|$ is the spectral norm of $\mathcal A$.
   → Ở đây $\|\mathcal A\|$ là chuẩn phổ của $\mathcal A$.
5. Relaxed variants project onto supporting half-spaces [17]; self-adaptive steps avoid estimating $\|\mathcal A\|$ [20, 22, 10]; operator splitting [21] and alternating direction methods [18] decompose the problem.
   → Các biến thể nới lỏng chiếu lên nửa không gian tựa [17]; bước tự thích nghi tránh phải ước lượng $\|\mathcal A\|$ [20, 22, 10]; tách toán tử [21] và phương pháp hướng luân phiên [18] phân rã bài toán.
6. These ideas are standard; DTAP adapts them to the nonlinear case.
   → Các ý tưởng này đã là chuẩn mực; DTAP vận dụng chúng cho trường hợp phi tuyến.

### 4. Bài toán SFP phi tuyến và tập khả thi

**Trước**
1. We study the nonlinear SFP (3), where $K\subseteq\mathbb{R}^n$ is closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$, and each differentiable component of $F=(F_1,\ldots,F_m)$ is convex or pseudoconvex on $K$.
   → Ta nghiên cứu SFP phi tuyến (3), trong đó $K\subseteq\mathbb{R}^n$ đóng và lồi, $Q=\prod_{i=1}^m(-\infty,b_i]$, và mỗi thành phần khả vi của $F=(F_1,\ldots,F_m)$ là lồi hoặc giả lồi trên $K$.
2. Pseudoconvex functions have convex sublevel sets, so the feasible set is convex even when some components are nonconvex.
   → Hàm giả lồi có các tập mức dưới lồi, nên tập khả thi là lồi ngay cả khi một số thành phần không lồi.
3. We seek feasibility, rather than minimization of every component.
   → Ta tìm tính khả thi, chứ không cực tiểu hóa mọi thành phần.

**Sau**
1. Replacing $\mathcal A$ by a nonlinear map $F$ gives the nonlinear SFP [9, 19] (3), where $K\subseteq\mathbb{R}^n$ is nonempty, closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$ is a normal box, and each $F_i$ is differentiable and convex or pseudoconvex on $K$.
   → Thay $\mathcal A$ bằng một ánh xạ phi tuyến $F$ ta được SFP phi tuyến [9, 19] (3), trong đó $K\subseteq\mathbb{R}^n$ khác rỗng, đóng và lồi, $Q=\prod_{i=1}^m(-\infty,b_i]$ là hộp chuẩn, và mỗi $F_i$ khả vi và lồi hoặc giả lồi trên $K$.
2. Since pseudoconvex functions have convex sublevel sets, the feasible set $\Omega=\{x\in K:F(x)\in Q\}$ is convex.
   → Vì hàm giả lồi có các tập mức dưới lồi, tập khả thi $\Omega=\{x\in K:F(x)\in Q\}$ là lồi.
3. We seek a point of $\Omega$, not a minimizer of any $F_i$.
   → Ta tìm một điểm thuộc $\Omega$, không tìm điểm cực tiểu của $F_i$ nào.

### 5. Các công trình liên quan (Li, Yen, Hu)

**Trước**
1. Nonlinear SFP and generalized convex feasibility have several relevant antecedents.
   → SFP phi tuyến và bài toán chấp nhận lồi suy rộng có một số công trình đi trước liên quan.
2. Li et al. [9] use a convex aggregate proximity function, a property not ensured by componentwise pseudoconvexity.
   → Li và cộng sự [9] dùng một hàm lân cận tổng hợp lồi, một tính chất mà tính giả lồi của từng thành phần không bảo đảm.
3. Yen et al. [19] combine equilibrium and nonlinear image constraints.
   → Yen và cộng sự [19] kết hợp ràng buộc cân bằng và ràng buộc ảnh phi tuyến.
4. Hu et al. [7] treat quasiconvex inequalities, which include our component class.
   → Hu và cộng sự [7] xét các bất đẳng thức tựa lồi, bao gồm lớp thành phần của ta.
5. Our method exploits the additional derivative information of convex components within this established feasibility setting.
   → Phương pháp của ta khai thác thông tin đạo hàm bổ sung của các thành phần lồi trong khung bài toán chấp nhận đã được xác lập này.

**Sau**
1. Li et al. [9] assume a convex aggregate proximity function, which componentwise pseudoconvexity does not ensure.
   → Li và cộng sự [9] giả thiết hàm lân cận tổng hợp lồi, điều mà tính giả lồi của từng thành phần không bảo đảm.
2. Yen et al. [19] use the same max-type violation measure and active-set device, but require quasilinear components, a class incomparable with ours.
   → Yen và cộng sự [19] dùng cùng độ đo vi phạm kiểu max và cùng kỹ thuật tập hoạt động, nhưng đòi các thành phần tựa tuyến tính, một lớp không so sánh được với lớp của ta.
3. Hu et al. [7] treat quasiconvex inequalities, which contain our class, without using the gradient inequality of convex components.
   → Hu và cộng sự [7] xét bất đẳng thức tựa lồi, một lớp chứa lớp của ta, nhưng không dùng bất đẳng thức gradient của các thành phần lồi.

### 6. Câu dẫn tới độ đo vi phạm $J$

- **Trước:** The box gives the explicit violation measure $J(x)=d_\infty(F(x),Q)=\max_{1\le i\le m}(F_i(x)-b_i)^+$.
  → Hộp cho ta độ đo vi phạm tường minh $J(x)=\ldots$
- **Sau:** Because $Q$ is a box, the $\ell_\infty$-distance from $F(x)$ to $Q$ has the closed form $J(x)=d_\infty(F(x),Q)=\max_{1\le i\le m}(F_i(x)-b_i)^+$.
  → Vì $Q$ là một hộp, khoảng cách $\ell_\infty$ từ $F(x)$ tới $Q$ có dạng tường minh $J(x)=\ldots$

### 7. Đoạn mô tả DTAP

**Trước**
1. The Dual-Track Adaptive Projection algorithm (DTAP) forms violation-weighted gradient sums from nearly maximal violations in each block.
   → Thuật toán Chiếu Thích nghi Hai Track (DTAP) lập các tổng gradient có trọng số theo độ vi phạm, từ các độ vi phạm gần lớn nhất trong mỗi khối.
2. Convex gradient inequalities justify a residual-scaled Polyak-type step [14, 10], whereas pseudoconvexity supports a safeguarded diminishing step.
   → Các bất đẳng thức gradient lồi biện minh cho một bước kiểu Polyak co theo phần dư [14, 10], còn tính giả lồi hỗ trợ một bước giảm dần có chặn an toàn.
3. A weighted combination is projected onto $K$.
   → Một tổ hợp có trọng số được chiếu lên $K$.
4. The proportional weight responds to block violations and is not claimed to be unique or optimal.
   → Trọng số tỉ lệ phản ứng theo độ vi phạm của từng khối và không được khẳng định là duy nhất hay tối ưu.
5. Its role in preventing neglect is used in the convergence proof.
   → Vai trò ngăn sự bỏ sót của nó được dùng trong chứng minh hội tụ.
6. A one-step bound valid for all weights in $[0,1]$ does not by itself establish convergence for every weight sequence.
   → Một cận một bước đúng với mọi trọng số trong $[0,1]$ tự nó không chứng minh được hội tụ với mọi dãy trọng số.
7. No prescribed operator norm, Lipschitz constant, or Hölder modulus is required, although the proof uses continuity and local bounds on the bounded iterate region.
   → Không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder, mặc dù chứng minh dùng tính liên tục và các cận địa phương trên miền bị chặn chứa dãy lặp.
8. The analysis uses a quasi-Fejér estimate to establish boundedness before invoking these local bounds.
   → Phân tích dùng một ước lượng tựa Fejér để chứng minh tính bị chặn trước khi dùng các cận địa phương này.
9. Continuous gradients need not be Lipschitz.
   → Gradient liên tục không nhất thiết Lipschitz.

**Sau**
1. DTAP splits the constraints into a convex track and a pseudoconvex track.
   → DTAP chia các ràng buộc thành một track lồi và một track giả lồi.
2. On each track it sums the gradients of the nearly most violated constraints, weighted by their violations.
   → Trên mỗi track, nó cộng các gradient của những ràng buộc gần bị vi phạm nhiều nhất, có trọng số theo độ vi phạm.
3. The gradient inequality of convex functions justifies a residual-scaled Polyak-type step on the convex track [14, 10]; pseudoconvexity gives only the sign of a directional derivative, so the pseudoconvex track uses a safeguarded diminishing step.
   → Bất đẳng thức gradient của hàm lồi biện minh cho một bước kiểu Polyak co theo phần dư trên track lồi [14, 10]; tính giả lồi chỉ cho biết dấu của đạo hàm theo hướng, nên track giả lồi dùng một bước giảm dần có chặn an toàn.
4. A proportional weight combines the two steps, and the result is projected onto $K$; the proof uses this weight only to keep a persistently violated track active (Remark 1).
   → Một trọng số tỉ lệ kết hợp hai bước, rồi kết quả được chiếu lên $K$; chứng minh chỉ dùng trọng số này để giữ cho một track bị vi phạm kéo dài vẫn có trọng số dương (Nhận xét 1).
5. No prescribed operator norm, Lipschitz constant, or Hölder modulus is needed: a quasi-Fejér inequality shows that the iterates are bounded, and the proof then uses local bounds, without Lipschitz gradients.
   → Không cần biết trước chuẩn toán tử, hằng số Lipschitz hay mô-đun Hölder: một bất đẳng thức tựa Fejér cho thấy dãy lặp bị chặn, sau đó chứng minh dùng các cận địa phương, không cần gradient Lipschitz.

### 8. Đoạn về ứng dụng chọn đặc trưng

**Trước**
1. Feature-selection criteria from fractional and fuzzy-rough models [15, 16] define separate threshold constraints.
   → Các tiêu chí chọn đặc trưng từ mô hình phân thức và mô hình tập thô mờ [15, 16] xác định các ràng buộc ngưỡng riêng rẽ.
2. This construction expresses simultaneous acceptance, not equivalence to the source optimization models.
   → Cách xây dựng này biểu diễn sự chấp nhận đồng thời, không tương đương với các mô hình tối ưu gốc.
3. The positive-semidefinite quadratic-over-positive-affine criterion is convex, so this application belongs to the convex subclass.
   → Tiêu chí dạng toàn phương nửa xác định dương chia cho hàm affine dương là lồi, nên ứng dụng này thuộc lớp con lồi.
4. Controlled examples with a nonconvex pseudoconvex constraint test the pseudoconvex track.
   → Các ví dụ có kiểm soát với một ràng buộc giả lồi không lồi kiểm tra track giả lồi.
5. Classification scores feature selections that are computed once and then reused, on the same holdout split that was fixed when they were computed, and tuned subgradient methods can match or outperform DTAP.
   → Phân loại chấm điểm các tập đặc trưng được tính một lần rồi dùng lại, trên cùng phép chia giữ lại đã cố định khi tính chúng, và các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP.

**Sau**
1. As an application, upper bounds on three criteria from a fractional model [15] and a fuzzy-rough model [16] define the constraints; a feasible weight vector satisfies all three bounds but need not solve either source problem.
   → Làm ứng dụng, các cận trên của ba tiêu chí lấy từ một mô hình phân thức [15] và một mô hình tập thô mờ [16] tạo thành các ràng buộc; một vector trọng số khả thi thỏa cả ba cận nhưng không nhất thiết là nghiệm của bài toán gốc nào.
2. These constraints are convex (Proposition 4.1), so we also use test problems with a nonconvex pseudoconvex constraint to exercise the pseudoconvex track.
   → Các ràng buộc này lồi (Mệnh đề 4.1), nên ta còn dùng các bài toán thử có ràng buộc giả lồi không lồi để kiểm tra track giả lồi.

### 9. Các đóng góp C1–C3

**Trước**
1. C1. A dual-track method combines convex decrease estimates and pseudoconvex sign information through an adaptive weight.
   → C1. Một phương pháp hai track kết hợp các ước lượng giảm của phần lồi và thông tin dấu của phần giả lồi qua một trọng số thích nghi.
2. C2. Under consistency, smoothness, and the stated step conditions, the whole sequence converges to a feasible point in finite-dimensional Euclidean space.
   → C2. Dưới giả thiết nhất quán, trơn và các điều kiện bước đã nêu, toàn bộ dãy hội tụ tới một điểm khả thi trong không gian Euclid hữu hạn chiều.
3. Convergence of distances and one feasible cluster point suffice.
   → Sự hội tụ của các khoảng cách và một điểm tụ khả thi là đủ.
4. C3. Experiments distinguish prediction from feasibility cost and report constraint activity, tuned subgradient comparisons, and initialization and scaling sensitivity.
   → C3. Các thực nghiệm phân biệt hiệu quả dự đoán với chi phí tìm điểm khả thi, và báo cáo mức hoạt động của ràng buộc, các so sánh với phương pháp dưới gradient đã tinh chỉnh, cùng độ nhạy với khởi đầu và thang bước.
5. They do not establish uniform superiority.
   → Chúng không chứng tỏ được ưu thế đồng đều.

**Sau**
1. C1. A dual-track method that uses the gradient inequality on the convex constraints and only sign information on the pseudoconvex ones, without assuming a convex proximity function, unlike [9], or a Hölder modulus, unlike the dynamic step of [7].
   → C1. Một phương pháp hai track dùng bất đẳng thức gradient trên các ràng buộc lồi và chỉ thông tin về dấu trên các ràng buộc giả lồi, không cần giả thiết hàm lân cận lồi như [9], cũng không cần mô-đun Hölder như bước động của [7].
2. C2. Convergence of the whole sequence to a feasible point under Assumption 1 (Theorem 3.12).
   → C2. Sự hội tụ của toàn bộ dãy tới một điểm khả thi dưới Giả thiết 1 (Định lý 3.12).
3. C3. Experiments that report constraint activity, compare DTAP with tuned subgradient methods, and measure its sensitivity to the starting point and the step scale.
   → C3. Các thực nghiệm báo cáo mức hoạt động của ràng buộc, so sánh DTAP với các phương pháp dưới gradient đã tinh chỉnh, và đo độ nhạy của DTAP với điểm xuất phát và thang bước.

---

## C. Mục 2. Preliminaries

### 10. Câu mở đầu

- **Trước:** Throughout, $H=\mathbb{R}^n$ is Euclidean space with inner product $\langle\cdot,\cdot\rangle$ and induced norm $\|\cdot\|$.
  → Trong toàn bài, $H=\mathbb{R}^n$ là không gian Euclid với tích vô hướng $\langle\cdot,\cdot\rangle$ và chuẩn cảm sinh $\|\cdot\|$.
- **Sau:** Throughout, $H=\mathbb{R}^n$ is the Euclidean space with inner product $\langle\cdot,\cdot\rangle$ and induced norm $\|\cdot\|$.
  → (như trên; chỉ thêm mạo từ "the")

### 11. Sau Mệnh đề 2.1

**Trước**
1. This characterization gives the projection inequality used in Lemma 3.2.
   → Đặc trưng này cho bất đẳng thức chiếu được dùng trong Bổ đề 3.2.
2. The sort-based projection onto a $p$-dimensional simplex takes $O(p\log p)$ operations [6].
   → Phép chiếu dựa trên sắp xếp lên một đơn hình $p$ chiều tốn $O(p\log p)$ phép toán [6].

**Sau**
1. This characterization yields Lemma 3.2 below.
   → Đặc trưng này cho ta Bổ đề 3.2 dưới đây.

*(Câu 2 cũ được chuyển xuống Nhận xét 6, xem mục 40.)*

### 12. Định nghĩa 2.2 (giả lồi)

- **Trước:** A function differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for every $x,y\in K$, (5).
  → Một hàm khả vi trên một lân cận mở của $K$ là giả lồi trên $K$ nếu, với mọi $x,y\in K$, (5).
- **Sau:** A function $f$ that is differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for all $x,y\in K$, (5).
  → Một hàm $f$ khả vi trên một lân cận mở của $K$ là giả lồi trên $K$ nếu, với mọi $x,y\in K$, (5).

### 13. Câu bị xóa cuối Mục 2

- **Trước:** This distinction is relevant to the mixed constraint functions studied below.
  → Sự phân biệt này có liên quan tới các hàm ràng buộc hỗn hợp được nghiên cứu dưới đây.
- **Sau:** *(xóa)*

---

## D. Mục 3. Thuật toán DTAP và sự hội tụ

### 14. Sau công thức (8)

- **Trước:** Then $F(x)\in Q$ iff $J(x)=0$, so finding a feasible point amounts to minimizing $J$ over $K$.
  → Khi đó $F(x)\in Q$ khi và chỉ khi $J(x)=0$, nên tìm một điểm khả thi quy về cực tiểu hóa $J$ trên $K$.
- **Sau:** Then $x\in K$ is feasible if and only if $J(x)=0$; when $\Omega\ne\emptyset$, the feasible points are the minimizers of $J$ over $K$.
  → Khi đó $x\in K$ khả thi khi và chỉ khi $J(x)=0$; khi $\Omega\ne\emptyset$, các điểm khả thi chính là các điểm cực tiểu của $J$ trên $K$.

### 15. Tiêu đề và câu đầu Mục 3.2

- **Trước:** [Tiêu đề] 3.2. Decomposition and dual-track scalarization. — We split the constraint index set into a *convex track* and a *pseudoconvex track*.
  → [Tiêu đề] 3.2. Phân rã và vô hướng hóa hai track. — Ta chia tập chỉ số ràng buộc thành một *track lồi* và một *track giả lồi*.
- **Sau:** [Tiêu đề] 3.2. Decomposition into two tracks. — We split $I:=\{1,\dots,m\}$ into a *convex track* $I^{\rm cvx}$ and a *pseudoconvex track* $I^{\rm ps}$, each with its own step rule.
  → [Tiêu đề] 3.2. Phân rã thành hai track. — Ta chia $I:=\{1,\dots,m\}$ thành *track lồi* $I^{\rm cvx}$ và *track giả lồi* $I^{\rm ps}$, mỗi track có quy tắc bước riêng.

### 16. Công thức (9) và câu về phép chia

**Trước**
1. For $x\in U$ define the componentwise violations and the maximal violation $v_i(x):=(F_i(x)-b_i)^+,\ J(x)=\max_{1\le i\le m}v_i(x)$. (9)
   → Với $x\in U$, định nghĩa độ vi phạm từng thành phần và độ vi phạm lớn nhất $v_i(x):=\ldots,\ J(x)=\ldots$ (9)
2. Thus $x\in\Omega$ iff $x\in K$ and $J(x)=0$.
   → Như vậy $x\in\Omega$ khi và chỉ khi $x\in K$ và $J(x)=0$.
3. Partition $I:=\{1,\dots,m\}$ into disjoint groups $I=I^{\rm cvx}\cup I^{\rm ps}$, where $I^{\rm cvx}$ indexes the convex constraints and $I^{\rm ps}$ the pseudoconvex ones (made precise in Assumption 1).
   → Chia $I:=\{1,\dots,m\}$ thành các nhóm rời nhau $I=I^{\rm cvx}\cup I^{\rm ps}$, trong đó $I^{\rm cvx}$ đánh chỉ số các ràng buộc lồi và $I^{\rm ps}$ các ràng buộc giả lồi (được phát biểu chính xác trong Giả thiết 1).

**Sau**
1. For $x\in U$ define the componentwise violations $v_i(x):=(F_i(x)-b_i)^+$, (9) so that $J(x)=\max_i v_i(x)$ by (8).
   → Với $x\in U$, định nghĩa độ vi phạm từng thành phần $v_i(x):=(F_i(x)-b_i)^+$, (9) nên $J(x)=\max_i v_i(x)$ theo (8).
2. Assumption 1 makes the partition precise.
   → Giả thiết 1 phát biểu chính xác phép chia này.

### 17. Tập hoạt động xấp xỉ

- **Trước:** To cope with the nonsmoothness of the maximum, we replace the exact maximizers by a $\delta$-enlarged *approximate active set* on each track:
  → Để xử lý tính không trơn của hàm max, ta thay các chỉ số đạt max chính xác bằng một *tập hoạt động xấp xỉ* được nới rộng $\delta$ trên mỗi track:
- **Sau:** To cope with the nonsmoothness of the maximum, we replace the set of indices at which the maximum is attained by a $\delta$-enlarged *approximate active set* on each track ('active' meaning within $\delta$ of the largest violation):
  → Để xử lý tính không trơn của hàm max, ta thay tập các chỉ số tại đó đạt giá trị lớn nhất bằng một *tập hoạt động xấp xỉ* được nới rộng $\delta$ trên mỗi track ("hoạt động" nghĩa là cách độ vi phạm lớn nhất không quá $\delta$):

### 18. Giả thiết 1, (A1)

**Trước**
1. (A1) (a) $\Omega\ne\emptyset$.
   → (A1) (a) $\Omega\ne\emptyset$.
2. (b) $I=\{1,\dots,m\}$ is partitioned as $I=I^{\rm cvx}\cup I^{\rm ps}$; for each $i$, $F_i:U\to\mathbb{R}$, and the restriction $F_i|_K$ is convex if $i\in I^{\rm cvx}$ and pseudoconvex if $i\in I^{\rm ps}$.
   → (b) $I$ được chia thành $I=I^{\rm cvx}\cup I^{\rm ps}$; với mỗi $i$, $F_i:U\to\mathbb{R}$, và thu hẹp $F_i|_K$ là lồi nếu $i\in I^{\rm cvx}$ và giả lồi nếu $i\in I^{\rm ps}$.

**Sau**
1. (A1) (a) $\Omega\ne\emptyset$ (consistency).
   → (A1) (a) $\Omega\ne\emptyset$ (tính nhất quán).
2. (b) $I=\{1,\dots,m\}$ is partitioned as $I=I^{\rm cvx}\cup I^{\rm ps}$; each $F_i:U\to\mathbb{R}$ is convex on $K$ if $i\in I^{\rm cvx}$ and pseudoconvex on $K$ if $i\in I^{\rm ps}$.
   → (b) $I$ được chia thành $I=I^{\rm cvx}\cup I^{\rm ps}$; mỗi $F_i:U\to\mathbb{R}$ là lồi trên $K$ nếu $i\in I^{\rm cvx}$ và giả lồi trên $K$ nếu $i\in I^{\rm ps}$.

### 19. Tên trọng số $\mu_k$ (Mục 3.4 và bước (1e))

- **Trước:** The Dual-Track Adaptive Projection algorithm combines the two track-specific step sizes through the soft weight $\mu_k$ and projects the combined update onto the base convex set $K$. — (1e) Soft proportional weight:
  → Thuật toán DTAP kết hợp hai độ dài bước riêng của từng track qua trọng số mềm $\mu_k$ và chiếu bước cập nhật kết hợp lên tập lồi cơ sở $K$. — (1e) Trọng số tỉ lệ mềm:
- **Sau:** The Dual-Track Adaptive Projection algorithm combines the two track-specific step sizes through the proportional weight $\mu_k$ and projects the combined update onto the base convex set $K$. — (1e) Proportional weight:
  → Thuật toán DTAP kết hợp hai độ dài bước riêng của từng track qua trọng số tỉ lệ $\mu_k$ và chiếu bước cập nhật kết hợp lên tập lồi cơ sở $K$. — (1e) Trọng số tỉ lệ:

### 20. Thuật toán 1: kiểm tra dừng

**Trước**
1. **Step 1 (per-track quantities).** (1a) Compute …
   → **Bước 1 (các đại lượng theo track).** (1a) Tính …
2. **Step 2 (projection).** $x^{k+1}=P_K(y^k)$.
   → **Bước 2 (chiếu).** $x^{k+1}=P_K(y^k)$.
3. **Step 3 (stopping).** If $J(x^k)\le\varepsilon$, stop and return $x^k$; otherwise set $k\leftarrow k+1$ and go to Step 1.
   → **Bước 3 (dừng).** Nếu $J(x^k)\le\varepsilon$ thì dừng và trả về $x^k$; ngược lại đặt $k\leftarrow k+1$ và quay lại Bước 1.

**Sau**
1. **Step 1 (per-track quantities).** If $J(x^k)\le\varepsilon$, stop and return $x^k$; otherwise: (1a) Compute …
   → **Bước 1 (các đại lượng theo track).** Nếu $J(x^k)\le\varepsilon$ thì dừng và trả về $x^k$; ngược lại: (1a) Tính …
2. **Step 2 (projection).** $x^{k+1}=P_K(y^k)$; set $k\leftarrow k+1$ and go to Step 1.
   → **Bước 2 (chiếu).** $x^{k+1}=P_K(y^k)$; đặt $k\leftarrow k+1$ và quay lại Bước 1.

### 21. Nhận xét 1

**Trước**
1. The proportional weight is an adaptive allocation based on the two maximal violations; we do not claim that it is the only convergent choice or that it is optimal.
   → Trọng số tỉ lệ là một cách phân bổ thích nghi dựa trên hai độ vi phạm lớn nhất; ta không khẳng định đó là lựa chọn hội tụ duy nhất hay là tối ưu.
2. Although the one-step inequality holds for any $\mu_k\in[0,1]$, this alone does not establish convergence for every such sequence.
   → Mặc dù bất đẳng thức một bước đúng với mọi $\mu_k\in[0,1]$, riêng điều đó không chứng minh được hội tụ với mọi dãy như vậy.

**Sau**
1. The proportional weight is an adaptive allocation based on the two maximal violations; we do not claim that it is the only choice for which DTAP converges, or that it is optimal.
   → Trọng số tỉ lệ là một cách phân bổ thích nghi dựa trên hai độ vi phạm lớn nhất; ta không khẳng định đó là lựa chọn duy nhất khiến DTAP hội tụ, hay là tối ưu.
2. Although the one-step inequality of Lemma 3.8 holds for every $\mu_k\in[0,1]$, it does not by itself imply convergence for every weight sequence.
   → Mặc dù bất đẳng thức một bước của Bổ đề 3.8 đúng với mọi $\mu_k\in[0,1]$, tự nó không suy ra hội tụ với mọi dãy trọng số.

### 22. Nhận xét 2, câu cuối

- **Trước:** The parameters $\rho_{\rm cvx}$, $\delta$, and $\{\gamma_k\}$ remain part of the algorithm.
  → Các tham số $\rho_{\rm cvx}$, $\delta$ và $\{\gamma_k\}$ vẫn là một phần của thuật toán.
- **Sau:** The user still chooses $\rho_{\rm cvx}$, $\delta$, and $\{\gamma_k\}$; these parameters do not depend on any constant of the problem.
  → Người dùng vẫn phải chọn $\rho_{\rm cvx}$, $\delta$ và $\{\gamma_k\}$; các tham số này không phụ thuộc vào hằng số nào của bài toán.

### 23. Đoạn tổng quan về chứng minh (chuyển xuống đầu Mục 3.6 và viết lại)

*Trước: đoạn nằm cuối Mục 3.5, trước tiêu đề 3.6. Sau: đoạn nằm ngay dưới tiêu đề 3.6 "Auxiliary lemmas".*

**Trước**
1. The convergence analysis of DTAP is more involved than for classical $CQ$ schemes because the two constraint tracks are asymmetric: on the convex track the gradient inequality gives a quantitative lower bound of order $v_i(x)^2$, hence a strict decrease, whereas on the pseudoconvex track the contrapositive of pseudoconvexity gives only sign information.
   → Phân tích hội tụ của DTAP phức tạp hơn các lược đồ $CQ$ cổ điển vì hai track ràng buộc không đối xứng: trên track lồi, bất đẳng thức gradient cho một cận dưới định lượng bậc $v_i(x)^2$, do đó giảm thực sự, còn trên track giả lồi, mệnh đề phản đảo của tính giả lồi chỉ cho thông tin về dấu.
2. The two are reconciled in a single one-step quasi-Fejér inequality with a carefully chosen Young parameter, and a contradiction argument rules out cluster points outside the feasible set.
   → Hai điều này được dung hòa trong một bất đẳng thức tựa Fejér một bước với tham số Young được chọn cẩn thận, và một lập luận phản chứng loại bỏ các điểm tụ nằm ngoài tập khả thi.
3. We then obtain the main result, strong convergence to a feasible point (Theorem 3.12), and deduce the two degenerate structural regimes as corollaries.
   → Sau đó ta thu được kết quả chính, hội tụ mạnh tới một điểm khả thi (Định lý 3.12), và suy ra hai chế độ cấu trúc suy biến như các hệ quả.

**Sau**
1. The two tracks need different arguments.
   → Hai track cần những lập luận khác nhau.
2. On the convex track, Lemma 3.4 bounds $\langle\nabla F_i(x),x-x^\star\rangle$ from below by the violation $v_i(x)$; this gives a decrease of $\|x^k-x^\star\|^2$ of order $\mu_kT_k$.
   → Trên track lồi, Bổ đề 3.4 chặn dưới $\langle\nabla F_i(x),x-x^\star\rangle$ bởi độ vi phạm $v_i(x)$; điều này cho mức giảm của $\|x^k-x^\star\|^2$ cỡ $\mu_kT_k$.
3. On the pseudoconvex track, definition (5) gives only the sign of this inner product.
   → Trên track giả lồi, định nghĩa (5) chỉ cho biết dấu của tích vô hướng này.
4. Lemma 3.8 combines both tracks in one quasi-Fejér inequality; the choice of the parameter $\zeta$ in Young's inequality keeps the convex-track term negative.
   → Bổ đề 3.8 gộp cả hai track trong một bất đẳng thức tựa Fejér; cách chọn tham số $\zeta$ trong bất đẳng thức Young giữ cho số hạng của track lồi luôn âm.
5. Stage 2 of Theorem 3.12 then shows, by contradiction, that at least one cluster point is feasible, and Stage 3 shows that the whole sequence converges to it.
   → Sau đó Giai đoạn 2 của Định lý 3.12 chứng minh bằng phản chứng rằng có ít nhất một điểm tụ khả thi, và Giai đoạn 3 chứng minh toàn bộ dãy hội tụ tới điểm đó.
6. The two degenerate cases follow as corollaries.
   → Hai trường hợp suy biến được suy ra như các hệ quả.

### 24. Chứng minh Bổ đề 3.5

- **Trước:** By (A1)(b), $F_j|_K$ is pseudoconvex; applying the contrapositive (5) with $y=x^\star$ gives $\langle\nabla F_j(x),x^\star-x\rangle<0$, i.e. …
  → Theo (A1)(b), $F_j|_K$ giả lồi; áp dụng mệnh đề phản đảo (5) với $y=x^\star$ ta được $\langle\nabla F_j(x),x^\star-x\rangle<0$, tức là …
- **Sau:** By (A1)(b), $F_j|_K$ is pseudoconvex; applying (5) with $y=x^\star$ gives $\langle\nabla F_j(x),x^\star-x\rangle<0$, i.e. …
  → Theo (A1)(b), $F_j|_K$ giả lồi; áp dụng (5) với $y=x^\star$ ta được $\langle\nabla F_j(x),x^\star-x\rangle<0$, tức là …

### 25. Câu đầu Mục 3.7

- **Trước:** The following quasi-Fejér inequality, within the framework of Combettes [5], yields boundedness of $\{x^k\}$ and decay of the convex-track violation.
  → Bất đẳng thức tựa Fejér sau đây, trong khuôn khổ của Combettes [5], cho tính bị chặn của $\{x^k\}$ và sự giảm của độ vi phạm trên track lồi.
- **Sau:** The following inequality is of quasi-Fejér type in the sense of Combettes [5]. It yields boundedness of $\{x^k\}$ and decay of the convex-track violation.
  → Bất đẳng thức sau đây thuộc loại tựa Fejér theo nghĩa của Combettes [5]. Nó cho tính bị chặn của $\{x^k\}$ và sự giảm của độ vi phạm trên track lồi.

### 26. Chứng minh Bổ đề 3.10: cố định $x^\star$ sớm hơn

**Trước**
1. Assume $I^{\rm cvx}\ne\emptyset$ and put $B:=\overline{\mathrm{conv}}\{x^k:k\ge0\}$, compact by Lemma 3.9 and contained in $K\subset U$.
   → Giả sử $I^{\rm cvx}\ne\emptyset$ và đặt $B:=\overline{\mathrm{conv}}\{x^k:k\ge0\}$, compact theo Bổ đề 3.9 và nằm trong $K\subset U$.
2. (sau (25)) Fix $x^\star\in\Omega$. Remark 3 gives …
   → (sau (25)) Cố định $x^\star\in\Omega$. Nhận xét 3 cho …

**Sau**
1. Assume $I^{\rm cvx}\ne\emptyset$, fix $x^\star\in\Omega$, and put $B:=\overline{\mathrm{conv}}\{x^k:k\ge0\}$, compact by Lemma 3.9 and contained in $K\subset U$.
   → Giả sử $I^{\rm cvx}\ne\emptyset$, cố định $x^\star\in\Omega$, và đặt $B:=\overline{\mathrm{conv}}\{x^k:k\ge0\}$, compact theo Bổ đề 3.9 và nằm trong $K\subset U$.
2. (sau (25)) Remark 3 gives …
   → (sau (25)) Nhận xét 3 cho …

### 27. Mục 3.8: tiêu đề, đoạn dẫn và phát biểu Định lý 3.12

**Trước**
1. [Tiêu đề] 3.8. Strong convergence to a feasible point
   → [Tiêu đề] 3.8. Hội tụ mạnh tới một điểm khả thi
2. The goal of the analysis is strong convergence of $\{x^k\}$ to a feasible point.
   → Mục tiêu của phân tích là sự hội tụ mạnh của $\{x^k\}$ tới một điểm khả thi.
3. The argument has three stages: exploit convex-track feasibility (Lemma 3.10) to confine the cluster set to the convex half; use a contradiction argument with pseudoconvexity to produce a cluster point in $\Omega$; and combine with distance convergence to upgrade to convergence of the whole sequence.
   → Lập luận có ba giai đoạn: khai thác tính khả thi của track lồi (Bổ đề 3.10) để giới hạn tập điểm tụ vào nửa lồi; dùng lập luận phản chứng với tính giả lồi để tạo ra một điểm tụ thuộc $\Omega$; và kết hợp với sự hội tụ của khoảng cách để nâng lên thành sự hội tụ của toàn bộ dãy.
4. Theorem 3.12. Under Assumption 1, the sequence $\{x^k\}$ generated by Algorithm 1 converges strongly to a point $x^\infty\in\Omega$.
   → Định lý 3.12. Dưới Giả thiết 1, dãy $\{x^k\}$ sinh bởi Thuật toán 1 hội tụ mạnh tới một điểm $x^\infty\in\Omega$.

**Sau**
1. [Tiêu đề] 3.8. Convergence to a feasible point
   → [Tiêu đề] 3.8. Hội tụ tới một điểm khả thi
2. We now prove that the whole sequence converges to a feasible point.
   → Bây giờ ta chứng minh toàn bộ dãy hội tụ tới một điểm khả thi.
3. The proof has three stages.
   → Chứng minh có ba giai đoạn.
4. Stage 1 uses Lemma 3.10 to show that every cluster point satisfies the convex constraints.
   → Giai đoạn 1 dùng Bổ đề 3.10 để chứng minh mọi điểm tụ thỏa các ràng buộc lồi.
5. Stage 2 shows, by contradiction and pseudoconvexity, that at least one cluster point is feasible.
   → Giai đoạn 2 chứng minh, bằng phản chứng và tính giả lồi, rằng có ít nhất một điểm tụ khả thi.
6. Stage 3 uses the convergence of $\|x^k-\bar x\|$ to show that the whole sequence converges to that point.
   → Giai đoạn 3 dùng sự hội tụ của $\|x^k-\bar x\|$ để chứng minh toàn bộ dãy hội tụ tới điểm đó.
7. Theorem 3.12. Under Assumption 1, the sequence $\{x^k\}$ generated by Algorithm 1 converges to a point $x^\infty\in\Omega$.
   → Định lý 3.12. Dưới Giả thiết 1, dãy $\{x^k\}$ sinh bởi Thuật toán 1 hội tụ tới một điểm $x^\infty\in\Omega$.

### 28. Tên các giai đoạn trong chứng minh Định lý 3.12

- **Trước:** *Stage 1 (convex half).* … *Stage 2 (pseudoconvex half by contradiction).*
  → *Giai đoạn 1 (nửa lồi).* … *Giai đoạn 2 (nửa giả lồi, bằng phản chứng).*
- **Sau:** *Stage 1 (convex constraints).* … *Stage 2 (a feasible cluster point).*
  → *Giai đoạn 1 (các ràng buộc lồi).* … *Giai đoạn 2 (một điểm tụ khả thi).*

### 29. Chứng minh Định lý 3.12, Claim 3

- **Trước:** … $F_{j^\star}(x^\star)\le b_{j^\star}<F_{j^\star}(\bar x)$; the contrapositive (5) with $x=\bar x$, $y=x^\star$ gives $\langle\nabla F_{j^\star}(\bar x),\bar x-x^\star\rangle>0$, …
  → … ; mệnh đề phản đảo (5) với $x=\bar x$, $y=x^\star$ cho $\langle\nabla F_{j^\star}(\bar x),\bar x-x^\star\rangle>0$, …
- **Sau:** … $F_{j^\star}(x^\star)\le b_{j^\star}<F_{j^\star}(\bar x)$; definition (5) with $x=\bar x$, $y=x^\star$ gives $\langle\nabla F_{j^\star}(\bar x),\bar x-x^\star\rangle>0$, …
  → … ; định nghĩa (5) với $x=\bar x$, $y=x^\star$ cho $\langle\nabla F_{j^\star}(\bar x),\bar x-x^\star\rangle>0$, …

### 30. Câu cuối Giai đoạn 3

- **Trước:** This argument requires neither uniqueness of the feasible point nor convexity of the target set: one feasible cluster point and convergence of its distance suffice.
  → Lập luận này không cần tính duy nhất của điểm khả thi, cũng không cần tính lồi của tập đích: một điểm tụ khả thi và sự hội tụ của khoảng cách tới nó là đủ.
- **Sau:** The argument does not require $\Omega$ to be a singleton: one feasible cluster point and the convergence of its distance suffice.
  → Lập luận không cần $\Omega$ chỉ có một điểm: một điểm tụ khả thi và sự hội tụ của khoảng cách tới nó là đủ.

### 31. Nhận xét 4 (vai trò của $\delta$)

**Trước**
1. Larger $\delta$ enlarges $K^{\rm cvx}_k,K^{\rm ps}_k$, which may aid numerical stability when several $v_i(x^k)$ are nearly equal; on the test problem (47), $\delta=10^{-1}$ and $\delta=10^{-3}$ produce identical iterates (Table 8): the pseudoconvex track has a single index, at every start either only $F_1$ is violated or $v_1-v_2\ge4.79$, and in these runs the convex track is satisfied from the second evaluated point on.
   → $\delta$ lớn hơn làm rộng $K^{\rm cvx}_k,K^{\rm ps}_k$, điều này có thể giúp ổn định số khi nhiều $v_i(x^k)$ gần bằng nhau; trên bài toán thử (47), $\delta=10^{-1}$ và $\delta=10^{-3}$ cho các dãy lặp giống hệt nhau (Bảng 8): track giả lồi chỉ có một chỉ số, tại mọi điểm xuất phát hoặc chỉ $F_1$ bị vi phạm hoặc $v_1-v_2\ge4.79$, và trong các lần chạy này track lồi được thỏa từ điểm đánh giá thứ hai trở đi.
2. The $\delta$ row of Table 8 is therefore a consistency check, not evidence about $\delta$.
   → Vì vậy dòng $\delta$ của Bảng 8 là một phép kiểm tra tính nhất quán, không phải bằng chứng về $\delta$.

**Sau**
1. Larger $\delta$ enlarges $K^{\rm cvx}_k$ and $K^{\rm ps}_k$, which may improve numerical stability when several $v_i(x^k)$ are nearly equal.
   → $\delta$ lớn hơn làm rộng $K^{\rm cvx}_k$ và $K^{\rm ps}_k$, điều này có thể cải thiện độ ổn định số khi nhiều $v_i(x^k)$ gần bằng nhau.

*(Phần giải thích về bài toán (47) được chuyển xuống Mục 4.4, xem mục 55.)*

### 32. Hệ quả 3.13 và 3.14

- **Trước:** The sequence converges strongly to a point $x^\infty\in\Omega$ … (cả hai hệ quả)
  → Dãy hội tụ mạnh tới một điểm $x^\infty\in\Omega$ …
- **Sau:** The sequence converges to a point $x^\infty\in\Omega$ … (cả hai hệ quả)
  → Dãy hội tụ tới một điểm $x^\infty\in\Omega$ …

---

## E. Mục 4. Thực nghiệm số

### 33. Câu bị xóa ở đầu Mục 4

- **Trước:** These two scopes are stated separately below.
  → Hai phạm vi này được nêu riêng dưới đây.
- **Sau:** *(xóa)*

### 34. Mục 4.1.1: thông tin tương tác

- **Trước:** … and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$.
  → … và $I(Z_i;Z_j;C)=\ldots$.
- **Sau:** … and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$ is their interaction information.
  → … và $I(Z_i;Z_j;C)=\ldots$ là thông tin tương tác của chúng.

### 35. Mục 4.1.2: ba số hạng của hàm mất mát AFRSFCV

- **Trước:** The three terms measure label-approximation error, incorrect-decision confidence, and Tikhonov regularization, respectively.
  → Ba số hạng lần lượt đo sai số xấp xỉ nhãn, độ tin cậy của quyết định sai, và hiệu chỉnh Tikhonov.
- **Sau:** The three terms are the label-approximation error, the weight of misclassifying features per sample, and a Tikhonov term.
  → Ba số hạng là sai số xấp xỉ nhãn, trọng số của các đặc trưng phân loại sai trên mỗi mẫu, và một số hạng Tikhonov.

### 36. Mục 4.1.3: $F_1,F_2$ là số hạng của (38)

- **Trước:** Here $F_1,F_2$ are the first two components of (38), without their coefficients, and $F_3$ is the objective in (34).
  → Ở đây $F_1,F_2$ là hai thành phần đầu của (38), bỏ hệ số, và $F_3$ là hàm mục tiêu trong (34).
- **Sau:** Here $F_1,F_2$ are the first two terms of (38), without their coefficients, and $F_3$ is the objective in (34).
  → Ở đây $F_1,F_2$ là hai số hạng đầu của (38), bỏ hệ số, và $F_3$ là hàm mục tiêu trong (34).

### 37. Câu bị xóa sau (42)

- **Trước:** A feasible weight need not minimize either baseline objective.
  → Một trọng số khả thi không nhất thiết cực tiểu hóa hàm mục tiêu nào của các phương pháp cơ sở.
- **Sau:** *(xóa; ý này đã có ở câu ngay trước)*

### 38. Mệnh đề 4.1, câu cuối

- **Trước:** It satisfies the function assumptions of Assumption 1 whenever $\Omega\ne\varnothing$.
  → Nó thỏa các giả thiết về hàm của Giả thiết 1 bất cứ khi nào $\Omega\ne\varnothing$.
- **Sau:** Hence (42) satisfies (A1) and (A2) of Assumption 1, with $U=U_\rho$, whenever $\Omega\ne\varnothing$.
  → Do đó (42) thỏa (A1) và (A2) của Giả thiết 1, với $U=U_\rho$, bất cứ khi nào $\Omega\ne\varnothing$.

### 39. Đoạn sau chứng minh Mệnh đề 4.1 (cách gán track, chặn an toàn, ngưỡng)

**Trước**
1. The assignment $I^{\rm cvx}=\{1,2\}$, $I^{\rm ps}=\{3\}$ used in the experiments is admissible because convexity implies pseudoconvexity.
   → Cách gán $I^{\rm cvx}=\{1,2\}$, $I^{\rm ps}=\{3\}$ dùng trong thực nghiệm là hợp lệ vì lồi kéo theo giả lồi.
2. It treats $F_3$ conservatively and does not test a genuinely nonconvex constraint.
   → Cách gán này xử lý $F_3$ một cách thận trọng và không kiểm tra một ràng buộc thực sự không lồi.
3. The all-convex assignment $I^{\rm cvx}=\{1,2,3\}$ is also available.
   → Cách gán toàn lồi $I^{\rm cvx}=\{1,2,3\}$ cũng dùng được.
4. Under the assumptions of Theorem 3.12, either assignment converges to a feasible weight.
   → Dưới các giả thiết của Định lý 3.12, cả hai cách gán đều hội tụ tới một trọng số khả thi.
5. Score positivity must be checked on each instance.
   → Tính dương của điểm số phải được kiểm tra trên từng bài toán.
6. Replacing a zero score by a positive floor changes the model and must be declared.
   → Thay một điểm số bằng 0 bởi một ngưỡng dưới dương sẽ làm thay đổi mô hình và phải được nêu rõ.
7. The implementation also uses $\max\{\rho^{\top}w,10^{-15}\}$ during evaluation.
   → Mã cài đặt còn dùng $\max\{\rho^{\top}w,10^{-15}\}$ khi tính giá trị.
8. This agrees with (41) only where the floor is inactive.
   → Điều này chỉ trùng với (41) ở những chỗ ngưỡng dưới không có tác dụng.
9. Applying the theorem to this implementation therefore requires that the floor remain inactive.
   → Vì vậy, áp dụng định lý cho mã cài đặt này đòi hỏi ngưỡng dưới luôn không có tác dụng.
10. Externally specified thresholds remain fixed.
    → Các ngưỡng được cho từ bên ngoài được giữ cố định.
11. Training-based thresholds instead define the benchmark instance and must be shared by all solvers.
    → Còn các ngưỡng tính từ dữ liệu huấn luyện thì xác định bài toán chuẩn và phải được mọi bộ giải dùng chung.
12. Separate empirical percentiles do not ensure $\Omega\ne\varnothing$.
    → Các phân vị thực nghiệm tính riêng rẽ không bảo đảm $\Omega\ne\varnothing$.
13. A common point must satisfy all constraints, and checks to a numerical tolerance establish only the corresponding approximate feasibility.
    → Một điểm chung phải thỏa mọi ràng buộc, và các phép kiểm tra theo một sai số số học chỉ xác lập được tính khả thi xấp xỉ tương ứng.
14. The threshold protocol and constraint-activity diagnostics are reported with the experiments.
    → Quy trình chọn ngưỡng và các chẩn đoán về mức hoạt động của ràng buộc được báo cáo cùng với thực nghiệm.

*(Thêm vào đây, Trước, ở đầu Mục 4.4 — được gộp vào đoạn này ở bản Sau, xem mục 49):*

15. The sampling pool contains $3\,000$ Dirichlet points and all simplex vertices.
    → Tập mẫu gồm $3\,000$ điểm Dirichlet và mọi đỉnh của đơn hình.
16. The heuristic chooses percentile levels from the sample size, the feature dimension, the number of classes and the class-imbalance ratio; the exact levels and thresholds are recorded in the supplementary metadata.
    → Quy tắc kinh nghiệm chọn mức phân vị từ cỡ mẫu, số chiều đặc trưng, số lớp và tỉ lệ mất cân bằng lớp; các mức và ngưỡng cụ thể được ghi trong siêu dữ liệu bổ sung.
17. In an application with prescribed thresholds, these values are inputs, and consistency remains an assumption.
    → Trong một ứng dụng có ngưỡng cho trước, các giá trị này là đầu vào, và tính nhất quán vẫn là một giả thiết.
18. All Fisher coordinates are positive on these instances, with minimum $5.99\times10^{-5}$.
    → Mọi tọa độ Fisher đều dương trên các bài toán này, nhỏ nhất là $5.99\times10^{-5}$.

**Sau**
1. The experiments use $I^{\rm cvx}=\{1,2\}$, $I^{\rm ps}=\{3\}$, which is admissible since convex functions are pseudoconvex; DTAP then uses only sign information for $F_3$, so no genuinely nonconvex constraint is tested.
   → Thực nghiệm dùng $I^{\rm cvx}=\{1,2\}$, $I^{\rm ps}=\{3\}$; cách gán này hợp lệ vì hàm lồi là giả lồi; khi đó DTAP chỉ dùng thông tin về dấu cho $F_3$, nên không có ràng buộc thực sự không lồi nào được kiểm tra.
2. The all-convex assignment $I^{\rm cvx}=\{1,2,3\}$ is also admissible, and Theorem 3.12 applies to both.
   → Cách gán toàn lồi $I^{\rm cvx}=\{1,2,3\}$ cũng hợp lệ, và Định lý 3.12 áp dụng cho cả hai.
3. Proposition 4.1 needs $\min_k\rho_k>0$; on all instances used here the smallest score is $4.77\times10^{-5}$.
   → Mệnh đề 4.1 cần $\min_k\rho_k>0$; trên mọi bài toán dùng ở đây, điểm số nhỏ nhất là $4.77\times10^{-5}$.
4. Hence the safeguard $\max\{\rho^\top w,10^{-15}\}$ in the implementation is never active, and the implemented $F_3$ is (41).
   → Do đó chặn an toàn $\max\{\rho^\top w,10^{-15}\}$ trong mã cài đặt không bao giờ có tác dụng, và $F_3$ được cài đặt đúng là (41).
5. The thresholds are calibrated on the training data: $b_i$ is the $q_i$-th percentile of $F_i$ over $3\,000$ Dirichlet points (seed 42) and the $p$ vertices of $K$, where a fixed rule chooses $q_i$ from the sample size, the number of features and classes, and the class imbalance (supplementary metadata).
   → Các ngưỡng được hiệu chỉnh trên dữ liệu huấn luyện: $b_i$ là phân vị thứ $q_i$ của $F_i$ trên $3\,000$ điểm Dirichlet (seed 42) và $p$ đỉnh của $K$, trong đó một quy tắc cố định chọn $q_i$ theo cỡ mẫu, số đặc trưng, số lớp và mức mất cân bằng lớp (siêu dữ liệu bổ sung).
6. All solvers share these thresholds.
   → Mọi bộ giải dùng chung các ngưỡng này.
7. Calibrating each $b_i$ separately does not guarantee $\Omega\ne\varnothing$; Section 4.4 checks feasibility numerically.
   → Hiệu chỉnh riêng từng $b_i$ không bảo đảm $\Omega\ne\varnothing$; Mục 4.4 kiểm tra tính khả thi bằng số.
8. Prescribed thresholds would be used as given.
   → Nếu ngưỡng được cho trước thì sẽ được dùng nguyên như vậy.

*(Ghi chú: $4.77\times10^{-5}$ là giá trị nhỏ nhất trên mọi fold huấn luyện và mọi bộ dữ liệu đầy đủ; $5.99\times10^{-5}$ cũ chỉ tính trên các bài toán dữ liệu đầy đủ ở Mục 4.4.)*

### 40. Nhận xét 6 (chi phí mỗi vòng lặp)

- **Trước:** Simplex projection costs $O(p\log p)$.
  → Phép chiếu lên đơn hình tốn $O(p\log p)$.
- **Sau:** Projection onto $K=\Delta_{p-1}$ by sorting costs $O(p\log p)$ operations [6].
  → Phép chiếu lên $K=\Delta_{p-1}$ bằng sắp xếp tốn $O(p\log p)$ phép toán [6].

*(Câu Sau gộp câu cũ ở Mục 2, xem mục 11.)*

### 41. Mục 4.2: câu về SG-const và SG-dyn

**Trước**
1. SG-const uses step $10^{-3}$.
   → SG-const dùng bước $10^{-3}$.
2. The dynamic subgradient comparison is considered separately with sampled and empirically tuned moduli in the solver diagnostic.
   → Phép so sánh với phương pháp dưới gradient động được xét riêng, với mô-đun lấy mẫu và mô-đun tinh chỉnh thực nghiệm, trong phần chẩn đoán bộ giải.

**Sau**
1. SG-const uses the step $\nu_k=10^{-3}$ and SG-dyn the sampled modulus $\widehat L$ (Section 4.2.1); tuned moduli are considered only in Section 4.4.
   → SG-const dùng bước $\nu_k=10^{-3}$ và SG-dyn dùng mô-đun lấy mẫu $\widehat L$ (Mục 4.2.1); mô-đun tinh chỉnh chỉ được xét ở Mục 4.4.

### 42. Mục 4.2.1: câu mở đầu

- **Trước:** The following updates specify the two baseline solvers for the models in Sections 4.1.1 and 4.1.2.
  → Các bước cập nhật sau đây mô tả hai bộ giải cơ sở cho các mô hình ở Mục 4.1.1 và 4.1.2.
- **Sau:** The following paragraphs specify the baseline solvers: N-Fscore and AFRSFCV for the models of Sections 4.1.1 and 4.1.2, and the subgradient methods SG-const and SG-dyn.
  → Các đoạn sau mô tả các bộ giải cơ sở: N-Fscore và AFRSFCV cho các mô hình ở Mục 4.1.1 và 4.1.2, và các phương pháp dưới gradient SG-const và SG-dyn.

### 43. N-Fscore: tích phân Euler

**Trước**
1. We integrate (45) by explicit Euler on $[0,T]$ with $N_{\rm step}$ steps under a fixed budget (no stopping rule), with the fixed parameters reported in the experimental protocol, and take as weight vector the projection $P_K(g(u(T)))$ of the network output at the final time onto the simplex $K$.
   → Ta tích phân (45) bằng phương pháp Euler hiện trên $[0,T]$ với $N_{\rm step}$ bước trong một ngân sách cố định (không có quy tắc dừng), với các tham số cố định nêu trong quy trình thực nghiệm, và lấy làm vector trọng số hình chiếu $P_K(g(u(T)))$ của đầu ra mạng tại thời điểm cuối lên đơn hình $K$.

**Sau**
1. We integrate (45) by the explicit Euler method on a uniform grid of $N_{\rm grid}$ points in $[0,T]$, without a stopping rule, using the parameters of Section 4.2.
   → Ta tích phân (45) bằng phương pháp Euler hiện trên một lưới đều gồm $N_{\rm grid}$ điểm trong $[0,T]$, không có quy tắc dừng, với các tham số ở Mục 4.2.
2. The weight vector is the projection $P_K(g(u(T)))$ of the final network output onto $K$.
   → Vector trọng số là hình chiếu $P_K(g(u(T)))$ của đầu ra cuối cùng của mạng lên $K$.

### 44. Đoạn mới "SG-const and SG-dyn" ở Mục 4.2.1 (chuyển từ Mục 4.4 lên và viết lại)

**Trước** (ở đoạn "Protocol and tuning cost", Mục 4.4)
1. SG-const uses $\nu_k=10^{-3}$.
   → SG-const dùng $\nu_k=10^{-3}$.
2. For SG-dyn, $\widehat L$ is the largest gradient norm at $500$ sampled points.
   → Với SG-dyn, $\widehat L$ là chuẩn gradient lớn nhất tại $500$ điểm lấy mẫu.
3. The subgradient implementation follows the most-violated-constraint strategy of [7].
   → Cài đặt phương pháp dưới gradient theo chiến lược ràng buộc bị vi phạm nhiều nhất của [7].
4. For $D_k=\arg\max_i v_i(x^k)$ it uses $x^{k+1}=P_K(x^k-\nu_k\bar h_k)$, $\bar h_k=\frac1{|D_k|}\sum_{i\in D_k}\nabla F_i(x^k)/\|\nabla F_i(x^k)\|$, where $\nu_k=10^{-3}$ for SG-const and $\nu_k=J(x^k)/L$ for SG-dyn.
   → Với $D_k=\arg\max_i v_i(x^k)$, nó dùng $x^{k+1}=\ldots$, $\bar h_k=\ldots$, trong đó $\nu_k=10^{-3}$ cho SG-const và $\nu_k=J(x^k)/L$ cho SG-dyn.
5. The averaging specifies how ties are handled.
   → Phép lấy trung bình quy định cách xử lý khi có nhiều chỉ số cùng đạt max.

**Sau** (đoạn mới ở Mục 4.2.1)
1. **SG-const and SG-dyn** These subgradient methods for quasiconvex feasibility [7] follow its most-violated-constraint strategy: with $\mathcal I_k=\arg\max_i v_i(w^k)$, $w^{k+1}=P_K(w^k-\nu_k\bar h_k)$, $\bar h_k=\frac1{|\mathcal I_k|}\sum_{i\in\mathcal I_k}\nabla F_i(w^k)/\|\nabla F_i(w^k)\|$.
   → **SG-const và SG-dyn** Các phương pháp dưới gradient cho bài toán chấp nhận tựa lồi này [7] theo chiến lược ràng buộc bị vi phạm nhiều nhất của bài báo đó: với $\mathcal I_k=\arg\max_i v_i(w^k)$, $w^{k+1}=\ldots$, $\bar h_k=\ldots$
2. SG-const uses $\nu_k=10^{-3}$; SG-dyn uses the dynamic step $\nu_k=J(w^k)/L$ (Hölder exponent 1), with $L=\widehat L$, the largest gradient norm at $500$ points sampled in $K$.
   → SG-const dùng $\nu_k=10^{-3}$; SG-dyn dùng bước động $\nu_k=J(w^k)/L$ (số mũ Hölder bằng 1), với $L=\widehat L$ là chuẩn gradient lớn nhất tại $500$ điểm lấy mẫu trong $K$.

*(Câu 5 cũ "The averaging specifies how ties are handled." bị bỏ.)*

### 45. Mục 4.2.2: quy trình đánh giá

**Trước**
1. No classifier parameter or vote threshold is chosen from these test outcomes.
   → Không có tham số phân loại hay ngưỡng bỏ phiếu nào được chọn từ các kết quả kiểm tra này.
2. The same holdouts were used when the selections were computed, and the threshold heuristic uses the whole-dataset sample size, dimensions and class counts before splitting.
   → Cùng các tập giữ lại đã được dùng khi tính các tập đặc trưng, và quy tắc kinh nghiệm chọn ngưỡng dùng cỡ mẫu, số chiều và số lượng mẫu mỗi lớp của toàn bộ dữ liệu trước khi chia.
3. Hence this is an exploratory evaluation, not an end-to-end or nested-validation study.
   → Vì vậy đây là một đánh giá khám phá, không phải một nghiên cứu đầu-cuối hay kiểm định lồng.

**Sau**
1. The test data are not used to select features or to choose any parameter or vote threshold.
   → Dữ liệu kiểm tra không được dùng để chọn đặc trưng hay chọn bất kỳ tham số hoặc ngưỡng bỏ phiếu nào.
2. The training/test split is fixed before the selections are computed, and the rule that chooses the threshold levels uses only the sample size, the number of features, the number of classes and the class sizes of the whole dataset, not any feature values.
   → Phép chia huấn luyện/kiểm tra được cố định trước khi tính các tập đặc trưng, và quy tắc chọn mức ngưỡng chỉ dùng cỡ mẫu, số đặc trưng, số lớp và kích thước các lớp của toàn bộ dữ liệu, không dùng giá trị đặc trưng nào.
3. Because a single split is used, this is an exploratory evaluation, not an end-to-end or nested-validation study.
   → Vì chỉ dùng một phép chia, đây là một đánh giá khám phá, không phải một nghiên cứu đầu-cuối hay kiểm định lồng.

### 46. Chỉ số ổn định Nogueira

- **Trước:** Here $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$; the unbiased variance correction is $N_f/(N_f-1)$, not $p/(p-1)$.
  → Ở đây $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$; hệ số hiệu chỉnh phương sai không chệch là $N_f/(N_f-1)$, không phải $p/(p-1)$.
- **Sau:** Here $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$, and $s_j^2$ is the unbiased variance over the $N_f$ folds.
  → Ở đây $\bar Z_j=N_f^{-1}\sum_b Z_{bj}$, và $s_j^2$ là phương sai không chệch trên $N_f$ fold.

### 47. Mục 4.3: độ ổn định

**Trước**
1. Its mean stability is $0.786$, compared with N-Fscore's $0.822$; thus the results support moderate reduction rather than uniform sparsity or stability superiority.
   → Độ ổn định trung bình của nó là $0.786$, so với $0.822$ của N-Fscore; như vậy kết quả ủng hộ mức giảm vừa phải, chứ không phải ưu thế đồng đều về độ thưa hay độ ổn định.

**Sau**
1. Its mean stability is $0.786$, compared with N-Fscore's $0.822$.
   → Độ ổn định trung bình của nó là $0.786$, so với $0.822$ của N-Fscore.
2. Thus DTAP reduces the number of features moderately; it does not select sparser or more stable sets than the base models.
   → Như vậy DTAP giảm số đặc trưng ở mức vừa phải; nó không chọn được các tập thưa hơn hay ổn định hơn các mô hình gốc.

### 48. Mục 4.3: kết quả của SG

- **Trước:** The per-dataset exceptions are included in Table 3, and all five methods appear in the summary.
  → Các ngoại lệ theo từng bộ dữ liệu có trong Bảng 3, và cả năm phương pháp đều có trong bảng tóm tắt.
- **Sau:** The SG results on Spambase, the only dataset where they differ from DTAP, are given below Table 3; Table 4 includes all five methods.
  → Kết quả SG trên Spambase, bộ dữ liệu duy nhất mà chúng khác DTAP, được ghi dưới Bảng 3; Bảng 4 gồm cả năm phương pháp.

### 49. Mục 4.4: đoạn mở đầu (kiểm tra tính khả thi)

**Trước**
1. The percentile calibration defines experimental thresholds; it does not guarantee that their sublevel sets intersect.
   → Việc hiệu chỉnh theo phân vị xác định các ngưỡng thực nghiệm; nó không bảo đảm các tập mức dưới của chúng giao nhau.
2. (Ba câu về tập mẫu, quy tắc chọn phân vị, ngưỡng cho trước: xem mục 39, câu 15–17.)
3. For the full-data instances below, saved numerical witnesses satisfy all three inequalities strictly under an independent evaluation; the smallest slack is $4.33\times10^{-4}$.
   → Với các bài toán dữ liệu đầy đủ dưới đây, các điểm chứng số đã lưu thỏa chặt cả ba bất đẳng thức khi được đánh giá độc lập; độ dôi nhỏ nhất là $4.33\times10^{-4}$.
4. This numerical check is distinct from an exact feasibility certificate.
   → Phép kiểm tra số này khác với một chứng nhận khả thi chính xác.
5. (Câu về tọa độ Fisher: xem mục 39, câu 18.)
6. We measure the frequency of $F_3(w^k)-b_3>10^{-6}$ over all evaluated points, including the terminating point.
   → Ta đo tần suất $F_3(w^k)-b_3>10^{-6}$ trên mọi điểm được đánh giá, kể cả điểm kết thúc.

**Sau**
1. As noted in Section 4.1.3, the calibrated thresholds need not yield $\Omega\ne\varnothing$.
   → Như đã nêu ở Mục 4.1.3, các ngưỡng đã hiệu chỉnh không nhất thiết cho $\Omega\ne\varnothing$.
2. For each full-data instance below, we keep the evaluated point with the largest slack $\min_i(b_i-F_i(w))$ over all runs.
   → Với mỗi bài toán dữ liệu đầy đủ dưới đây, ta giữ lại điểm được đánh giá có độ dôi $\min_i(b_i-F_i(w))$ lớn nhất trên mọi lần chạy.
3. Re-evaluated on matrices rebuilt from the data, each of these points satisfies all three inequalities strictly; the smallest slack is $4.33\times10^{-4}$.
   → Khi tính lại trên các ma trận dựng lại từ dữ liệu, mỗi điểm này thỏa chặt cả ba bất đẳng thức; độ dôi nhỏ nhất là $4.33\times10^{-4}$.
4. This is a numerical check, not an exact certificate of feasibility.
   → Đây là một phép kiểm tra số, không phải chứng nhận chính xác về tính khả thi.
5. We count the iterates of a run, including the last (its evaluated points), at which $F_3(w^k)-b_3>10^{-6}$.
   → Ta đếm các điểm lặp của một lần chạy, kể cả điểm cuối (các điểm được đánh giá của nó), tại đó $F_3(w^k)-b_3>10^{-6}$.

### 50. Mục 4.4: mức hoạt động của $F_3$

**Trước**
1. Table 6 shows that the third track is inactive on seven of the eight standard-start runs for the classification datasets and active at only one of the $48$ evaluated points on Abalone.
   → Bảng 6 cho thấy track thứ ba không hoạt động ở bảy trên tám lần chạy từ điểm xuất phát chuẩn trên các bộ dữ liệu phân loại, và chỉ hoạt động tại một trong $48$ điểm được đánh giá trên Abalone.
2. Moreover, the quadratic-over-linear function $F_3$ is convex when $Q_R\succeq0$ and $\rho^\top w>0$.
   → Hơn nữa, hàm toàn phương chia tuyến tính $F_3$ là lồi khi $Q_R\succeq0$ và $\rho^\top w>0$.
3. These feature-selection instances therefore test a convex subclass and do not demonstrate a need for the nonconvex extension.
   → Vì vậy các bài toán chọn đặc trưng này kiểm tra một lớp con lồi và không cho thấy cần đến phần mở rộng không lồi.
4. We include the valid all-convex comparator, which assigns all three constraints to the convex track.
   → Ta đưa vào phương án so sánh toàn lồi hợp lệ, gán cả ba ràng buộc vào track lồi.
5. Movement Libras is an additional solver robustness case, separate from the eight-dataset classification study.
   → Movement Libras là một trường hợp bổ sung về độ bền của bộ giải, tách riêng khỏi nghiên cứu phân loại trên tám bộ dữ liệu.

**Sau**
1. Table 6 shows that, from the standard start, $F_3$ is violated at no evaluated point on seven of the eight classification datasets, and at one of the $48$ evaluated points on Abalone.
   → Bảng 6 cho thấy, từ điểm xuất phát chuẩn, $F_3$ không bị vi phạm tại điểm được đánh giá nào trên bảy trong tám bộ dữ liệu phân loại, và bị vi phạm tại một trong $48$ điểm được đánh giá trên Abalone.
2. Since $F_3$ is convex (Proposition 4.1), these feature-selection instances test a convex subclass and do not demonstrate a need for the nonconvex extension.
   → Vì $F_3$ lồi (Mệnh đề 4.1), các bài toán chọn đặc trưng này kiểm tra một lớp con lồi và không cho thấy cần đến phần mở rộng không lồi.
3. We also report the all-convex comparator (AC), which assigns all three constraints to the convex track.
   → Ta cũng báo cáo phương án so sánh toàn lồi (AC), gán cả ba ràng buộc vào track lồi.

### 51. Mục 4.4: đoạn "Protocol and tuning cost"

- **Trước:** (năm câu định nghĩa SG, xem mục 44) — The tuned variant selects $L=c\widehat L$ from the manually specified grid $c\in\{10^{-3},10^{-2.5},\ldots,10^1\}$ using three random starting points (seeds 1101–1103).
  → … Biến thể tinh chỉnh chọn $L=c\widehat L$ từ lưới đặt thủ công $c\in\{\ldots\}$ bằng ba điểm xuất phát ngẫu nhiên (seed 1101–1103).
- **Sau:** SG-const and SG-dyn are defined in Section 4.2.1. Besides SG-dyn with the sampled modulus $\widehat L$, a tuned variant selects $L=c\widehat L$ from the manually specified grid $c\in\{10^{-3},10^{-2.5},\ldots,10^1\}$ using three random starting points (seeds 1101–1103).
  → SG-const và SG-dyn được định nghĩa ở Mục 4.2.1. Bên cạnh SG-dyn với mô-đun lấy mẫu $\widehat L$, một biến thể tinh chỉnh chọn $L=c\widehat L$ từ lưới đặt thủ công $c\in\{\ldots\}$ bằng ba điểm xuất phát ngẫu nhiên (seed 1101–1103).

### 52. Mục 4.4: Abalone, sai khác giữa DTAP và AC

**Trước**
1. … the values of $J$ along the two trajectories differ by at most $3.18\times10^{-5}$ relative to AC, and both runs stop after $48$ evaluated points.
   → … các giá trị của $J$ dọc hai quỹ đạo sai khác nhau nhiều nhất $3.18\times10^{-5}$ so với AC, và cả hai lần chạy dừng sau $48$ điểm được đánh giá.
2. The columns are therefore not a comparison of the two assignments, whose success counts differ only from the random starts ($26/36$ versus $36/36$).
   → Vì vậy các cột này không phải là phép so sánh hai cách gán, mà số lần thành công của chúng chỉ khác nhau từ các điểm xuất phát ngẫu nhiên ($26/36$ so với $36/36$).

**Sau**
1. … the values of $J$ along the two trajectories satisfy $|J_{\rm DTAP}-J_{\rm AC}|\le3.18\times10^{-5}\,J_{\rm AC}$ at every evaluated point, and both runs stop after $48$ evaluated points.
   → … các giá trị của $J$ dọc hai quỹ đạo thỏa $|J_{\rm DTAP}-J_{\rm AC}|\le3.18\times10^{-5}\,J_{\rm AC}$ tại mọi điểm được đánh giá, và cả hai lần chạy dừng sau $48$ điểm được đánh giá.
2. The columns are therefore not a comparison of the two assignments, whose success counts differ only on the random starts ($26/36$ versus $36/36$).
   → Vì vậy các cột này không phải là phép so sánh hai cách gán, mà số lần thành công của chúng chỉ khác nhau trên các điểm xuất phát ngẫu nhiên ($26/36$ so với $36/36$).

### 53. Mục 4.4: biến thể cân bằng

**Trước**
1. A balanced DTAP variant also obtains $26/36$; it assigns equal weights when both tracks are nonzero and full weight to the sole nonzero track.
   → Một biến thể DTAP cân bằng cũng đạt $26/36$; nó gán trọng số bằng nhau khi cả hai track khác không và toàn bộ trọng số cho track khác không duy nhất.
2. Thus these tests do not establish a uniform advantage of residual-share weighting or robustness to initialization.
   → Như vậy các phép thử này không chứng tỏ được ưu thế đồng đều của cách đặt trọng số theo tỉ phần phần dư, cũng như độ bền đối với điểm khởi đầu.

**Sau**
1. A balanced DTAP variant also obtains $26/36$; it assigns equal weights when both tracks are violated and full weight to the only violated track otherwise.
   → Một biến thể DTAP cân bằng cũng đạt $26/36$; nó gán trọng số bằng nhau khi cả hai track bị vi phạm, và ngược lại gán toàn bộ trọng số cho track duy nhất bị vi phạm.
2. Thus these tests do not establish a uniform advantage of the proportional weight or robustness to initialization.
   → Như vậy các phép thử này không chứng tỏ được ưu thế đồng đều của trọng số tỉ lệ, cũng như độ bền đối với điểm khởi đầu.

### 54. Mục 4.4: bài toán giả lồi không lồi

- **Trước:** To exercise the third track directly, consider $K=[-2,2]^d$ and (47).
  → Để kiểm tra trực tiếp track thứ ba, xét $K=[-2,2]^d$ và (47).
- **Sau:** To exercise the pseudoconvex track directly, consider $K=[-2,2]^d$ and (47).
  → Để kiểm tra trực tiếp track giả lồi, xét $K=[-2,2]^d$ và (47).

### 55. Mục 4.4: giải thích dòng $\delta$ của Bảng 8 (chuyển từ Nhận xét 4 xuống)

- **Trước:** *(nằm trong Nhận xét 4, xem mục 31)*
- **Sau:** On (47), $\delta=10^{-1}$ and $\delta=10^{-3}$ give identical iterates because the pseudoconvex track has a single index, at every start either only $F_1$ is violated or $v_1-v_2\ge4.79$, and the convex track is satisfied from the second evaluated point on; the $\delta$ row of Table 8 is therefore a consistency check, not evidence about the role of $\delta$.
  → Trên (47), $\delta=10^{-1}$ và $\delta=10^{-3}$ cho các dãy lặp giống hệt nhau vì track giả lồi chỉ có một chỉ số, tại mọi điểm xuất phát hoặc chỉ $F_1$ bị vi phạm hoặc $v_1-v_2\ge4.79$, và track lồi được thỏa từ điểm đánh giá thứ hai trở đi; vì vậy dòng $\delta$ của Bảng 8 là một phép kiểm tra tính nhất quán, không phải bằng chứng về vai trò của $\delta$.

### 56. Câu bị xóa trước đoạn "Reproducibility"

- **Trước:** The experiments support neither universal speed superiority nor a finite-budget robustness claim.
  → Các thực nghiệm không ủng hộ ưu thế tốc độ phổ quát, cũng không ủng hộ khẳng định về độ bền trong ngân sách hữu hạn.
- **Sau:** *(xóa; ý này đã có ở Abstract và Conclusion)*

### 57. Đoạn "Reproducibility"

- **Trước:** In this environment the package also reproduces exactly every numerical entry of Tables 1–5 (Tables 4 and 5 from unrounded scores) and of Table 6, and the counts quoted in Sections 4.3 and 4.4.
  → Trong môi trường này, gói mã còn tái tạo chính xác mọi giá trị số trong Bảng 1–5 (Bảng 4 và 5 từ điểm chưa làm tròn) và Bảng 6, cùng các số đếm nêu ở Mục 4.3 và 4.4.
- **Sau:** With Python 3.13.4 and NumPy 2.1.3, the package also reproduces exactly every numerical entry of Tables 1–5 (Tables 4 and 5 from unrounded scores) and of Table 6, and the counts quoted in Sections 4.3 and 4.4.
  → Với Python 3.13.4 và NumPy 2.1.3, gói mã còn tái tạo chính xác mọi giá trị số trong Bảng 1–5 (Bảng 4 và 5 từ điểm chưa làm tròn) và Bảng 6, cùng các số đếm nêu ở Mục 4.3 và 4.4.

---

## F. Mục 5. Conclusion — viết lại toàn bộ

**Trước**
1. We studied normal-box nonlinear split feasibility with convex and pseudoconvex component functions.
   → Ta đã nghiên cứu bài toán chấp nhận tách phi tuyến với hộp chuẩn và các hàm thành phần lồi và giả lồi.
2. DTAP combines a residual-scaled convex step with a safeguarded pseudoconvex step and projects onto the base set.
   → DTAP kết hợp một bước lồi co theo phần dư với một bước giả lồi có chặn an toàn và chiếu lên tập cơ sở.
3. Its whole-sequence convergence follows from quasi-Fejér descent and the existence of one feasible cluster point.
   → Sự hội tụ của toàn bộ dãy suy ra từ tính giảm tựa Fejér và sự tồn tại của một điểm tụ khả thi.
4. No prescribed regularity modulus is needed to execute the method, but continuity, consistency, and local bounds remain essential to the analysis.
   → Không cần biết trước mô-đun chính quy nào để chạy phương pháp, nhưng tính liên tục, tính nhất quán và các cận địa phương vẫn thiết yếu cho phân tích.
5. The proportional weight is an admissible residual-responsive choice, not an optimality result.
   → Trọng số tỉ lệ là một lựa chọn chấp nhận được, phản ứng theo phần dư, không phải một kết quả về tính tối ưu.
6. The feature-selection criterion with a positive-semidefinite quadratic numerator and positive affine denominator is convex, so that application illustrates a convex special case.
   → Tiêu chí chọn đặc trưng có tử số toàn phương nửa xác định dương và mẫu số affine dương là lồi, nên ứng dụng đó minh họa một trường hợp riêng lồi.
7. The activity measurements and controlled nonconvex tests distinguish these settings.
   → Các phép đo mức hoạt động và các phép thử không lồi có kiểm soát phân biệt các bối cảnh này.
8. Tuned subgradient methods can match or outperform DTAP, and initialization and scaling affect performance within a finite budget.
   → Các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, và điểm khởi đầu cùng thang bước ảnh hưởng tới hiệu năng trong một ngân sách hữu hạn.
9. The best-iterate bound in Remark 5 concerns only the convex-track residual.
   → Cận cho điểm lặp tốt nhất ở Nhận xét 5 chỉ liên quan đến phần dư của track lồi.
10. Rates for the full residual and performance guarantees under additional geometric assumptions remain open.
    → Tốc độ cho toàn bộ phần dư và các bảo đảm hiệu năng dưới các giả thiết hình học bổ sung vẫn còn là vấn đề mở.

**Sau**
1. DTAP solves normal-box nonlinear split feasibility problems with convex and pseudoconvex components by combining a residual-scaled convex step with a safeguarded pseudoconvex step.
   → DTAP giải các bài toán chấp nhận tách phi tuyến với hộp chuẩn và các thành phần lồi và giả lồi, bằng cách kết hợp một bước lồi co theo phần dư với một bước giả lồi có chặn an toàn.
2. Under consistency and continuous differentiability, the whole sequence converges to a feasible point; no regularity modulus is an input, although the analysis uses bounds on a compact set containing the iterates.
   → Dưới giả thiết nhất quán và khả vi liên tục, toàn bộ dãy hội tụ tới một điểm khả thi; không có mô-đun chính quy nào là đầu vào, mặc dù phân tích dùng các cận trên một tập compact chứa dãy lặp.
3. In the feature-selection application all constraints are convex, and test problems with a nonconvex pseudoconvex constraint exercise the pseudoconvex track.
   → Trong ứng dụng chọn đặc trưng, mọi ràng buộc đều lồi, và các bài toán thử có ràng buộc giả lồi không lồi kiểm tra track giả lồi.
4. In the experiments, tuned subgradient methods can match or outperform DTAP, whose finite-budget performance depends on the starting point and the step scale.
   → Trong thực nghiệm, các phương pháp dưới gradient đã tinh chỉnh có thể bằng hoặc tốt hơn DTAP, mà hiệu năng trong ngân sách hữu hạn của nó phụ thuộc vào điểm xuất phát và thang bước.
5. Rates for the full residual $J(x^k)$, beyond the convex-track bound of Remark 5, and guarantees under error-bound conditions remain open.
   → Tốc độ cho toàn bộ phần dư $J(x^k)$, ngoài cận của track lồi ở Nhận xét 5, và các bảo đảm dưới điều kiện cận sai số vẫn còn là vấn đề mở.

---

## Phụ lục. Các thay đổi chỉ về ký hiệu (không liệt kê chi tiết ở trên)

| Vị trí | Trước | Sau |
|---|---|---|
| Chứng minh Bổ đề 3.8 và Mệnh đề 3.11 (tham số Young) | $\epsilon$ | $\zeta$ (tránh trùng với ngưỡng dừng $\varepsilon$) |
| (15) | có định nghĩa $\Phi^{\rm ps}(x)$ | bỏ $\Phi^{\rm ps}(x)$ (không được dùng ở đâu) |
| Chứng minh Định lý 3.12, đoạn "Reaching the contradiction" | $L'$ | $L'_B$ (như trong Bổ đề 3.7) |
| (41), chứng minh Mệnh đề 4.1 | $D_\rho$ | $U_\rho$ |
| Định nghĩa SG (mục 44) | $D_k$, $x^k$ | $\mathcal I_k$, $w^k$ |
| Nhận xét 6 | "including $Q$" | "including $Q_R$" |
| Mục 4.2.2 (kiểm định signed-rank) | "all-zero pairs have $p=1$" → *các cặp toàn số 0 có $p=1$* | "all-zero pairs receive the $p$-value $1$" → *các cặp toàn số 0 nhận giá trị $p$ bằng 1* |
| Đầu Mục 4.1 (câu thêm) | — | "Here $n$ is the number of samples; subscripts index features and superscripts index iterations." → *Ở đây $n$ là số mẫu; chỉ số dưới đánh số đặc trưng, chỉ số trên đánh số vòng lặp.* |
| Mục 4.2.2 (câu thêm) | — | "We denote the voted feature set by $A^\star$." → *Ta ký hiệu tập đặc trưng được bỏ phiếu chọn là $A^\star$.* |
