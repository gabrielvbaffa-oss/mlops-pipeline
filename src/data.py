import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import Tuple


def load_data(filepath: str) -> np.ndarray:
    """
    Carrega pontos lat/lng de um arquivo CSV.

    O CSV deve ter colunas 'lat' e 'lng'.
    Retorna um array numpy de shape (n, 2).
    """
    df = pd.read_csv(filepath)
    points = df[['lat', 'lng']].values

    return points


def prepare_features(points: np.ndarray) -> Tuple[np.ndarray, StandardScaler]:
    """
    Normaliza os features usando StandardScaler.
    """
    scaler = StandardScaler()
    features = scaler.fit_transform(points)

    return features, scaler
