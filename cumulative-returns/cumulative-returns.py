def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here

    cumulative_return = []
    Wt = 1

    for i in range(len(returns)):
        Wt = Wt * (1 + returns[i])
        cumulative_return.append(Wt - 1)

    return cumulative_return