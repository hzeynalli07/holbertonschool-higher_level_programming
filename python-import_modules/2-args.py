#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv-dən faylın adını çıxarırıq (dilimləmə/slicing)
    argv = sys.argv[1:]
    count = len(argv)

    # 1. Başlıq hissəsinin çapı
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # 2. Arqumentlərin siyahısının çapı
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
