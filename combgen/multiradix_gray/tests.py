from combgen.multiradix_gray.coroutine import gen_all


def main():
    for c, a in enumerate(gen_all([2, 3, 2])):
        print(c + 1, a)


if __name__ == '__main__':
    main()
