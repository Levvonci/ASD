#Uso la prima moneta e la confronto con le altre

X = [1, 2, 1, 1, 1, 1]

start = X[0]

for i in range(1, len(X)):
    if start < X[i]:
        print(i)
    elif start > X[i]:
        print(start)
