def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here

    feature_matrix = []
    row_id = 0

    for t in range(max(lags), len(series)):
        feature_matrix.append([])

        for l in lags:
            feature_matrix[row_id].append(series[t - l])
        
        row_id += 1

    return feature_matrix

