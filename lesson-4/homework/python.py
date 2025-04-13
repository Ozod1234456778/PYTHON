1. Sort a Dictionary by Value (Ascending and Descending)

sorted_ascending = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

sorted_descending = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted Dictionary (Ascending):", sorted_ascending)
print("Sorted Dictionary (Descending):", sorted_descending)

2. Add a Key to a Dictionary
sample_dict = {0: 10, 1: 20}

sample_dict[2] = 30
print("Updated Dictionary:", sample_dict)

3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatenated_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", concatenated_dict)

4. Generate a Dictionary with Squares
n = 5
square_dict = {x: x**2 for x in range(1, n+1)}
print("Dictionary with Squares:", square_dict)

5. Dictionary of Squares (1 to 15)

square_dict_1_to_15 = {x: x**2 for x in range(1, 16)}

print("Dictionary of Squares (1 to 15):", square_dict_1_to_15)


Set Exercises

1. Create a Set
python
Копировать
Редактировать

sample_set = {1, 2, 3, 4, 5}

print("Created Set:", sample_set)

2. Iterate Over a Set
python
Копировать
Редактировать

sample_set = {1, 2, 3, 4, 5}

for item in sample_set:
    print(item)

3. Add Member(s) to a Set
sample_set = {1, 2, 3}
sample_set.add(4) 
sample_set.update([5, 6]) 

print("Updated Set:", sample_set)

4. Remove Item(s) from a Set
sample_set = {1, 2, 3, 4, 5}

sample_set.remove(3)  
sample_set.discard(6) 

print("Set after removing items:", sample_set)

5. Remove an Item if Present in the Set
sample_set = {1, 2, 3, 4, 5}

if 3 in sample_set:
    sample_set.remove(3)

print("Set after removing item (if present):", sample_set)

























