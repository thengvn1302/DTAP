"""Classification scoring and feature-selection stability metrics."""
from typing import Tuple

import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from src.common.config import KNN_K, SVM_PARAMS


def nogueira_stability(Z: np.ndarray) -> float:
    """Nogueira et al. (2018) feature-selection stability index in [-1, 1].

    Z : (K, m) binary matrix with Z[i, j] = 1 iff feature j is selected in fold i.
    """
    K, m = Z.shape
    if m <= 1:
        return 1.0
    k_bar = float(Z.sum(axis=1).mean())
    p = k_bar / m
    if p <= 0.0 or p >= 1.0:
        return 1.0
    s2 = Z.var(axis=0, ddof=1)   # unbiased K/(K-1) * p_j(1-p_j), Definition 4 of Nogueira et al.
    return float(1.0 - s2.mean() / (p * (1.0 - p)))


def score_fold(X_train, y_train, X_test, y_test, selected_idx) -> Tuple[float, float, float, float]:
    """Train SVM + KNN on selected features; return (svm_acc%, knn_acc%, svm_roc, knn_roc).

    ROC is macro one-vs-rest AUC.
    """
    if len(selected_idx) == 0:
        return 0.0, 0.0, float("nan"), float("nan")
    Xtr = X_train[:, selected_idx]
    Xte = X_test[:, selected_idx]

    knn = KNeighborsClassifier(n_neighbors=KNN_K).fit(Xtr, y_train)
    svm_acc = SVC(**SVM_PARAMS, random_state=42).fit(Xtr, y_train).score(Xte, y_test) * 100.0
    knn_acc = knn.score(Xte, y_test) * 100.0

    n_cls = len(np.unique(y_train))
    svm_roc = knn_roc = float("nan")
    try:
        svm_p = SVC(**SVM_PARAMS, probability=True, random_state=42).fit(Xtr, y_train).predict_proba(Xte)
        knn_p = knn.predict_proba(Xte)
        if n_cls == 2:
            svm_roc = float(roc_auc_score(y_test, svm_p[:, 1]))
            knn_roc = float(roc_auc_score(y_test, knn_p[:, 1]))
        else:
            svm_roc = float(roc_auc_score(y_test, svm_p, multi_class="ovr", average="macro"))
            knn_roc = float(roc_auc_score(y_test, knn_p, multi_class="ovr", average="macro"))
    except Exception:
        pass
    return svm_acc, knn_acc, svm_roc, knn_roc


def mean_std(v) -> Tuple[float, float]:
    v = np.asarray(v, float)
    return float(v.mean()), float(v.std())
