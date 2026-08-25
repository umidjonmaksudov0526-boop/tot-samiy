import os
import shutil

while True:
    print("\n===== FILE MANAGER =====")
    print("1. Papkadagi fayllarni ko‘rish")
    print("2. Yangi papka yaratish")
    print("3. Yangi fayl yaratish")
    print("4. Faylni o‘qish")
    print("5. Faylga yozish")
    print("6. Faylni o‘chirish")
    print("7. Papkani o‘chirish")
    print("8. Fayl hajmini ko‘rish")
    print("9. Chiqish")
    
    choice = input("\nTanlang: ")

    if choice == "1":
        print("\nElementlar:")
        for item in os.listdir():
            print(item)

    elif choice == "2":
        folder_name = input("Papka nomi: ")
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print("Papka yaratildi.")
        else:
            print("Bu papka allaqachon mavjud.")

    elif choice == "3":
        file_name = input("Fayl nomi: ")
        with open(file_name, "w") as f:
            pass
        print("Fayl yaratildi.")

    elif choice == "4":
        file_name = input("Fayl nomi: ")
        if os.path.isfile(file_name):
            with open(file_name, "r") as f:
                print("\nFayl mazmuni:")
                print(f.read())
        else:
            print("Fayl topilmadi.")

    elif choice == "5":
        file_name = input("Fayl nomi: ")
        text = input("Yoziladigan matn: ")
        with open(file_name, "a") as f:
            f.write(text + "\n")
        print("Matn yozildi.")

    elif choice == "6":
        file_name = input("O'chiriladigan fayl nomi: ")
        if os.path.isfile(file_name):
            os.remove(file_name)
            print("Fayl o'chirildi.")
        else:
            print("Bunday fayl yo'q.")

    elif choice == "7":
        folder_name = input("O'chiriladigan papka nomi: ")
        if os.path.isdir(folder_name):
            shutil.rmtree(folder_name)
            print("Papka o'chirildi.")
        else:
            print("Bunday papka yo'q.")

    elif choice == "8":
        file_name = input("Fayl nomi: ")
        if os.path.isfile(file_name):
            print(f"Fayl hajmi: {os.path.getsize(file_name)} bytes")
        else:
            print("Fayl topilmadi.")

    elif choice == "9":
        print("Dastur tugatildi.")
        break

    else:
        print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")
