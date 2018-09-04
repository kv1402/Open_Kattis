

def main():
    r, l = input().split()

    if(int(r) + int(l) == 0):
        print("Not a moose")
    elif(int(r) != int(l)):
        if(int(r)>int(l)):
            print("Odd {}".format(int(r)+int(r)))
        else:
            print("Odd {}".format(int(l)+int(l)))
    else:
        print("Even {}".format(int(r)+int(l)))


if __name__ == '__main__':
    main()
