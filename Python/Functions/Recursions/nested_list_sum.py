def nested_sum(li):
    """
    Docstring for nested_sum
    @params li: nested lists
    @returns total sum
    """
    total = 0
    for el in li:
        if isinstance(el, list):
            total += nested_sum(el)
        else:
            total += el
    return total

if __name__ == "__main__":
    lists = [[5, [6, 7], [[8, 9], 10]], 45]
    print("Nested Lists Sum: ", nested_sum(lists))