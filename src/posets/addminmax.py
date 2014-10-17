def add_min_max(poset, minimum, maximum):
    # Takes as input a poset and returns a modified poset with a unique maximum
    # element and a unique maximum element.
    def poset_with_min_max(a, b):
        if a == minimum or b == maximum:
            return True
        return poset(a, b)

    return poset_with_min_max
