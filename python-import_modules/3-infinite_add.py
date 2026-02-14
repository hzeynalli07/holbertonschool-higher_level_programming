#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] proqramın adıdır, bizə 1-ci indeksdən sonrakılar lazımdır
    args = sys.argv[1:]
    total = 0

    for arg in args:
        total += int(arg)

    print("{}".format(total))
