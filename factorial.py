string = input()
splittedstring = split.string

a = []
for namStr in splitedstring:
    a.append(int(namStr))
print(a)

def mymax (*a):
    max = a[0]
    for i in range(1, len(a)):
        if max < a[i]:
            max = a[i]
    return max

print(mymax(a))
