
import sys

def main():
    sum1 = 0
    num = 1

    for line in range(5):
        x = input()
        ab = x.split()
        temp = 0
        for i in range(4):
            temp += int(ab[i])
        if temp > sum1:
            sum1, num = temp, int(line)
    print(num+1, sum1)



if __name__ == '__main__':
    main()
