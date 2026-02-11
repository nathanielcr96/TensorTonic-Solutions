def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here

    coverage_list = []
    for user in recommendations:
        coverage_list.extend(user)

    coverage_list = set(coverage_list)

    coverage = len(coverage_list) / n_items

    return coverage