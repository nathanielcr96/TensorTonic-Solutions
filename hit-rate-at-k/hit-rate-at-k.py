def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here

    count = 0
    for i in range(len(recommendations)):
        user = recommendations[i]

        if k != 0:
            top_K = user[0 : k].copy()

        for element in top_K:
            if element in ground_truth[i]:
                count += 1
                break
        
    return count / len(recommendations)