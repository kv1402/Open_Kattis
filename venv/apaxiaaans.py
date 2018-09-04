##fikse dette opp


def main():
    name = input()
    l = len(name)
    list = []
    counter = 1

    for c in range(0,l):
        for i in range(counter,l):
          if(name[c]== name[i]):
              counter +=counter
          else:
              list.append(name[c])
              break


    print(list)
if __name__ == '__main__':
    main()
