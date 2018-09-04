
import sys
import math

def main():

    for line in sys.stdin:
        ab = line.split()
        h = int(ab[0])
        v = int(ab[1])

        l = h/math.sin(math.radians(v))
        print(math.ceil(l))

if __name__ == '__main__':
    main()
