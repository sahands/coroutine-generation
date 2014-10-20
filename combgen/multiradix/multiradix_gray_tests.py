from multiradix_gray_coroutine import multiradix_gray_coroutine


def main():
    c = 0
    for a in multiradix_gray_coroutine([2, 3, 2]):
        print(a)
        c += 1
    print(c)


if __name__ == '__main__':
    main()
