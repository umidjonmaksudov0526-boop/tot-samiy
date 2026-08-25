import os

print(f"Joriy papka: {os.getcwd()}")
print("\nIchidagi elementlar:")
for item in os.listdir():
    print(item)
