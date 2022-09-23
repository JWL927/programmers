num = int(input())
a = []
sum = 0

for i in range(0, num):
    a.append(int(input()))

a.sort()

for i in range(0, num):
    sum = sum + a[i]

avg = sum / num
mid = a[len(a)/2]
# number that appears most
scope = a[len(a) - 1] - a[0]

print(avg)
print(mid)
# print(number that appears most)
print(scope)
