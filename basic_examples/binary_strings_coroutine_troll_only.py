def binary_strings_lex_local(a, i):
    while True:
            a[i] = 1
            yield True
            a[i] = 0
            yield False
