
def main():
    num = int(input())
    arr = []

    for i in range(0,num):
        arr.append(int(input()))

    for i in range(0,num):
        if(arr[i]%2) == 0:
            print(arr[i], " is even")
        else:
            print(arr[i], " is odd")



if __name__ == "__main__":
    main()
