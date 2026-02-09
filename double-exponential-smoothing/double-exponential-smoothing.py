def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here

    level = [series[0]]
    trend = [series[1] - series[0]]

    for t in range(1, len(series)):
        level.append(alpha * series[t] + (1 - alpha) * (level[t - 1] + trend[t - 1]))
        trend.append(beta * (level[t] - level[t - 1]) + (1 - beta) * trend[t - 1])

    return level