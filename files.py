'''
r = read / ler
w = write / escrever
a = append / adicionar
t = text / texto
b = binary / binario
+ = create file if doesnt exist / cria arquivo se nao existir


#with open("names.txt", "w+") as lnames:
#    names = lnames.write("Romulo\n")

#with open("names.txt", "r") as lnames:
#    names = lnames.read()
#print(names)

with open("names.txt", "a") as lnames:
    names = lnames.write("Obelix\n")

with open("names.txt", "r") as lnames:
    names = lnames.read()
print(names)
'''

file = open("names.txt", "w")

names = list()
names.append("Romulo\n")
names.append("Obelix\n")
names.append("Batman\n")
names.append("Clark Kent\n")
names.append("Joker\n")

file.writelines(names)


file = open("names.txt", "r")
print(file.readlines())





