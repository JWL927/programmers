num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

num2.sort()
num2.reverse()

print(num2[num1[1] - 1])

#Network crashed so i couldn't push my git to github