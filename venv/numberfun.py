import sys
import math

def main():

    testCase = int(input())
    list = [];

    for i in range(0,testCase):
        num = input().split()
        a = int(num[0])
        b = int(num[1])
        c = int(num[2])

        if(a+b == c):
            list.append("Possible")
        elif(math.fabs(a-b) == c):
            list.append("Possible")
        elif(a/b == c):
            list.append("Possible")
        elif(b/a == c):
            list.append("Possible")
        elif(a*b == c):
            list.append("Possible")
        else:
            list.append("Impossible")

    for elem in list:
        print(elem)




if __name__ == '__main__':
    main()
