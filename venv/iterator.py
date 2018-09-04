M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(M)

G = (sum(row) for row in M)
print(G)

print(next(G))
print(next(G))
print(next(G))


#https://gist.github.com/Atlas7/116603cbddfb9a1287252c25fd45a4b4
