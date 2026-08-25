students = ["Ali\n", "Vali\n", "Sardor\n", "Madina\n", "Aziza\n"]

with open("students.txt", "w") as file:
    file.writelines(students)
print("students.txt fayliga yozildi.")
