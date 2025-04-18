1
def insert_underscores(txt):
    result = ""
    i = 0
    count = 0
    vowels = "aeiouAEIOU"

    while i < len(txt):
        result += txt[i]
        count += 1
 if count == 3:
            if i + 1 < len(txt):
  if txt[i + 1] != '_' and txt[i] not in vowels:
        result += "_"
     count = 0
  else:
   count -= 1  # delay underscore
            else:
   break
    i += 1
    return result
print(insert_underscores("hello"))       
print(insert_underscores("assalom"))      
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  

2
n = int(input())
for i in range(n):
    print(i ** 2)
3
i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

num = int(input("Enter number: "))
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print("Sum is:", total)

n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)
      
num = int(input())
count = 0
while num != 0:
    num //= 10
    count += 1
print(count)

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

for i in range(-10, 0):
    print(i)
  for i in range(5):
    print(i)
print("Done!")


start = 25
end = 50
print("Prime numbers between 25 and 50:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b


n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"{n}! = {fact}")


4. Return Uncommon Elements of Lists

def uncommon_elements(list1, list2):
    from collections import Counter
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for item in c1:
        if c1[item] > c2.get(item, 0):
            result.extend([item] * (c1[item] - c2.get(item, 0)))
   
    for item in c2:
        if c2[item] > c1.get(item, 0):
            result.extend([item] * (c2[item] - c1.get(item, 0)))
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))  # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))  # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]

























