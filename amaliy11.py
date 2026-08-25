names = []
surnames = []

with open("students.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) >= 2:
                names.append(parts[0])
                surnames.append(parts[1])

print("Names:")
print(names)
print("\nSurnames:")
print(surnames)
