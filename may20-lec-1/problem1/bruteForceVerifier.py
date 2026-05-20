### CODE PART A

def count_all_even_brute():
    n = 1000
    even = 0

    while n <= 9999:
        if  (n % 10) % 2 == 0 and ((n % 100) // 10) % 2 == 0 and ((n % 1000) // 100) % 2 == 0 and ((n % 10000) // 1000) % 2 == 0:
            even += 1
        
        n += 1

    return even


# print(count_all_even_brute())

## this testsall the whole digit but my question asked for every even digits ahh so now i used floor division and 
## module operator to test individual digits 

### CODE PART B 

def count_all_even_formula():
    first_digit_choice = 4
    other_digit_choice = 5

    return first_digit_choice * other_digit_choice ** 3

# print(count_all_even_formula())


assert count_all_even_brute() == count_all_even_formula()
print("Answer:", count_all_even_formula())