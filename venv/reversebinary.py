
def main():

    binar = input()
    bi = bin(int(binar))
    s = list(bi)

    for i in range(2,len(bi)):
        if(int(bi[i])==1):
            s[i]==0
        else:
            s[i]==1

    print(s[2])
    print(s)
    print(bi)

if __name__ == '__main__':
    main()
