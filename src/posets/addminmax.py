def add_min_max(poset, minimum, maximum):
    # Takes as input a poset and returns a modified poset with a unique maximum
    # element and a unique maximum element added.
    def poset_with_min_max(a, b):
        return a == minimum or b == maximum or poset(a, b)

    return poset_with_min_max
