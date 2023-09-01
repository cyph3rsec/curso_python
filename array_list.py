numbers = int(input("How many number will you enter?: "))

arr: [float] = [0 for num in range(numbers)]

for n in range(0, numbers):
    arr[n] = float(input("Enter a number: "))

print("------ Array/ List ------")
print()

for num in range(0, numbers):
    print(f"Number: {arr[num]:.2f}")
