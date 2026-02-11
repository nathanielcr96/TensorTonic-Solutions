import math
import numpy as np

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    pass

    logloss = []
    for i in range(len(y_true)):
        p = np.clip(y_pred[i], eps, 1 - eps)
        
        logloss.append(- (y_true[i] * math.log(p) + (1 - y_true[i]) * math.log(1 - p)))

    return logloss