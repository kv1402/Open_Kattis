        ##Print integers from 1 to N in order, each on its own line, replacing the ones divisible by X with Fizz,
        # the ones divisible by Y with Buzz and ones divisible by both X and Y with FizzBuzz.


import sys

def main():

    for line in sys.stdin:
        ab = line.split()
        x = int(ab[0])
        y = int(ab[1])
        n = int(ab[2])

        for i in range(1,n+1):
            if(i%x ==0 and i%y ==0 ):
                print("FizzBuzz")
            elif(i%x == 0):
                print("Fizz")
            elif(i%y == 0):
                print("Buzz")
            else:
                print(i)


if __name__ == '__main__':
    main()
