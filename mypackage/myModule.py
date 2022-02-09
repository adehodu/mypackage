def top_n(items, n):
    """
    Returns the top 'n' items in an array in descending order

    Args:
        items: an array of numbers
        m: Number of items to be returned

    Egs:
        >>>top_n([8,3,9,4,5], 3)
        [9,8,5]
    """

    return sorted(items, reverse=True)[:n]