import sys

def main():
    for line in sys.stdin:
        ab= line.split()
        a = int(ab[0])
        b = int(ab[1])

        if(b>=45):
            print(a," ",b-45)
        elif(a== 0):
            a = 23
            c = b + 15
            print(a," ",c)
        else:
            d = a-1
            c = b + 15
            print(d," ", c)



if __name__ == "__main__":
    main()
