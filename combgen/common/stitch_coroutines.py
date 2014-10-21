from combgen.common import stitch


def stitch_coroutines(coroutine_list):
    reversed_iterator = reversed(coroutine_list)  # Stitch in reverse order
    lead = next(reversed_iterator)  # Start with the last coroutine
    for X in reversed_iterator:
        lead = stitch(X, lead)
    return lead
