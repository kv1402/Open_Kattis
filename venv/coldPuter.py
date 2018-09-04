import sys

def main():
    num = int(input())
    sum = 0

    for line in sys.stdin:
        ab = line.split()
        for i in range(0,num):
            b = int(ab[i])
            if(b< 0):
                sum += 1


        print(sum)



if __name__ == '__main__':
    main()
