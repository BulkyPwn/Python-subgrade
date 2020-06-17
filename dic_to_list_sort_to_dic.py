dic = {
    'a': 1,
    "cbb": 2,
    "c": 100
}

l1 = []
l2 = []

i = 0

for (k, v) in dic.items():
    l1.append(k)
    l2.append(v)
    i += 1

i = len(l1) - 1
j = 0

while (i >= 0):
    j = 0
    while (j < i):
        if (l1[i] < l1[j]):
            temp = l1[j]
            l1[j] = l1[i]
            l1[i] = temp


            temp = l2[j]
            l2[j] = l2[i]
            l2[i] = temp
        j += 1
    i -= 1

print(l1)
#print('\n')
print(l2)

dic_sorted = dict(zip(l1,l2))
print(dic_sorted)