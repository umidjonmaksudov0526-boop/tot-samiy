import os

file_name = "data.txt"

if os.path.exists(file_name):
    size = os.path.getsize(file_name)
    print(f"Fayl hajmi: {size} bytes")
else:
    print(f"{file_name} topilmadi.")
