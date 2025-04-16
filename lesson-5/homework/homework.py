1-def is_leap(year): """ Determines whether a given year is a leap year.

A year is a leap year if:
- It is divisible by 4, and
- It is NOT divisible by 100, unless it is also divisible by 400.

Parameters:
year (int): The year to be checked.

Returns:
bool: True if the year is a leap year, False otherwise.
"""

def kabisa_yilmi(yil):
    """
    Berilgan yil kabisa yili ekanligini aniqlaydi.

    Kabisa yili bo‘lishi uchun:
    - Yil 4 ga bo‘linishi kerak
    - Lekin 100 ga bo‘linmasligi kerak, agar 400 ga ham bo‘linmasa
    - Agar yil 400 ga bo‘linadigan bo‘lsa, u holda baribir kabisa yil bo‘ladi

    Parametr:
    yil (int): Tekshiriladigan yil

    Natija:
    bool: Agar kabisa yil bo‘lsa, True qaytaradi, aks holda False
    """
    if not isinstance(yil, int):
        raise ValueError("Yil butun son bo‘lishi kerak.")

    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)

   
    if not isinstance(yil, int):
        raise ValueError("Yil butun son bo‘lishi kerak.")

    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)


  
2. Conditional Statements Exercise
n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
a = 3
b = 10
start = a if a <= b else b
end = b if b >= a else a
even_numbers = [x for x in range(start, end + 1) if x % 2 == 0]
print(even_numbers)
