n = int(input())
a = []

for i in range(0, n):
    b = int(input())
    a.append(b)

for i in range(0, n):
    min = i
    for j in range(i+1, n):
        if(a[j] < a[min]):
            min = j
    tmp = a[i]
    a[i] = a[min]
    a[min] = tmp

for i in range(0, n):
    print(a[i])
