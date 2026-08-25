import os

name = input("Nom kiriting: ")

if os.path.exists(name):
    if os.path.isdir(name):
        print("Bu papka.")
    elif os.path.isfile(name):
        print("Bu fayl.")
else:
    print("Bunday fayl yoki papka mavjud emas.")
