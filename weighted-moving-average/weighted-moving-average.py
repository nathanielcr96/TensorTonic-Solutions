def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    # Write code here

    WMA = []
    sum_weights = sum(weights)

    for i in range(len(values) - len(weights) + 1):
        sum_weighted_values = 0
        for j in range(len(weights)):
            sum_weighted_values += weights[j] * values[i + j]

        WMA.append(sum_weighted_values / sum_weights) 

    return WMA