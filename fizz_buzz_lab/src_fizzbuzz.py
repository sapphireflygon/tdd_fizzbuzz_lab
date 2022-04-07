
def fizzbuzz(num):
    while num >= 1:
        if num % 3 == 0 and num % 5 == 0:
            return "fizzbuzz"
        elif num % 3 == 0:
            return "fizz"
        elif num % 5 == 0:
            return "buzz"
        else:
            return str(num)
    return "The game starts at 1 you fool!"
    
    