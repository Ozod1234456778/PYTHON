import threading

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    primes = []
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
    result.extend(primes)

def threaded_prime_checker(start, end, num_threads):
    thread_list = []
    result = []
    step = (end - start) // num_threads
    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(sub_start, sub_end, result))
        thread_list.append(thread)
        thread.start()

    for thread in thread_list:
        thread.join()

    result.sort()
    print("Prime numbers found:")
    print(result)


threaded_prime_checker(1, 100, 4)
 Exercise 2: Threaded File Processing - Word Count

import threading
from collections import defaultdict

def process_lines(lines, result_dict, lock):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().split()
        for word in words:
            local_count[word.lower()] += 1
    with lock:
        for word, count in local_count.items():
            result_dict[word] += count

def threaded_word_count(filename, num_threads):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    result_dict = defaultdict(int)
    threads = []
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else total_lines
        thread = threading.Thread(target=process_lines, args=(lines[start:end], result_dict, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Word occurrences:")
    for word, count in sorted(result_dict.items()):
        print(f"{word}: {count}")


threaded_word_count('sample.txt', 4)
