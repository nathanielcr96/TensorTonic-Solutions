def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here

    EMA = []

    for t in range(len(values)):
        if t == 0:
            EMA.append(values[t])

        else:

            EMA.append(alpha * values[t] + (1 - alpha) * EMA[t-1])

    return EMA