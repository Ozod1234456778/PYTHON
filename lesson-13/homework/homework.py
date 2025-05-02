from datetime import datetime

birth_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d")
today = datetime.today()

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

if days < 0:
    months -= 1
    days += 30
if months < 0:
    years -= 1
    months += 12

print(f"Siz {years} yil, {months} oy, {days} kunliksiz.")
️ Days Until Next Birthday

from datetime import datetime, timedelta

birth_str = input("Tug‘ilgan kuningizni kiriting (MM-DD): ")
this_year = datetime.now().year
next_birthday = datetime.strptime(f"{this_year}-{birth_str}", "%Y-%m-%d")
today = datetime.today()

if next_birthday < today:
    next_birthday = datetime.strptime(f"{this_year + 1}-{birth_str}", "%Y-%m-%d")

days_left = (next_birthday - today).days
print(f"Keyingi tug‘ilgan kuningizgacha {days_left} kun qoldi.")
️ Meeting Scheduler

from datetime import datetime, timedelta

now_str = input("Hozirgi sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
duration_h = int(input("Uchrashuv soatlari: "))
duration_m = int(input("Uchrashuv daqiqalari: "))

now = datetime.strptime(now_str, "%Y-%m-%d %H:%M")
end_time = now + timedelta(hours=duration_h, minutes=duration_m)

print("Uchrashuv tugash vaqti:", end_time.strftime("%Y-%m-%d %H:%M"))
️ Timezone Converter
(Requires pytz package: pip install pytz)


from datetime import datetime
import pytz

dt_str = input("Sana va vaqt (YYYY-MM-DD HH:MM): ")
from_zone = input("Hozirgi timezone (masalan, Asia/Tashkent): ")
to_zone = input("Qaysi timezonega o‘tkazilsin (masalan, Europe/London): ")

dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

dt = from_tz.localize(dt)
converted = dt.astimezone(to_tz)

print("Yangi vaqt:", converted.strftime("%Y-%m-%d %H:%M %Z%z"))
️ Countdown Timer

import time
from datetime import datetime

target_str = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    if target <= now:
        print("Vaqt tugadi!")
        break
    remaining = target - now
    print("Qolgan vaqt:", remaining)
    time.sleep(1)
️ Email Validator

import re

email = input("Email kiriting: ")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Email to‘g‘ri.")
else:
    print("Email noto‘g‘ri.")
️ Phone Number Formatter

phone = input("Telefon raqam (faqat raqam): ")
if len(phone) == 10 and phone.isdigit():
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatlangan:", formatted)
else:
    print("Noto‘g‘ri raqam formati.")
️ Password Strength Checker

import re

password = input("Parolni kiriting: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password)):
    print("Parol kuchli.")
else:
    print("Parol zaif. Kamida 8 belgidan iborat bo‘lsin, katta, kichik harf va raqam bo‘lishi kerak.")
️ Word Finder

text = "Bu yerda matn bor. Bu matnda so‘zlarni izlash mumkin."
word = input("Qidirilayotgan so‘zni kiriting: ")

found = [m.start() for m in re.finditer(word, text)]
print(f"{word} so‘zi {len(found)} marta topildi. Joylashuvlari: {found}")
 Date Extractor

import re

text = input("Matn kiriting: ")
pattern = r"\b\d{4}-\d{2}-\d{2}\b"  # YYYY-MM-DD format

dates = re.findall(pattern, text)
print("Topilgan sanalar:", dates)
