  1:Create a list containing five different fruits and print the third fruit.
    
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[2]) 
    
  2:Create two lists of numbers and concatenate them into a single list.
    list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2
print(combined_list)

3:Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
  
  numbers = [10, 20, 30, 40, 50]
middle_index = len(numbers) // 2
new_list = [numbers[0], numbers[middle_index], numbers[-1]]
print(new_list)
  
  4:Create a list of your five favorite movies and convert it into a tuple.

favorite_movies = ["Inception", "The Dark Knight", "The Matrix", "Interstellar", "Pulp Fiction"]
favorite_movies_tuple = tuple(favorite_movies)
print(favorite_movies_tuple)

5:Given a list of cities, check if "Paris" is in the list and print the result.

  cities = ["New York", "London", "Paris", "Tokyo", "Berlin"]
is_paris_in_list = "Paris" in cities
print(is_paris_in_list)

6:Create a list of numbers and duplicate it without using loops.

numbers = [1, 2, 3, 4, 5]
duplicated_numbers = numbers + numbers
print(duplicated_numb

7:Given a list of numbers, swap the first and last elements.
  
  numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

  8:Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
  
  numbers = tuple(range(1, 11))
sliced_numbers = numbers[3:8]
print(sliced_numbers)
  
  9:Create a list of colors and count how many times "blue" appears in the list.
  
  colors = ["red", "blue", "green", "blue", "yellow", "blue", "purple"]
blue_count = colors.count("blue")
print(blue_count)

10:Given a tuple of animals, find the index of "lion".
  
  animals = ("elephant", "tiger", "lion", "zebra", "giraffe")
lion_index = animals.index("lion")
print(lion_index)

11:Create two tuples of numbers and merge them into a single tuple.

  tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

12:Given a list and a tuple, find and print their lengths.
  
my_list = [10, 20, 30, 40, 50]
my_tuple = (1, 2, 3, 4, 5, 6)
list_length = len(my_list)
tuple_length = len(my_tuple)
print(f"Length of the list: {list_length}")
print(f"Length of the tuple: {tuple_length}")

  13:Create a tuple of five numbers and convert it into a list.
  
  my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

14:Given a tuple of numbers, find and print the maximum and minimum values.

numbers = (10, 20, 30, 40, 50)
max_value = max(numbers)
min_value = min(numbers)
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

  15:Create a tuple of words and print it in reverse order.
  
  words = ("apple", "banana", "cherry", "date", "elderberry")
reversed_words = words[::-1]
print(reversed_words)




  


