def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here

    seas_avg = []
    
    for p in range(period):
        vec_period = []
        sum_period = 0

        for i in range(p, len(series), period):
            vec_period.append(series[i])
            sum_period += series[i]
        
        seas_avg.append(sum_period / len(vec_period))

    return seas_avg