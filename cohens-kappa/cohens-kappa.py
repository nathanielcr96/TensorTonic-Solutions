def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    pass

    p0 = 0.0
    pe = 0.0

    labels = []
    labels.extend(rater1)
    labels.extend(rater2)
    labels = set(labels)

    for k in labels:
        pe += rater1.count(k) / len(rater1) * rater2.count(k) / len(rater2)

    for pair in zip(rater1, rater2):
        if pair[0] == pair[1]:
            p0 += 1

    p0 = p0 / len(rater1)

    if pe == 1.0:
        kappa = 1.0

    else:
        kappa = (p0 - pe) / (1 - pe)

    return kappa