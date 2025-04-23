1. ZeroDivisionError:

try:
    a = int(input("Sonni kiriting: "))
    b = int(input("Bo‘luvchini kiriting: "))
    result = a / b
    print("Natija:", result)
except ZeroDivisionError:
    print("0 ga bo‘lish mumkin emas!")
2. ValueError (Agar son emas bo‘lsa):

try:
    num = int(input("Butun son kiriting: "))
    print("Siz kiritgan son:", num)
except ValueError:
    print("Xatolik: Bu butun son emas.")
3. FileNotFoundError:


try:
    with open("fayl.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Fayl topilmadi.")
4. TypeError (Agar raqam emas bo‘lsa):

try:
    a = float(input("1-sonni kiriting: "))
    b = float(input("2-sonni kiriting: "))
    print("Yig‘indi:", a + b)
except ValueError:
    raise TypeError("Faqat raqam kiriting.")
5. PermissionError:

try:
    with open("/root/secret.txt", "r") as file:
        print(file.read())
except PermissionError:
    print("Faylga ruxsat yo‘q.")
6. IndexError:

my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index mavjud emas.")
7. KeyboardInterrupt:

try:
    num = input("Son kiriting (Ctrl+C bosmang): ")
    print("Kiritilgan:", num)
except KeyboardInterrupt:
    print("\nKiritish bekor qilindi.")
8. ArithmeticError:

try:
    a = 1.0
    b = 0.0
    print(a / b)
except ArithmeticError as e:
    print("Arifmetik xato:", e)
9. UnicodeDecodeError:

try:
    with open("file.txt", encoding="utf-8") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Fayl kodlashda xato bor.")
10. AttributeError:

my_list = [1, 2, 3]
try:
    my_list.upper()
except AttributeError:
    print("Bu metod ro‘yxat uchun mavjud emas.")
Fayl bilan ishlash (File I/O):
1. Faylni o‘qish:


with open("fayl.txt", "r") as f:
    print(f.read())
2. Faylning birinchi n qatorini o‘qish:

n = 3
with open("fayl.txt", "r") as f:
    for i in range(n):
        print(f.readline(), end="")
3. Faylga yozish va ko‘rsatish:

with open("fayl.txt", "a") as f:
    f.write("Yangi matn\n")

with open("fayl.txt", "r") as f:
    print(f.read())
4. Oxirgi n qatorni o‘qish:

n = 2
with open("fayl.txt") as f:
    lines = f.readlines()
    print(''.join(lines[-n:]))
5. Faylni qatorma-qator o‘qib listga saqlash:

with open("fayl.txt", "r") as f:
    lines = f.readlines()
print(lines)
6. Faylni o‘qib stringga saqlash:

with open("fayl.txt", "r") as f:
    data = f.read()
print(data)
7. Faylni massivga (list) saqlash:

with open("fayl.txt", "r") as f:
    arr = [line.strip() for line in f]
print(arr)
8. Eng uzun so‘zni topish:

with open("fayl.txt", "r") as f:
    words = f.read().split()
    longest = max(words, key=len)
print("Eng uzun so‘z:", longest)
9. Qatorlar sonini hisoblash:

with open("fayl.txt", "r") as f:
    count = len(f.readlines())
print("Qatorlar soni:", count)
10. So‘zlar chastotasi:

from collections import Counter
with open("fayl.txt", "r") as f:
    words = f.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)
11. Fayl o‘lchamini olish:

import os
print("Fayl o‘lchami:", os.path.getsize("fayl.txt"), "bayt")
12. Listni faylga yozish:

lines = ["salom", "dunyo", "python"]
with open("fayl.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
13. Fayldan boshqa faylga nusxa ko‘chirish:

with open("fayl.txt", "r") as f1, open("yangi.txt", "w") as f2:
    f2.write(f1.read())
14. 2 ta faylning mos qatorlarini birlashtirish:

with open("file1.txt") as f1, open("file2.txt") as f2:
    for l1, l2 in zip(f1, f2):
        print(l1.strip() + " " + l2.strip())
15. Tasodifiy qator o‘qish:

import random
with open("fayl.txt") as f:
    lines = f.readlines()
    print(random.choice(lines))
16. Fayl yopilganmi yoki yo‘q:

f = open("fayl.txt")
print("Yopildimi:", f.closed)
f.close()
print("Yopildimi:", f.closed)
17. Yangi qatordan tozalash:

with open("fayl.txt", "r") as f:
    lines = [line.strip() for line in f]
print(lines)
18. Fayldagi so‘zlar soni:

with open("fayl.txt") as f:
    words = f.read().replace(",", " ").split()
print("So‘zlar soni:", len(words))
19. Har xil fayllardan harflarni yig‘ish:

files = ["a.txt", "b.txt"]
chars = []
for name in files:
    with open(name, "r") as f:
        chars += list(f.read())
print(chars)
20. A-Z fayllar yaratish:

import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"{letter} fayli")
21. Har qatorda n ta harf bilan fayl yaratish:

import string
n = 5
with open("alphabet.txt", "w") as f:
    for i in range(0, 26, n):
        f.write(''.join(string.ascii_uppercase[i:i+n]) + "\n")
