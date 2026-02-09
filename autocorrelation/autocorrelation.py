def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here

    autC = [1]
    AVG = 0

    for x in series:
        AVG += x

    AVG = AVG / len(series)

    VAR = 0

    for x in series:
        VAR += (x - AVG)**2


    for k in range(1, max_lag + 1):
        rk = 0

        for t in range(len(series) - k):

            rk += (series[t] - AVG)*(series[t + k] - AVG)
        
        if VAR != 0:
            autC.append(rk / VAR)
        else:
            autC.append(0)

    return autC
