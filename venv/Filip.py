

import sys

def main():
    for line in sys.stdin:
        ab = line.split()
        a = ab[0]
        b = ab[1]

        newstr =int( a[2] + a[1] + a[0])
        newstr1 = int(b[2] + b[1] + b[0])


        print(newstr) if newstr > newstr1 else print(newstr1)



if __name__ == '__main__':
    main()
