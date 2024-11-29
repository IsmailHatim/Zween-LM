import logging
import random
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Set random seed for reproducibility
def set_all_seed(seed_value=42):
    random.seed(seed_value)
    np.random.seed(seed_value)

# Calculate evaluation metrics
def calculate_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=1)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=1)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=1)
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
