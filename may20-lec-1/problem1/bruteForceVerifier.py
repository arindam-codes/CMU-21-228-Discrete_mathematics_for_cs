def count_all_even_brute():
    n = 1000
    even = 0

    while n <= 9999:
        if n % 2 == 0:
            even += 1
            n += 1
        elif n <= 9999:
            n += 1

    return even


print(count_all_even_brute())