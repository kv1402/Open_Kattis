
import sys

def main():

    arr = [1,1,2,2,2,8]
    myarr = [0,0,0,0,0,0];

    for line in sys.stdin:
        ab = line.split()

        for i in range(0,6):
            if(int(ab[i])== arr[i]):
                myarr[i] = 0
            elif(int(ab[i])> arr[i]):
                myarr[i] = -1
            else:
                b = arr[i] - int(ab[i])
                myarr[i] = b

        str1 = " ".join(str(e) for e in myarr)
        print(str1)


if __name__ == '__main__':
    main()
