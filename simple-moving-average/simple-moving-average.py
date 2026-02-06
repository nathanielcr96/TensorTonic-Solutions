def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here

    SMA = []
    for i in range(len(values) - window_size + 1):
        sum_window = 0
        for j in range(window_size):
            sum_window += values[i + j]

        SMA.append(sum_window / window_size)

    return SMA