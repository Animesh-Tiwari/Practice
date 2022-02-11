n = int(input())

even = []
odd = []
sum1 = []

for i in range(n):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
for j in range(len(even)):
    sum1.append(even[j]+odd[j])
print(sum1)
