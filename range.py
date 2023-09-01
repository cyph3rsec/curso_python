'''
for a in range(1, 20, 2):
    print(a)

for b in range(1, 20, 3):
    print(b, end=", ")

for c in range(20, 0, -3):
    print(c, end=", ")
'''
tab = int(input("Digite um numero para multiplicar: "))

for c in range(10):
    print("%d x %d = %d" % (tab, c+1, tab*(c+1)))