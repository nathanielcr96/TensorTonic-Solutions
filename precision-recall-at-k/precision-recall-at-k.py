def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    topk_rel = []

    for i in range(0, k):
        if recommended[i] in relevant:
            topk_rel.append(recommended[i])

    precision = len(topk_rel) / k 
    recall = len(topk_rel) / len(relevant)

    return [precision, recall]