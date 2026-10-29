import os
from typing import Tuple

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

from src.common.consts import DATA_DIR


def load_dataset(name: str, cfg_entry: dict, data_dir: str = None) -> Tuple[np.ndarray, np.ndarray]:
    """Load a dataset from its config entry. Returns raw (unscaled) (X, y)."""
    data_dir = str(DATA_DIR) if data_dir is None else data_dir
    loader_key = cfg_entry["loader"]
    if not loader_key.startswith("csv:"):
        raise ValueError(f"Dataset '{name}' must use loader='csv:<file>.csv'")

    fname = loader_key.split(":", 1)[1].strip()
    path = os.path.join(data_dir, fname)
    if not os.path.isfile(path):
        raise FileNotFoundError(f"Dataset file for '{name}' not found: {path}")

    df = pd.read_csv(path)
    X_df = df.iloc[:, :-1].copy()
    for col in X_df.columns:
        if X_df[col].dtype == object:
            X_df[col] = LabelEncoder().fit_transform(X_df[col].astype(str))
    X = X_df.values.astype(np.float64)
    y = LabelEncoder().fit_transform(df.iloc[:, -1].values)
    return X, y


def scale_train_test(X_train: np.ndarray, X_test: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Min-max scale to [0, 1], fitting on the training split only."""
    scaler = MinMaxScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test)
