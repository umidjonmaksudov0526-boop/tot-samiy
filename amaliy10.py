new_student = input("Yangi student: ")

with open("students.txt", "a") as file:
    file.write(f"\n{new_student}")
print("Yangi student qo'shildi.")
