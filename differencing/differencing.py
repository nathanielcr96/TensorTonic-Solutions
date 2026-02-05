def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here

    dx = []

    # Save the original in 0 order
    dx.append(series)
    
    if order != 0:
        for j in range(1, order + 1):
            dx.append([])

            for t in range(1, len(dx[j - 1])):
                dx[j].append(dx[j - 1][t] - dx[j - 1][t - 1])

    return dx[order]