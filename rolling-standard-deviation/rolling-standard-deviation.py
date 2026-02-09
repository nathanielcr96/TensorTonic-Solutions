def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here

    import numpy as np

    rol_std = []

    for i in range(len(values) - window_size + 1):
        mu = 0

        for j in range(i, i + window_size):
            mu += values[j]
        
        mu = mu / window_size

        var = 0

        for j in range(i, i + window_size):
            var += (values[j] - mu)**2

        var = var / window_size

        rol_std.append(np.sqrt(var))

    return rol_std