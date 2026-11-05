#!/usr/bin/env python3
"""Apply every proposal of proposed_edits.md to a copy of the revised manuscript.

Reads  DTAP Finally/main_document.tex  (unchanged)
Writes DTAP Finally/main_document_v2.tex
Every replacement must match exactly once; otherwise the script stops.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "DTAP Finally" / "main_document.tex"
DST = ROOT / "DTAP Finally" / "main_document_v2.tex"

s = SRC.read_text(encoding="utf-8")


def rep(old, new, tag):
    global s
    n = s.count(old)
    if n != 1:
        sys.exit("[%s] expected 1 match, found %d:\n%s" % (tag, n, old[:200]))
    s = s.replace(old, new)


# ---------------------------------------------------------------- front matter
rep("Adaptive step size; Strong convergence; Feature selection",
    "Adaptive step size; Global convergence; Feature selection", "G4 keyword")

a = s.index("\\begin{abstract}\n") + len("\\begin{abstract}\n")
b = s.index("\n\\end{abstract}")
s = s[:a] + (
    r"We study a nonlinear split feasibility problem in $\R^n$ whose output set is a normal box "
    r"and whose components are differentiable and either convex or pseudoconvex. The Dual-Track "
    r"Adaptive Projection (DTAP) algorithm splits the constraints into a convex and a pseudoconvex "
    r"track. It takes a residual-scaled Polyak-type step on the nearly most violated convex "
    r"constraints and a safeguarded diminishing step on the nearly most violated pseudoconvex ones, "
    r"combines the two steps by a proportional weight, and projects onto the base set. The weight "
    r"is a residual-responsive choice, without a claim of optimality. The step sizes require no "
    r"prescribed operator norm, Lipschitz constant, or H\"older modulus; the proof uses bounds over "
    r"a bounded set containing the iterates. If the problem is consistent and the components are "
    r"continuously differentiable, the whole sequence converges to a feasible point. In a "
    r"feature-selection application all three constraints are convex. Experiments with "
    r"constraint-activity counts, tuned subgradient methods and nonconvex pseudoconvex test "
    r"problems show that tuned subgradient methods can match or outperform DTAP, and that DTAP is "
    r"sensitive to its starting point and step scale.") + s[b:]

# ---------------------------------------------------------------- Introduction
rep(r"The split feasibility problem (SFP) models constrained reconstruction~\citep{censor1994}. For closed convex sets $C\subseteq\R^n$, $Q\subseteq\R^m$, and a matrix $\mathcal A$, it seeks",
    r"The split feasibility problem (SFP) was introduced by Censor and Elfving~\citep{censor1994} as a model for constrained inverse problems. Given nonempty closed convex sets $C\subseteq\R^n$ and $Q\subseteq\R^m$ and a matrix $\mathcal A\in\R^{m\times n}$, it asks to", "7-8")
rep(r"Byrne's $CQ$ algorithm~\citep{byrne2002} uses", r"Byrne's $CQ$ algorithm~\citep{byrne2002} iterates", "9")
rep(r"Supporting half-spaces simplify projections~\citep{yang2004}, while self-adaptive steps reduce parameter dependence~\citep{zhang2009adaptive,zhao2011adaptive,lopez2012}. Operator splitting~\citep{zhang2012simultaneous} and modified alternating directions~\citep{yang2014alternating} provide decomposition strategies. Adaptive steps and decomposition are therefore established principles.",
    r"Here $\norm{\mathcal A}$ is the spectral norm of $\mathcal A$. Relaxed variants project onto supporting half-spaces~\citep{yang2004}; self-adaptive steps avoid estimating $\norm{\mathcal A}$~\citep{zhang2009adaptive,zhao2011adaptive,lopez2012}; operator splitting~\citep{zhang2012simultaneous} and alternating direction methods~\citep{yang2014alternating} decompose the problem. These ideas are standard; DTAP adapts them to the nonlinear case.", "9-11")
rep("We study the nonlinear SFP\n\\begin{equation}\\label{eq:nsfp-intro}",
    "Replacing $\\mathcal A$ by a nonlinear map $F$ gives the nonlinear SFP~\\citep{li2013nsfp,yen2019}\n\\begin{equation}\\label{eq:nsfp-intro}", "12")
rep(r"where $K\subseteq\R^n$ is closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$, and each differentiable component of $F=(F_1,\ldots,F_m)$ is convex or pseudoconvex on $K$. Pseudoconvex functions have convex sublevel sets, so the feasible set is convex even when some components are nonconvex. We seek feasibility, rather than minimization of every component.",
    r"where $K\subseteq\R^n$ is nonempty, closed and convex, $Q=\prod_{i=1}^m(-\infty,b_i]$ is a normal box, and each $F_i$ is differentiable and convex or pseudoconvex on $K$. Since pseudoconvex functions have convex sublevel sets, the feasible set $\Omega=\{x\in K:F(x)\in Q\}$ is convex. We seek a point of $\Omega$, not a minimizer of any $F_i$.", "13-15")
rep(r"Nonlinear SFP and generalized convex feasibility have several relevant antecedents. Li et al.~\citep{li2013nsfp} use a convex aggregate proximity function, a property not ensured by componentwise pseudoconvexity. Yen et al.~\citep{yen2019} combine equilibrium and nonlinear image constraints. Hu et al.~\citep{hu2022quasi} treat quasiconvex inequalities, which include our component class. Our method exploits the additional derivative information of convex components within this established feasibility setting.",
    r"Li et al.~\citep{li2013nsfp} assume a convex aggregate proximity function, which componentwise pseudoconvexity does not ensure. Yen et al.~\citep{yen2019} use the same max-type violation measure and active-set device, but require quasilinear components, a class incomparable with ours. Hu et al.~\citep{hu2022quasi} treat quasiconvex inequalities, which contain our class, without using the gradient inequality of convex components.", "16-18")
rep("The box gives the explicit violation measure",
    r"Because $Q$ is a box, the $\ell_\infty$-distance from $F(x)$ to $Q$ has the closed form", "19")
a = s.index(r"The Dual-Track Adaptive Projection algorithm (\dtap) forms violation-weighted")
b = s.index("Continuous gradients need not be Lipschitz.", a) + len("Continuous gradients need not be Lipschitz.")
s = s[:a] + (
    r"DTAP splits the constraints into a convex track and a pseudoconvex track. On each track it "
    r"sums the gradients of the nearly most violated constraints, weighted by their violations. The "
    r"gradient inequality of convex functions justifies a residual-scaled Polyak-type step on the "
    r"convex track~\citep{polyak1969,lopez2012}; pseudoconvexity gives only the sign of a "
    r"directional derivative, so the pseudoconvex track uses a safeguarded diminishing step. A "
    r"proportional weight combines the two steps, and the result is projected onto $K$; the proof "
    r"uses this weight only to keep a persistently violated track active "
    r"(Remark~\ref{rem:weight-scope}). No prescribed operator norm, Lipschitz constant, or "
    r"H\"older modulus is needed: a quasi-Fej\'er inequality shows that the iterates are bounded, "
    r"and the proof then uses local bounds, without Lipschitz gradients.") + s[b:]
a = s.index(r"Feature-selection criteria from fractional and fuzzy-rough models")
b = s.index("tuned subgradient methods can match or outperform DTAP.", a) + len("tuned subgradient methods can match or outperform DTAP.")
s = s[:a] + (
    r"As an application, upper bounds on three criteria from a fractional "
    r"model~\citep{wang2021fractional} and a fuzzy-rough model~\citep{wang2026afrsfcv} define the "
    r"constraints; a feasible weight vector satisfies all three bounds but need not solve either "
    r"source problem. These constraints are convex (Proposition~\ref{prop:fs-reg}), so we also use "
    r"test problems with a nonconvex pseudoconvex constraint to exercise the pseudoconvex track.") + s[b:]
rep(r"\item A dual-track method combines convex decrease estimates and pseudoconvex sign information through an adaptive weight.",
    r"\item A dual-track method that uses the gradient inequality on the convex constraints and only sign information on the pseudoconvex ones, without assuming a convex proximity function, unlike~\citep{li2013nsfp}, or a H\"older modulus, unlike the dynamic step of~\citep{hu2022quasi}.", "C1")
rep(r"\item Under consistency, smoothness, and the stated step conditions, the whole sequence converges to a feasible point in finite-dimensional Euclidean space. Convergence of distances and one feasible cluster point suffice.",
    r"\item Convergence of the whole sequence to a feasible point under Assumption~\ref{ass:standing} (Theorem~\ref{thm:strong}).", "C2")
rep(r"\item Experiments distinguish prediction from feasibility cost and report constraint activity, tuned subgradient comparisons, and initialization and scaling sensitivity. They do not establish uniform superiority.",
    r"\item Experiments that report constraint activity, compare DTAP with tuned subgradient methods, and measure its sensitivity to the starting point and the step scale.", "C3")

# ---------------------------------------------------------------- Section 2
rep(r"Throughout, $H=\R^n$ is Euclidean space", r"Throughout, $H=\R^n$ is the Euclidean space", "31")
rep(r"This characterization gives the projection inequality used in Lemma~\ref{lem:proj-nonexp}. The sort-based projection onto a $p$-dimensional simplex takes $O(p\log p)$ operations~\citep{condat2016simplex}.",
    r"This characterization yields Lemma~\ref{lem:proj-nonexp} below.", "32-33")
rep(r"A function differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for every $x,y\in K$,",
    r"A function $f$ that is differentiable on an open neighbourhood of $K$ is pseudoconvex on $K$ if, for all $x,y\in K$,", "34")
rep(" This distinction is relevant to the mixed constraint functions studied below.", "", "36")

# ---------------------------------------------------------------- Section 3
rep("Then $F(x)\\in Q$ iff $J(x)=0$, so finding a feasible point amounts to minimizing $J$\nover $K$.",
    "Then $x\\in K$ is feasible if and only if $J(x)=0$; when $\\Omega\\ne\\emptyset$, the feasible\npoints are the minimizers of $J$ over $K$.", "38")
rep(r"\subsection{Decomposition and dual-track scalarization}", r"\subsection{Decomposition into two tracks}", "37")
rep("We split the constraint index set into a \\emph{convex track} and a\n\\emph{pseudoconvex track}.",
    "We split $I:=\\{1,\\dots,m\\}$ into a \\emph{convex track} $I^{\\cvx}$ and a\n\\emph{pseudoconvex track} $I^{\\ps}$, each with its own step rule.", "G2")
rep("For $x\\in U$ define the componentwise violations and the\nmaximal violation\n",
    "For $x\\in U$ define the componentwise violations\n", "G12a")
rep("v_i(x):=\\bigl(F_i(x)-b_i\\bigr)^+,\\qquad J(x)=\\max_{1\\le i\\le m}v_i(x).",
    "v_i(x):=\\bigl(F_i(x)-b_i\\bigr)^+,", "G12b")
rep("Thus $x\\in\\Omega$ iff $x\\in K$ and $J(x)=0$. Partition $I:=\\{1,\\dots,m\\}$ into disjoint\ngroups $I=I^{\\cvx}\\cup I^{\\ps}$, where $I^{\\cvx}$ indexes the convex constraints and\n$I^{\\ps}$ the pseudoconvex ones (made precise in Assumption~\\ref{ass:standing}). The\n\\emph{per-track maximal violations} are",
    "so that $J(x)=\\max_i v_i(x)$ by~\\eqref{eq:Jdef}. Assumption~\\ref{ass:standing} makes the\npartition precise. The \\emph{per-track maximal violations} are", "G2b")
rep("we replace the exact maximizers by a $\\delta$-enlarged \\emph{approximate active\nset} on each track:",
    "we replace the set of indices at which the maximum is attained by a $\\delta$-enlarged\n\\emph{approximate active set} on each track (`active' meaning within $\\delta$ of the largest\nviolation):", "39/G6")
rep("\\Phi^{\\ps}(x)&:=\\tfrac12\\!\\!\\sum_{j\\in K^{\\ps}(x)}\\!\\! v_j(x)^2, & g^{\\ps}(x)",
    "& & g^{\\ps}(x)", "G12c")
rep("\\textup{(a)} $\\Omega\\ne\\emptyset$. \\textup{(b)} $I=\\{1,\\dots,m\\}$\nis partitioned as $I=I^{\\cvx}\\cup I^{\\ps}$; for each $i$, $F_i:U\\to\\R$, and the\nrestriction $F_i|_K$ is convex if $i\\in I^{\\cvx}$ and pseudoconvex if $i\\in I^{\\ps}$.",
    "\\textup{(a)} $\\Omega\\ne\\emptyset$ (consistency). \\textup{(b)} $I=\\{1,\\dots,m\\}$\nis partitioned as $I=I^{\\cvx}\\cup I^{\\ps}$; each $F_i:U\\to\\R$ is convex on $K$ if\n$i\\in I^{\\cvx}$ and pseudoconvex on $K$ if $i\\in I^{\\ps}$.", "G5/40")
rep("through the soft weight $\\mu_k$", "through the proportional weight $\\mu_k$", "G1a")
rep("\\algstep{Step 1 (per-track quantities).}\n",
    "\\algstep{Step 1 (per-track quantities).} If $J(x^k)\\le\\varepsilon$, stop and return $x^k$; otherwise:\n", "42a")
rep("\\item[(1e)] Soft proportional weight:", "\\item[(1e)] Proportional weight:", "G1b")
rep("\\algstep{Step 2 (projection).}\\quad $x^{k+1}=P_K(y^k)$.\n\n\\algstep{Step 3 (stopping).}\\quad If $J(x^k)\\le\\varepsilon$, stop and return $x^k$;\notherwise set $k\\leftarrow k+1$ and go to Step~1.",
    "\\algstep{Step 2 (projection).}\\quad $x^{k+1}=P_K(y^k)$; set $k\\leftarrow k+1$ and go to Step~1.", "42b")
rep("we do not claim that it is the only convergent choice or that it is optimal.",
    "we do not claim that it is the only choice for which DTAP converges, or that it is optimal.", "43a")
rep("Although the one-step inequality holds for\nany $\\mu_k\\in[0,1]$, this alone does not establish convergence for every such sequence.",
    "Although the one-step inequality of Lemma~\\ref{lem:fejer} holds\nfor every $\\mu_k\\in[0,1]$, it does not by itself imply convergence for every weight sequence.", "43b")
rep("The parameters $\\rho_{\\cvx}$, $\\delta$, and $\\{\\gamma_k\\}$ remain part of the algorithm.",
    "The user still chooses $\\rho_{\\cvx}$, $\\delta$, and $\\{\\gamma_k\\}$; these parameters do not\ndepend on any constant of the problem.", "44")

# move the analysis overview (309-323) to the start of 3.6 and rewrite its first paragraph
a = s.index("The convergence analysis of \\dtap{} is more involved than")
m = s.index("Throughout, $\\{x^k\\}$ is the infinite sequence generated by Algorithm~\\ref{alg:dtap}", a)
b = s.index("\\subsection{Auxiliary lemmas}", m)
throughout = s[m:b].strip()
s = s[:a] + s[b:]
overview = (
    "The two tracks need different arguments. On the convex track, Lemma~\\ref{lem:grad-cvx} bounds\n"
    "$\\inner{\\nabla F_i(x)}{x-x^\\star}$ from below by the violation $v_i(x)$; this gives a decrease of\n"
    "$\\norm{x^k-x^\\star}^2$ of order $\\mu_kT_k$. On the pseudoconvex track,\n"
    "definition~\\eqref{eq:contrapositive} gives only the sign of this inner product.\n"
    "Lemma~\\ref{lem:fejer} combines both tracks in one quasi-Fej\\'er inequality; the choice of the\n"
    "parameter $\\zeta$ in Young's inequality keeps the convex-track term negative. Stage~2 of\n"
    "Theorem~\\ref{thm:strong} then shows, by contradiction, that at least one cluster point is\n"
    "feasible, and Stage~3 shows that the whole sequence converges to it. The two degenerate cases\n"
    "follow as corollaries.\n\n" + throughout + "\n\n")
rep("\\subsection{Auxiliary lemmas}\\label{ssec:aux}\nWe begin with two preparatory results used repeatedly below.",
    "\\subsection{Auxiliary lemmas}\\label{ssec:aux}\n" + overview + "We begin with two preparatory results used repeatedly below.", "45/G13")

rep("applying the contrapositive~\\eqref{eq:contrapositive}\nwith $y=x^\\star$", "applying~\\eqref{eq:contrapositive}\nwith $y=x^\\star$", "G11a")
rep("the contrapositive~\\eqref{eq:contrapositive} with $x=\\bar x$, $y=x^\\star$",
    "definition~\\eqref{eq:contrapositive} with $x=\\bar x$, $y=x^\\star$", "G11b")
rep("The following quasi-Fej\\'er inequality, within the framework of~\\citet{combettes2001quasifejer}, yields boundedness of $\\{x^k\\}$ and decay of the convex-track violation. Set",
    "The following inequality is of quasi-Fej\\'er type in the sense of\nCombettes~\\citep{combettes2001quasifejer}. It yields boundedness of $\\{x^k\\}$ and decay of the\nconvex-track violation. Set", "47")
s = re.sub(r"\\epsilon(?![a-zA-Z])", r"\\zeta", s)      # G7: Young parameter
rep("Assume $I^{\\cvx}\\ne\\emptyset$ and\nput $B:=", "Assume $I^{\\cvx}\\ne\\emptyset$, fix\n$x^\\star\\in\\Omega$, and put $B:=", "48a")
rep("Fix $x^\\star\\in\\Omega$. Remark~\\ref{rem:grad-cvx-sum} gives\n$\\inner{g^{\\cvx}_k}{x^k-x^\\star}\\ge2\\Phi^{\\cvx}_k>0$",
    "Remark~\\ref{rem:grad-cvx-sum} gives\n$\\inner{g^{\\cvx}_k}{x^k-x^\\star}\\ge2\\Phi^{\\cvx}_k>0$", "48b")
rep("\\subsection{Strong convergence to a feasible point}", "\\subsection{Convergence to a feasible point}", "G4a")
rep("The goal of the analysis is strong convergence of $\\{x^k\\}$ to a feasible point. The\nargument has three stages: exploit convex-track feasibility (Lemma~\\ref{lem:jcvx0}) to\nconfine the cluster set to the convex half; use a contradiction argument with\npseudoconvexity to produce a cluster point in $\\Omega$; and combine with distance\nconvergence to upgrade to convergence of the whole sequence.",
    "We now prove that the whole sequence converges to a feasible point. The proof has three\nstages. Stage~1 uses Lemma~\\ref{lem:jcvx0} to show that every cluster point satisfies the\nconvex constraints. Stage~2 shows, by contradiction and pseudoconvexity, that at least one\ncluster point is feasible. Stage~3 uses the convergence of $\\norm{x^k-\\bar x}$ to show that\nthe whole sequence converges to that point.", "49")
n = s.count("converges strongly to")
if n != 3:
    sys.exit("[G4] expected 3 'converges strongly to', found %d" % n)
s = s.replace("converges strongly to", "converges to")
rep("\\emph{Stage 1 (convex half).}", "\\emph{Stage 1 (convex constraints).}", "49a")
rep("\\emph{Stage 2 (pseudoconvex half by contradiction).}", "\\emph{Stage 2 (a feasible cluster point).}", "49b")
rep("This argument requires neither uniqueness of the feasible point nor convexity of the\ntarget set: one feasible cluster point and convergence of its distance suffice.",
    "The argument does not require $\\Omega$ to be a singleton: one feasible cluster point and\nthe convergence of its distance suffice.", "50")
a = s.index("Larger $\\delta$ enlarges $K^{\\cvx}_k,K^{\\ps}_k$")
b = s.index("not evidence about $\\delta$.", a) + len("not evidence about $\\delta$.")
s = s[:a] + ("Larger $\\delta$ enlarges $K^{\\cvx}_k$ and $K^{\\ps}_k$, which may improve numerical\n"
             "stability when several $v_i(x^k)$ are nearly equal.") + s[b:]
rep("$\\norm{g^{\\ps}_k}\\le\\abs{I^{\\ps}}V_B L'$ with\n$L':=", "$\\norm{g^{\\ps}_k}\\le\\abs{I^{\\ps}}V_B L'_B$ with\n$L'_B:=", "52a")
rep("$G':=\\max\\{1,\\abs{I^{\\ps}}V_B L'\\}$", "$G':=\\max\\{1,\\abs{I^{\\ps}}V_B L'_B\\}$", "52b")

# ---------------------------------------------------------------- Section 4
rep(" These two scopes are stated separately below.", "", "III-744")
rep("$y\\in\\{1,\\ldots,r\\}^n$ the class labels.",
    "$y\\in\\{1,\\ldots,r\\}^n$ the class labels. Here $n$ is the number of samples; subscripts index features and superscripts index iterations.", "53")
rep("and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$. Entropy",
    "and $I(Z_i;Z_j;C)=I(Z_i;C)+I(Z_j;C)-I((Z_i,Z_j);C)$ is their interaction information. Entropy", "54")
rep("The three terms measure label-approximation error, incorrect-decision confidence, and Tikhonov regularization, respectively.",
    "The three terms are the label-approximation error, the weight of misclassifying features per sample, and a Tikhonov term.", "55")
rep("D_\\rho=\\{w:\\rho^{\\top}w>0\\}", "U_\\rho=\\{w:\\rho^{\\top}w>0\\}", "G7-Urho-a")
rep("the first two components of~", "the first two terms of~", "56")
rep(" A feasible weight need not minimize either baseline objective.", "", "III-807")
rep("It satisfies the function assumptions of Assumption~\\ref{ass:standing} whenever $\\Omega\\ne\\varnothing$.",
    "Hence~\\eqref{eq:nsfp-fs} satisfies (A1) and (A2) of Assumption~\\ref{ass:standing}, with $U=U_\\rho$, whenever $\\Omega\\ne\\varnothing$.", "57")
rep("the open half-space $D_\\rho$", "the open half-space $U_\\rho$", "G7-Urho-b")
rep("For $w\\in D_\\rho$ and any direction", "For $w\\in U_\\rho$ and any direction", "G7-Urho-c")
a = s.index("The assignment $I^{\\cvx}=\\{1,2\\}$, $I^{\\ps}=\\{3\\}$ used in the experiments is admissible")
b = s.index("requires that the floor remain inactive.", a) + len("requires that the floor remain inactive.")
s = s[:a] + (
    "The experiments use $I^{\\cvx}=\\{1,2\\}$, $I^{\\ps}=\\{3\\}$, which is admissible since convex "
    "functions are pseudoconvex; DTAP then uses only sign information for $F_3$, so no genuinely "
    "nonconvex constraint is tested. The all-convex assignment $I^{\\cvx}=\\{1,2,3\\}$ is also "
    "admissible, and Theorem~\\ref{thm:strong} applies to both. Proposition~\\ref{prop:fs-reg} needs "
    "$\\min_k\\rho_k>0$; on all instances used here the smallest score is $4.77\\times10^{-5}$. Hence "
    "the safeguard $\\max\\{\\rho^\\top w,10^{-15}\\}$ in the implementation is never active, and the "
    "implemented $F_3$ is~\\eqref{eq:fsF3}.") + s[b:]
a = s.index("Externally specified thresholds remain fixed.")
b = s.index("reported with the experiments.", a) + len("reported with the experiments.")
s = s[:a] + (
    "The thresholds are calibrated on the training data: $b_i$ is the $q_i$-th percentile of $F_i$ "
    "over $3\\,000$ Dirichlet points (seed $42$) and the $p$ vertices of $K$, where a fixed rule "
    "chooses $q_i$ from the sample size, the number of features and classes, and the class "
    "imbalance (supplementary metadata). All solvers share these thresholds. Calibrating each $b_i$ "
    "separately does not guarantee $\\Omega\\ne\\varnothing$; Section~\\ref{ssec:feasibility-audit} "
    "checks feasibility numerically. Prescribed thresholds would be used as given.") + s[b:]
rep("Simplex projection costs $O(p\\log p)$.",
    "Projection onto $K=\\Delta_{p-1}$ by sorting costs $O(p\\log p)$ operations~\\citep{condat2016simplex}.", "32b")
rep("storage, including $Q$.", "storage, including $Q_R$.", "61")
rep("SG-const uses step $10^{-3}$. The dynamic subgradient comparison is considered separately with sampled and empirically tuned moduli in the solver diagnostic.",
    "SG-const uses the step $\\nu_k=10^{-3}$ and SG-dyn the sampled modulus $\\widehat L$ (Section~\\ref{sssec:baselines}); tuned moduli are considered only in Section~\\ref{ssec:feasibility-audit}.", "62")
rep("The following updates specify the two baseline solvers for the models in Sections~\\ref{sssec:nfscore} and~\\ref{sssec:afrsfcv-model}.",
    "The following paragraphs specify the baseline solvers: N-Fscore and AFRSFCV for the models of Sections~\\ref{sssec:nfscore} and~\\ref{sssec:afrsfcv-model}, and the subgradient methods SG-const and SG-dyn.", "64")
rep("We integrate~\\eqref{eq:pnn} by explicit Euler on $[0,T]$ with $N_{\\mathrm{step}}$ steps under a fixed budget (no stopping rule), with the fixed parameters reported in the experimental protocol, and take as weight vector the projection $P_K\\bigl(g(u(T))\\bigr)$ of the network output at the final time onto the simplex $K$.",
    "We integrate~\\eqref{eq:pnn} by the explicit Euler method on a uniform grid of $N_{\\mathrm{grid}}$ points in $[0,T]$, without a stopping rule, using the parameters of Section~\\ref{ssec:setup}. The weight vector is the projection $P_K\\bigl(g(u(T))\\bigr)$ of the final network output onto $K$.", "65")
anchor = "the final weight $w^\\star=w(\\tau^T)\\in K$ feeds the shared selection rule of Section~\\ref{ssec:selection}."
rep(anchor, anchor + "\n\n"
    "\\paragraph*{SG-const and SG-dyn}\n"
    "These subgradient methods for quasiconvex feasibility~\\citep{hu2022quasi} follow its\n"
    "most-violated-constraint strategy: with $\\mathcal I_k=\\argmax_i v_i(w^k)$,\n"
    "\\[\n"
    "w^{k+1}=P_K(w^k-\\nu_k\\bar h_k),\\qquad\n"
    "\\bar h_k=\\frac1{|\\mathcal I_k|}\\sum_{i\\in\\mathcal I_k}\\frac{\\nabla F_i(w^k)}{\\|\\nabla F_i(w^k)\\|}.\n"
    "\\]\n"
    "SG-const uses $\\nu_k=10^{-3}$; SG-dyn uses the dynamic step $\\nu_k=J(w^k)/L$ (H\\\"older\n"
    "exponent $1$), with $L=\\widehat L$, the largest gradient norm at $500$ points sampled in $K$.", "G8")
rep("$\\lfloor N_f/2\\rfloor+1$ folds.", "$\\lfloor N_f/2\\rfloor+1$ folds. We denote the voted feature set by $A^\\star$.", "G10")
a = s.index("No classifier parameter or vote threshold")
b = s.index("not an end-to-end or nested-validation study.", a) + len("not an end-to-end or nested-validation study.")
s = s[:a] + (
    "The test data are not used to select features or to choose any parameter or vote threshold.\n"
    "The training/test split is fixed before the selections are computed, and the rule that chooses\n"
    "the threshold levels uses only the sample size, the number of features, the number of classes\n"
    "and the class sizes of the whole dataset, not any feature values. Because a single split is\n"
    "used, this is an exploratory evaluation, not an end-to-end or nested-validation study.") + s[b:]
rep("Here $\\bar Z_j=N_f^{-1}\\sum_b Z_{bj}$; the unbiased variance correction is\n$N_f/(N_f-1)$, not $p/(p-1)$.",
    "Here $\\bar Z_j=N_f^{-1}\\sum_b Z_{bj}$, and $s_j^2$ is the unbiased variance over the $N_f$\nfolds.", "67")
rep("all-zero pairs have $p=1$.", "all-zero pairs receive the $p$-value $1$.", "68")
rep("$0.822$;\nthus the results support moderate reduction rather than uniform sparsity\nor stability superiority.",
    "$0.822$.\nThus DTAP reduces the number of features moderately; it does not select sparser or more\nstable sets than the base models.", "69")
rep("The per-dataset exceptions\nare included in Table~\\ref{tab:acc}, and all five methods appear in the summary.",
    "The SG results on Spambase, the only\ndataset where they differ from DTAP, are given below Table~\\ref{tab:acc};\nTable~\\ref{tab:perf-summary} includes all five methods.", "70")
a = s.index("The percentile calibration defines experimental thresholds;")
b = s.index("consistency remains an\nassumption.", a) + len("consistency remains an\nassumption.")
s = s[:a] + "As noted in Section~\\ref{ssec:reduction}, the calibrated thresholds need not yield\n$\\Omega\\ne\\varnothing$." + s[b:]
a = s.index("For the full-data instances below, saved numerical witnesses")
b = s.index("with minimum $5.99\\times10^{-5}$.", a) + len("with minimum $5.99\\times10^{-5}$.")
s = s[:a] + (
    "For each full-data instance below, we keep the evaluated point with the largest slack\n"
    "$\\min_i(b_i-F_i(w))$ over all runs. Re-evaluated on matrices rebuilt from the data, each of\n"
    "these points satisfies all three inequalities strictly; the smallest slack is\n"
    "$4.33\\times10^{-4}$. This is a numerical check, not an exact certificate of feasibility.") + s[b:]
a = s.index("We measure the frequency of $F_3(w^k)-b_3>10^{-6}$")
b = s.index("from the eight-dataset classification study.", a) + len("from the eight-dataset classification study.")
s = s[:a] + (
    "We count the iterates of a run, including the last (its evaluated points), at which\n"
    "$F_3(w^k)-b_3>10^{-6}$. This measures violation along the trajectory, rather than whether the\n"
    "constraint is binding at its limit. Table~\\ref{tab:activation-tuning} shows that, from the\n"
    "standard start, $F_3$ is violated at no evaluated point on seven of the eight classification\n"
    "datasets, and at one of the $48$ evaluated points on Abalone. Since $F_3$ is convex\n"
    "(Proposition~\\ref{prop:fs-reg}), these feature-selection instances test a convex subclass and\n"
    "do not demonstrate a need for the nonconvex extension. We also report the all-convex\n"
    "comparator (AC), which assigns all three constraints to the convex track.") + s[b:]
a = s.index("SG-const uses $\\nu_k=10^{-3}$. For SG-dyn,\n$\\widehat L$ is the largest gradient norm")
b = s.index("The tuned variant selects $L=c\\widehat L$", a) + len("The tuned variant selects")
s = s[:a] + ("SG-const and SG-dyn are defined in Section~\\ref{sssec:baselines}. Besides SG-dyn with the\n"
             "sampled modulus $\\widehat L$, a tuned variant selects") + s[b:]
rep("the values of $J$\nalong the two trajectories differ by at most $3.18\\times10^{-5}$ relative to AC,",
    "the values of $J$\nalong the two trajectories satisfy $|J_{\\rm DTAP}-J_{\\rm AC}|\\le3.18\\times10^{-5}\\,J_{\\rm AC}$ at\nevery evaluated point,", "79")
rep("differ only from the random starts", "differ only on the random starts", "80")
rep("it assigns\nequal weights when both tracks are nonzero and full weight to the sole\nnonzero track. Thus these tests do not establish a uniform advantage of\nresidual-share weighting or robustness to initialization.",
    "it assigns\nequal weights when both tracks are violated and full weight to the only violated track\notherwise. Thus these tests do not establish a uniform advantage of the proportional weight\nor robustness to initialization.", "81/G1")
rep("To exercise the third track directly", "To exercise the pseudoconvex track directly", "G3")
rep("evaluations of its tuning search.\nWith $\\nu_k=10^{-3}$", "evaluations of its tuning search.\n\nWith $\\nu_k=10^{-3}$", "82a")
rep("evaluated points.\nAll DTAP failures occur", "evaluated points.\n\nAll DTAP failures occur", "82b")
rep("that is best in general.\n",
    "that is best in general.\nOn~\\eqref{eq:logball-test}, $\\delta=10^{-1}$ and $\\delta=10^{-3}$ give identical iterates because\n"
    "the pseudoconvex track has a single index, at every start either only $F_1$ is violated or\n"
    "$v_1-v_2\\ge4.79$, and the convex track is satisfied from the second evaluated point on; the\n"
    "$\\delta$ row of Table~\\ref{tab:dtap-sweep} is therefore a consistency check, not evidence about\n"
    "the role of $\\delta$.\n", "51b")
rep("stated below. The experiments support neither\nuniversal speed superiority nor a finite-budget robustness claim.", "stated below.", "III-1203")
rep("In this environment the package also", "With Python~3.13.4 and NumPy~2.1.3, the package also", "83")

# ---------------------------------------------------------------- Conclusion
a = s.index("\\section{Conclusion}\\label{sec:conclusion}\n") + len("\\section{Conclusion}\\label{sec:conclusion}\n")
b = s.index("\n", a)
s = s[:a] + (
    "DTAP solves normal-box nonlinear split feasibility problems with convex and pseudoconvex "
    "components by combining a residual-scaled convex step with a safeguarded pseudoconvex step. "
    "Under consistency and continuous differentiability, the whole sequence converges to a feasible "
    "point; no regularity modulus is an input, although the analysis uses bounds on a compact set "
    "containing the iterates. In the feature-selection application all constraints are convex, and "
    "test problems with a nonconvex pseudoconvex constraint exercise the pseudoconvex track. In the "
    "experiments, tuned subgradient methods can match or outperform DTAP, whose finite-budget "
    "performance depends on the starting point and the step scale. Rates for the full residual "
    "$J(x^k)$, beyond the convex-track bound of Remark~\\ref{rem:rate}, and guarantees under "
    "error-bound conditions remain open.") + s[b:]

DST.write_text(s, encoding="utf-8")
print("written", DST)
