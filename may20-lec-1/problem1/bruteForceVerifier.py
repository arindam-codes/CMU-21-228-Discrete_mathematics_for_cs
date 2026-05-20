def count_all_even_brute():
    n = 1000
    even = 0

    while n <= 9999:
        if  (n % 10) % 2 == 0 and ((n % 100) // 10) % 2 == 0 and ((n % 1000) // 100) % 2 == 0 and ((n % 10000) // 1000) % 2 == 0:
            even += 1
        
        n += 1

    return even


print(count_all_even_brute())

## this testsall the whole digit but my question asked for every even digits ahh so now i used floor division and 
## module operator to test individual digits 

