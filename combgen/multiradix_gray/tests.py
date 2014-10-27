from combgen.multiradix_gray.coroutine import gen_all


def main():
    for c, a in enumerate(gen_all([3, 2, 3])):
        print('{c:2d} - {a}'.format(c=c + 1, a=''.join(str(x) for x in a)))


if __name__ == '__main__':
    main()
