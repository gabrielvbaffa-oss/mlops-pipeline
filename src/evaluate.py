import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def evaluate_model(model: KMeans, features: np.ndarray) -> dict:
    """
    Avalia o modelo treinado e retorna um dicionário com as métricas.
    """
    metrics = {
        "inertia": round(model.inertia_, 4),
        "silhouette_score": round(
            silhouette_score(features, model.labels_), 4
        ),
        "n_clusters": model.n_clusters
    }

    return metrics