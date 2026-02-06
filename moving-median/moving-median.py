def moving_median(values, window_size):
    """
    Compute the rolling median for each window position.
    """
    # Write code here

    Moving_median = []

    for i in range(len(values) - window_size + 1):
        median_values = values[i : i + window_size].copy()

        median_values.sort()

        if window_size % 2 == 0:
            # Even case
            top_num = int(window_size / 2)
            bottom_num = int(window_size / 2 - 1)
            Moving_median.append((median_values[top_num] + median_values[bottom_num]) / 2)

        else:
            # Odd case
            middle = int((window_size - 1) / 2)
            Moving_median.append(median_values[middle])

    return Moving_median