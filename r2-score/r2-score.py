import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    pass
    
    AVG = 0
    for y in y_pred:
      AVG += y

    AVG = AVG/len(y_pred)

    if len(set(y_true)) == 1:
      if y_true == y_pred:
        R2 = 1.0

      else:
        R2 = 0.0

    else:

      sum_t = 0
      sum_b = 0

      for pair in zip(y_true, y_pred):
        sum_t += (pair[0] - pair[1]) ** 2
        sum_b += (pair[0] - AVG) ** 2

      if sum_b == 0:
        R2 = 1

      else:  
        R2 = 1 - sum_t / sum_b

    return R2

